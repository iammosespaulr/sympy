# Generated from /Users/mosespaul/Desktop/Coding/GSoC/sympy2/sympy/parsing/latex/LaTeX.g4 by ANTLR 4.8
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\u00c6\u01fb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write(u"d\n\3\3\3\7\3g\n\3\f\3\16\3j\13\3\3\4\3\4\3\4\3\4\3\5")
        buf.write(u"\3\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6x\n\6\f\6\16\6{\13\6")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0083\n\7\f\7\16\7\u0086")
        buf.write(u"\13\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u008e\n\b\f\b\16\b")
        buf.write(u"\u0091\13\b\3\t\3\t\3\t\6\t\u0096\n\t\r\t\16\t\u0097")
        buf.write(u"\5\t\u009a\n\t\3\n\3\n\3\n\3\n\7\n\u00a0\n\n\f\n\16\n")
        buf.write(u"\u00a3\13\n\5\n\u00a5\n\n\3\13\3\13\7\13\u00a9\n\13\f")
        buf.write(u"\13\16\13\u00ac\13\13\3\f\3\f\7\f\u00b0\n\f\f\f\16\f")
        buf.write(u"\u00b3\13\f\3\r\3\r\5\r\u00b7\n\r\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\5\16\u00bf\n\16\3\17\3\17\3\17\3\17\5\17\u00c5")
        buf.write(u"\n\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u00cd\n\20\3")
        buf.write(u"\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\5\21\u00db\n\21\3\21\5\21\u00de\n\21\7\21\u00e0")
        buf.write(u"\n\21\f\21\16\21\u00e3\13\21\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\3\22\3\22\3\22\5\22\u00ef\n\22\3\22\5\22\u00f2")
        buf.write(u"\n\22\7\22\u00f4\n\22\f\22\16\22\u00f7\13\22\3\23\3\23")
        buf.write(u"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0102\n\23\3")
        buf.write(u"\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u010c\n\24")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\5\25\u011a\n\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write(u"\5\27\u0122\n\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u012a")
        buf.write(u"\n\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\33\3\33\3\33\7\33\u013c\n\33\f\33")
        buf.write(u"\16\33\u013f\13\33\5\33\u0141\n\33\3\34\3\34\3\34\3\34")
        buf.write(u"\7\34\u0147\n\34\f\34\16\34\u014a\13\34\3\34\3\34\3\35")
        buf.write(u"\3\35\5\35\u0150\n\35\3\35\7\35\u0153\n\35\f\35\16\35")
        buf.write(u"\u0156\13\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write(u"\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$")
        buf.write(u"\5$\u017b\n$\3$\5$\u017e\n$\3$\5$\u0181\n$\3$\5$\u0184")
        buf.write(u"\n$\5$\u0186\n$\3$\3$\3$\3$\3$\5$\u018d\n$\3$\3$\5$\u0191")
        buf.write(u"\n$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u019e\n$\3$\5")
        buf.write(u"$\u01a1\n$\3$\3$\3$\5$\u01a6\n$\3$\3$\3$\3$\3$\5$\u01ad")
        buf.write(u"\n$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01ba\n$\3$\3")
        buf.write(u"$\3$\3$\3$\3$\5$\u01c2\n$\3%\3%\3%\3%\3%\5%\u01c9\n%")
        buf.write(u"\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01d4\n&\3&\3&\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\5\'\u01dd\n\'\3(\3(\3)\3)\3)\3)\3)\3)\5")
        buf.write(u")\u01e7\n)\3*\3*\3*\3*\3*\3*\5*\u01ef\n*\3+\3+\3+\3+")
        buf.write(u"\3+\3,\3,\3,\3,\3,\3,\4\u0148\u0154\b\4\n\f\16 \"-\2")
        buf.write(u"\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write(u"\64\668:<>@BDFHJLNPRTV\2\13\4\2\u00b6\u00b6\u00c3\u00c3")
        buf.write(u"\3\2\17\20\5\2\21\22\u00a7\u00a9\u00b1\u00b1\4\2\u00b4")
        buf.write(u"\u00b4\u00c6\u00c6\3\2\u00b4\u00b5\4\2\3\3\5\5\3\2\u00ab")
        buf.write(u"\u00ad\4\2*DNN\3\2()\2\u021d\2X\3\2\2\2\4Z\3\2\2\2\6")
        buf.write(u"k\3\2\2\2\bo\3\2\2\2\nq\3\2\2\2\f|\3\2\2\2\16\u0087\3")
        buf.write(u"\2\2\2\20\u0099\3\2\2\2\22\u00a4\3\2\2\2\24\u00a6\3\2")
        buf.write(u"\2\2\26\u00ad\3\2\2\2\30\u00b6\3\2\2\2\32\u00b8\3\2\2")
        buf.write(u"\2\34\u00c0\3\2\2\2\36\u00c8\3\2\2\2 \u00d0\3\2\2\2\"")
        buf.write(u"\u00e4\3\2\2\2$\u0101\3\2\2\2&\u010b\3\2\2\2(\u0119\3")
        buf.write(u"\2\2\2*\u011b\3\2\2\2,\u0129\3\2\2\2.\u012b\3\2\2\2\60")
        buf.write(u"\u012f\3\2\2\2\62\u0133\3\2\2\2\64\u0140\3\2\2\2\66\u0142")
        buf.write(u"\3\2\2\28\u014d\3\2\2\2:\u0157\3\2\2\2<\u015f\3\2\2\2")
        buf.write(u">\u0167\3\2\2\2@\u016b\3\2\2\2B\u016f\3\2\2\2D\u0176")
        buf.write(u"\3\2\2\2F\u01c1\3\2\2\2H\u01c8\3\2\2\2J\u01ca\3\2\2\2")
        buf.write(u"L\u01dc\3\2\2\2N\u01de\3\2\2\2P\u01e0\3\2\2\2R\u01e8")
        buf.write(u"\3\2\2\2T\u01f0\3\2\2\2V\u01f5\3\2\2\2XY\5\4\3\2Y\3\3")
        buf.write(u"\2\2\2Z[\b\3\1\2[\\\5\b\5\2\\h\3\2\2\2]c\f\4\2\2^d\t")
        buf.write(u"\2\2\2_d\7\u00b7\2\2`d\7\u00b8\2\2ad\7\u00b9\2\2bd\7")
        buf.write(u"\u00ba\2\2c^\3\2\2\2c_\3\2\2\2c`\3\2\2\2ca\3\2\2\2cb")
        buf.write(u"\3\2\2\2de\3\2\2\2eg\5\4\3\5f]\3\2\2\2gj\3\2\2\2hf\3")
        buf.write(u"\2\2\2hi\3\2\2\2i\5\3\2\2\2jh\3\2\2\2kl\5\b\5\2lm\t\2")
        buf.write(u"\2\2mn\5\b\5\2n\7\3\2\2\2op\5\n\6\2p\t\3\2\2\2qr\b\6")
        buf.write(u"\1\2rs\5\f\7\2sy\3\2\2\2tu\f\4\2\2uv\t\3\2\2vx\5\n\6")
        buf.write(u"\5wt\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\13\3\2\2")
        buf.write(u"\2{y\3\2\2\2|}\b\7\1\2}~\5\20\t\2~\u0084\3\2\2\2\177")
        buf.write(u"\u0080\f\4\2\2\u0080\u0081\t\4\2\2\u0081\u0083\5\f\7")
        buf.write(u"\5\u0082\177\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082")
        buf.write(u"\3\2\2\2\u0084\u0085\3\2\2\2\u0085\r\3\2\2\2\u0086\u0084")
        buf.write(u"\3\2\2\2\u0087\u0088\b\b\1\2\u0088\u0089\5\22\n\2\u0089")
        buf.write(u"\u008f\3\2\2\2\u008a\u008b\f\4\2\2\u008b\u008c\t\4\2")
        buf.write(u"\2\u008c\u008e\5\16\b\5\u008d\u008a\3\2\2\2\u008e\u0091")
        buf.write(u"\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write(u"\17\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\t\3\2\2\u0093")
        buf.write(u"\u009a\5\20\t\2\u0094\u0096\5\24\13\2\u0095\u0094\3\2")
        buf.write(u"\2\2\u0096\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098")
        buf.write(u"\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0092\3\2\2\2\u0099")
        buf.write(u"\u0095\3\2\2\2\u009a\21\3\2\2\2\u009b\u009c\t\3\2\2\u009c")
        buf.write(u"\u00a5\5\22\n\2\u009d\u00a1\5\24\13\2\u009e\u00a0\5\26")
        buf.write(u"\f\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f")
        buf.write(u"\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3")
        buf.write(u"\u00a1\3\2\2\2\u00a4\u009b\3\2\2\2\u00a4\u009d\3\2\2")
        buf.write(u"\2\u00a5\23\3\2\2\2\u00a6\u00aa\5 \21\2\u00a7\u00a9\5")
        buf.write(u"\30\r\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write(u"\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\25\3\2\2\2\u00ac")
        buf.write(u"\u00aa\3\2\2\2\u00ad\u00b1\5\"\22\2\u00ae\u00b0\5\30")
        buf.write(u"\r\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af")
        buf.write(u"\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\27\3\2\2\2\u00b3\u00b1")
        buf.write(u"\3\2\2\2\u00b4\u00b7\7\u00c5\2\2\u00b5\u00b7\5\32\16")
        buf.write(u"\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\31\3")
        buf.write(u"\2\2\2\u00b8\u00be\7\37\2\2\u00b9\u00bf\5\36\20\2\u00ba")
        buf.write(u"\u00bf\5\34\17\2\u00bb\u00bc\5\36\20\2\u00bc\u00bd\5")
        buf.write(u"\34\17\2\u00bd\u00bf\3\2\2\2\u00be\u00b9\3\2\2\2\u00be")
        buf.write(u"\u00ba\3\2\2\2\u00be\u00bb\3\2\2\2\u00bf\33\3\2\2\2\u00c0")
        buf.write(u"\u00c1\7\u00af\2\2\u00c1\u00c4\7\27\2\2\u00c2\u00c5\5")
        buf.write(u"\b\5\2\u00c3\u00c5\5\6\4\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write(u"\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\7\30\2")
        buf.write(u"\2\u00c7\35\3\2\2\2\u00c8\u00c9\7\u00b0\2\2\u00c9\u00cc")
        buf.write(u"\7\27\2\2\u00ca\u00cd\5\b\5\2\u00cb\u00cd\5\6\4\2\u00cc")
        buf.write(u"\u00ca\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce\3\2\2")
        buf.write(u"\2\u00ce\u00cf\7\30\2\2\u00cf\37\3\2\2\2\u00d0\u00d1")
        buf.write(u"\b\21\1\2\u00d1\u00d2\5$\23\2\u00d2\u00e1\3\2\2\2\u00d3")
        buf.write(u"\u00d4\f\4\2\2\u00d4\u00da\7\u00b0\2\2\u00d5\u00db\5")
        buf.write(u",\27\2\u00d6\u00d7\7\27\2\2\u00d7\u00d8\5\b\5\2\u00d8")
        buf.write(u"\u00d9\7\30\2\2\u00d9\u00db\3\2\2\2\u00da\u00d5\3\2\2")
        buf.write(u"\2\u00da\u00d6\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00de")
        buf.write(u"\5P)\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write(u"\u00e0\3\2\2\2\u00df\u00d3\3\2\2\2\u00e0\u00e3\3\2\2")
        buf.write(u"\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2!\3\2")
        buf.write(u"\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5\b\22\1\2\u00e5\u00e6")
        buf.write(u"\5&\24\2\u00e6\u00f5\3\2\2\2\u00e7\u00e8\f\4\2\2\u00e8")
        buf.write(u"\u00ee\7\u00b0\2\2\u00e9\u00ef\5,\27\2\u00ea\u00eb\7")
        buf.write(u"\27\2\2\u00eb\u00ec\5\b\5\2\u00ec\u00ed\7\30\2\2\u00ed")
        buf.write(u"\u00ef\3\2\2\2\u00ee\u00e9\3\2\2\2\u00ee\u00ea\3\2\2")
        buf.write(u"\2\u00ef\u00f1\3\2\2\2\u00f0\u00f2\5P)\2\u00f1\u00f0")
        buf.write(u"\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3")
        buf.write(u"\u00e7\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2")
        buf.write(u"\2\u00f5\u00f6\3\2\2\2\u00f6#\3\2\2\2\u00f7\u00f5\3\2")
        buf.write(u"\2\2\u00f8\u0102\5(\25\2\u00f9\u0102\5*\26\2\u00fa\u0102")
        buf.write(u"\5F$\2\u00fb\u0102\5,\27\2\u00fc\u0102\5:\36\2\u00fd")
        buf.write(u"\u0102\5<\37\2\u00fe\u0102\5> \2\u00ff\u0102\5@!\2\u0100")
        buf.write(u"\u0102\5B\"\2\u0101\u00f8\3\2\2\2\u0101\u00f9\3\2\2\2")
        buf.write(u"\u0101\u00fa\3\2\2\2\u0101\u00fb\3\2\2\2\u0101\u00fc")
        buf.write(u"\3\2\2\2\u0101\u00fd\3\2\2\2\u0101\u00fe\3\2\2\2\u0101")
        buf.write(u"\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102%\3\2\2\2\u0103")
        buf.write(u"\u010c\5(\25\2\u0104\u010c\5*\26\2\u0105\u010c\5,\27")
        buf.write(u"\2\u0106\u010c\5:\36\2\u0107\u010c\5<\37\2\u0108\u010c")
        buf.write(u"\5> \2\u0109\u010c\5@!\2\u010a\u010c\5B\"\2\u010b\u0103")
        buf.write(u"\3\2\2\2\u010b\u0104\3\2\2\2\u010b\u0105\3\2\2\2\u010b")
        buf.write(u"\u0106\3\2\2\2\u010b\u0107\3\2\2\2\u010b\u0108\3\2\2")
        buf.write(u"\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c\'\3")
        buf.write(u"\2\2\2\u010d\u010e\7\25\2\2\u010e\u010f\5\b\5\2\u010f")
        buf.write(u"\u0110\7\26\2\2\u0110\u011a\3\2\2\2\u0111\u0112\7\27")
        buf.write(u"\2\2\u0112\u0113\5\b\5\2\u0113\u0114\7\30\2\2\u0114\u011a")
        buf.write(u"\3\2\2\2\u0115\u0116\7\31\2\2\u0116\u0117\5\b\5\2\u0117")
        buf.write(u"\u0118\7\32\2\2\u0118\u011a\3\2\2\2\u0119\u010d\3\2\2")
        buf.write(u"\2\u0119\u0111\3\2\2\2\u0119\u0115\3\2\2\2\u011a)\3\2")
        buf.write(u"\2\2\u011b\u011c\7\37\2\2\u011c\u011d\5\b\5\2\u011d\u011e")
        buf.write(u"\7\37\2\2\u011e+\3\2\2\2\u011f\u0121\t\5\2\2\u0120\u0122")
        buf.write(u"\5P)\2\u0121\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122")
        buf.write(u"\u012a\3\2\2\2\u0123\u012a\7\u00b5\2\2\u0124\u012a\7")
        buf.write(u"\u00b2\2\2\u0125\u012a\5.\30\2\u0126\u012a\5\60\31\2")
        buf.write(u"\u0127\u012a\5\66\34\2\u0128\u012a\5\62\32\2\u0129\u011f")
        buf.write(u"\3\2\2\2\u0129\u0123\3\2\2\2\u0129\u0124\3\2\2\2\u0129")
        buf.write(u"\u0125\3\2\2\2\u0129\u0126\3\2\2\2\u0129\u0127\3\2\2")
        buf.write(u"\2\u0129\u0128\3\2\2\2\u012a-\3\2\2\2\u012b\u012c\7\33")
        buf.write(u"\2\2\u012c\u012d\5\66\34\2\u012d\u012e\7\34\2\2\u012e")
        buf.write(u"/\3\2\2\2\u012f\u0130\7!\2\2\u0130\u0131\5\66\34\2\u0131")
        buf.write(u"\u0132\7 \2\2\u0132\61\3\2\2\2\u0133\u0134\7\u00ae\2")
        buf.write(u"\2\u0134\u0135\7\27\2\2\u0135\u0136\5\64\33\2\u0136\u0137")
        buf.write(u"\7\30\2\2\u0137\63\3\2\2\2\u0138\u013d\t\6\2\2\u0139")
        buf.write(u"\u013a\7\3\2\2\u013a\u013c\t\6\2\2\u013b\u0139\3\2\2")
        buf.write(u"\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e")
        buf.write(u"\3\2\2\2\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u0140")
        buf.write(u"\u0138\3\2\2\2\u0140\u0141\3\2\2\2\u0141\65\3\2\2\2\u0142")
        buf.write(u"\u0143\7V\2\2\u0143\u0148\58\35\2\u0144\u0145\7\4\2\2")
        buf.write(u"\u0145\u0147\58\35\2\u0146\u0144\3\2\2\2\u0147\u014a")
        buf.write(u"\3\2\2\2\u0148\u0149\3\2\2\2\u0148\u0146\3\2\2\2\u0149")
        buf.write(u"\u014b\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c\7W\2\2")
        buf.write(u"\u014c\67\3\2\2\2\u014d\u0154\5\4\3\2\u014e\u0150\t\7")
        buf.write(u"\2\2\u014f\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151")
        buf.write(u"\3\2\2\2\u0151\u0153\5\4\3\2\u0152\u014f\3\2\2\2\u0153")
        buf.write(u"\u0156\3\2\2\2\u0154\u0155\3\2\2\2\u0154\u0152\3\2\2")
        buf.write(u"\2\u01559\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\7\u00aa")
        buf.write(u"\2\2\u0158\u0159\7\27\2\2\u0159\u015a\5\b\5\2\u015a\u015b")
        buf.write(u"\7\30\2\2\u015b\u015c\7\27\2\2\u015c\u015d\5\b\5\2\u015d")
        buf.write(u"\u015e\7\30\2\2\u015e;\3\2\2\2\u015f\u0160\t\b\2\2\u0160")
        buf.write(u"\u0161\7\27\2\2\u0161\u0162\5\b\5\2\u0162\u0163\7\30")
        buf.write(u"\2\2\u0163\u0164\7\27\2\2\u0164\u0165\5\b\5\2\u0165\u0166")
        buf.write(u"\7\30\2\2\u0166=\3\2\2\2\u0167\u0168\7E\2\2\u0168\u0169")
        buf.write(u"\5\b\5\2\u0169\u016a\7F\2\2\u016a?\3\2\2\2\u016b\u016c")
        buf.write(u"\7G\2\2\u016c\u016d\5\b\5\2\u016d\u016e\7H\2\2\u016e")
        buf.write(u"A\3\2\2\2\u016f\u0170\7M\2\2\u0170\u0171\7\u00af\2\2")
        buf.write(u"\u0171\u0172\7\27\2\2\u0172\u0173\5\b\5\2\u0173\u0174")
        buf.write(u"\5\b\5\2\u0174\u0175\7\30\2\2\u0175C\3\2\2\2\u0176\u0177")
        buf.write(u"\t\t\2\2\u0177E\3\2\2\2\u0178\u0185\5D#\2\u0179\u017b")
        buf.write(u"\5P)\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write(u"\u017d\3\2\2\2\u017c\u017e\5R*\2\u017d\u017c\3\2\2\2")
        buf.write(u"\u017d\u017e\3\2\2\2\u017e\u0186\3\2\2\2\u017f\u0181")
        buf.write(u"\5R*\2\u0180\u017f\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write(u"\u0183\3\2\2\2\u0182\u0184\5P)\2\u0183\u0182\3\2\2\2")
        buf.write(u"\u0183\u0184\3\2\2\2\u0184\u0186\3\2\2\2\u0185\u017a")
        buf.write(u"\3\2\2\2\u0185\u0180\3\2\2\2\u0186\u018c\3\2\2\2\u0187")
        buf.write(u"\u0188\7\25\2\2\u0188\u0189\5L\'\2\u0189\u018a\7\26\2")
        buf.write(u"\2\u018a\u018d\3\2\2\2\u018b\u018d\5N(\2\u018c\u0187")
        buf.write(u"\3\2\2\2\u018c\u018b\3\2\2\2\u018d\u01c2\3\2\2\2\u018e")
        buf.write(u"\u0190\t\5\2\2\u018f\u0191\5P)\2\u0190\u018f\3\2\2\2")
        buf.write(u"\u0190\u0191\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193")
        buf.write(u"\7\25\2\2\u0193\u0194\5H%\2\u0194\u0195\7\26\2\2\u0195")
        buf.write(u"\u01c2\3\2\2\2\u0196\u019d\7\'\2\2\u0197\u0198\5P)\2")
        buf.write(u"\u0198\u0199\5R*\2\u0199\u019e\3\2\2\2\u019a\u019b\5")
        buf.write(u"R*\2\u019b\u019c\5P)\2\u019c\u019e\3\2\2\2\u019d\u0197")
        buf.write(u"\3\2\2\2\u019d\u019a\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write(u"\u01a5\3\2\2\2\u019f\u01a1\5\n\6\2\u01a0\u019f\3\2\2")
        buf.write(u"\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a6")
        buf.write(u"\7\u00b2\2\2\u01a3\u01a6\5:\36\2\u01a4\u01a6\5\n\6\2")
        buf.write(u"\u01a5\u01a0\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4")
        buf.write(u"\3\2\2\2\u01a6\u01c2\3\2\2\2\u01a7\u01ac\7\u00a5\2\2")
        buf.write(u"\u01a8\u01a9\7\33\2\2\u01a9\u01aa\5\b\5\2\u01aa\u01ab")
        buf.write(u"\7\34\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01a8\3\2\2\2\u01ac")
        buf.write(u"\u01ad\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\7\27\2")
        buf.write(u"\2\u01af\u01b0\5\b\5\2\u01b0\u01b1\7\30\2\2\u01b1\u01c2")
        buf.write(u"\3\2\2\2\u01b2\u01b9\t\n\2\2\u01b3\u01b4\5T+\2\u01b4")
        buf.write(u"\u01b5\5R*\2\u01b5\u01ba\3\2\2\2\u01b6\u01b7\5R*\2\u01b7")
        buf.write(u"\u01b8\5T+\2\u01b8\u01ba\3\2\2\2\u01b9\u01b3\3\2\2\2")
        buf.write(u"\u01b9\u01b6\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc")
        buf.write(u"\5\f\7\2\u01bc\u01c2\3\2\2\2\u01bd\u01be\7#\2\2\u01be")
        buf.write(u"\u01bf\5J&\2\u01bf\u01c0\5\f\7\2\u01c0\u01c2\3\2\2\2")
        buf.write(u"\u01c1\u0178\3\2\2\2\u01c1\u018e\3\2\2\2\u01c1\u0196")
        buf.write(u"\3\2\2\2\u01c1\u01a7\3\2\2\2\u01c1\u01b2\3\2\2\2\u01c1")
        buf.write(u"\u01bd\3\2\2\2\u01c2G\3\2\2\2\u01c3\u01c4\5\b\5\2\u01c4")
        buf.write(u"\u01c5\7\3\2\2\u01c5\u01c6\5H%\2\u01c6\u01c9\3\2\2\2")
        buf.write(u"\u01c7\u01c9\5\b\5\2\u01c8\u01c3\3\2\2\2\u01c8\u01c7")
        buf.write(u"\3\2\2\2\u01c9I\3\2\2\2\u01ca\u01cb\7\u00af\2\2\u01cb")
        buf.write(u"\u01cc\7\27\2\2\u01cc\u01cd\t\5\2\2\u01cd\u01ce\7$\2")
        buf.write(u"\2\u01ce\u01d3\5\b\5\2\u01cf\u01d0\7\u00b0\2\2\u01d0")
        buf.write(u"\u01d1\7\27\2\2\u01d1\u01d2\t\3\2\2\u01d2\u01d4\7\30")
        buf.write(u"\2\2\u01d3\u01cf\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5")
        buf.write(u"\3\2\2\2\u01d5\u01d6\7\30\2\2\u01d6K\3\2\2\2\u01d7\u01dd")
        buf.write(u"\5\b\5\2\u01d8\u01d9\5\b\5\2\u01d9\u01da\7\3\2\2\u01da")
        buf.write(u"\u01db\5L\'\2\u01db\u01dd\3\2\2\2\u01dc\u01d7\3\2\2\2")
        buf.write(u"\u01dc\u01d8\3\2\2\2\u01ddM\3\2\2\2\u01de\u01df\5\16")
        buf.write(u"\b\2\u01dfO\3\2\2\2\u01e0\u01e6\7\u00af\2\2\u01e1\u01e7")
        buf.write(u"\5,\27\2\u01e2\u01e3\7\27\2\2\u01e3\u01e4\5\b\5\2\u01e4")
        buf.write(u"\u01e5\7\30\2\2\u01e5\u01e7\3\2\2\2\u01e6\u01e1\3\2\2")
        buf.write(u"\2\u01e6\u01e2\3\2\2\2\u01e7Q\3\2\2\2\u01e8\u01ee\7\u00b0")
        buf.write(u"\2\2\u01e9\u01ef\5,\27\2\u01ea\u01eb\7\27\2\2\u01eb\u01ec")
        buf.write(u"\5\b\5\2\u01ec\u01ed\7\30\2\2\u01ed\u01ef\3\2\2\2\u01ee")
        buf.write(u"\u01e9\3\2\2\2\u01ee\u01ea\3\2\2\2\u01efS\3\2\2\2\u01f0")
        buf.write(u"\u01f1\7\u00af\2\2\u01f1\u01f2\7\27\2\2\u01f2\u01f3\5")
        buf.write(u"\6\4\2\u01f3\u01f4\7\30\2\2\u01f4U\3\2\2\2\u01f5\u01f6")
        buf.write(u"\7\u00af\2\2\u01f6\u01f7\7\27\2\2\u01f7\u01f8\5\6\4\2")
        buf.write(u"\u01f8\u01f9\7\30\2\2\u01f9W\3\2\2\2\63chy\u0084\u008f")
        buf.write(u"\u0097\u0099\u00a1\u00a4\u00aa\u00b1\u00b6\u00be\u00c4")
        buf.write(u"\u00cc\u00da\u00dd\u00e1\u00ee\u00f1\u00f5\u0101\u010b")
        buf.write(u"\u0119\u0121\u0129\u013d\u0140\u0148\u014f\u0154\u017a")
        buf.write(u"\u017d\u0180\u0183\u0185\u018c\u0190\u019d\u01a0\u01a5")
        buf.write(u"\u01ac\u01b9\u01c1\u01c8\u01d3\u01dc\u01e6\u01ee")
        return buf.getvalue()


class LaTeXParser ( Parser ):

    grammarFileName = "LaTeX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"','", u"'\\\\'", u"'&'", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'\\quad'", 
                     u"'\\qquad'", u"<INVALID>", u"'\\negmedspace'", u"'\\negthickspace'", 
                     u"'+'", u"'-'", u"'*'", u"'/'", u"'\\pm'", u"'\\mp'", 
                     u"'('", u"')'", u"'{'", u"'}'", u"'\\{'", u"'\\}'", 
                     u"'['", u"']'", u"'\\left'", u"'\\right'", u"'|'", 
                     u"'\\right|'", u"'\\left|'", u"'\\|'", u"'\\lim'", 
                     u"<INVALID>", u"'\\varlimsup'", u"'\\varliminf'", u"'\\int'", 
                     u"'\\sum'", u"'\\prod'", u"'\\exp'", u"'\\log'", u"'\\ln'", 
                     u"'\\sin'", u"'\\cos'", u"'\\tan'", u"'\\csc'", u"'\\sec'", 
                     u"'\\cot'", u"'\\arcsin'", u"'\\arccos'", u"'\\arctan'", 
                     u"'\\arccsc'", u"'\\arcsec'", u"'\\arccot'", u"'\\sinh'", 
                     u"'\\cosh'", u"'\\tanh'", u"'\\csch'", u"'\\sech'", 
                     u"'\\coth'", u"'\\arsinh'", u"'\\arcosh'", u"'\\artanh'", 
                     u"'\\arcsch'", u"'\\arsech'", u"'\\arcoth'", u"'\\lfloor'", 
                     u"'\\rfloor'", u"'\\lceil'", u"'\\rceil'", u"'\\imath'", 
                     u"'\\jmath'", u"'\\aleph'", u"'\\beth'", u"'\\delta'", 
                     u"'\\Gamma'", u"'\\gamma'", u"'\\nabla'", u"'\\Sigma'", 
                     u"'\\sigma'", u"'\\Xi'", u"'\\xi'", u"'\\zeta'", u"<INVALID>", 
                     u"<INVALID>", u"'\\circ'", u"'\\radian'", u"'\\oint'", 
                     u"'\\otimes'", u"'\\oplus'", u"'\\ominus'", u"'\\odot'", 
                     u"'\\bigoplus'", u"'\\bigotimes'", u"'\\oslash'", u"'\\tilde'", 
                     u"'\\vec'", u"'\\hat'", u"'\\hbar'", u"'\\dagger'", 
                     u"'\\star'", u"'\\dot'", u"'\\ddot'", u"'\\ldots'", 
                     u"'\\vdots'", u"'\\dots'", u"'\\cdots'", u"'\\widehat'", 
                     u"'\\underline'", u"'\\overbrace'", u"'\\overleftarrow'", 
                     u"'\\not'", u"'\\varnothing'", u"'\\bigvee'", u"'\\coprod'", 
                     u"'\\neg'", u"'\\mapsto'", u"'\\bigwedge'", u"'\\curlyvee'", 
                     u"'\\curlywedge'", u"'\\ni'", u"'\\subsetneq'", u"'\\sqsubset'", 
                     u"'\\sqsupseteq'", u"'\\sqsupset'", u"'\\sqsubseteq'", 
                     u"'\\complement'", u"'\\supsetneq'", u"'\\sqcup'", 
                     u"'\\sqcap'", u"'\\nexists'", u"'\\nsubseteq'", u"'\\nsupseteq'", 
                     u"'\\underbrace'", u"'\\underset'", u"'\\bigcup'", 
                     u"'\\bigcap'", u"'\\longmapsto'", u"'\\therefore'", 
                     u"'\\because'", u"'\\emptyset'", u"'\\subset'", u"'\\supset'", 
                     u"'\\subseteq'", u"'\\supseteq'", u"'\\notin'", u"'\\exists'", 
                     u"'\\forall'", u"'\\cup'", u"'\\cap'", u"'\\overline'", 
                     u"'\\in'", u"'\\wedge'", u"'\\vee'", u"'\\smile'", 
                     u"'\\frown'", u"'\\mathbb'", u"'\\stackrel'", u"'\\Im'", 
                     u"'\\Re'", u"'\\multicolumn'", u"'\\multirow'", u"'\\sqrt'", 
                     u"'\\longdiv'", u"'\\times'", u"'\\cdot'", u"'\\div'", 
                     u"'\\frac'", u"'\\binom'", u"'\\dbinom'", u"'\\tbinom'", 
                     u"'\\mathit'", u"'_'", u"'^'", u"':'", u"<INVALID>", 
                     u"'\\partial'", u"<INVALID>", u"<INVALID>", u"'='", 
                     u"'<'", u"'\\leq'", u"'>'", u"'\\geq'", u"'\\geqq'", 
                     u"'\\leqq'", u"'\\leqslant'", u"'\\geqslant'", u"'\\ll'", 
                     u"'\\gg'", u"'\\lll'", u"'\\ggg'", u"'&='", u"'\\neq'", 
                     u"'!'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"WS", u"THINSPACE", u"MEDSPACE", u"THICKSPACE", u"QUAD", 
                      u"QQUAD", u"NEGTHINSPACE", u"NEGMEDSPACE", u"NEGTHICKSPACE", 
                      u"ADD", u"SUB", u"MUL", u"DIV", u"PM", u"MP", u"L_PAREN", 
                      u"R_PAREN", u"L_BRACE", u"R_BRACE", u"L_BRACE_LITERAL", 
                      u"R_BRACE_LITERAL", u"L_BRACKET", u"R_BRACKET", u"CMD_LEFT", 
                      u"CMD_RIGHT", u"BAR", u"R_BAR", u"L_BAR", u"BAR_VAL", 
                      u"FUNC_LIM", u"LIM_APPROACH_SYM", u"VAR_LIMIT_SUPER", 
                      u"VAR_LIMIT_INF", u"FUNC_INT", u"FUNC_SUM", u"FUNC_PROD", 
                      u"FUNC_EXP", u"FUNC_LOG", u"FUNC_LN", u"FUNC_SIN", 
                      u"FUNC_COS", u"FUNC_TAN", u"FUNC_CSC", u"FUNC_SEC", 
                      u"FUNC_COT", u"FUNC_ARCSIN", u"FUNC_ARCCOS", u"FUNC_ARCTAN", 
                      u"FUNC_ARCCSC", u"FUNC_ARCSEC", u"FUNC_ARCCOT", u"FUNC_SINH", 
                      u"FUNC_COSH", u"FUNC_TANH", u"FUNC_CSCH", u"FUNC_SECH", 
                      u"FUNC_COTH", u"FUNC_ARSINH", u"FUNC_ARCOSH", u"FUNC_ARTANH", 
                      u"FUNC_ARCSCH", u"FUNC_ARSECH", u"FUNC_ARCOTH", u"L_FLOOR", 
                      u"R_FLOOR", u"L_CEIL", u"R_CEIL", u"I_MATH", u"J_MATH", 
                      u"ALEPH", u"BETH", u"DELTA", u"FUNC_GAMMA", u"LOWER_GAMMA", 
                      u"NABLA", u"SIGMA", u"LOWER_SIGMA", u"XI", u"LOWER_XI", 
                      u"LOWER_ZETA", u"BEGIN_ARR", u"END_ARR", u"CIRC", 
                      u"RADIAN", u"O_INT", u"O_TIMES", u"O_PLUS", u"O_MINUS", 
                      u"O_DOT", u"BIG_O_PLUS", u"BIG_O_TIMES", u"O_SLASH", 
                      u"TILDE", u"VEC", u"HAT", u"HBAR", u"DAGGER", u"STAR", 
                      u"DOT", u"DDOT", u"LDOTS", u"VDOTS", u"DOTS", u"CDOTS", 
                      u"WIDE_HAT", u"UNDERLINE", u"OVERBRACE", u"OVER_LEFTARROW", 
                      u"NOT", u"VAR_NOTHING", u"BIG_VEE", u"CO_PRODUCT", 
                      u"NEG", u"MAPS_TO", u"BIG_WEDGE", u"CURLY_VEE", u"CURLY_WEDGE", 
                      u"N_I", u"SUBSET_NEQ", u"SQ_SUBSET", u"SQ_SUBSET_EQ", 
                      u"SQ_SUPERSET", u"SQ_SUPERSET_EQ", u"COMPLEMENT", 
                      u"SUPERSET_NEQ", u"SQ_CUP", u"SQ_CAP", u"NEXISTS", 
                      u"N_SUBSET_EQ", u"N_SUPERSET_EQ", u"UNDER_BRACE", 
                      u"UNDER_SET", u"BIG_CUP", u"BIG_CAP", u"LONG_MAPS_TO", 
                      u"THEREFORE", u"BECAUSE", u"EMPTY_SET", u"SUBSET", 
                      u"SUPERSET", u"SUBSET_EQ", u"SUPERSET_EQ", u"NOT_IN", 
                      u"EXISTS", u"FOR_ALL", u"CUP", u"CAP", u"OVERLINE", 
                      u"IN", u"WEDGE", u"VEE", u"SMILE", u"FROWN", u"MATH_BB", 
                      u"STACK_REL", u"IM", u"RE", u"MULTI_COL", u"MULTI_ROW", 
                      u"FUNC_SQRT", u"LONG_DIV", u"CMD_TIMES", u"CMD_CDOT", 
                      u"CMD_DIV", u"CMD_FRAC", u"CMD_BINOM", u"CMD_DBINOM", 
                      u"CMD_TBINOM", u"CMD_MATHIT", u"UNDERSCORE", u"CARET", 
                      u"COLON", u"DIFFERENTIAL", u"PARTIAL", u"LETTER", 
                      u"NUMBER", u"EQUAL", u"LT", u"LTE", u"GT", u"GTE", 
                      u"GTE_Q", u"LTE_Q", u"LTE_S", u"GTE_S", u"LL", u"GG", 
                      u"LLL", u"GGG", u"AND_EQUAL", u"NEQ", u"BANG", u"SYMBOL" ]

    RULE_math = 0
    RULE_relation = 1
    RULE_equality = 2
    RULE_expr = 3
    RULE_additive = 4
    RULE_mp = 5
    RULE_mp_nofunc = 6
    RULE_unary = 7
    RULE_unary_nofunc = 8
    RULE_postfix = 9
    RULE_postfix_nofunc = 10
    RULE_postfix_op = 11
    RULE_eval_at = 12
    RULE_eval_at_sub = 13
    RULE_eval_at_sup = 14
    RULE_exp = 15
    RULE_exp_nofunc = 16
    RULE_comp = 17
    RULE_comp_nofunc = 18
    RULE_group = 19
    RULE_abs_group = 20
    RULE_atom = 21
    RULE_matrix = 22
    RULE_determinant = 23
    RULE_mathit = 24
    RULE_mathit_text = 25
    RULE_array = 26
    RULE_array_elements = 27
    RULE_frac = 28
    RULE_binom = 29
    RULE_floor = 30
    RULE_ceil = 31
    RULE_delta = 32
    RULE_func_normal = 33
    RULE_func = 34
    RULE_args = 35
    RULE_limit_sub = 36
    RULE_func_arg = 37
    RULE_func_arg_noparens = 38
    RULE_subexpr = 39
    RULE_supexpr = 40
    RULE_subeq = 41
    RULE_supeq = 42

    ruleNames =  [ u"math", u"relation", u"equality", u"expr", u"additive", 
                   u"mp", u"mp_nofunc", u"unary", u"unary_nofunc", u"postfix", 
                   u"postfix_nofunc", u"postfix_op", u"eval_at", u"eval_at_sub", 
                   u"eval_at_sup", u"exp", u"exp_nofunc", u"comp", u"comp_nofunc", 
                   u"group", u"abs_group", u"atom", u"matrix", u"determinant", 
                   u"mathit", u"mathit_text", u"array", u"array_elements", 
                   u"frac", u"binom", u"floor", u"ceil", u"delta", u"func_normal", 
                   u"func", u"args", u"limit_sub", u"func_arg", u"func_arg_noparens", 
                   u"subexpr", u"supexpr", u"subeq", u"supeq" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WS=4
    THINSPACE=5
    MEDSPACE=6
    THICKSPACE=7
    QUAD=8
    QQUAD=9
    NEGTHINSPACE=10
    NEGMEDSPACE=11
    NEGTHICKSPACE=12
    ADD=13
    SUB=14
    MUL=15
    DIV=16
    PM=17
    MP=18
    L_PAREN=19
    R_PAREN=20
    L_BRACE=21
    R_BRACE=22
    L_BRACE_LITERAL=23
    R_BRACE_LITERAL=24
    L_BRACKET=25
    R_BRACKET=26
    CMD_LEFT=27
    CMD_RIGHT=28
    BAR=29
    R_BAR=30
    L_BAR=31
    BAR_VAL=32
    FUNC_LIM=33
    LIM_APPROACH_SYM=34
    VAR_LIMIT_SUPER=35
    VAR_LIMIT_INF=36
    FUNC_INT=37
    FUNC_SUM=38
    FUNC_PROD=39
    FUNC_EXP=40
    FUNC_LOG=41
    FUNC_LN=42
    FUNC_SIN=43
    FUNC_COS=44
    FUNC_TAN=45
    FUNC_CSC=46
    FUNC_SEC=47
    FUNC_COT=48
    FUNC_ARCSIN=49
    FUNC_ARCCOS=50
    FUNC_ARCTAN=51
    FUNC_ARCCSC=52
    FUNC_ARCSEC=53
    FUNC_ARCCOT=54
    FUNC_SINH=55
    FUNC_COSH=56
    FUNC_TANH=57
    FUNC_CSCH=58
    FUNC_SECH=59
    FUNC_COTH=60
    FUNC_ARSINH=61
    FUNC_ARCOSH=62
    FUNC_ARTANH=63
    FUNC_ARCSCH=64
    FUNC_ARSECH=65
    FUNC_ARCOTH=66
    L_FLOOR=67
    R_FLOOR=68
    L_CEIL=69
    R_CEIL=70
    I_MATH=71
    J_MATH=72
    ALEPH=73
    BETH=74
    DELTA=75
    FUNC_GAMMA=76
    LOWER_GAMMA=77
    NABLA=78
    SIGMA=79
    LOWER_SIGMA=80
    XI=81
    LOWER_XI=82
    LOWER_ZETA=83
    BEGIN_ARR=84
    END_ARR=85
    CIRC=86
    RADIAN=87
    O_INT=88
    O_TIMES=89
    O_PLUS=90
    O_MINUS=91
    O_DOT=92
    BIG_O_PLUS=93
    BIG_O_TIMES=94
    O_SLASH=95
    TILDE=96
    VEC=97
    HAT=98
    HBAR=99
    DAGGER=100
    STAR=101
    DOT=102
    DDOT=103
    LDOTS=104
    VDOTS=105
    DOTS=106
    CDOTS=107
    WIDE_HAT=108
    UNDERLINE=109
    OVERBRACE=110
    OVER_LEFTARROW=111
    NOT=112
    VAR_NOTHING=113
    BIG_VEE=114
    CO_PRODUCT=115
    NEG=116
    MAPS_TO=117
    BIG_WEDGE=118
    CURLY_VEE=119
    CURLY_WEDGE=120
    N_I=121
    SUBSET_NEQ=122
    SQ_SUBSET=123
    SQ_SUBSET_EQ=124
    SQ_SUPERSET=125
    SQ_SUPERSET_EQ=126
    COMPLEMENT=127
    SUPERSET_NEQ=128
    SQ_CUP=129
    SQ_CAP=130
    NEXISTS=131
    N_SUBSET_EQ=132
    N_SUPERSET_EQ=133
    UNDER_BRACE=134
    UNDER_SET=135
    BIG_CUP=136
    BIG_CAP=137
    LONG_MAPS_TO=138
    THEREFORE=139
    BECAUSE=140
    EMPTY_SET=141
    SUBSET=142
    SUPERSET=143
    SUBSET_EQ=144
    SUPERSET_EQ=145
    NOT_IN=146
    EXISTS=147
    FOR_ALL=148
    CUP=149
    CAP=150
    OVERLINE=151
    IN=152
    WEDGE=153
    VEE=154
    SMILE=155
    FROWN=156
    MATH_BB=157
    STACK_REL=158
    IM=159
    RE=160
    MULTI_COL=161
    MULTI_ROW=162
    FUNC_SQRT=163
    LONG_DIV=164
    CMD_TIMES=165
    CMD_CDOT=166
    CMD_DIV=167
    CMD_FRAC=168
    CMD_BINOM=169
    CMD_DBINOM=170
    CMD_TBINOM=171
    CMD_MATHIT=172
    UNDERSCORE=173
    CARET=174
    COLON=175
    DIFFERENTIAL=176
    PARTIAL=177
    LETTER=178
    NUMBER=179
    EQUAL=180
    LT=181
    LTE=182
    GT=183
    GTE=184
    GTE_Q=185
    LTE_Q=186
    LTE_S=187
    GTE_S=188
    LL=189
    GG=190
    LLL=191
    GGG=192
    AND_EQUAL=193
    NEQ=194
    BANG=195
    SYMBOL=196

    def __init__(self, input, output=sys.stdout):
        super(LaTeXParser, self).__init__(input, output=output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.MathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def relation(self):
            return self.getTypedRuleContext(LaTeXParser.RelationContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_math




    def math(self):

        localctx = LaTeXParser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_math)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.relation(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.RelationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def relation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.RelationContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.RelationContext,i)


        def LT(self):
            return self.getToken(LaTeXParser.LT, 0)

        def LTE(self):
            return self.getToken(LaTeXParser.LTE, 0)

        def GT(self):
            return self.getToken(LaTeXParser.GT, 0)

        def GTE(self):
            return self.getToken(LaTeXParser.GTE, 0)

        def EQUAL(self):
            return self.getToken(LaTeXParser.EQUAL, 0)

        def AND_EQUAL(self):
            return self.getToken(LaTeXParser.AND_EQUAL, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_relation



    def relation(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.RelationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_relation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.RelationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relation)
                    self.state = 91
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 97
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [LaTeXParser.EQUAL, LaTeXParser.AND_EQUAL]:
                        self.state = 92
                        _la = self._input.LA(1)
                        if not(_la==LaTeXParser.EQUAL or _la==LaTeXParser.AND_EQUAL):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass
                    elif token in [LaTeXParser.LT]:
                        self.state = 93
                        self.match(LaTeXParser.LT)
                        pass
                    elif token in [LaTeXParser.LTE]:
                        self.state = 94
                        self.match(LaTeXParser.LTE)
                        pass
                    elif token in [LaTeXParser.GT]:
                        self.state = 95
                        self.match(LaTeXParser.GT)
                        pass
                    elif token in [LaTeXParser.GTE]:
                        self.state = 96
                        self.match(LaTeXParser.GTE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 99
                    self.relation(3) 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EqualityContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.EqualityContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.ExprContext,i)


        def EQUAL(self):
            return self.getToken(LaTeXParser.EQUAL, 0)

        def AND_EQUAL(self):
            return self.getToken(LaTeXParser.AND_EQUAL, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_equality




    def equality(self):

        localctx = LaTeXParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.expr()
            self.state = 106
            _la = self._input.LA(1)
            if not(_la==LaTeXParser.EQUAL or _la==LaTeXParser.AND_EQUAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 107
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def additive(self):
            return self.getTypedRuleContext(LaTeXParser.AdditiveContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_expr




    def expr(self):

        localctx = LaTeXParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.additive(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.AdditiveContext, self).__init__(parent, invokingState)
            self.parser = parser

        def mp(self):
            return self.getTypedRuleContext(LaTeXParser.MpContext,0)


        def additive(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.AdditiveContext,i)


        def ADD(self):
            return self.getToken(LaTeXParser.ADD, 0)

        def SUB(self):
            return self.getToken(LaTeXParser.SUB, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_additive



    def additive(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.AdditiveContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_additive, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.mp(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.AdditiveContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                    self.state = 114
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 115
                    _la = self._input.LA(1)
                    if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 116
                    self.additive(3) 
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.MpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(LaTeXParser.UnaryContext,0)


        def mp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.MpContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.MpContext,i)


        def MUL(self):
            return self.getToken(LaTeXParser.MUL, 0)

        def CMD_TIMES(self):
            return self.getToken(LaTeXParser.CMD_TIMES, 0)

        def CMD_CDOT(self):
            return self.getToken(LaTeXParser.CMD_CDOT, 0)

        def DIV(self):
            return self.getToken(LaTeXParser.DIV, 0)

        def CMD_DIV(self):
            return self.getToken(LaTeXParser.CMD_DIV, 0)

        def COLON(self):
            return self.getToken(LaTeXParser.COLON, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_mp



    def mp(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.MpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_mp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.MpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mp)
                    self.state = 125
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 126
                    _la = self._input.LA(1)
                    if not(_la==LaTeXParser.MUL or _la==LaTeXParser.DIV or ((((_la - 165)) & ~0x3f) == 0 and ((1 << (_la - 165)) & ((1 << (LaTeXParser.CMD_TIMES - 165)) | (1 << (LaTeXParser.CMD_CDOT - 165)) | (1 << (LaTeXParser.CMD_DIV - 165)) | (1 << (LaTeXParser.COLON - 165)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 127
                    self.mp(3) 
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mp_nofuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Mp_nofuncContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unary_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Unary_nofuncContext,0)


        def mp_nofunc(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.Mp_nofuncContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.Mp_nofuncContext,i)


        def MUL(self):
            return self.getToken(LaTeXParser.MUL, 0)

        def CMD_TIMES(self):
            return self.getToken(LaTeXParser.CMD_TIMES, 0)

        def CMD_CDOT(self):
            return self.getToken(LaTeXParser.CMD_CDOT, 0)

        def DIV(self):
            return self.getToken(LaTeXParser.DIV, 0)

        def CMD_DIV(self):
            return self.getToken(LaTeXParser.CMD_DIV, 0)

        def COLON(self):
            return self.getToken(LaTeXParser.COLON, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_mp_nofunc



    def mp_nofunc(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.Mp_nofuncContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_mp_nofunc, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.unary_nofunc()
            self._ctx.stop = self._input.LT(-1)
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.Mp_nofuncContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mp_nofunc)
                    self.state = 136
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 137
                    _la = self._input.LA(1)
                    if not(_la==LaTeXParser.MUL or _la==LaTeXParser.DIV or ((((_la - 165)) & ~0x3f) == 0 and ((1 << (_la - 165)) & ((1 << (LaTeXParser.CMD_TIMES - 165)) | (1 << (LaTeXParser.CMD_CDOT - 165)) | (1 << (LaTeXParser.CMD_DIV - 165)) | (1 << (LaTeXParser.COLON - 165)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 138
                    self.mp_nofunc(3) 
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.UnaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(LaTeXParser.UnaryContext,0)


        def ADD(self):
            return self.getToken(LaTeXParser.ADD, 0)

        def SUB(self):
            return self.getToken(LaTeXParser.SUB, 0)

        def postfix(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.PostfixContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.PostfixContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_unary




    def unary(self):

        localctx = LaTeXParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.ADD, LaTeXParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 145
                self.unary()
                pass
            elif token in [LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACE_LITERAL, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_EXP, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_CSCH, LaTeXParser.FUNC_SECH, LaTeXParser.FUNC_COTH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_ARCSCH, LaTeXParser.FUNC_ARSECH, LaTeXParser.FUNC_ARCOTH, LaTeXParser.L_FLOOR, LaTeXParser.L_CEIL, LaTeXParser.DELTA, LaTeXParser.FUNC_GAMMA, LaTeXParser.BEGIN_ARR, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_BINOM, LaTeXParser.CMD_DBINOM, LaTeXParser.CMD_TBINOM, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 146
                        self.postfix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 149 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_nofuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Unary_nofuncContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unary_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Unary_nofuncContext,0)


        def ADD(self):
            return self.getToken(LaTeXParser.ADD, 0)

        def SUB(self):
            return self.getToken(LaTeXParser.SUB, 0)

        def postfix(self):
            return self.getTypedRuleContext(LaTeXParser.PostfixContext,0)


        def postfix_nofunc(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.Postfix_nofuncContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.Postfix_nofuncContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_unary_nofunc




    def unary_nofunc(self):

        localctx = LaTeXParser.Unary_nofuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_unary_nofunc)
        self._la = 0 # Token type
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.ADD, LaTeXParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 154
                self.unary_nofunc()
                pass
            elif token in [LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACE_LITERAL, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_EXP, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_CSCH, LaTeXParser.FUNC_SECH, LaTeXParser.FUNC_COTH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_ARCSCH, LaTeXParser.FUNC_ARSECH, LaTeXParser.FUNC_ARCOTH, LaTeXParser.L_FLOOR, LaTeXParser.L_CEIL, LaTeXParser.DELTA, LaTeXParser.FUNC_GAMMA, LaTeXParser.BEGIN_ARR, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_BINOM, LaTeXParser.CMD_DBINOM, LaTeXParser.CMD_TBINOM, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.postfix()
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 156
                        self.postfix_nofunc() 
                    self.state = 161
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.PostfixContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(LaTeXParser.ExpContext,0)


        def postfix_op(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.Postfix_opContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.Postfix_opContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_postfix




    def postfix(self):

        localctx = LaTeXParser.PostfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_postfix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.exp(0)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 165
                    self.postfix_op() 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Postfix_nofuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Postfix_nofuncContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exp_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Exp_nofuncContext,0)


        def postfix_op(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.Postfix_opContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.Postfix_opContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_postfix_nofunc




    def postfix_nofunc(self):

        localctx = LaTeXParser.Postfix_nofuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_postfix_nofunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.exp_nofunc(0)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 172
                    self.postfix_op() 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Postfix_opContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Postfix_opContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BANG(self):
            return self.getToken(LaTeXParser.BANG, 0)

        def eval_at(self):
            return self.getTypedRuleContext(LaTeXParser.Eval_atContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_postfix_op




    def postfix_op(self):

        localctx = LaTeXParser.Postfix_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_postfix_op)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.BANG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(LaTeXParser.BANG)
                pass
            elif token in [LaTeXParser.BAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.eval_at()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eval_atContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Eval_atContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BAR(self):
            return self.getToken(LaTeXParser.BAR, 0)

        def eval_at_sup(self):
            return self.getTypedRuleContext(LaTeXParser.Eval_at_supContext,0)


        def eval_at_sub(self):
            return self.getTypedRuleContext(LaTeXParser.Eval_at_subContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_eval_at




    def eval_at(self):

        localctx = LaTeXParser.Eval_atContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_eval_at)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(LaTeXParser.BAR)
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 183
                self.eval_at_sup()
                pass

            elif la_ == 2:
                self.state = 184
                self.eval_at_sub()
                pass

            elif la_ == 3:
                self.state = 185
                self.eval_at_sup()
                self.state = 186
                self.eval_at_sub()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eval_at_subContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Eval_at_subContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def equality(self):
            return self.getTypedRuleContext(LaTeXParser.EqualityContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_eval_at_sub




    def eval_at_sub(self):

        localctx = LaTeXParser.Eval_at_subContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_eval_at_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 191
            self.match(LaTeXParser.L_BRACE)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 192
                self.expr()
                pass

            elif la_ == 2:
                self.state = 193
                self.equality()
                pass


            self.state = 196
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eval_at_supContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Eval_at_supContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def equality(self):
            return self.getTypedRuleContext(LaTeXParser.EqualityContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_eval_at_sup




    def eval_at_sup(self):

        localctx = LaTeXParser.Eval_at_supContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_eval_at_sup)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(LaTeXParser.CARET)
            self.state = 199
            self.match(LaTeXParser.L_BRACE)
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 200
                self.expr()
                pass

            elif la_ == 2:
                self.state = 201
                self.equality()
                pass


            self.state = 204
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.ExpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(LaTeXParser.CompContext,0)


        def exp(self):
            return self.getTypedRuleContext(LaTeXParser.ExpContext,0)


        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def subexpr(self):
            return self.getTypedRuleContext(LaTeXParser.SubexprContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_exp



    def exp(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.comp()
            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 209
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 210
                    self.match(LaTeXParser.CARET)
                    self.state = 216
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [LaTeXParser.L_BRACKET, LaTeXParser.L_BAR, LaTeXParser.BEGIN_ARR, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                        self.state = 211
                        self.atom()
                        pass
                    elif token in [LaTeXParser.L_BRACE]:
                        self.state = 212
                        self.match(LaTeXParser.L_BRACE)
                        self.state = 213
                        self.expr()
                        self.state = 214
                        self.match(LaTeXParser.R_BRACE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 219
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        self.state = 218
                        self.subexpr()

             
                self.state = 225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp_nofuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Exp_nofuncContext, self).__init__(parent, invokingState)
            self.parser = parser

        def comp_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Comp_nofuncContext,0)


        def exp_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Exp_nofuncContext,0)


        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def subexpr(self):
            return self.getTypedRuleContext(LaTeXParser.SubexprContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_exp_nofunc



    def exp_nofunc(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.Exp_nofuncContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exp_nofunc, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.comp_nofunc()
            self._ctx.stop = self._input.LT(-1)
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.Exp_nofuncContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_nofunc)
                    self.state = 229
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 230
                    self.match(LaTeXParser.CARET)
                    self.state = 236
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [LaTeXParser.L_BRACKET, LaTeXParser.L_BAR, LaTeXParser.BEGIN_ARR, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                        self.state = 231
                        self.atom()
                        pass
                    elif token in [LaTeXParser.L_BRACE]:
                        self.state = 232
                        self.match(LaTeXParser.L_BRACE)
                        self.state = 233
                        self.expr()
                        self.state = 234
                        self.match(LaTeXParser.R_BRACE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 239
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        self.state = 238
                        self.subexpr()

             
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.CompContext, self).__init__(parent, invokingState)
            self.parser = parser

        def group(self):
            return self.getTypedRuleContext(LaTeXParser.GroupContext,0)


        def abs_group(self):
            return self.getTypedRuleContext(LaTeXParser.Abs_groupContext,0)


        def func(self):
            return self.getTypedRuleContext(LaTeXParser.FuncContext,0)


        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def frac(self):
            return self.getTypedRuleContext(LaTeXParser.FracContext,0)


        def binom(self):
            return self.getTypedRuleContext(LaTeXParser.BinomContext,0)


        def floor(self):
            return self.getTypedRuleContext(LaTeXParser.FloorContext,0)


        def ceil(self):
            return self.getTypedRuleContext(LaTeXParser.CeilContext,0)


        def delta(self):
            return self.getTypedRuleContext(LaTeXParser.DeltaContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_comp




    def comp(self):

        localctx = LaTeXParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comp)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.group()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.abs_group()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.func()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.atom()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 250
                self.frac()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 251
                self.binom()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 252
                self.floor()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 253
                self.ceil()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 254
                self.delta()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_nofuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Comp_nofuncContext, self).__init__(parent, invokingState)
            self.parser = parser

        def group(self):
            return self.getTypedRuleContext(LaTeXParser.GroupContext,0)


        def abs_group(self):
            return self.getTypedRuleContext(LaTeXParser.Abs_groupContext,0)


        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def frac(self):
            return self.getTypedRuleContext(LaTeXParser.FracContext,0)


        def binom(self):
            return self.getTypedRuleContext(LaTeXParser.BinomContext,0)


        def floor(self):
            return self.getTypedRuleContext(LaTeXParser.FloorContext,0)


        def ceil(self):
            return self.getTypedRuleContext(LaTeXParser.CeilContext,0)


        def delta(self):
            return self.getTypedRuleContext(LaTeXParser.DeltaContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_comp_nofunc




    def comp_nofunc(self):

        localctx = LaTeXParser.Comp_nofuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comp_nofunc)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACE_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.group()
                pass
            elif token in [LaTeXParser.BAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.abs_group()
                pass
            elif token in [LaTeXParser.L_BRACKET, LaTeXParser.L_BAR, LaTeXParser.BEGIN_ARR, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                self.atom()
                pass
            elif token in [LaTeXParser.CMD_FRAC]:
                self.enterOuterAlt(localctx, 4)
                self.state = 260
                self.frac()
                pass
            elif token in [LaTeXParser.CMD_BINOM, LaTeXParser.CMD_DBINOM, LaTeXParser.CMD_TBINOM]:
                self.enterOuterAlt(localctx, 5)
                self.state = 261
                self.binom()
                pass
            elif token in [LaTeXParser.L_FLOOR]:
                self.enterOuterAlt(localctx, 6)
                self.state = 262
                self.floor()
                pass
            elif token in [LaTeXParser.L_CEIL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 263
                self.ceil()
                pass
            elif token in [LaTeXParser.DELTA]:
                self.enterOuterAlt(localctx, 8)
                self.state = 264
                self.delta()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.GroupContext, self).__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(LaTeXParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(LaTeXParser.R_PAREN, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def L_BRACE_LITERAL(self):
            return self.getToken(LaTeXParser.L_BRACE_LITERAL, 0)

        def R_BRACE_LITERAL(self):
            return self.getToken(LaTeXParser.R_BRACE_LITERAL, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_group




    def group(self):

        localctx = LaTeXParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_group)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(LaTeXParser.L_PAREN)
                self.state = 268
                self.expr()
                self.state = 269
                self.match(LaTeXParser.R_PAREN)
                pass
            elif token in [LaTeXParser.L_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(LaTeXParser.L_BRACE)
                self.state = 272
                self.expr()
                self.state = 273
                self.match(LaTeXParser.R_BRACE)
                pass
            elif token in [LaTeXParser.L_BRACE_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.match(LaTeXParser.L_BRACE_LITERAL)
                self.state = 276
                self.expr()
                self.state = 277
                self.match(LaTeXParser.R_BRACE_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Abs_groupContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Abs_groupContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BAR(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.BAR)
            else:
                return self.getToken(LaTeXParser.BAR, i)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_abs_group




    def abs_group(self):

        localctx = LaTeXParser.Abs_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_abs_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(LaTeXParser.BAR)
            self.state = 282
            self.expr()
            self.state = 283
            self.match(LaTeXParser.BAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.AtomContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self):
            return self.getToken(LaTeXParser.LETTER, 0)

        def SYMBOL(self):
            return self.getToken(LaTeXParser.SYMBOL, 0)

        def subexpr(self):
            return self.getTypedRuleContext(LaTeXParser.SubexprContext,0)


        def NUMBER(self):
            return self.getToken(LaTeXParser.NUMBER, 0)

        def DIFFERENTIAL(self):
            return self.getToken(LaTeXParser.DIFFERENTIAL, 0)

        def matrix(self):
            return self.getTypedRuleContext(LaTeXParser.MatrixContext,0)


        def determinant(self):
            return self.getTypedRuleContext(LaTeXParser.DeterminantContext,0)


        def array(self):
            return self.getTypedRuleContext(LaTeXParser.ArrayContext,0)


        def mathit(self):
            return self.getTypedRuleContext(LaTeXParser.MathitContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_atom




    def atom(self):

        localctx = LaTeXParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.LETTER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 287
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 286
                    self.subexpr()


                pass
            elif token in [LaTeXParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(LaTeXParser.NUMBER)
                pass
            elif token in [LaTeXParser.DIFFERENTIAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
                self.match(LaTeXParser.DIFFERENTIAL)
                pass
            elif token in [LaTeXParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 4)
                self.state = 291
                self.matrix()
                pass
            elif token in [LaTeXParser.L_BAR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 292
                self.determinant()
                pass
            elif token in [LaTeXParser.BEGIN_ARR]:
                self.enterOuterAlt(localctx, 6)
                self.state = 293
                self.array()
                pass
            elif token in [LaTeXParser.CMD_MATHIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 294
                self.mathit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.MatrixContext, self).__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(LaTeXParser.L_BRACKET, 0)

        def array(self):
            return self.getTypedRuleContext(LaTeXParser.ArrayContext,0)


        def R_BRACKET(self):
            return self.getToken(LaTeXParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_matrix




    def matrix(self):

        localctx = LaTeXParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(LaTeXParser.L_BRACKET)
            self.state = 298
            self.array()
            self.state = 299
            self.match(LaTeXParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeterminantContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.DeterminantContext, self).__init__(parent, invokingState)
            self.parser = parser

        def L_BAR(self):
            return self.getToken(LaTeXParser.L_BAR, 0)

        def array(self):
            return self.getTypedRuleContext(LaTeXParser.ArrayContext,0)


        def R_BAR(self):
            return self.getToken(LaTeXParser.R_BAR, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_determinant




    def determinant(self):

        localctx = LaTeXParser.DeterminantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_determinant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(LaTeXParser.L_BAR)
            self.state = 302
            self.array()
            self.state = 303
            self.match(LaTeXParser.R_BAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.MathitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CMD_MATHIT(self):
            return self.getToken(LaTeXParser.CMD_MATHIT, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def mathit_text(self):
            return self.getTypedRuleContext(LaTeXParser.Mathit_textContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_mathit




    def mathit(self):

        localctx = LaTeXParser.MathitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_mathit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(LaTeXParser.CMD_MATHIT)
            self.state = 306
            self.match(LaTeXParser.L_BRACE)
            self.state = 307
            self.mathit_text()
            self.state = 308
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mathit_textContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Mathit_textContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.NUMBER)
            else:
                return self.getToken(LaTeXParser.NUMBER, i)

        def LETTER(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.LETTER)
            else:
                return self.getToken(LaTeXParser.LETTER, i)

        def getRuleIndex(self):
            return LaTeXParser.RULE_mathit_text




    def mathit_text(self):

        localctx = LaTeXParser.Mathit_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_mathit_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LaTeXParser.LETTER or _la==LaTeXParser.NUMBER:
                self.state = 310
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.NUMBER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LaTeXParser.T__0:
                    self.state = 311
                    self.match(LaTeXParser.T__0)
                    self.state = 312
                    _la = self._input.LA(1)
                    if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.NUMBER):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 317
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.ArrayContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_ARR(self):
            return self.getToken(LaTeXParser.BEGIN_ARR, 0)

        def array_elements(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.Array_elementsContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.Array_elementsContext,i)


        def END_ARR(self):
            return self.getToken(LaTeXParser.END_ARR, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_array




    def array(self):

        localctx = LaTeXParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(LaTeXParser.BEGIN_ARR)
            self.state = 321
            self.array_elements()
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 322
                    self.match(LaTeXParser.T__1)
                    self.state = 323
                    self.array_elements() 
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 329
            self.match(LaTeXParser.END_ARR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Array_elementsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def relation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.RelationContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.RelationContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_array_elements




    def array_elements(self):

        localctx = LaTeXParser.Array_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_array_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.relation(0)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 333
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.T__0 or _la==LaTeXParser.T__2:
                        self.state = 332
                        _la = self._input.LA(1)
                        if not(_la==LaTeXParser.T__0 or _la==LaTeXParser.T__2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()


                    self.state = 335
                    self.relation(0) 
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FracContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.FracContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.upper = None # ExprContext
            self.lower = None # ExprContext

        def CMD_FRAC(self):
            return self.getToken(LaTeXParser.CMD_FRAC, 0)

        def L_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.L_BRACE)
            else:
                return self.getToken(LaTeXParser.L_BRACE, i)

        def R_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.R_BRACE)
            else:
                return self.getToken(LaTeXParser.R_BRACE, i)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.ExprContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_frac




    def frac(self):

        localctx = LaTeXParser.FracContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_frac)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(LaTeXParser.CMD_FRAC)
            self.state = 342
            self.match(LaTeXParser.L_BRACE)
            self.state = 343
            localctx.upper = self.expr()
            self.state = 344
            self.match(LaTeXParser.R_BRACE)
            self.state = 345
            self.match(LaTeXParser.L_BRACE)
            self.state = 346
            localctx.lower = self.expr()
            self.state = 347
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinomContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.BinomContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.n = None # ExprContext
            self.k = None # ExprContext

        def L_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.L_BRACE)
            else:
                return self.getToken(LaTeXParser.L_BRACE, i)

        def R_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.R_BRACE)
            else:
                return self.getToken(LaTeXParser.R_BRACE, i)

        def CMD_BINOM(self):
            return self.getToken(LaTeXParser.CMD_BINOM, 0)

        def CMD_DBINOM(self):
            return self.getToken(LaTeXParser.CMD_DBINOM, 0)

        def CMD_TBINOM(self):
            return self.getToken(LaTeXParser.CMD_TBINOM, 0)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.ExprContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_binom




    def binom(self):

        localctx = LaTeXParser.BinomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_binom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            _la = self._input.LA(1)
            if not(((((_la - 169)) & ~0x3f) == 0 and ((1 << (_la - 169)) & ((1 << (LaTeXParser.CMD_BINOM - 169)) | (1 << (LaTeXParser.CMD_DBINOM - 169)) | (1 << (LaTeXParser.CMD_TBINOM - 169)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 350
            self.match(LaTeXParser.L_BRACE)
            self.state = 351
            localctx.n = self.expr()
            self.state = 352
            self.match(LaTeXParser.R_BRACE)
            self.state = 353
            self.match(LaTeXParser.L_BRACE)
            self.state = 354
            localctx.k = self.expr()
            self.state = 355
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.FloorContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.val = None # ExprContext

        def L_FLOOR(self):
            return self.getToken(LaTeXParser.L_FLOOR, 0)

        def R_FLOOR(self):
            return self.getToken(LaTeXParser.R_FLOOR, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_floor




    def floor(self):

        localctx = LaTeXParser.FloorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_floor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(LaTeXParser.L_FLOOR)
            self.state = 358
            localctx.val = self.expr()
            self.state = 359
            self.match(LaTeXParser.R_FLOOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CeilContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.CeilContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.val = None # ExprContext

        def L_CEIL(self):
            return self.getToken(LaTeXParser.L_CEIL, 0)

        def R_CEIL(self):
            return self.getToken(LaTeXParser.R_CEIL, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_ceil




    def ceil(self):

        localctx = LaTeXParser.CeilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_ceil)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(LaTeXParser.L_CEIL)
            self.state = 362
            localctx.val = self.expr()
            self.state = 363
            self.match(LaTeXParser.R_CEIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeltaContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.DeltaContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.x = None # ExprContext
            self.y = None # ExprContext

        def DELTA(self):
            return self.getToken(LaTeXParser.DELTA, 0)

        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.ExprContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_delta




    def delta(self):

        localctx = LaTeXParser.DeltaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_delta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(LaTeXParser.DELTA)
            self.state = 366
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 367
            self.match(LaTeXParser.L_BRACE)
            self.state = 368
            localctx.x = self.expr()
            self.state = 369
            localctx.y = self.expr()
            self.state = 370
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_normalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Func_normalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FUNC_EXP(self):
            return self.getToken(LaTeXParser.FUNC_EXP, 0)

        def FUNC_LOG(self):
            return self.getToken(LaTeXParser.FUNC_LOG, 0)

        def FUNC_LN(self):
            return self.getToken(LaTeXParser.FUNC_LN, 0)

        def FUNC_SIN(self):
            return self.getToken(LaTeXParser.FUNC_SIN, 0)

        def FUNC_COS(self):
            return self.getToken(LaTeXParser.FUNC_COS, 0)

        def FUNC_TAN(self):
            return self.getToken(LaTeXParser.FUNC_TAN, 0)

        def FUNC_CSC(self):
            return self.getToken(LaTeXParser.FUNC_CSC, 0)

        def FUNC_SEC(self):
            return self.getToken(LaTeXParser.FUNC_SEC, 0)

        def FUNC_COT(self):
            return self.getToken(LaTeXParser.FUNC_COT, 0)

        def FUNC_ARCSIN(self):
            return self.getToken(LaTeXParser.FUNC_ARCSIN, 0)

        def FUNC_ARCCOS(self):
            return self.getToken(LaTeXParser.FUNC_ARCCOS, 0)

        def FUNC_ARCTAN(self):
            return self.getToken(LaTeXParser.FUNC_ARCTAN, 0)

        def FUNC_ARCCSC(self):
            return self.getToken(LaTeXParser.FUNC_ARCCSC, 0)

        def FUNC_ARCSEC(self):
            return self.getToken(LaTeXParser.FUNC_ARCSEC, 0)

        def FUNC_ARCCOT(self):
            return self.getToken(LaTeXParser.FUNC_ARCCOT, 0)

        def FUNC_SINH(self):
            return self.getToken(LaTeXParser.FUNC_SINH, 0)

        def FUNC_COSH(self):
            return self.getToken(LaTeXParser.FUNC_COSH, 0)

        def FUNC_TANH(self):
            return self.getToken(LaTeXParser.FUNC_TANH, 0)

        def FUNC_CSCH(self):
            return self.getToken(LaTeXParser.FUNC_CSCH, 0)

        def FUNC_SECH(self):
            return self.getToken(LaTeXParser.FUNC_SECH, 0)

        def FUNC_COTH(self):
            return self.getToken(LaTeXParser.FUNC_COTH, 0)

        def FUNC_ARSINH(self):
            return self.getToken(LaTeXParser.FUNC_ARSINH, 0)

        def FUNC_ARCOSH(self):
            return self.getToken(LaTeXParser.FUNC_ARCOSH, 0)

        def FUNC_ARTANH(self):
            return self.getToken(LaTeXParser.FUNC_ARTANH, 0)

        def FUNC_ARCSCH(self):
            return self.getToken(LaTeXParser.FUNC_ARCSCH, 0)

        def FUNC_ARSECH(self):
            return self.getToken(LaTeXParser.FUNC_ARSECH, 0)

        def FUNC_ARCOTH(self):
            return self.getToken(LaTeXParser.FUNC_ARCOTH, 0)

        def FUNC_GAMMA(self):
            return self.getToken(LaTeXParser.FUNC_GAMMA, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_func_normal




    def func_normal(self):

        localctx = LaTeXParser.Func_normalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_func_normal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            _la = self._input.LA(1)
            if not(((((_la - 40)) & ~0x3f) == 0 and ((1 << (_la - 40)) & ((1 << (LaTeXParser.FUNC_EXP - 40)) | (1 << (LaTeXParser.FUNC_LOG - 40)) | (1 << (LaTeXParser.FUNC_LN - 40)) | (1 << (LaTeXParser.FUNC_SIN - 40)) | (1 << (LaTeXParser.FUNC_COS - 40)) | (1 << (LaTeXParser.FUNC_TAN - 40)) | (1 << (LaTeXParser.FUNC_CSC - 40)) | (1 << (LaTeXParser.FUNC_SEC - 40)) | (1 << (LaTeXParser.FUNC_COT - 40)) | (1 << (LaTeXParser.FUNC_ARCSIN - 40)) | (1 << (LaTeXParser.FUNC_ARCCOS - 40)) | (1 << (LaTeXParser.FUNC_ARCTAN - 40)) | (1 << (LaTeXParser.FUNC_ARCCSC - 40)) | (1 << (LaTeXParser.FUNC_ARCSEC - 40)) | (1 << (LaTeXParser.FUNC_ARCCOT - 40)) | (1 << (LaTeXParser.FUNC_SINH - 40)) | (1 << (LaTeXParser.FUNC_COSH - 40)) | (1 << (LaTeXParser.FUNC_TANH - 40)) | (1 << (LaTeXParser.FUNC_CSCH - 40)) | (1 << (LaTeXParser.FUNC_SECH - 40)) | (1 << (LaTeXParser.FUNC_COTH - 40)) | (1 << (LaTeXParser.FUNC_ARSINH - 40)) | (1 << (LaTeXParser.FUNC_ARCOSH - 40)) | (1 << (LaTeXParser.FUNC_ARTANH - 40)) | (1 << (LaTeXParser.FUNC_ARCSCH - 40)) | (1 << (LaTeXParser.FUNC_ARSECH - 40)) | (1 << (LaTeXParser.FUNC_ARCOTH - 40)) | (1 << (LaTeXParser.FUNC_GAMMA - 40)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.FuncContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.root = None # ExprContext
            self.base = None # ExprContext

        def func_normal(self):
            return self.getTypedRuleContext(LaTeXParser.Func_normalContext,0)


        def L_PAREN(self):
            return self.getToken(LaTeXParser.L_PAREN, 0)

        def func_arg(self):
            return self.getTypedRuleContext(LaTeXParser.Func_argContext,0)


        def R_PAREN(self):
            return self.getToken(LaTeXParser.R_PAREN, 0)

        def func_arg_noparens(self):
            return self.getTypedRuleContext(LaTeXParser.Func_arg_noparensContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(LaTeXParser.SubexprContext,0)


        def supexpr(self):
            return self.getTypedRuleContext(LaTeXParser.SupexprContext,0)


        def args(self):
            return self.getTypedRuleContext(LaTeXParser.ArgsContext,0)


        def LETTER(self):
            return self.getToken(LaTeXParser.LETTER, 0)

        def SYMBOL(self):
            return self.getToken(LaTeXParser.SYMBOL, 0)

        def FUNC_INT(self):
            return self.getToken(LaTeXParser.FUNC_INT, 0)

        def DIFFERENTIAL(self):
            return self.getToken(LaTeXParser.DIFFERENTIAL, 0)

        def frac(self):
            return self.getTypedRuleContext(LaTeXParser.FracContext,0)


        def additive(self):
            return self.getTypedRuleContext(LaTeXParser.AdditiveContext,0)


        def FUNC_SQRT(self):
            return self.getToken(LaTeXParser.FUNC_SQRT, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.ExprContext,i)


        def L_BRACKET(self):
            return self.getToken(LaTeXParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(LaTeXParser.R_BRACKET, 0)

        def mp(self):
            return self.getTypedRuleContext(LaTeXParser.MpContext,0)


        def FUNC_SUM(self):
            return self.getToken(LaTeXParser.FUNC_SUM, 0)

        def FUNC_PROD(self):
            return self.getToken(LaTeXParser.FUNC_PROD, 0)

        def subeq(self):
            return self.getTypedRuleContext(LaTeXParser.SubeqContext,0)


        def FUNC_LIM(self):
            return self.getToken(LaTeXParser.FUNC_LIM, 0)

        def limit_sub(self):
            return self.getTypedRuleContext(LaTeXParser.Limit_subContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_func




    def func(self):

        localctx = LaTeXParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.FUNC_EXP, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_CSCH, LaTeXParser.FUNC_SECH, LaTeXParser.FUNC_COTH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_ARCSCH, LaTeXParser.FUNC_ARSECH, LaTeXParser.FUNC_ARCOTH, LaTeXParser.FUNC_GAMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.func_normal()
                self.state = 387
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 376
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.UNDERSCORE:
                        self.state = 375
                        self.subexpr()


                    self.state = 379
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.CARET:
                        self.state = 378
                        self.supexpr()


                    pass

                elif la_ == 2:
                    self.state = 382
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.CARET:
                        self.state = 381
                        self.supexpr()


                    self.state = 385
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.UNDERSCORE:
                        self.state = 384
                        self.subexpr()


                    pass


                self.state = 394
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 389
                    self.match(LaTeXParser.L_PAREN)
                    self.state = 390
                    self.func_arg()
                    self.state = 391
                    self.match(LaTeXParser.R_PAREN)
                    pass

                elif la_ == 2:
                    self.state = 393
                    self.func_arg_noparens()
                    pass


                pass
            elif token in [LaTeXParser.LETTER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LaTeXParser.UNDERSCORE:
                    self.state = 397
                    self.subexpr()


                self.state = 400
                self.match(LaTeXParser.L_PAREN)
                self.state = 401
                self.args()
                self.state = 402
                self.match(LaTeXParser.R_PAREN)
                pass
            elif token in [LaTeXParser.FUNC_INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 404
                self.match(LaTeXParser.FUNC_INT)
                self.state = 411
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LaTeXParser.UNDERSCORE]:
                    self.state = 405
                    self.subexpr()
                    self.state = 406
                    self.supexpr()
                    pass
                elif token in [LaTeXParser.CARET]:
                    self.state = 408
                    self.supexpr()
                    self.state = 409
                    self.subexpr()
                    pass
                elif token in [LaTeXParser.ADD, LaTeXParser.SUB, LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACE_LITERAL, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_EXP, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_CSCH, LaTeXParser.FUNC_SECH, LaTeXParser.FUNC_COTH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_ARCSCH, LaTeXParser.FUNC_ARSECH, LaTeXParser.FUNC_ARCOTH, LaTeXParser.L_FLOOR, LaTeXParser.L_CEIL, LaTeXParser.DELTA, LaTeXParser.FUNC_GAMMA, LaTeXParser.BEGIN_ARR, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_BINOM, LaTeXParser.CMD_DBINOM, LaTeXParser.CMD_TBINOM, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                    pass
                else:
                    pass
                self.state = 419
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 414
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        self.state = 413
                        self.additive(0)


                    self.state = 416
                    self.match(LaTeXParser.DIFFERENTIAL)
                    pass

                elif la_ == 2:
                    self.state = 417
                    self.frac()
                    pass

                elif la_ == 3:
                    self.state = 418
                    self.additive(0)
                    pass


                pass
            elif token in [LaTeXParser.FUNC_SQRT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 421
                self.match(LaTeXParser.FUNC_SQRT)
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LaTeXParser.L_BRACKET:
                    self.state = 422
                    self.match(LaTeXParser.L_BRACKET)
                    self.state = 423
                    localctx.root = self.expr()
                    self.state = 424
                    self.match(LaTeXParser.R_BRACKET)


                self.state = 428
                self.match(LaTeXParser.L_BRACE)
                self.state = 429
                localctx.base = self.expr()
                self.state = 430
                self.match(LaTeXParser.R_BRACE)
                pass
            elif token in [LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD]:
                self.enterOuterAlt(localctx, 5)
                self.state = 432
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.FUNC_SUM or _la==LaTeXParser.FUNC_PROD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 439
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LaTeXParser.UNDERSCORE]:
                    self.state = 433
                    self.subeq()
                    self.state = 434
                    self.supexpr()
                    pass
                elif token in [LaTeXParser.CARET]:
                    self.state = 436
                    self.supexpr()
                    self.state = 437
                    self.subeq()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 441
                self.mp(0)
                pass
            elif token in [LaTeXParser.FUNC_LIM]:
                self.enterOuterAlt(localctx, 6)
                self.state = 443
                self.match(LaTeXParser.FUNC_LIM)
                self.state = 444
                self.limit_sub()
                self.state = 445
                self.mp(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.ArgsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def args(self):
            return self.getTypedRuleContext(LaTeXParser.ArgsContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_args




    def args(self):

        localctx = LaTeXParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_args)
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.expr()
                self.state = 450
                self.match(LaTeXParser.T__0)
                self.state = 451
                self.args()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Limit_subContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Limit_subContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def L_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.L_BRACE)
            else:
                return self.getToken(LaTeXParser.L_BRACE, i)

        def LIM_APPROACH_SYM(self):
            return self.getToken(LaTeXParser.LIM_APPROACH_SYM, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.R_BRACE)
            else:
                return self.getToken(LaTeXParser.R_BRACE, i)

        def LETTER(self):
            return self.getToken(LaTeXParser.LETTER, 0)

        def SYMBOL(self):
            return self.getToken(LaTeXParser.SYMBOL, 0)

        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def ADD(self):
            return self.getToken(LaTeXParser.ADD, 0)

        def SUB(self):
            return self.getToken(LaTeXParser.SUB, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_limit_sub




    def limit_sub(self):

        localctx = LaTeXParser.Limit_subContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_limit_sub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 457
            self.match(LaTeXParser.L_BRACE)
            self.state = 458
            _la = self._input.LA(1)
            if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 459
            self.match(LaTeXParser.LIM_APPROACH_SYM)
            self.state = 460
            self.expr()
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LaTeXParser.CARET:
                self.state = 461
                self.match(LaTeXParser.CARET)
                self.state = 462
                self.match(LaTeXParser.L_BRACE)
                self.state = 463
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 464
                self.match(LaTeXParser.R_BRACE)


            self.state = 467
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_argContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Func_argContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def func_arg(self):
            return self.getTypedRuleContext(LaTeXParser.Func_argContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_func_arg




    def func_arg(self):

        localctx = LaTeXParser.Func_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_func_arg)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.expr()
                self.state = 471
                self.match(LaTeXParser.T__0)
                self.state = 472
                self.func_arg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_arg_noparensContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Func_arg_noparensContext, self).__init__(parent, invokingState)
            self.parser = parser

        def mp_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Mp_nofuncContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_func_arg_noparens




    def func_arg_noparens(self):

        localctx = LaTeXParser.Func_arg_noparensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_func_arg_noparens)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.mp_nofunc(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.SubexprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_subexpr




    def subexpr(self):

        localctx = LaTeXParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.L_BRACKET, LaTeXParser.L_BAR, LaTeXParser.BEGIN_ARR, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 479
                self.atom()
                pass
            elif token in [LaTeXParser.L_BRACE]:
                self.state = 480
                self.match(LaTeXParser.L_BRACE)
                self.state = 481
                self.expr()
                self.state = 482
                self.match(LaTeXParser.R_BRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SupexprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.SupexprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_supexpr




    def supexpr(self):

        localctx = LaTeXParser.SupexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(LaTeXParser.CARET)
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.L_BRACKET, LaTeXParser.L_BAR, LaTeXParser.BEGIN_ARR, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 487
                self.atom()
                pass
            elif token in [LaTeXParser.L_BRACE]:
                self.state = 488
                self.match(LaTeXParser.L_BRACE)
                self.state = 489
                self.expr()
                self.state = 490
                self.match(LaTeXParser.R_BRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubeqContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.SubeqContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def equality(self):
            return self.getTypedRuleContext(LaTeXParser.EqualityContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_subeq




    def subeq(self):

        localctx = LaTeXParser.SubeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_subeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 495
            self.match(LaTeXParser.L_BRACE)
            self.state = 496
            self.equality()
            self.state = 497
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SupeqContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.SupeqContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def equality(self):
            return self.getTypedRuleContext(LaTeXParser.EqualityContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_supeq




    def supeq(self):

        localctx = LaTeXParser.SupeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_supeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 500
            self.match(LaTeXParser.L_BRACE)
            self.state = 501
            self.equality()
            self.state = 502
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.relation_sempred
        self._predicates[4] = self.additive_sempred
        self._predicates[5] = self.mp_sempred
        self._predicates[6] = self.mp_nofunc_sempred
        self._predicates[15] = self.exp_sempred
        self._predicates[16] = self.exp_nofunc_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def relation_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def additive_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def mp_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def mp_nofunc_sempred(self, localctx, predIndex):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp_sempred(self, localctx, predIndex):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp_nofunc_sempred(self, localctx, predIndex):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         



