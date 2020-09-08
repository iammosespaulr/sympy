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
		| '&'
		| '\\mathcal'
		| '\\mathscr'
		| '\\mathit'
		| '\\mathnormal'
		| '\\mathrm'
		| '\\mathbf'
		| '\\mathsf'
		| '\\mathtt'
		| '\\mathcal'
		| '\\mathfrak'
		| '\\tiny'
		| '\\boldsymbol'
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

L_ANGLE: '\\langle';
R_ANGLE: '\\rangle';

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
FUNC_IINT: '\\iint';
FUNC_IIINT: '\\iiint';
FUNC_IIIINT: '\\iiiint';

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

//DELTA: '\\Delta'; LOWER_DELTA: '\\delta'; FUNC_GAMMA: '\\Gamma'; LOWER_GAMMA: '\\gamma'; NABLA:
// '\\nabla';
SIGMA: '\\Sigma';
//LOWER_SIGMA: '\\sigma'; 
PI: '\\Pi';
//ZETA: '\\zeta';

OP_NAME: '\\operatorname';

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
MATH_BB: '\\mathbb' -> skip;
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

UNDERSCORE: '_';
CARET: '^';
COLON: ':';

fragment WS_CHAR: [ \t\r\n];
DIFFERENTIAL:
	('d' | PARTIAL) (
		WS_CHAR*? CARET (
			(NUMBER | LETTER)
			| L_BRACE (NUMBER | LETTER) R_BRACE
		)
	)? WS_CHAR*? (LETTER | SYMBOL) (
		WS_CHAR*? CARET (
			(NUMBER | LETTER)
			| L_BRACE (NUMBER | LETTER) R_BRACE
		)
	)?;

PARTIAL: '\\partial';

LETTER: [a-zA-Z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u024F];
TEXT_STUFF: [_.,?"'/$];
LETTERS_ALL_LANG:
	[\u02C6-\u02D1\u02E0-\u02E4\u02EC\u02EE\u0370-\u0374\u0376\u0377\u037A-\u037D\u0386\u0388-\u038A\u038C\u038E-\u03A1\u03A3-\u03F5\u03F7-\u0481\u048A-\u0527\u0531-\u0556\u0559\u0561-\u0587\u05D0-\u05EA\u05F0-\u05F2\u0620-\u064A\u066E\u066F\u0671-\u06D3\u06D5\u06E5\u06E6\u06EE\u06EF\u06FA-\u06FC\u06FF\u0710\u0712-\u072F\u074D-\u07A5\u07B1\u07CA-\u07EA\u07F4\u07F5\u07FA\u0800-\u0815\u081A\u0824\u0828\u0840-\u0858\u08A0\u08A2-\u08AC\u0904-\u0939\u093D\u0950\u0958-\u0961\u0971-\u0977\u0979-\u097F\u0985-\u098C\u098F\u0990\u0993-\u09A8\u09AA-\u09B0\u09B2\u09B6-\u09B9\u09BD\u09CE\u09DC\u09DD\u09DF-\u09E1\u09F0\u09F1\u0A05-\u0A0A\u0A0F\u0A10\u0A13-\u0A28\u0A2A-\u0A30\u0A32\u0A33\u0A35\u0A36\u0A38\u0A39\u0A59-\u0A5C\u0A5E\u0A72-\u0A74\u0A85-\u0A8D\u0A8F-\u0A91\u0A93-\u0AA8\u0AAA-\u0AB0\u0AB2\u0AB3\u0AB5-\u0AB9\u0ABD\u0AD0\u0AE0\u0AE1\u0B05-\u0B0C\u0B0F\u0B10\u0B13-\u0B28\u0B2A-\u0B30\u0B32\u0B33\u0B35-\u0B39\u0B3D\u0B5C\u0B5D\u0B5F-\u0B61\u0B71\u0B83\u0B85-\u0B8A\u0B8E-\u0B90\u0B92-\u0B95\u0B99\u0B9A\u0B9C\u0B9E\u0B9F\u0BA3\u0BA4\u0BA8-\u0BAA\u0BAE-\u0BB9\u0BD0\u0C05-\u0C0C\u0C0E-\u0C10\u0C12-\u0C28\u0C2A-\u0C33\u0C35-\u0C39\u0C3D\u0C58\u0C59\u0C60\u0C61\u0C85-\u0C8C\u0C8E-\u0C90\u0C92-\u0CA8\u0CAA-\u0CB3\u0CB5-\u0CB9\u0CBD\u0CDE\u0CE0\u0CE1\u0CF1\u0CF2\u0D05-\u0D0C\u0D0E-\u0D10\u0D12-\u0D3A\u0D3D\u0D4E\u0D60\u0D61\u0D7A-\u0D7F\u0D85-\u0D96\u0D9A-\u0DB1\u0DB3-\u0DBB\u0DBD\u0DC0-\u0DC6\u0E01-\u0E30\u0E32\u0E33\u0E40-\u0E46\u0E81\u0E82\u0E84\u0E87\u0E88\u0E8A\u0E8D\u0E94-\u0E97\u0E99-\u0E9F\u0EA1-\u0EA3\u0EA5\u0EA7\u0EAA\u0EAB\u0EAD-\u0EB0\u0EB2\u0EB3\u0EBD\u0EC0-\u0EC4\u0EC6\u0EDC-\u0EDF\u0F00\u0F40-\u0F47\u0F49-\u0F6C\u0F88-\u0F8C\u1000-\u102A\u103F\u1050-\u1055\u105A-\u105D\u1061\u1065\u1066\u106E-\u1070\u1075-\u1081\u108E\u10A0-\u10C5\u10C7\u10CD\u10D0-\u10FA\u10FC-\u1248\u124A-\u124D\u1250-\u1256\u1258\u125A-\u125D\u1260-\u1288\u128A-\u128D\u1290-\u12B0\u12B2-\u12B5\u12B8-\u12BE\u12C0\u12C2-\u12C5\u12C8-\u12D6\u12D8-\u1310\u1312-\u1315\u1318-\u135A\u1380-\u138F\u13A0-\u13F4\u1401-\u166C\u166F-\u167F\u1681-\u169A\u16A0-\u16EA\u1700-\u170C\u170E-\u1711\u1720-\u1731\u1740-\u1751\u1760-\u176C\u176E-\u1770\u1780-\u17B3\u17D7\u17DC\u1820-\u1877\u1880-\u18A8\u18AA\u18B0-\u18F5\u1900-\u191C\u1950-\u196D\u1970-\u1974\u1980-\u19AB\u19C1-\u19C7\u1A00-\u1A16\u1A20-\u1A54\u1AA7\u1B05-\u1B33\u1B45-\u1B4B\u1B83-\u1BA0\u1BAE\u1BAF\u1BBA-\u1BE5\u1C00-\u1C23\u1C4D-\u1C4F\u1C5A-\u1C7D\u1CE9-\u1CEC\u1CEE-\u1CF1\u1CF5\u1CF6\u1D00-\u1DBF\u1E00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FBE\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC\u1FF2-\u1FF4\u1FF6-\u1FFC\u2071\u207F\u2090-\u209C\u2102\u2107\u210A-\u2113\u2115\u2119-\u211D\u2124\u2126\u2128\u212A-\u212D\u212F-\u2139\u213C-\u213F\u2145-\u2149\u214E\u2183\u2184\u2C00-\u2C2E\u2C30-\u2C5E\u2C60-\u2CE4\u2CEB-\u2CEE\u2CF2\u2CF3\u2D00-\u2D25\u2D27\u2D2D\u2D30-\u2D67\u2D6F\u2D80-\u2D96\u2DA0-\u2DA6\u2DA8-\u2DAE\u2DB0-\u2DB6\u2DB8-\u2DBE\u2DC0-\u2DC6\u2DC8-\u2DCE\u2DD0-\u2DD6\u2DD8-\u2DDE\u2E2F\u3005\u3006\u3031-\u3035\u303B\u303C\u3041-\u3096\u309D-\u309F\u30A1-\u30FA\u30FC-\u30FF\u3105-\u312D\u3131-\u318E\u31A0-\u31BA\u31F0-\u31FF\u3400-\u4DB5\u4E00-\u9FCC\uA000-\uA48C\uA4D0-\uA4FD\uA500-\uA60C\uA610-\uA61F\uA62A\uA62B\uA640-\uA66E\uA67F-\uA697\uA6A0-\uA6E5\uA717-\uA71F\uA722-\uA788\uA78B-\uA78E\uA790-\uA793\uA7A0-\uA7AA\uA7F8-\uA801\uA803-\uA805\uA807-\uA80A\uA80C-\uA822\uA840-\uA873\uA882-\uA8B3\uA8F2-\uA8F7\uA8FB\uA90A-\uA925\uA930-\uA946\uA960-\uA97C\uA984-\uA9B2\uA9CF\uAA00-\uAA28\uAA40-\uAA42\uAA44-\uAA4B\uAA60-\uAA76\uAA7A\uAA80-\uAAAF\uAAB1\uAAB5\uAAB6\uAAB9-\uAABD\uAAC0\uAAC2\uAADB-\uAADD\uAAE0-\uAAEA\uAAF2-\uAAF4\uAB01-\uAB06\uAB09-\uAB0E\uAB11-\uAB16\uAB20-\uAB26\uAB28-\uAB2E\uABC0-\uABE2\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uF900-\uFA6D\uFA70-\uFAD9\uFB00-\uFB06\uFB13-\uFB17\uFB1D\uFB1F-\uFB28\uFB2A-\uFB36\uFB38-\uFB3C\uFB3E\uFB40\uFB41\uFB43\uFB44\uFB46-\uFBB1\uFBD3-\uFD3D\uFD50-\uFD8F\uFD92-\uFDC7\uFDF0-\uFDFB\uFE70-\uFE74\uFE76-\uFEFC\uFF21-\uFF3A\uFF41-\uFF5A\uFF66-\uFFBE\uFFC2-\uFFC7\uFFCA-\uFFCF\uFFD2-\uFFD7\uFFDA-\uFFDC]
		;
fragment DIGIT: [0-9]+;
//Real number as defined in CFITSIO Lexical Parser
fragment FLOAT: ([0-9]* [.][0-9]+)
	| ([0-9]* [.]* [0-9]+ [eEdD][+-]? [0-9]+)
	| ([0-9]* [.]);
NUMBER: (DIGIT | FLOAT);

DAYS: [0-3][0-9];
MONTH: [0-1][0-9];
YEAR: [0-9][0-9][0-9][0-9];

DATE: (
		(
			(MONTH WS_CHAR*? [.] WS_CHAR*? DAYS WS_CHAR*?)
			| (DAYS WS_CHAR*? [.] WS_CHAR*? MONTH WS_CHAR*?)
		) [.] WS_CHAR*? YEAR
	)
	| (
		YEAR WS_CHAR*? [.] (
			(WS_CHAR*? MONTH WS_CHAR*? [.] WS_CHAR*? DAYS)
			| (WS_CHAR*? DAYS WS_CHAR*? [.] WS_CHAR*? MONTH)
		)
	);

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
	| func_multi
	| atom
	| frac
	| binom
	| floor
	| ceil;
//| delta;

comp_nofunc:
	group
	| abs_group
	| atom
	| frac
	| binom
	| floor
	| ceil;
//| delta;

group:
	L_PAREN (expr | array_elements) R_PAREN
	| L_BRACKET (expr | array_elements) R_BRACKET
	| L_BRACE (expr | array_elements) R_BRACE
	| L_BRACE_LITERAL (expr | array_elements) R_BRACE_LITERAL
	| L_BRACE_LITERAL (expr | array_elements) PERIOD
	| PERIOD (expr | array_elements) R_BRACE_LITERAL
	| L_PAREN (expr | array_elements) PERIOD
	| PERIOD (expr | array_elements) R_PAREN;

abs_group: BAR expr BAR;

atom: (LETTER | SYMBOL) subexpr?
	| NUMBER
	| DIFFERENTIAL
	| PARTIAL
	| determinant
	| array
	| prime
	| dot
	| ddot
	| angularunit
	| bra
	| ket
	| date;

operation:
	OP_NAME (
		L_BRACE (
			DIFFERENTIAL? (NUMBER | LETTER)+
			| SYMBOL
			| func_normal
		) R_BRACE
		| (NUMBER | LETTER | SYMBOL | func_normal)
	);

date: DATE;

bra: L_ANGLE expr (R_BAR | BAR);

ket: (L_BAR | BAR) expr R_ANGLE;

angularunit: (NUMBER | LETTER) CARET L_BRACE CIRC R_BRACE;

preprime: (LETTER | SYMBOL) (
		('\'' | '’')*
		| ((CARET L_BRACE PRIME* R_BRACE) | (CARET PRIME))
	);
prime: preprime (L_PAREN expr R_PAREN)?;

dot: DOT ((L_BRACE expr R_BRACE) | atom);

ddot: DDOT ((L_BRACE expr R_BRACE) | atom);

determinant:
	L_BAR (BEGIN_ARR)? array_elements (('\\\\') array_elements)*? (
		END_ARR
	)? R_BAR;

TEXT:
	'\\text' (WS)*? L_BRACE (WS)*? (
		NUMBER
		| LETTER
		| TEXT_STUFF
		| LETTERS_ALL_LANG
		| (WS)
	)+ (WS)*? R_BRACE (WS)*? -> skip;

array:
	BEGIN_ARR array_elements (('\\\\') array_elements)*? END_ARR;

array_elements: (relation) (('&' | (',' ('&')?))? (relation))*?;

frac:
	CMD_FRAC L_BRACE upper = expr R_BRACE L_BRACE lower = expr R_BRACE;

binom:
	CMD_BINOM L_BRACE n = expr R_BRACE L_BRACE k = expr R_BRACE;

floor: L_FLOOR val = expr R_FLOOR;

ceil: L_CEIL val = expr R_CEIL;

//delta: LOWER_DELTA UNDERSCORE L_BRACE x = expr y = expr R_BRACE;

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
	//| FUNC_GAMMA | LOWER_GAMMA | ZETA | NABLA | DELTA | LOWER_SIGMA
	| VEC
	| HAT
	| operation;

func:
	func_normal (subexpr? supexpr? | supexpr? subexpr?) (
		L_PAREN func_arg R_PAREN
		| func_arg_noparens
	)
	| (LETTER | SYMBOL) subexpr? // e.g. f(x)
	L_PAREN args R_PAREN
	| FUNC_INT (subexpr supexpr | supexpr subexpr)? (
		(additive? DIFFERENTIAL)
		| frac
		| additive
	)
	| FUNC_SQRT (L_BRACKET root = expr R_BRACKET)? L_BRACE base = expr R_BRACE
	| (FUNC_SUM | FUNC_PROD) (subeq supexpr | supexpr subeq) mp
	| FUNC_LIM limit_sub mp;

func_multi:
	(
		FUNC_IINT (subexpr supexpr | supexpr subexpr)? (
			(additive? DIFFERENTIAL DIFFERENTIAL)
			| frac
			| additive
		)
	)
	| (
		FUNC_IIINT (subexpr supexpr | supexpr subexpr)? (
			(additive? DIFFERENTIAL DIFFERENTIAL DIFFERENTIAL)
			| frac
			| additive
		)
	)
	| (
		FUNC_IIIINT (subexpr supexpr | supexpr subexpr)? (
			(
				additive? DIFFERENTIAL DIFFERENTIAL DIFFERENTIAL DIFFERENTIAL
			)
			| frac
			| additive
		)
	);

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
