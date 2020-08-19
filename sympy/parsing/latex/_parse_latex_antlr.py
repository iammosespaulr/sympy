# Ported from latex2sympy by @augustt198
# https://github.com/augustt198/latex2sympy
# See license in LICENSE.txt

import sympy
from sympy.external import import_module
from sympy.printing.str import StrPrinter
from sympy.physics.quantum.state import Bra, Ket
from sympy import MutableDenseMatrix
from .errors import LaTeXParsingError


LaTeXParser = LaTeXLexer = MathErrorListener = None

try:
    LaTeXParser = import_module('sympy.parsing.latex._antlr.latexparser',
                                import_kwargs={'fromlist': ['LaTeXParser']}).LaTeXParser
    LaTeXLexer = import_module('sympy.parsing.latex._antlr.latexlexer',
                               import_kwargs={'fromlist': ['LaTeXLexer']}).LaTeXLexer
except Exception:
    pass

ErrorListener = import_module('antlr4.error.ErrorListener',
                              warn_not_installed=True,
                              import_kwargs={'fromlist': ['ErrorListener']}
                              )



if ErrorListener:
    class MathErrorListener(ErrorListener.ErrorListener):  # type: ignore
        def __init__(self, src):
            super(ErrorListener.ErrorListener, self).__init__()
            self.src = src

        def syntaxError(self, recog, symbol, line, col, msg, e):
            fmt = "%s\n%s\n%s"
            marker = "~" * col + "^"

            if msg.startswith("missing"):
                err = fmt % (msg, self.src, marker)
            elif msg.startswith("no viable"):
                err = fmt % ("I expected something else here", self.src, marker)
            elif msg.startswith("mismatched"):
                names = LaTeXParser.literalNames
                expected = [
                    names[i] for i in e.getExpectedTokens() if i < len(names)
                ]
                if len(expected) < 10:
                    expected = " ".join(expected)
                    err = (fmt % ("I expected one of these: " + expected + " here", self.src,
                                  marker))
                else:
                    err = (fmt % ("I expected something else here", self.src,
                                  marker))
            else:
                err = fmt % ("I don't understand what's here", self.src, marker)
            raise LaTeXParsingError(err)


def parse_latex(sympy):
    antlr4 = import_module('antlr4', warn_not_installed=True)

    if None in [antlr4, MathErrorListener]:
        raise ImportError("LaTeX parsing requires the antlr4 python package,"
                          " provided by pip (antlr4-python2-runtime or"
                          " antlr4-python3-runtime) or"
                          " conda (antlr-python-runtime)")

    matherror = MathErrorListener(sympy)

    stream = antlr4.InputStream(sympy)
    lex = LaTeXLexer(stream)
    lex.removeErrorListeners()
    lex.addErrorListener(matherror)

    tokens = antlr4.CommonTokenStream(lex)
    parser = LaTeXParser(tokens)

    # remove default console error listener
    parser.removeErrorListeners()
    parser.addErrorListener(matherror)

    relation = parser.math().relation()
    expr = convert_relation(relation)

    return expr

def checkassignmentvseq(lh, rh):
    return not isinstance(lh, (sympy.MutableDenseMatrix, tuple)) and isinstance(rh, (sympy.MutableDenseMatrix, tuple))
def convert_relation(rel):
    if rel.expr():
        return convert_expr(rel.expr())
    lh = convert_relation(rel.relation(0))
    rh = convert_relation(rel.relation(1))
    #print(rule2text(rel))
    #print(type(lh), lh)
    #print(type(rh), rh)
    #print(any(isinstance(x, (sympy.MutableDenseMatrix, tuple, sympy.ImmutableMatrix)) for x in (lh, rh)), not all(isinstance(x, (sympy.MutableDenseMatrix, tuple, sympy.ImmutableMatrix)) for x in (lh, rh)))
    if any(isinstance(x, (sympy.MutableDenseMatrix, tuple, sympy.ImmutableMatrix)) for x in (lh, rh)) and not all(isinstance(x, (sympy.MutableDenseMatrix, tuple, sympy.ImmutableMatrix)) for x in (lh, rh)):
        l = sympy.Symbol('l')
        if checkassignmentvseq(lh, rh):
            val = tuple([x.subs(l, rh) for x in sympy.solve(sympy.Eq(lh, l), lh.free_symbols)])
            if len(val) > 1:
                return val
            else:
                if val:
                    return val[0]
                else:
                    pass
        elif checkassignmentvseq(rh, lh):
            val = tuple([x.subs(l, lh) for x in sympy.solve(sympy.Eq(rh, l), rh.free_symbols)])
            if len(val) > 1:
                return val
            else:
                if val:
                    return val[0]
                else:
                    pass
        else:
            pass
    if rel.LT():
        return sympy.StrictLessThan(lh, rh)
    elif rel.LTE():
        return sympy.LessThan(lh, rh)
    elif rel.GT():
        return sympy.StrictGreaterThan(lh, rh)
    elif rel.GTE():
        return sympy.GreaterThan(lh, rh)
    elif rel.EQUAL():
        return sympy.Eq(lh, rh)
    elif rel.NEQ():
        return sympy.Ne(lh, rh)

def convert_expr(expr):
    return convert_add(expr.additive())


def convert_add(add):
    if add.ADD():
        lh = convert_add(add.additive(0))
        rh = convert_add(add.additive(1))
        return sympy.Add(lh, rh, evaluate=False)
    elif add.SUB():
        lh = convert_add(add.additive(0))
        rh = convert_add(add.additive(1))
        return sympy.Add(lh, -1 * rh, evaluate=False)
    else:
        return convert_mp(add.mp())


def convert_mp(mp):
    if hasattr(mp, 'mp'):
        mp_left = mp.mp(0)
        mp_right = mp.mp(1)
    else:
        mp_left = mp.mp_nofunc(0)
        mp_right = mp.mp_nofunc(1)

    if mp.MUL() or mp.CMD_TIMES() or mp.CMD_CDOT():
        lh = convert_mp(mp_left)
        rh = convert_mp(mp_right)
        return sympy.Mul(lh, rh, evaluate=False)
    elif mp.DIV() or mp.CMD_DIV() or mp.COLON():
        lh = convert_mp(mp_left)
        rh = convert_mp(mp_right)
        return sympy.Mul(lh, sympy.Pow(rh, -1, evaluate=False), evaluate=False)
    else:
        if hasattr(mp, 'unary'):
            return convert_unary(mp.unary())
        else:
            return convert_unary(mp.unary_nofunc())


def convert_unary(unary):
    if hasattr(unary, 'unary'):
        nested_unary = unary.unary()
    else:
        nested_unary = unary.unary_nofunc()
    if hasattr(unary, 'postfix_nofunc'):
        first = unary.postfix()
        tail = unary.postfix_nofunc()
        postfix = [first] + tail
    else:
        postfix = unary.postfix()

    if unary.ADD():
        return convert_unary(nested_unary)
    elif unary.SUB():
        numabs = convert_unary(nested_unary)
        if numabs == 1:
            # Use Integer(-1) instead of Mul(-1, 1)
            return -numabs
        else:
            return sympy.Mul(-1, convert_unary(nested_unary), evaluate=False)
    elif postfix:
        return convert_postfix_list(postfix)


def convert_postfix_list(arr, i=0):
    if i >= len(arr):
        raise LaTeXParsingError("Index out of bounds")

    res = convert_postfix(arr[i])
    if isinstance(res, sympy.Expr):
        if i == len(arr) - 1:
            return res  # nothing to multiply by
        else:
            if i > 0:
                left = convert_postfix(arr[i - 1])
                right = convert_postfix(arr[i + 1])
                if isinstance(left, sympy.Expr) and isinstance(
                        right, sympy.Expr):
                    left_syms = convert_postfix(arr[i - 1]).atoms(sympy.Symbol)
                    right_syms = convert_postfix(arr[i + 1]).atoms(
                        sympy.Symbol)
                    # if the left and right sides contain no variables and the
                    # symbol in between is 'x', treat as multiplication.
                    if len(left_syms) == 0 and len(right_syms) == 0 and str(
                            res) == "x":
                        return convert_postfix_list(arr, i + 1)
            # multiply by next
            return sympy.Mul(
                res, convert_postfix_list(arr, i + 1), evaluate=False)
    elif isinstance(res, tuple):
        if i == len(arr) - 1:
            return res  # nothing to multiply by
        else:
            if i > 0:
                left = convert_postfix(arr[i - 1])
                right = convert_postfix(arr[i + 1])
                if isinstance(left, sympy.Expr) and isinstance(
                        right, sympy.Expr):
                    left_syms = convert_postfix(arr[i - 1]).atoms(sympy.Symbol)
                    right_syms = convert_postfix(arr[i + 1]).atoms(
                        sympy.Symbol)
                    # if the left and right sides contain no variables and the
                    # symbol in between is 'x', treat as multiplication.
                    if len(left_syms) == 0 and len(right_syms) == 0 and str(
                            res) == "x":
                        return convert_postfix_list(arr, i + 1)
            # multiply by next
            return sympy.Mul(
                res, convert_postfix_list(arr, i + 1), evaluate=False)
    elif isinstance(res, MutableDenseMatrix):
        if i == len(arr) - 1:
            return res  # nothing to multiply by
        else:
            if i > 0:
                left = convert_postfix(arr[i - 1])
                right = convert_postfix(arr[i + 1])
                if isinstance(left, sympy.Expr) and isinstance(
                        right, sympy.Expr):
                    left_syms = convert_postfix(arr[i - 1]).atoms(sympy.Symbol)
                    right_syms = convert_postfix(arr[i + 1]).atoms(
                        sympy.Symbol)
                    # if the left and right sides contain no variables and the
                    # symbol in between is 'x', treat as multiplication.
                    if len(left_syms) == 0 and len(right_syms) == 0 and str(
                            res) == "x":
                        return convert_postfix_list(arr, i + 1)
            # multiply by next
            return sympy.Mul(
                res, convert_postfix_list(arr, i + 1), evaluate=False)
    else:  # must be derivative
        wrt = res[0]
        if i == len(arr) - 1:
            raise LaTeXParsingError("Expected expression for derivative")
        else:
            expr = convert_postfix_list(arr, i + 1)
            return sympy.Derivative(expr, wrt)


def do_subs(expr, at):
    if at.expr():
        at_expr = convert_expr(at.expr())
        syms = at_expr.atoms(sympy.Symbol)
        if len(syms) == 0:
            return expr
        elif len(syms) > 0:
            sym = next(iter(syms))
            return expr.subs(sym, at_expr)
    elif at.equality():
        lh = convert_expr(at.equality().expr(0))
        rh = convert_expr(at.equality().expr(1))
        return expr.subs(lh, rh)


def convert_postfix(postfix):
    if hasattr(postfix, 'exp'):
        exp_nested = postfix.exp()
    else:
        exp_nested = postfix.exp_nofunc()

    exp = convert_exp(exp_nested)
    for op in postfix.postfix_op():
        if op.BANG():
            if isinstance(exp, list):
                raise LaTeXParsingError("Cannot apply postfix to derivative")
            exp = sympy.factorial(exp, evaluate=False)
        elif op.eval_at():
            ev = op.eval_at()
            at_b = None
            at_a = None
            if ev.eval_at_sup():
                at_b = do_subs(exp, ev.eval_at_sup())
            if ev.eval_at_sub():
                at_a = do_subs(exp, ev.eval_at_sub())
            if at_b is not None and at_a is not None:
                exp = sympy.Add(at_b, -1 * at_a, evaluate=False)
            elif at_b is not None:
                exp = at_b
            elif at_a is not None:
                exp = at_a

    return exp


def convert_exp(exp):
    if hasattr(exp, 'exp'):
        exp_nested = exp.exp()
    else:
        exp_nested = exp.exp_nofunc()

    if exp_nested:
        base = convert_exp(exp_nested)
        if isinstance(base, list):
            raise LaTeXParsingError("Cannot raise derivative to power")
        if exp.atom():
            exponent = convert_atom(exp.atom())
        elif exp.expr():
            exponent = convert_expr(exp.expr())
        return sympy.Pow(base, exponent, evaluate=False)
    else:
        if hasattr(exp, 'comp'):
            return convert_comp(exp.comp())
        else:
            return convert_comp(exp.comp_nofunc())


def convert_comp(comp):
    if comp.group():
        expr = convert_expr(comp.group().expr())
        matrix_form  = (comp.group().L_BRACE() and comp.group().R_BRACE()) or \
            (comp.group().L_PAREN() and comp.group().R_PAREN()) or \
            (comp.group().L_BRACKET() and comp.group().R_BRACKET()) or \
            (comp.group().L_BRACE_LITERAL() and comp.group().R_BRACE_LITERAL())
        if isinstance(expr, tuple) and matrix_form:
            return MutableDenseMatrix(expr)
        return expr
    elif comp.abs_group():
        return sympy.Abs(convert_expr(comp.abs_group().expr()), evaluate=False)
    elif comp.atom():
        return convert_atom(comp.atom())
    elif comp.frac():
        return convert_frac(comp.frac())
    elif comp.binom():
        return convert_binom(comp.binom())
    elif comp.floor():
        return convert_floor(comp.floor())
    elif comp.ceil():
        return convert_ceil(comp.ceil())
    #elif comp.delta():
    #    return convert_delta(comp.delta())
    elif comp.func():
        return convert_func(comp.func())


def convert_atom(atom):
    if atom.LETTER():
        subscriptName = ''
        if atom.subexpr():
            subscript = None
            if atom.subexpr().expr():  # subscript is expr
                subscript = convert_expr(atom.subexpr().expr())
            else:  # subscript is atom
                subscript = convert_atom(atom.subexpr().atom())
            subscriptName = '_{' + StrPrinter().doprint(subscript) + '}'
        return sympy.Symbol(atom.LETTER().getText() + subscriptName)
    elif atom.SYMBOL():
        s = atom.SYMBOL().getText()[1:]
        if s == "infty":
            return sympy.oo
        if s == "pi":
            return sympy.pi
        else:
            if atom.subexpr():
                subscript = None
                if atom.subexpr().expr():  # subscript is expr
                    subscript = convert_expr(atom.subexpr().expr())
                else:  # subscript is atom
                    subscript = convert_atom(atom.subexpr().atom())
                subscriptName = StrPrinter().doprint(subscript)
                s += '_{' + subscriptName + '}'
            return sympy.Symbol(s)
    elif atom.NUMBER():
        s = atom.NUMBER().getText().replace(",", "")
        if len(s) > 1:
            s = s.lstrip('0')
            if not s:
                s = '0'
        return sympy.Number(s)
    elif atom.DIFFERENTIAL():
        var = get_differential_var(atom.DIFFERENTIAL())
        #print("Atom: ", var)
        return sympy.Symbol('d' + var.name)
    elif atom.prime():
        if atom.prime().expr():
            val = convert_expr(atom.prime().expr())
        else:
            #func = sympy.Function(sympy.Symbol(atom.prime().preprime().LETTER().getText()))('t')
            #return func.diff(sympy.Symbol('t'), 1)
            return sympy.Symbol(rule2text(atom.prime().preprime()))
        text = rule2text(atom.prime())
        funcv = text.split('^')[0]
        if funcv == text:
            funcv = funcv.replace("’","'")
            interim = funcv.split("(")[0]
            n_times = interim.count("'")
            funcv = interim.strip("'")
        else:
            n_times = text.count('\\prime')
        x = sympy.Symbol('x')
        func = sympy.Function(funcv)(x)
        return func.diff(x, n_times).subs(x, val)
    elif atom.dot():
        if atom.dot().atom():
            val = convert_atom(atom.dot().atom())
        elif atom.dot().expr():
            val = convert_expr(atom.dot().expr())
        t = sympy.Symbol('t')
        return sympy.Derivative(val, (t, 1))
    elif atom.ddot():
        if atom.ddot().atom():
            val = convert_atom(atom.ddot().atom())
        elif atom.ddot().expr():
            val = convert_expr(atom.ddot().expr())
        t = sympy.Symbol('t')
        return sympy.Derivative(val, (t, 2))
    elif atom.angularunit():
        text = rule2text(atom.angularunit())
        val = sympy.parse_expr(text.split('^')[0])
        return sympy.rad(val)
    elif atom.mathit():
        text = rule2text(atom.mathit().mathit_text())
        return sympy.Symbol(text)
    elif atom.array():
        array = tuple([list(map(convert_relation, x.relation())) for x in atom.array().array_elements()])
        return array
    elif atom.determinant():
        determinant = sympy.Matrix([list(map(convert_relation, x.relation())) for x in atom.determinant().array_elements()]).det()
        return determinant
    elif atom.matrix():
        matrix = sympy.Matrix([list(map(convert_relation, x.relation())) for x in atom.matrix().array_elements()])
        return matrix
    elif atom.bra():
        val = convert_expr(atom.bra().expr())
        return Bra(val)
    elif atom.ket():
        val = convert_expr(atom.ket().expr())
        return Ket(val)
    


def rule2text(ctx):
    stream = ctx.start.getInputStream()
    # starting index of starting token
    startIdx = ctx.start.start
    # stopping index of stopping token
    stopIdx = ctx.stop.stop

    return stream.getText(startIdx, stopIdx)


def convert_frac(frac):
    diff_op = False
    partial_op = False
    lower_itv = frac.lower.getSourceInterval()
    lower_itv_len = lower_itv[1] - lower_itv[0] + 1
    if (frac.lower.start == frac.lower.stop
            and frac.lower.start.type == LaTeXLexer.DIFFERENTIAL and frac.lower.start.text[0] == 'd'):
        wrt = get_differential_var_str(frac.lower.start.text)
        #print('wrt: ', wrt)
        symb = wrt.split("^")[0]
        nbot = "1"
        if symb + "^" in wrt:
            if "^{" in wrt:
                start = symb +'^{'
                end = '}'
                nbot = wrt[wrt.find(start) + len(start) : wrt.rfind(end)]
                wrt = wrt.replace(start[1:] + nbot + end, '')
            else:
                nbot = wrt[2]
                wrt = wrt.replace("^" + nbot, '', 1)
        nbot = parse_latex(nbot)
        #print("Symb :", symb)
        #print("Lower :", wrt)
        #print("nbot :", nbot)
        diff_op = True
    elif (frac.lower.start == frac.lower.stop
            and frac.lower.start.type == LaTeXLexer.DIFFERENTIAL and '\\partial' in frac.lower.start.text):
        wrt = get_differential_var_str(frac.lower.start.text)
        wrt = wrt[1:]
        #print('wrt: ', wrt)
        symb = wrt.split("^")[0]
        nbot = "1"
        if symb + "^" in wrt:
            if "^{" in wrt:
                start = symb +'^{'
                end = '}'
                nbot = wrt[wrt.find(start) + len(start) : wrt.rfind(end)]
                wrt = wrt.replace(start[1:] + nbot + end, '')
            else:
                nbot = wrt[2]
                wrt = wrt.replace("^" + nbot, '', 1)
        nbot = parse_latex(nbot)
        #print("Symb :", symb)
        #print("Lower :", wrt)
        #print("nbot :", nbot)
        partial_op = True
    #print(diff_op, partial_op)
    if diff_op or partial_op:
        wrt = sympy.Symbol(wrt)
        if (diff_op and frac.upper.start == frac.upper.stop
                and frac.upper.start.type == LaTeXLexer.LETTER
                and frac.upper.start.text == 'd'):
            return [wrt]
        elif (partial_op and frac.upper.start == frac.upper.stop
              and frac.upper.start.type == LaTeXLexer.SYMBOL
              and frac.upper.start.text == '\\partial'):
            return [wrt]
        upper_text = rule2text(frac.upper)
        ntop = "1"
        if "d^" in upper_text:
            if "^{" in upper_text:
                start = 'd^{'
                end = '}'
                ntop = upper_text[upper_text.find(start) + len(start) : upper_text.rfind(end)]
                upper_text = upper_text.replace(start[1:]+ntop+end, '')
            else:
                ntop = upper_text[2]
                upper_text = upper_text.replace("^" + ntop, '', 1)
        if "\\partial^" in upper_text:
            if "^{" in upper_text:
                start = '\\partial^{'
                end = '}'
                ntop = upper_text[upper_text.find(start) + len(start) : upper_text.rfind(end)]
                upper_text = upper_text.replace(start+ntop+end, 'd')
            else:
                ntop = upper_text[2]
                upper_text = upper_text.replace("^" + ntop, '', 1)
        ntop = parse_latex(ntop)
        #print("Upper:", upper_text)
        #print("ntop :", ntop)

        expr_top = None
        if diff_op and upper_text.startswith('d'):
            expr_top = parse_latex(upper_text[1:])
        if partial_op and upper_text.startswith('d'):
            expr_top = sympy.Function(parse_latex(upper_text[1:]))(wrt)
        #print("expr_top: ", expr_top)
        if expr_top:
            return sympy.Derivative(expr_top, (wrt, ntop))

    expr_top = convert_expr(frac.upper)
    expr_bot = convert_expr(frac.lower)
    inverse_denom = sympy.Pow(expr_bot, -1, evaluate=False)
    if expr_top == 1:
        return inverse_denom
    else:
        return sympy.Mul(expr_top, inverse_denom, evaluate=False)

def convert_binom(binom):
    expr_n = convert_expr(binom.n)
    expr_k = convert_expr(binom.k)
    return sympy.binomial(expr_n, expr_k, evaluate=False)

def convert_floor(floor):
    val = convert_expr(floor.val)
    return sympy.floor(val, evaluate=False)

def convert_ceil(ceil):
    val = convert_expr(ceil.val)
    return sympy.ceiling(val, evaluate=False)

def convert_delta(delta):
    x, y = convert_expr(delta.x), convert_expr(delta.y)
    return sympy.KroneckerDelta(x, y, evaluate=False)

def convert_func(func):
    if func.func_normal():
        if func.L_PAREN():  # function called with parenthesis
            arg = convert_func_arg(func.func_arg())
        else:
            arg = convert_func_arg(func.func_arg_noparens())

        name = func.func_normal().start.text[1:]

        # change arc<trig> -> a<trig>
        if name in ["arcsin", "arccos", "arctan", "arccsc", "arcsec", "arccot"]:
            name = "a" + name[3:]
            expr = getattr(sympy.functions, name)(arg, evaluate=False)
        if name in ["arsinh", "arcosh", "artanh", "arcsch", "arsech", "arcoth"]:
            name = "a" + name[2:]
            expr = getattr(sympy.functions, name)(arg, evaluate=False)

        if name == "exp":
            expr = sympy.exp(arg, evaluate=False)

        if (name == "log" or name == "ln"):
            if func.subexpr():
                if func.subexpr().expr():
                    base = convert_expr(func.subexpr().expr())
                elif func.subexpr().atom():
                    base = convert_atom(func.subexpr().atom())
            elif name == "log":
                base = 10
            elif name == "ln":
                base = sympy.E
            expr = sympy.log(arg, base, evaluate=False)
        
        if name == "Gamma":
            a = arg                
            if func.func_arg().func_arg():
                x = convert_func_arg(func.func_arg().func_arg())
                expr = sympy.uppergamma(a, x, evaluate=False)
            else:
                def _gamma(x):
                    return sympy.gamma(x, evaluate=False)
                if isinstance(a, MutableDenseMatrix):
                    expr = a.applyfunc(_gamma)
                elif isinstance(a, tuple):
                    expr = tuple(sympy.Array(a).applyfunc(_gamma).tolist())
                else:
                    expr = sympy.gamma(a, evaluate=False)

        if name == "gamma":
            a = arg
            x = convert_func_arg(func.func_arg().func_arg())
            expr = sympy.lowergamma(a, x, evaluate=False)

        if name == "Delta":
            pass

        if name == "nabla":
            pass

        if name == "zeta":
            s = arg
            if func.func_arg().func_arg():
                a = convert_func_arg(func.func_arg().func_arg())
                expr = sympy.zeta(s, a, evaluate=False)
            else:
                expr = sympy.zeta(s, evaluate=False)

        func_pow = None
        should_pow = True
        if func.supexpr():
            if func.supexpr().expr():
                func_pow = convert_expr(func.supexpr().expr())
            else:
                func_pow = convert_atom(func.supexpr().atom())

        if name in ["sin", "cos", "tan", "csc", "sec", "cot", "sinh", \
             "cosh", "tanh", "csch", "sech", "coth"]:
            if func_pow == -1:
                name = "a" + name
                should_pow = False
            expr = getattr(sympy.functions, name)(arg, evaluate=False)

        if func_pow and should_pow:
            expr = sympy.Pow(expr, func_pow, evaluate=False)

        return expr
    elif func.LETTER() or func.SYMBOL():
        if func.LETTER():
            fname = func.LETTER().getText()
        elif func.SYMBOL():
            fname = func.SYMBOL().getText()[1:]
        fname = str(fname)  # can't be unicode
        if func.subexpr():
            subscript = None
            if func.subexpr().expr():  # subscript is expr
                subscript = convert_expr(func.subexpr().expr())
            else:  # subscript is atom
                subscript = convert_atom(func.subexpr().atom())
            subscriptName = StrPrinter().doprint(subscript)
            fname += '_{' + subscriptName + '}'
        input_args = func.args()
        output_args = []
        while input_args.args():  # handle multiple arguments to function
            output_args.append(convert_expr(input_args.expr()))
            input_args = input_args.args()
        output_args.append(convert_expr(input_args.expr()))
        return sympy.Function(fname)(*output_args)
    elif func.FUNC_INT():
        return handle_integral(func)
    elif func.FUNC_SQRT():
        expr = convert_expr(func.base)
        if func.root:
            r = convert_expr(func.root)
            return sympy.root(expr, r)
        else:
            return sympy.sqrt(expr)
    elif func.FUNC_SUM():
        return handle_sum_or_prod(func, "summation")
    elif func.FUNC_PROD():
        return handle_sum_or_prod(func, "product")
    elif func.FUNC_LIM():
        return handle_limit(func)


def convert_func_arg(arg):
    if hasattr(arg, 'expr'):
        return convert_expr(arg.expr())
    else:
        return convert_mp(arg.mp_nofunc())


def handle_integral(func):
    if func.additive():
        integrand = convert_add(func.additive())
    elif func.frac():
        integrand = convert_frac(func.frac())
    else:
        integrand = 1

    int_var = None
    if func.DIFFERENTIAL():
        int_var = get_differential_var(func.DIFFERENTIAL())
    else:
        for sym in integrand.atoms(sympy.Symbol):
            s = str(sym)
            if len(s) > 1 and s[0] == 'd':
                if s[1] == '\\':
                    int_var = sympy.Symbol(s[2:])
                else:
                    int_var = sympy.Symbol(s[1:])
                int_sym = sym
        if int_var:
            integrand = integrand.subs(int_sym, 1)
        else:
            # Assume dx by default
            int_var = sympy.Symbol('x')

    if func.subexpr():
        if func.subexpr().atom():
            lower = convert_atom(func.subexpr().atom())
        else:
            lower = convert_expr(func.subexpr().expr())
        if func.supexpr().atom():
            upper = convert_atom(func.supexpr().atom())
        else:
            upper = convert_expr(func.supexpr().expr())
        return sympy.Integral(integrand, (int_var, lower, upper))
    else:
        return sympy.Integral(integrand, int_var)


def handle_sum_or_prod(func, name):
    val = convert_mp(func.mp())
    iter_var = convert_expr(func.subeq().equality().expr(0))
    start = convert_expr(func.subeq().equality().expr(1))
    if func.supexpr().expr():  # ^{expr}
        end = convert_expr(func.supexpr().expr())
    else:  # ^atom
        end = convert_atom(func.supexpr().atom())

    if name == "summation":
        return sympy.Sum(val, (iter_var, start, end))
    elif name == "product":
        return sympy.Product(val, (iter_var, start, end))


def handle_limit(func):
    sub = func.limit_sub()
    if sub.LETTER():
        var = sympy.Symbol(sub.LETTER().getText())
    elif sub.SYMBOL():
        var = sympy.Symbol(sub.SYMBOL().getText()[1:])
    else:
        var = sympy.Symbol('x')
    if sub.SUB():
        direction = "-"
    else:
        direction = "+"
    approaching = convert_expr(sub.expr())
    content = convert_mp(func.mp())

    return sympy.Limit(content, var, approaching, direction)


def get_differential_var(d):
    text = get_differential_var_str(d.getText())
    #print("Get Diff var: ", text)
    return sympy.Symbol(text)


def get_differential_var_str(text):
    #print("Text: ", text, '\\partial' in text)
    if '\\partial' in text:
        text = text[text.index('\\partial', 0)+8:]
    else:    
        for i in range(1, len(text)):
            c = text[i]
            if not (c == " " or c == "\r" or c == "\n" or c == "\t"):
                idx = i
                break
        text = text[idx:]
    if text[0] == "\\":
        text = text[1:]
    #print("Get Diff Var Str:", text)
    return text
