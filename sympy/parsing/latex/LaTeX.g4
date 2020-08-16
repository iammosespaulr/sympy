/*
 ANTLR4 LaTeX Math Grammar
 
 Ported from latex2sympy by @augustt198 https://github.com/augustt198/latex2sympy See license in
 LICENSE.txt
 */

/*
 After changing this file, it is necessary to run `python setup.py antlr` in the root directory of
 the repository. This will regenerate the code in `sympy/parsing/latex/_antlr/*.py`.
 */

grammar LaTeX;

options {
	language = Python2;
}

WS: [ \t\r\n]+ -> skip;
THINSPACE: ('\\,' | '\\thinspace') -> skip;
MEDSPACE: ('\\:' | '\\medspace') -> skip;
THICKSPACE: ('\\;' | '\\thickspace') -> skip;
QUAD: '\\quad' -> skip;
QQUAD: '\\qquad' -> skip;
NEGTHINSPACE: ('\\!' | '\\negthinspace') -> skip;
NEGMEDSPACE: '\\negmedspace' -> skip;
NEGTHICKSPACE: '\\negthickspace' -> skip;
CMD_LEFT: '\\left' -> skip;
CMD_RIGHT: '\\right' -> skip;

IGNORE:
	(
		'\\vrule'
		| '\\vcenter'
		| '\\vbox'
		| '\\vskip'
		| '\\vspace'
		| '\\hfil'
		| '\\*'
		| '\\-'
		| '\\.'
		| '\\/'
		| '\\"'
		| '\\('
		| '\\='
	) -> skip;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

PM: '\\pm';
MP: '\\mp';

L_PAREN: '(';
R_PAREN: ')';
L_BRACE: '{';
R_BRACE: '}';
L_BRACE_LITERAL: '\\{';
R_BRACE_LITERAL: '\\}';
L_BRACKET: '[';
R_BRACKET: ']';

BAR: '|';

R_BAR: '\\right|';
L_BAR: '\\left|';
LEFT_BRACKET: '\\left[';
RIGHT_BRACKET: '\\right]';

L_ANGLE: '\\langle';
R_ANGLE: '\\rangle';

L_L_ANGLE: '\\left\\angle';
R_R_ANGLE: '\\right\\angle';

PERIOD: '.';
BAR_VAL: '\\|';

FUNC_LIM: '\\lim';
LIM_APPROACH_SYM:
	'\\to'
	| '\\rightarrow'
	| '\\Rightarrow'
	| '\\longrightarrow'
	| '\\Longrightarrow';

FUNC_INT: '\\int';
FUNC_SUM: ('\\sum' | SIGMA);
FUNC_PROD: ('\\prod' | PI);

FUNC_EXP: '\\exp';
FUNC_LOG: '\\log';
FUNC_LN: '\\ln';

FUNC_SIN: '\\sin';
FUNC_COS: '\\cos';
FUNC_TAN: '\\tan';
FUNC_CSC: '\\csc';
FUNC_SEC: '\\sec';
FUNC_COT: '\\cot';

FUNC_ARCSIN: '\\arcsin';
FUNC_ARCCOS: '\\arccos';
FUNC_ARCTAN: '\\arctan';
FUNC_ARCCSC: '\\arccsc';
FUNC_ARCSEC: '\\arcsec';
FUNC_ARCCOT: '\\arccot';

FUNC_SINH: '\\sinh';
FUNC_COSH: '\\cosh';
FUNC_TANH: '\\tanh';
FUNC_CSCH: '\\csch';
FUNC_SECH: '\\sech';
FUNC_COTH: '\\coth';

FUNC_ARSINH: '\\arsinh';
FUNC_ARCOSH: '\\arcosh';
FUNC_ARTANH: '\\artanh';
FUNC_ARCSCH: '\\arcsch';
FUNC_ARSECH: '\\arsech';
FUNC_ARCOTH: '\\arcoth';

L_FLOOR: '\\lfloor';
R_FLOOR: '\\rfloor';
L_CEIL: '\\lceil';
R_CEIL: '\\rceil';

I_MATH: '\\imath';
J_MATH: '\\jmath';

DELTA: '\\Delta';
LOWER_DELTA: '\\delta';
FUNC_GAMMA: '\\Gamma';
LOWER_GAMMA: '\\gamma';
NABLA: '\\nabla';
SIGMA: '\\Sigma';
LOWER_SIGMA: '\\sigma';
PI: '\\Pi';
ZETA: '\\zeta';

BEGIN_ARR:
	'\\begin' L_BRACE (LETTER | '*')+ R_BRACE (
		L_BRACE LETTER* R_BRACE
	)?;
END_ARR: '\\end' L_BRACE (LETTER | '*')+ R_BRACE;

O_INT: '\\oint';
O_TIMES: '\\otimes';
O_PLUS: '\\oplus';
O_MINUS: '\\ominus';
O_DOT: '\\odot';
BIG_O_PLUS: '\\bigoplus';
BIG_O_TIMES: '\\bigotimes';
O_SLASH: '\\oslash';

TILDE: '\\tilde';
VEC: '\\vec';
HAT: '\\hat';
HBAR: '\\hbar';
DAGGER: '\\dagger';
STAR: '\\star';

DOT: '\\dot';
DDOT: '\\ddot';
PRIME: '\\prime';

CIRC: '\\circ';

LDOTS: '\\ldots';
VDOTS: '\\vdots';
DOTS: '\\dots';
CDOTS: '\\cdots';

WIDE_HAT: '\\widehat';
UNDERLINE: '\\underline';
OVERBRACE: '\\overbrace';
OVER_LEFTARROW: '\\overleftarrow';

NOT: '\\not';
VAR_NOTHING: '\\varnothing';
BIG_VEE: '\\bigvee';
CO_PRODUCT: '\\coprod';
NEG: '\\neg';
MAPS_TO: '\\mapsto';
BIG_WEDGE: '\\bigwedge';
CURLY_VEE: '\\curlyvee';
CURLY_WEDGE: '\\curlywedge';
N_I: '\\ni';
SUBSET_NEQ: '\\subsetneq';
SQ_SUBSET: '\\sqsubset';
SQ_SUBSET_EQ: '\\sqsupseteq';
SQ_SUPERSET: '\\sqsupset';
SQ_SUPERSET_EQ: '\\sqsubseteq';
COMPLEMENT: '\\complement';
SUPERSET_NEQ: '\\supsetneq';
SQ_CUP: '\\sqcup';
SQ_CAP: '\\sqcap';
NEXISTS: '\\nexists';
N_SUBSET_EQ: '\\nsubseteq';
N_SUPERSET_EQ: '\\nsupseteq';
UNDER_BRACE: '\\underbrace';
UNDER_SET: '\\underset';
BIG_CUP: '\\bigcup';
BIG_CAP: '\\bigcap';
LONG_MAPS_TO: '\\longmapsto';
THEREFORE: '\\therefore';
BECAUSE: '\\because';
EMPTY_SET: '\\emptyset';
SUBSET: '\\subset';
SUPERSET: '\\supset';
SUBSET_EQ: '\\subseteq';
SUPERSET_EQ: '\\supseteq';
NOT_IN: '\\notin';
EXISTS: '\\exists';
FOR_ALL: '\\forall';
CUP: '\\cup';
CAP: '\\cap';
OVERLINE: '\\overline';
IN: '\\in';
WEDGE: '\\wedge';
VEE: '\\vee';

SMILE: '\\smile';
FROWN: '\\frown';
MATH_BB: '\\mathbb';
STACK_REL: '\\stackrel';
IM: '\\Im';
RE: '\\Re';

MULTI_COL: '\\multicolumn';
MULTI_ROW: '\\multirow';

FUNC_SQRT: '\\sqrt';
LONG_DIV: '\\longdiv';

CMD_TIMES: '\\times';
CMD_CDOT: '\\cdot';

CMD_DIV: '\\div';
CMD_FRAC: ('\\frac' | '\\tfrac' | '\\dfrac');

CMD_BINOM: ('\\binom' | '\\dbinom' | '\\tbinom');

CMD_MATHIT: '\\mathit';

UNDERSCORE: '_';
CARET: '^';
COLON: ':';

fragment WS_CHAR: [ \t\r\n];
DIFFERENTIAL:
	'd' (
		WS_CHAR*? CARET (
			(NUMBER | LETTER)
			| L_BRACE (NUMBER | LETTER) R_BRACE
		)
	)? WS_CHAR*? ([a-zA-Z] | '\\' [a-zA-Z]+) (
		WS_CHAR*? CARET (
			(NUMBER | LETTER)
			| L_BRACE (NUMBER | LETTER) R_BRACE
		)
	)?;

PARTIAL: '\\partial';

LETTER: [a-zA-Z];
fragment DIGIT: [0-9]+;
//Real number as defined in CFITSIO Lexical Parser
fragment FLOAT: ([0-9]* [.][0-9]+)
	| ([0-9]* [.]* [0-9]+ [eEdD][+-]? [0-9]+)
	| ([0-9]* [.]);
NUMBER: (DIGIT | FLOAT);

EQUAL: (('&' WS_CHAR*?)? '=') | ('=' (WS_CHAR*? '&')?);
NEQ: '\\neq';

LT: '<';
LTE: ('\\leq' | 'le' | LTE_Q | LTE_S);
LTE_Q: '\\leqq';
LTE_S: '\\leqslant';

GT: '>';
GTE: ('\\geq' | 'ge' | GTE_Q | GTE_S);
GTE_Q: '\\geqq';
GTE_S: '\\geqslant';

LL: '\\ll';
GG: '\\gg';
LLL: '\\lll';
GGG: '\\ggg';

BANG: '!';

SYMBOL: '\\' [a-zA-Z]+;

math: relation;

relation:
	relation (EQUAL | LT | LTE | GT | GTE | NEQ) relation
	| expr;

equality: expr EQUAL expr;

expr: additive;

additive: additive (ADD | SUB) additive | mp;

// mult part
mp:
	mp (MUL | CMD_TIMES | CMD_CDOT | DIV | CMD_DIV | COLON) mp
	| unary;

mp_nofunc:
	mp_nofunc (
		MUL
		| CMD_TIMES
		| CMD_CDOT
		| DIV
		| CMD_DIV
		| COLON
	) mp_nofunc
	| unary_nofunc;

unary: (ADD | SUB) unary | postfix+;

unary_nofunc:
	(ADD | SUB) unary_nofunc
	| postfix postfix_nofunc*;

postfix: exp postfix_op*;
postfix_nofunc: exp_nofunc postfix_op*;
postfix_op: BANG | eval_at;

eval_at:
	BAR (eval_at_sup | eval_at_sub | eval_at_sup eval_at_sub);

eval_at_sub: UNDERSCORE L_BRACE (expr | equality) R_BRACE;

eval_at_sup: CARET L_BRACE (expr | equality) R_BRACE;

exp: exp CARET (atom | L_BRACE expr R_BRACE) subexpr? | comp;

exp_nofunc:
	exp_nofunc CARET (atom | L_BRACE expr R_BRACE) subexpr?
	| comp_nofunc;

comp:
	group
	| abs_group
	| func
	| atom
	| frac
	| binom
	| floor
	| ceil
	| delta;

comp_nofunc:
	group
	| abs_group
	| atom
	| frac
	| binom
	| floor
	| ceil
	| delta;

group:
	L_PAREN expr R_PAREN
	| L_BRACKET expr R_BRACKET
	| L_BRACE expr R_BRACE
	| L_BRACE_LITERAL expr R_BRACE_LITERAL
	| L_BRACE_LITERAL expr PERIOD
	| PERIOD expr R_BRACE_LITERAL
	| L_PAREN expr PERIOD
	| PERIOD expr R_PAREN;

abs_group: BAR expr BAR;

atom: (LETTER | SYMBOL) subexpr?
	| NUMBER
	| DIFFERENTIAL
	| matrix
	| determinant
	| array
	| mathit
	| prime
	| dot
	| ddot
	| angularunit
	| bra
	| ket;

bra: L_ANGLE expr (R_BAR | BAR);

ket: (L_BAR | BAR) expr R_ANGLE;

angularunit: (NUMBER | LETTER) CARET L_BRACE CIRC R_BRACE;

preprime:
	(LETTER | SYMBOL) (
		(CARET L_BRACE PRIME* R_BRACE)
		| '\''*
		| '’'*
	);
prime: ( preprime L_PAREN expr R_PAREN);

dot: DOT ((L_BRACE expr R_BRACE) | atom);

ddot: DDOT ((L_BRACE expr R_BRACE) | atom);

matrix:
	LEFT_BRACKET (BEGIN_ARR)? array_elements (
		('\\\\') array_elements
	)*? (END_ARR)? RIGHT_BRACKET;

determinant:
	L_BAR (BEGIN_ARR)? array_elements (('\\\\') array_elements)*? (
		END_ARR
	)? R_BAR;

mathit: CMD_MATHIT L_BRACE mathit_text R_BRACE;
mathit_text: (NUMBER | LETTER)+;

TEXT:
	'\\text' (WS)*? L_BRACE (WS)*? (NUMBER | LETTER)+ (WS)*? R_BRACE (
		WS
	)*? -> skip;

array:
	BEGIN_ARR array_elements (('\\\\') array_elements)*? END_ARR;

array_elements: (relation) (('&' | ',')? (relation))*?;

frac:
	CMD_FRAC L_BRACE upper = expr R_BRACE L_BRACE lower = expr R_BRACE;

binom:
	CMD_BINOM L_BRACE n = expr R_BRACE L_BRACE k = expr R_BRACE;

floor: L_FLOOR val = expr R_FLOOR;

ceil: L_CEIL val = expr R_CEIL;

delta: LOWER_DELTA UNDERSCORE L_BRACE x = expr y = expr R_BRACE;

func_normal:
	FUNC_EXP
	| FUNC_LOG
	| FUNC_LN
	| FUNC_SIN
	| FUNC_COS
	| FUNC_TAN
	| FUNC_CSC
	| FUNC_SEC
	| FUNC_COT
	| FUNC_ARCSIN
	| FUNC_ARCCOS
	| FUNC_ARCTAN
	| FUNC_ARCCSC
	| FUNC_ARCSEC
	| FUNC_ARCCOT
	| FUNC_SINH
	| FUNC_COSH
	| FUNC_TANH
	| FUNC_CSCH
	| FUNC_SECH
	| FUNC_COTH
	| FUNC_ARSINH
	| FUNC_ARCOSH
	| FUNC_ARTANH
	| FUNC_ARCSCH
	| FUNC_ARSECH
	| FUNC_ARCOTH
	| FUNC_GAMMA
	| LOWER_GAMMA
	| ZETA
	| NABLA
	| DELTA
	| LOWER_SIGMA
	| VEC
	| HAT;

func:
	func_normal (subexpr? supexpr? | supexpr? subexpr?) (
		L_PAREN func_arg R_PAREN
		| func_arg_noparens
	)
	| (LETTER | SYMBOL) subexpr? // e.g. f(x)
	L_PAREN args R_PAREN
	| FUNC_INT (subexpr supexpr | supexpr subexpr)? (
		additive? DIFFERENTIAL
		| frac
		| additive
	)
	| FUNC_SQRT (L_BRACKET root = expr R_BRACKET)? L_BRACE base = expr R_BRACE
	| (FUNC_SUM | FUNC_PROD) (subeq supexpr | supexpr subeq) mp
	| FUNC_LIM limit_sub mp;

args: (expr ',' args) | expr;

limit_sub:
	('\\limits')? UNDERSCORE L_BRACE (LETTER | SYMBOL) LIM_APPROACH_SYM expr (
		CARET L_BRACE (ADD | SUB) R_BRACE
	)? R_BRACE;

func_arg: expr | (expr ',' func_arg);
func_arg_noparens: mp_nofunc;

subexpr: UNDERSCORE (atom | L_BRACE expr R_BRACE);
supexpr: CARET (atom | L_BRACE expr R_BRACE);

subeq: UNDERSCORE L_BRACE equality R_BRACE;
supeq: UNDERSCORE L_BRACE equality R_BRACE;
