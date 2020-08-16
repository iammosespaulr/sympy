# Generated from /Users/mosespaul/Desktop/Coding/Mathpix/sympy/sympy/parsing/latex/LaTeX.g4 by ANTLR 4.8
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\u00cb\u0270\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62")
        buf.write(u"\4\63\t\63\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3o\n\3\f")
        buf.write(u"\3\16\3r\13\3\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write(u"\3\6\3\6\7\6\u0080\n\6\f\6\16\6\u0083\13\6\3\7\3\7\3")
        buf.write(u"\7\3\7\3\7\3\7\7\7\u008b\n\7\f\7\16\7\u008e\13\7\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\7\b\u0096\n\b\f\b\16\b\u0099\13")
        buf.write(u"\b\3\t\3\t\3\t\6\t\u009e\n\t\r\t\16\t\u009f\5\t\u00a2")
        buf.write(u"\n\t\3\n\3\n\3\n\3\n\7\n\u00a8\n\n\f\n\16\n\u00ab\13")
        buf.write(u"\n\5\n\u00ad\n\n\3\13\3\13\7\13\u00b1\n\13\f\13\16\13")
        buf.write(u"\u00b4\13\13\3\f\3\f\7\f\u00b8\n\f\f\f\16\f\u00bb\13")
        buf.write(u"\f\3\r\3\r\5\r\u00bf\n\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\5\16\u00c7\n\16\3\17\3\17\3\17\3\17\5\17\u00cd\n\17")
        buf.write(u"\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u00d5\n\20\3\20\3")
        buf.write(u"\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\5\21\u00e3\n\21\3\21\5\21\u00e6\n\21\7\21\u00e8\n\21")
        buf.write(u"\f\21\16\21\u00eb\13\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\3\22\3\22\5\22\u00f7\n\22\3\22\5\22\u00fa")
        buf.write(u"\n\22\7\22\u00fc\n\22\f\22\16\22\u00ff\13\22\3\23\3\23")
        buf.write(u"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u010a\n\23\3")
        buf.write(u"\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0114\n\24")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\5\25\u0136\n\25\3\26\3\26\3\26\3\26\3\27\3\27\5\27")
        buf.write(u"\u013e\n\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\3\27\5\27\u014c\n\27\3\30\3\30\3\30\3\30")
        buf.write(u"\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\33\3\33\3\33\3\33\7\33\u0160\n\33\f\33\16\33\u0163\13")
        buf.write(u"\33\3\33\3\33\7\33\u0167\n\33\f\33\16\33\u016a\13\33")
        buf.write(u"\3\33\7\33\u016d\n\33\f\33\16\33\u0170\13\33\5\33\u0172")
        buf.write(u"\n\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\5\35\u017f\n\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\5\36\u0187\n\36\3\37\3\37\5\37\u018b\n\37\3\37\3\37")
        buf.write(u"\3\37\7\37\u0190\n\37\f\37\16\37\u0193\13\37\3\37\5\37")
        buf.write(u"\u0196\n\37\3\37\3\37\3 \3 \5 \u019c\n \3 \3 \3 \7 \u01a1")
        buf.write(u"\n \f \16 \u01a4\13 \3 \5 \u01a7\n \3 \3 \3!\3!\3!\3")
        buf.write(u"!\3!\3\"\6\"\u01b1\n\"\r\"\16\"\u01b2\3#\3#\3#\3#\7#")
        buf.write(u"\u01b9\n#\f#\16#\u01bc\13#\3#\3#\3$\3$\5$\u01c2\n$\3")
        buf.write(u"$\7$\u01c5\n$\f$\16$\u01c8\13$\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write(u"%\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write(u"(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3+\3+\5+\u01ed\n+\3+\5+")
        buf.write(u"\u01f0\n+\3+\5+\u01f3\n+\3+\5+\u01f6\n+\5+\u01f8\n+\3")
        buf.write(u"+\3+\3+\3+\3+\5+\u01ff\n+\3+\3+\5+\u0203\n+\3+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\3+\3+\5+\u0210\n+\3+\5+\u0213\n+\3")
        buf.write(u"+\3+\3+\5+\u0218\n+\3+\3+\3+\3+\3+\5+\u021f\n+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u022c\n+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\5+\u0234\n+\3,\3,\3,\3,\3,\5,\u023b\n,\3-\5-\u023e")
        buf.write(u"\n-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0249\n-\3-\3-\3.\3")
        buf.write(u".\3.\3.\3.\5.\u0252\n.\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\5\60\u025c\n\60\3\61\3\61\3\61\3\61\3\61\3\61\5")
        buf.write(u"\61\u0264\n\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write(u"\3\63\3\63\3\63\6\u0191\u01a2\u01ba\u01c6\b\4\n\f\16")
        buf.write(u" \"\64\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(u",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bd\2\f\4\2\u00bb")
        buf.write(u"\u00be\u00c1\u00c2\3\2\25\26\5\2\27\30\u00ae\u00b0\u00b6")
        buf.write(u"\u00b6\4\2\u00b9\u00b9\u00ca\u00ca\3\2#$\4\2##%%\3\2")
        buf.write(u"\u00b9\u00ba\3\2\6\7\b\2\63MTTVXZZ\\\\hi\3\2\61\62\2")
        buf.write(u"\u029f\2f\3\2\2\2\4h\3\2\2\2\6s\3\2\2\2\bw\3\2\2\2\n")
        buf.write(u"y\3\2\2\2\f\u0084\3\2\2\2\16\u008f\3\2\2\2\20\u00a1\3")
        buf.write(u"\2\2\2\22\u00ac\3\2\2\2\24\u00ae\3\2\2\2\26\u00b5\3\2")
        buf.write(u"\2\2\30\u00be\3\2\2\2\32\u00c0\3\2\2\2\34\u00c8\3\2\2")
        buf.write(u"\2\36\u00d0\3\2\2\2 \u00d8\3\2\2\2\"\u00ec\3\2\2\2$\u0109")
        buf.write(u"\3\2\2\2&\u0113\3\2\2\2(\u0135\3\2\2\2*\u0137\3\2\2\2")
        buf.write(u",\u014b\3\2\2\2.\u014d\3\2\2\2\60\u0151\3\2\2\2\62\u0155")
        buf.write(u"\3\2\2\2\64\u015b\3\2\2\2\66\u0173\3\2\2\28\u0178\3\2")
        buf.write(u"\2\2:\u0180\3\2\2\2<\u0188\3\2\2\2>\u0199\3\2\2\2@\u01aa")
        buf.write(u"\3\2\2\2B\u01b0\3\2\2\2D\u01b4\3\2\2\2F\u01bf\3\2\2\2")
        buf.write(u"H\u01c9\3\2\2\2J\u01d1\3\2\2\2L\u01d9\3\2\2\2N\u01dd")
        buf.write(u"\3\2\2\2P\u01e1\3\2\2\2R\u01e8\3\2\2\2T\u0233\3\2\2\2")
        buf.write(u"V\u023a\3\2\2\2X\u023d\3\2\2\2Z\u0251\3\2\2\2\\\u0253")
        buf.write(u"\3\2\2\2^\u0255\3\2\2\2`\u025d\3\2\2\2b\u0265\3\2\2\2")
        buf.write(u"d\u026a\3\2\2\2fg\5\4\3\2g\3\3\2\2\2hi\b\3\1\2ij\5\b")
        buf.write(u"\5\2jp\3\2\2\2kl\f\4\2\2lm\t\2\2\2mo\5\4\3\5nk\3\2\2")
        buf.write(u"\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\5\3\2\2\2rp\3\2\2\2")
        buf.write(u"st\5\b\5\2tu\7\u00bb\2\2uv\5\b\5\2v\7\3\2\2\2wx\5\n\6")
        buf.write(u"\2x\t\3\2\2\2yz\b\6\1\2z{\5\f\7\2{\u0081\3\2\2\2|}\f")
        buf.write(u"\4\2\2}~\t\3\2\2~\u0080\5\n\6\5\177|\3\2\2\2\u0080\u0083")
        buf.write(u"\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write(u"\13\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0085\b\7\1\2\u0085")
        buf.write(u"\u0086\5\20\t\2\u0086\u008c\3\2\2\2\u0087\u0088\f\4\2")
        buf.write(u"\2\u0088\u0089\t\4\2\2\u0089\u008b\5\f\7\5\u008a\u0087")
        buf.write(u"\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008c")
        buf.write(u"\u008d\3\2\2\2\u008d\r\3\2\2\2\u008e\u008c\3\2\2\2\u008f")
        buf.write(u"\u0090\b\b\1\2\u0090\u0091\5\22\n\2\u0091\u0097\3\2\2")
        buf.write(u"\2\u0092\u0093\f\4\2\2\u0093\u0094\t\4\2\2\u0094\u0096")
        buf.write(u"\5\16\b\5\u0095\u0092\3\2\2\2\u0096\u0099\3\2\2\2\u0097")
        buf.write(u"\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\17\3\2\2\2\u0099")
        buf.write(u"\u0097\3\2\2\2\u009a\u009b\t\3\2\2\u009b\u00a2\5\20\t")
        buf.write(u"\2\u009c\u009e\5\24\13\2\u009d\u009c\3\2\2\2\u009e\u009f")
        buf.write(u"\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write(u"\u00a2\3\2\2\2\u00a1\u009a\3\2\2\2\u00a1\u009d\3\2\2")
        buf.write(u"\2\u00a2\21\3\2\2\2\u00a3\u00a4\t\3\2\2\u00a4\u00ad\5")
        buf.write(u"\22\n\2\u00a5\u00a9\5\24\13\2\u00a6\u00a8\5\26\f\2\u00a7")
        buf.write(u"\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2")
        buf.write(u"\2\u00a9\u00aa\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9")
        buf.write(u"\3\2\2\2\u00ac\u00a3\3\2\2\2\u00ac\u00a5\3\2\2\2\u00ad")
        buf.write(u"\23\3\2\2\2\u00ae\u00b2\5 \21\2\u00af\u00b1\5\30\r\2")
        buf.write(u"\u00b0\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0")
        buf.write(u"\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\25\3\2\2\2\u00b4\u00b2")
        buf.write(u"\3\2\2\2\u00b5\u00b9\5\"\22\2\u00b6\u00b8\5\30\r\2\u00b7")
        buf.write(u"\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2")
        buf.write(u"\2\u00b9\u00ba\3\2\2\2\u00ba\27\3\2\2\2\u00bb\u00b9\3")
        buf.write(u"\2\2\2\u00bc\u00bf\7\u00c9\2\2\u00bd\u00bf\5\32\16\2")
        buf.write(u"\u00be\u00bc\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf\31\3\2")
        buf.write(u"\2\2\u00c0\u00c6\7#\2\2\u00c1\u00c7\5\36\20\2\u00c2\u00c7")
        buf.write(u"\5\34\17\2\u00c3\u00c4\5\36\20\2\u00c4\u00c5\5\34\17")
        buf.write(u"\2\u00c5\u00c7\3\2\2\2\u00c6\u00c1\3\2\2\2\u00c6\u00c2")
        buf.write(u"\3\2\2\2\u00c6\u00c3\3\2\2\2\u00c7\33\3\2\2\2\u00c8\u00c9")
        buf.write(u"\7\u00b4\2\2\u00c9\u00cc\7\35\2\2\u00ca\u00cd\5\b\5\2")
        buf.write(u"\u00cb\u00cd\5\6\4\2\u00cc\u00ca\3\2\2\2\u00cc\u00cb")
        buf.write(u"\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\7\36\2\2\u00cf")
        buf.write(u"\35\3\2\2\2\u00d0\u00d1\7\u00b5\2\2\u00d1\u00d4\7\35")
        buf.write(u"\2\2\u00d2\u00d5\5\b\5\2\u00d3\u00d5\5\6\4\2\u00d4\u00d2")
        buf.write(u"\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write(u"\u00d7\7\36\2\2\u00d7\37\3\2\2\2\u00d8\u00d9\b\21\1\2")
        buf.write(u"\u00d9\u00da\5$\23\2\u00da\u00e9\3\2\2\2\u00db\u00dc")
        buf.write(u"\f\4\2\2\u00dc\u00e2\7\u00b5\2\2\u00dd\u00e3\5,\27\2")
        buf.write(u"\u00de\u00df\7\35\2\2\u00df\u00e0\5\b\5\2\u00e0\u00e1")
        buf.write(u"\7\36\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00dd\3\2\2\2\u00e2")
        buf.write(u"\u00de\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e6\5^\60")
        buf.write(u"\2\u00e5\u00e4\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e8")
        buf.write(u"\3\2\2\2\u00e7\u00db\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9")
        buf.write(u"\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea!\3\2\2\2\u00eb")
        buf.write(u"\u00e9\3\2\2\2\u00ec\u00ed\b\22\1\2\u00ed\u00ee\5&\24")
        buf.write(u"\2\u00ee\u00fd\3\2\2\2\u00ef\u00f0\f\4\2\2\u00f0\u00f6")
        buf.write(u"\7\u00b5\2\2\u00f1\u00f7\5,\27\2\u00f2\u00f3\7\35\2\2")
        buf.write(u"\u00f3\u00f4\5\b\5\2\u00f4\u00f5\7\36\2\2\u00f5\u00f7")
        buf.write(u"\3\2\2\2\u00f6\u00f1\3\2\2\2\u00f6\u00f2\3\2\2\2\u00f7")
        buf.write(u"\u00f9\3\2\2\2\u00f8\u00fa\5^\60\2\u00f9\u00f8\3\2\2")
        buf.write(u"\2\u00f9\u00fa\3\2\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00ef")
        buf.write(u"\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd")
        buf.write(u"\u00fe\3\2\2\2\u00fe#\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100")
        buf.write(u"\u010a\5(\25\2\u0101\u010a\5*\26\2\u0102\u010a\5T+\2")
        buf.write(u"\u0103\u010a\5,\27\2\u0104\u010a\5H%\2\u0105\u010a\5")
        buf.write(u"J&\2\u0106\u010a\5L\'\2\u0107\u010a\5N(\2\u0108\u010a")
        buf.write(u"\5P)\2\u0109\u0100\3\2\2\2\u0109\u0101\3\2\2\2\u0109")
        buf.write(u"\u0102\3\2\2\2\u0109\u0103\3\2\2\2\u0109\u0104\3\2\2")
        buf.write(u"\2\u0109\u0105\3\2\2\2\u0109\u0106\3\2\2\2\u0109\u0107")
        buf.write(u"\3\2\2\2\u0109\u0108\3\2\2\2\u010a%\3\2\2\2\u010b\u0114")
        buf.write(u"\5(\25\2\u010c\u0114\5*\26\2\u010d\u0114\5,\27\2\u010e")
        buf.write(u"\u0114\5H%\2\u010f\u0114\5J&\2\u0110\u0114\5L\'\2\u0111")
        buf.write(u"\u0114\5N(\2\u0112\u0114\5P)\2\u0113\u010b\3\2\2\2\u0113")
        buf.write(u"\u010c\3\2\2\2\u0113\u010d\3\2\2\2\u0113\u010e\3\2\2")
        buf.write(u"\2\u0113\u010f\3\2\2\2\u0113\u0110\3\2\2\2\u0113\u0111")
        buf.write(u"\3\2\2\2\u0113\u0112\3\2\2\2\u0114\'\3\2\2\2\u0115\u0116")
        buf.write(u"\7\33\2\2\u0116\u0117\5\b\5\2\u0117\u0118\7\34\2\2\u0118")
        buf.write(u"\u0136\3\2\2\2\u0119\u011a\7!\2\2\u011a\u011b\5\b\5\2")
        buf.write(u"\u011b\u011c\7\"\2\2\u011c\u0136\3\2\2\2\u011d\u011e")
        buf.write(u"\7\35\2\2\u011e\u011f\5\b\5\2\u011f\u0120\7\36\2\2\u0120")
        buf.write(u"\u0136\3\2\2\2\u0121\u0122\7\37\2\2\u0122\u0123\5\b\5")
        buf.write(u"\2\u0123\u0124\7 \2\2\u0124\u0136\3\2\2\2\u0125\u0126")
        buf.write(u"\7\37\2\2\u0126\u0127\5\b\5\2\u0127\u0128\7,\2\2\u0128")
        buf.write(u"\u0136\3\2\2\2\u0129\u012a\7,\2\2\u012a\u012b\5\b\5\2")
        buf.write(u"\u012b\u012c\7 \2\2\u012c\u0136\3\2\2\2\u012d\u012e\7")
        buf.write(u"\33\2\2\u012e\u012f\5\b\5\2\u012f\u0130\7,\2\2\u0130")
        buf.write(u"\u0136\3\2\2\2\u0131\u0132\7,\2\2\u0132\u0133\5\b\5\2")
        buf.write(u"\u0133\u0134\7\34\2\2\u0134\u0136\3\2\2\2\u0135\u0115")
        buf.write(u"\3\2\2\2\u0135\u0119\3\2\2\2\u0135\u011d\3\2\2\2\u0135")
        buf.write(u"\u0121\3\2\2\2\u0135\u0125\3\2\2\2\u0135\u0129\3\2\2")
        buf.write(u"\2\u0135\u012d\3\2\2\2\u0135\u0131\3\2\2\2\u0136)\3\2")
        buf.write(u"\2\2\u0137\u0138\7#\2\2\u0138\u0139\5\b\5\2\u0139\u013a")
        buf.write(u"\7#\2\2\u013a+\3\2\2\2\u013b\u013d\t\5\2\2\u013c\u013e")
        buf.write(u"\5^\60\2\u013d\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write(u"\u014c\3\2\2\2\u013f\u014c\7\u00ba\2\2\u0140\u014c\7")
        buf.write(u"\u00b7\2\2\u0141\u014c\5<\37\2\u0142\u014c\5> \2\u0143")
        buf.write(u"\u014c\5D#\2\u0144\u014c\5@!\2\u0145\u014c\5\66\34\2")
        buf.write(u"\u0146\u014c\58\35\2\u0147\u014c\5:\36\2\u0148\u014c")
        buf.write(u"\5\62\32\2\u0149\u014c\5.\30\2\u014a\u014c\5\60\31\2")
        buf.write(u"\u014b\u013b\3\2\2\2\u014b\u013f\3\2\2\2\u014b\u0140")
        buf.write(u"\3\2\2\2\u014b\u0141\3\2\2\2\u014b\u0142\3\2\2\2\u014b")
        buf.write(u"\u0143\3\2\2\2\u014b\u0144\3\2\2\2\u014b\u0145\3\2\2")
        buf.write(u"\2\u014b\u0146\3\2\2\2\u014b\u0147\3\2\2\2\u014b\u0148")
        buf.write(u"\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c")
        buf.write(u"-\3\2\2\2\u014d\u014e\7(\2\2\u014e\u014f\5\b\5\2\u014f")
        buf.write(u"\u0150\t\6\2\2\u0150/\3\2\2\2\u0151\u0152\t\7\2\2\u0152")
        buf.write(u"\u0153\5\b\5\2\u0153\u0154\7)\2\2\u0154\61\3\2\2\2\u0155")
        buf.write(u"\u0156\t\b\2\2\u0156\u0157\7\u00b5\2\2\u0157\u0158\7")
        buf.write(u"\35\2\2\u0158\u0159\7p\2\2\u0159\u015a\7\36\2\2\u015a")
        buf.write(u"\63\3\2\2\2\u015b\u0171\t\5\2\2\u015c\u015d\7\u00b5\2")
        buf.write(u"\2\u015d\u0161\7\35\2\2\u015e\u0160\7o\2\2\u015f\u015e")
        buf.write(u"\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161")
        buf.write(u"\u0162\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u0161\3\2\2")
        buf.write(u"\2\u0164\u0172\7\36\2\2\u0165\u0167\7\3\2\2\u0166\u0165")
        buf.write(u"\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168")
        buf.write(u"\u0169\3\2\2\2\u0169\u0172\3\2\2\2\u016a\u0168\3\2\2")
        buf.write(u"\2\u016b\u016d\7\4\2\2\u016c\u016b\3\2\2\2\u016d\u0170")
        buf.write(u"\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f")
        buf.write(u"\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u015c\3\2\2")
        buf.write(u"\2\u0171\u0168\3\2\2\2\u0171\u016e\3\2\2\2\u0172\65\3")
        buf.write(u"\2\2\2\u0173\u0174\5\64\33\2\u0174\u0175\7\33\2\2\u0175")
        buf.write(u"\u0176\5\b\5\2\u0176\u0177\7\34\2\2\u0177\67\3\2\2\2")
        buf.write(u"\u0178\u017e\7m\2\2\u0179\u017a\7\35\2\2\u017a\u017b")
        buf.write(u"\5\b\5\2\u017b\u017c\7\36\2\2\u017c\u017f\3\2\2\2\u017d")
        buf.write(u"\u017f\5,\27\2\u017e\u0179\3\2\2\2\u017e\u017d\3\2\2")
        buf.write(u"\2\u017f9\3\2\2\2\u0180\u0186\7n\2\2\u0181\u0182\7\35")
        buf.write(u"\2\2\u0182\u0183\5\b\5\2\u0183\u0184\7\36\2\2\u0184\u0187")
        buf.write(u"\3\2\2\2\u0185\u0187\5,\27\2\u0186\u0181\3\2\2\2\u0186")
        buf.write(u"\u0185\3\2\2\2\u0187;\3\2\2\2\u0188\u018a\7&\2\2\u0189")
        buf.write(u"\u018b\7]\2\2\u018a\u0189\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write(u"\u018b\u018c\3\2\2\2\u018c\u0191\5F$\2\u018d\u018e\7")
        buf.write(u"\5\2\2\u018e\u0190\5F$\2\u018f\u018d\3\2\2\2\u0190\u0193")
        buf.write(u"\3\2\2\2\u0191\u0192\3\2\2\2\u0191\u018f\3\2\2\2\u0192")
        buf.write(u"\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0196\7^\2\2")
        buf.write(u"\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197")
        buf.write(u"\3\2\2\2\u0197\u0198\7\'\2\2\u0198=\3\2\2\2\u0199\u019b")
        buf.write(u"\7%\2\2\u019a\u019c\7]\2\2\u019b\u019a\3\2\2\2\u019b")
        buf.write(u"\u019c\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u01a2\5F$\2")
        buf.write(u"\u019e\u019f\7\5\2\2\u019f\u01a1\5F$\2\u01a0\u019e\3")
        buf.write(u"\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a2")
        buf.write(u"\u01a0\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2")
        buf.write(u"\2\u01a5\u01a7\7^\2\2\u01a6\u01a5\3\2\2\2\u01a6\u01a7")
        buf.write(u"\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\7$\2\2\u01a9")
        buf.write(u"?\3\2\2\2\u01aa\u01ab\7\u00b3\2\2\u01ab\u01ac\7\35\2")
        buf.write(u"\2\u01ac\u01ad\5B\"\2\u01ad\u01ae\7\36\2\2\u01aeA\3\2")
        buf.write(u"\2\2\u01af\u01b1\t\b\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b2")
        buf.write(u"\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write(u"C\3\2\2\2\u01b4\u01b5\7]\2\2\u01b5\u01ba\5F$\2\u01b6")
        buf.write(u"\u01b7\7\5\2\2\u01b7\u01b9\5F$\2\u01b8\u01b6\3\2\2\2")
        buf.write(u"\u01b9\u01bc\3\2\2\2\u01ba\u01bb\3\2\2\2\u01ba\u01b8")
        buf.write(u"\3\2\2\2\u01bb\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd")
        buf.write(u"\u01be\7^\2\2\u01beE\3\2\2\2\u01bf\u01c6\5\4\3\2\u01c0")
        buf.write(u"\u01c2\t\t\2\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2\2")
        buf.write(u"\2\u01c2\u01c3\3\2\2\2\u01c3\u01c5\5\4\3\2\u01c4\u01c1")
        buf.write(u"\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c6")
        buf.write(u"\u01c4\3\2\2\2\u01c7G\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9")
        buf.write(u"\u01ca\7\u00b1\2\2\u01ca\u01cb\7\35\2\2\u01cb\u01cc\5")
        buf.write(u"\b\5\2\u01cc\u01cd\7\36\2\2\u01cd\u01ce\7\35\2\2\u01ce")
        buf.write(u"\u01cf\5\b\5\2\u01cf\u01d0\7\36\2\2\u01d0I\3\2\2\2\u01d1")
        buf.write(u"\u01d2\7\u00b2\2\2\u01d2\u01d3\7\35\2\2\u01d3\u01d4\5")
        buf.write(u"\b\5\2\u01d4\u01d5\7\36\2\2\u01d5\u01d6\7\35\2\2\u01d6")
        buf.write(u"\u01d7\5\b\5\2\u01d7\u01d8\7\36\2\2\u01d8K\3\2\2\2\u01d9")
        buf.write(u"\u01da\7N\2\2\u01da\u01db\5\b\5\2\u01db\u01dc\7O\2\2")
        buf.write(u"\u01dcM\3\2\2\2\u01dd\u01de\7P\2\2\u01de\u01df\5\b\5")
        buf.write(u"\2\u01df\u01e0\7Q\2\2\u01e0O\3\2\2\2\u01e1\u01e2\7U\2")
        buf.write(u"\2\u01e2\u01e3\7\u00b4\2\2\u01e3\u01e4\7\35\2\2\u01e4")
        buf.write(u"\u01e5\5\b\5\2\u01e5\u01e6\5\b\5\2\u01e6\u01e7\7\36\2")
        buf.write(u"\2\u01e7Q\3\2\2\2\u01e8\u01e9\t\n\2\2\u01e9S\3\2\2\2")
        buf.write(u"\u01ea\u01f7\5R*\2\u01eb\u01ed\5^\60\2\u01ec\u01eb\3")
        buf.write(u"\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ef\3\2\2\2\u01ee")
        buf.write(u"\u01f0\5`\61\2\u01ef\u01ee\3\2\2\2\u01ef\u01f0\3\2\2")
        buf.write(u"\2\u01f0\u01f8\3\2\2\2\u01f1\u01f3\5`\61\2\u01f2\u01f1")
        buf.write(u"\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f5\3\2\2\2\u01f4")
        buf.write(u"\u01f6\5^\60\2\u01f5\u01f4\3\2\2\2\u01f5\u01f6\3\2\2")
        buf.write(u"\2\u01f6\u01f8\3\2\2\2\u01f7\u01ec\3\2\2\2\u01f7\u01f2")
        buf.write(u"\3\2\2\2\u01f8\u01fe\3\2\2\2\u01f9\u01fa\7\33\2\2\u01fa")
        buf.write(u"\u01fb\5Z.\2\u01fb\u01fc\7\34\2\2\u01fc\u01ff\3\2\2\2")
        buf.write(u"\u01fd\u01ff\5\\/\2\u01fe\u01f9\3\2\2\2\u01fe\u01fd\3")
        buf.write(u"\2\2\2\u01ff\u0234\3\2\2\2\u0200\u0202\t\5\2\2\u0201")
        buf.write(u"\u0203\5^\60\2\u0202\u0201\3\2\2\2\u0202\u0203\3\2\2")
        buf.write(u"\2\u0203\u0204\3\2\2\2\u0204\u0205\7\33\2\2\u0205\u0206")
        buf.write(u"\5V,\2\u0206\u0207\7\34\2\2\u0207\u0234\3\2\2\2\u0208")
        buf.write(u"\u020f\7\60\2\2\u0209\u020a\5^\60\2\u020a\u020b\5`\61")
        buf.write(u"\2\u020b\u0210\3\2\2\2\u020c\u020d\5`\61\2\u020d\u020e")
        buf.write(u"\5^\60\2\u020e\u0210\3\2\2\2\u020f\u0209\3\2\2\2\u020f")
        buf.write(u"\u020c\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0217\3\2\2")
        buf.write(u"\2\u0211\u0213\5\n\6\2\u0212\u0211\3\2\2\2\u0212\u0213")
        buf.write(u"\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0218\7\u00b7\2\2")
        buf.write(u"\u0215\u0218\5H%\2\u0216\u0218\5\n\6\2\u0217\u0212\3")
        buf.write(u"\2\2\2\u0217\u0215\3\2\2\2\u0217\u0216\3\2\2\2\u0218")
        buf.write(u"\u0234\3\2\2\2\u0219\u021e\7\u00ac\2\2\u021a\u021b\7")
        buf.write(u"!\2\2\u021b\u021c\5\b\5\2\u021c\u021d\7\"\2\2\u021d\u021f")
        buf.write(u"\3\2\2\2\u021e\u021a\3\2\2\2\u021e\u021f\3\2\2\2\u021f")
        buf.write(u"\u0220\3\2\2\2\u0220\u0221\7\35\2\2\u0221\u0222\5\b\5")
        buf.write(u"\2\u0222\u0223\7\36\2\2\u0223\u0234\3\2\2\2\u0224\u022b")
        buf.write(u"\t\13\2\2\u0225\u0226\5b\62\2\u0226\u0227\5`\61\2\u0227")
        buf.write(u"\u022c\3\2\2\2\u0228\u0229\5`\61\2\u0229\u022a\5b\62")
        buf.write(u"\2\u022a\u022c\3\2\2\2\u022b\u0225\3\2\2\2\u022b\u0228")
        buf.write(u"\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022e\5\f\7\2\u022e")
        buf.write(u"\u0234\3\2\2\2\u022f\u0230\7.\2\2\u0230\u0231\5X-\2\u0231")
        buf.write(u"\u0232\5\f\7\2\u0232\u0234\3\2\2\2\u0233\u01ea\3\2\2")
        buf.write(u"\2\u0233\u0200\3\2\2\2\u0233\u0208\3\2\2\2\u0233\u0219")
        buf.write(u"\3\2\2\2\u0233\u0224\3\2\2\2\u0233\u022f\3\2\2\2\u0234")
        buf.write(u"U\3\2\2\2\u0235\u0236\5\b\5\2\u0236\u0237\7\7\2\2\u0237")
        buf.write(u"\u0238\5V,\2\u0238\u023b\3\2\2\2\u0239\u023b\5\b\5\2")
        buf.write(u"\u023a\u0235\3\2\2\2\u023a\u0239\3\2\2\2\u023bW\3\2\2")
        buf.write(u"\2\u023c\u023e\7\b\2\2\u023d\u023c\3\2\2\2\u023d\u023e")
        buf.write(u"\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0240\7\u00b4\2\2")
        buf.write(u"\u0240\u0241\7\35\2\2\u0241\u0242\t\5\2\2\u0242\u0243")
        buf.write(u"\7/\2\2\u0243\u0248\5\b\5\2\u0244\u0245\7\u00b5\2\2\u0245")
        buf.write(u"\u0246\7\35\2\2\u0246\u0247\t\3\2\2\u0247\u0249\7\36")
        buf.write(u"\2\2\u0248\u0244\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024a")
        buf.write(u"\3\2\2\2\u024a\u024b\7\36\2\2\u024bY\3\2\2\2\u024c\u0252")
        buf.write(u"\5\b\5\2\u024d\u024e\5\b\5\2\u024e\u024f\7\7\2\2\u024f")
        buf.write(u"\u0250\5Z.\2\u0250\u0252\3\2\2\2\u0251\u024c\3\2\2\2")
        buf.write(u"\u0251\u024d\3\2\2\2\u0252[\3\2\2\2\u0253\u0254\5\16")
        buf.write(u"\b\2\u0254]\3\2\2\2\u0255\u025b\7\u00b4\2\2\u0256\u025c")
        buf.write(u"\5,\27\2\u0257\u0258\7\35\2\2\u0258\u0259\5\b\5\2\u0259")
        buf.write(u"\u025a\7\36\2\2\u025a\u025c\3\2\2\2\u025b\u0256\3\2\2")
        buf.write(u"\2\u025b\u0257\3\2\2\2\u025c_\3\2\2\2\u025d\u0263\7\u00b5")
        buf.write(u"\2\2\u025e\u0264\5,\27\2\u025f\u0260\7\35\2\2\u0260\u0261")
        buf.write(u"\5\b\5\2\u0261\u0262\7\36\2\2\u0262\u0264\3\2\2\2\u0263")
        buf.write(u"\u025e\3\2\2\2\u0263\u025f\3\2\2\2\u0264a\3\2\2\2\u0265")
        buf.write(u"\u0266\7\u00b4\2\2\u0266\u0267\7\35\2\2\u0267\u0268\5")
        buf.write(u"\6\4\2\u0268\u0269\7\36\2\2\u0269c\3\2\2\2\u026a\u026b")
        buf.write(u"\7\u00b4\2\2\u026b\u026c\7\35\2\2\u026c\u026d\5\6\4\2")
        buf.write(u"\u026d\u026e\7\36\2\2\u026ee\3\2\2\2>p\u0081\u008c\u0097")
        buf.write(u"\u009f\u00a1\u00a9\u00ac\u00b2\u00b9\u00be\u00c6\u00cc")
        buf.write(u"\u00d4\u00e2\u00e5\u00e9\u00f6\u00f9\u00fd\u0109\u0113")
        buf.write(u"\u0135\u013d\u014b\u0161\u0168\u016e\u0171\u017e\u0186")
        buf.write(u"\u018a\u0191\u0195\u019b\u01a2\u01a6\u01b2\u01ba\u01c1")
        buf.write(u"\u01c6\u01ec\u01ef\u01f2\u01f5\u01f7\u01fe\u0202\u020f")
        buf.write(u"\u0212\u0217\u021e\u022b\u0233\u023a\u023d\u0248\u0251")
        buf.write(u"\u025b\u0263")
        return buf.getvalue()


class LaTeXParser ( Parser ):

    grammarFileName = "LaTeX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'''", u"'\u2019'", u"'\\\\'", u"'&'", 
                     u"','", u"'\\limits'", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'\\quad'", u"'\\qquad'", 
                     u"<INVALID>", u"'\\negmedspace'", u"'\\negthickspace'", 
                     u"'\\left'", u"'\\right'", u"<INVALID>", u"'+'", u"'-'", 
                     u"'*'", u"'/'", u"'\\pm'", u"'\\mp'", u"'('", u"')'", 
                     u"'{'", u"'}'", u"'\\{'", u"'\\}'", u"'['", u"']'", 
                     u"'|'", u"'\\right|'", u"'\\left|'", u"'\\left['", 
                     u"'\\right]'", u"'\\langle'", u"'\\rangle'", u"'\\left\\angle'", 
                     u"'\\right\\angle'", u"'.'", u"'\\|'", u"'\\lim'", 
                     u"<INVALID>", u"'\\int'", u"<INVALID>", u"<INVALID>", 
                     u"'\\exp'", u"'\\log'", u"'\\ln'", u"'\\sin'", u"'\\cos'", 
                     u"'\\tan'", u"'\\csc'", u"'\\sec'", u"'\\cot'", u"'\\arcsin'", 
                     u"'\\arccos'", u"'\\arctan'", u"'\\arccsc'", u"'\\arcsec'", 
                     u"'\\arccot'", u"'\\sinh'", u"'\\cosh'", u"'\\tanh'", 
                     u"'\\csch'", u"'\\sech'", u"'\\coth'", u"'\\arsinh'", 
                     u"'\\arcosh'", u"'\\artanh'", u"'\\arcsch'", u"'\\arsech'", 
                     u"'\\arcoth'", u"'\\lfloor'", u"'\\rfloor'", u"'\\lceil'", 
                     u"'\\rceil'", u"'\\imath'", u"'\\jmath'", u"'\\Delta'", 
                     u"'\\delta'", u"'\\Gamma'", u"'\\gamma'", u"'\\nabla'", 
                     u"'\\Sigma'", u"'\\sigma'", u"'\\Pi'", u"'\\zeta'", 
                     u"<INVALID>", u"<INVALID>", u"'\\oint'", u"'\\otimes'", 
                     u"'\\oplus'", u"'\\ominus'", u"'\\odot'", u"'\\bigoplus'", 
                     u"'\\bigotimes'", u"'\\oslash'", u"'\\tilde'", u"'\\vec'", 
                     u"'\\hat'", u"'\\hbar'", u"'\\dagger'", u"'\\star'", 
                     u"'\\dot'", u"'\\ddot'", u"'\\prime'", u"'\\circ'", 
                     u"'\\ldots'", u"'\\vdots'", u"'\\dots'", u"'\\cdots'", 
                     u"'\\widehat'", u"'\\underline'", u"'\\overbrace'", 
                     u"'\\overleftarrow'", u"'\\not'", u"'\\varnothing'", 
                     u"'\\bigvee'", u"'\\coprod'", u"'\\neg'", u"'\\mapsto'", 
                     u"'\\bigwedge'", u"'\\curlyvee'", u"'\\curlywedge'", 
                     u"'\\ni'", u"'\\subsetneq'", u"'\\sqsubset'", u"'\\sqsupseteq'", 
                     u"'\\sqsupset'", u"'\\sqsubseteq'", u"'\\complement'", 
                     u"'\\supsetneq'", u"'\\sqcup'", u"'\\sqcap'", u"'\\nexists'", 
                     u"'\\nsubseteq'", u"'\\nsupseteq'", u"'\\underbrace'", 
                     u"'\\underset'", u"'\\bigcup'", u"'\\bigcap'", u"'\\longmapsto'", 
                     u"'\\therefore'", u"'\\because'", u"'\\emptyset'", 
                     u"'\\subset'", u"'\\supset'", u"'\\subseteq'", u"'\\supseteq'", 
                     u"'\\notin'", u"'\\exists'", u"'\\forall'", u"'\\cup'", 
                     u"'\\cap'", u"'\\overline'", u"'\\in'", u"'\\wedge'", 
                     u"'\\vee'", u"'\\smile'", u"'\\frown'", u"'\\mathbb'", 
                     u"'\\stackrel'", u"'\\Im'", u"'\\Re'", u"'\\multicolumn'", 
                     u"'\\multirow'", u"'\\sqrt'", u"'\\longdiv'", u"'\\times'", 
                     u"'\\cdot'", u"'\\div'", u"<INVALID>", u"<INVALID>", 
                     u"'\\mathit'", u"'_'", u"'^'", u"':'", u"<INVALID>", 
                     u"'\\partial'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'\\neq'", u"'<'", u"<INVALID>", u"'\\leqq'", u"'\\leqslant'", 
                     u"'>'", u"<INVALID>", u"'\\geqq'", u"'\\geqslant'", 
                     u"'\\ll'", u"'\\gg'", u"'\\lll'", u"'\\ggg'", u"'!'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"WS", u"THINSPACE", 
                      u"MEDSPACE", u"THICKSPACE", u"QUAD", u"QQUAD", u"NEGTHINSPACE", 
                      u"NEGMEDSPACE", u"NEGTHICKSPACE", u"CMD_LEFT", u"CMD_RIGHT", 
                      u"IGNORE", u"ADD", u"SUB", u"MUL", u"DIV", u"PM", 
                      u"MP", u"L_PAREN", u"R_PAREN", u"L_BRACE", u"R_BRACE", 
                      u"L_BRACE_LITERAL", u"R_BRACE_LITERAL", u"L_BRACKET", 
                      u"R_BRACKET", u"BAR", u"R_BAR", u"L_BAR", u"LEFT_BRACKET", 
                      u"RIGHT_BRACKET", u"L_ANGLE", u"R_ANGLE", u"L_L_ANGLE", 
                      u"R_R_ANGLE", u"PERIOD", u"BAR_VAL", u"FUNC_LIM", 
                      u"LIM_APPROACH_SYM", u"FUNC_INT", u"FUNC_SUM", u"FUNC_PROD", 
                      u"FUNC_EXP", u"FUNC_LOG", u"FUNC_LN", u"FUNC_SIN", 
                      u"FUNC_COS", u"FUNC_TAN", u"FUNC_CSC", u"FUNC_SEC", 
                      u"FUNC_COT", u"FUNC_ARCSIN", u"FUNC_ARCCOS", u"FUNC_ARCTAN", 
                      u"FUNC_ARCCSC", u"FUNC_ARCSEC", u"FUNC_ARCCOT", u"FUNC_SINH", 
                      u"FUNC_COSH", u"FUNC_TANH", u"FUNC_CSCH", u"FUNC_SECH", 
                      u"FUNC_COTH", u"FUNC_ARSINH", u"FUNC_ARCOSH", u"FUNC_ARTANH", 
                      u"FUNC_ARCSCH", u"FUNC_ARSECH", u"FUNC_ARCOTH", u"L_FLOOR", 
                      u"R_FLOOR", u"L_CEIL", u"R_CEIL", u"I_MATH", u"J_MATH", 
                      u"DELTA", u"LOWER_DELTA", u"FUNC_GAMMA", u"LOWER_GAMMA", 
                      u"NABLA", u"SIGMA", u"LOWER_SIGMA", u"PI", u"ZETA", 
                      u"BEGIN_ARR", u"END_ARR", u"O_INT", u"O_TIMES", u"O_PLUS", 
                      u"O_MINUS", u"O_DOT", u"BIG_O_PLUS", u"BIG_O_TIMES", 
                      u"O_SLASH", u"TILDE", u"VEC", u"HAT", u"HBAR", u"DAGGER", 
                      u"STAR", u"DOT", u"DDOT", u"PRIME", u"CIRC", u"LDOTS", 
                      u"VDOTS", u"DOTS", u"CDOTS", u"WIDE_HAT", u"UNDERLINE", 
                      u"OVERBRACE", u"OVER_LEFTARROW", u"NOT", u"VAR_NOTHING", 
                      u"BIG_VEE", u"CO_PRODUCT", u"NEG", u"MAPS_TO", u"BIG_WEDGE", 
                      u"CURLY_VEE", u"CURLY_WEDGE", u"N_I", u"SUBSET_NEQ", 
                      u"SQ_SUBSET", u"SQ_SUBSET_EQ", u"SQ_SUPERSET", u"SQ_SUPERSET_EQ", 
                      u"COMPLEMENT", u"SUPERSET_NEQ", u"SQ_CUP", u"SQ_CAP", 
                      u"NEXISTS", u"N_SUBSET_EQ", u"N_SUPERSET_EQ", u"UNDER_BRACE", 
                      u"UNDER_SET", u"BIG_CUP", u"BIG_CAP", u"LONG_MAPS_TO", 
                      u"THEREFORE", u"BECAUSE", u"EMPTY_SET", u"SUBSET", 
                      u"SUPERSET", u"SUBSET_EQ", u"SUPERSET_EQ", u"NOT_IN", 
                      u"EXISTS", u"FOR_ALL", u"CUP", u"CAP", u"OVERLINE", 
                      u"IN", u"WEDGE", u"VEE", u"SMILE", u"FROWN", u"MATH_BB", 
                      u"STACK_REL", u"IM", u"RE", u"MULTI_COL", u"MULTI_ROW", 
                      u"FUNC_SQRT", u"LONG_DIV", u"CMD_TIMES", u"CMD_CDOT", 
                      u"CMD_DIV", u"CMD_FRAC", u"CMD_BINOM", u"CMD_MATHIT", 
                      u"UNDERSCORE", u"CARET", u"COLON", u"DIFFERENTIAL", 
                      u"PARTIAL", u"LETTER", u"NUMBER", u"EQUAL", u"NEQ", 
                      u"LT", u"LTE", u"LTE_Q", u"LTE_S", u"GT", u"GTE", 
                      u"GTE_Q", u"GTE_S", u"LL", u"GG", u"LLL", u"GGG", 
                      u"BANG", u"SYMBOL", u"TEXT" ]

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
    RULE_bra = 22
    RULE_ket = 23
    RULE_angularunit = 24
    RULE_preprime = 25
    RULE_prime = 26
    RULE_dot = 27
    RULE_ddot = 28
    RULE_matrix = 29
    RULE_determinant = 30
    RULE_mathit = 31
    RULE_mathit_text = 32
    RULE_array = 33
    RULE_array_elements = 34
    RULE_frac = 35
    RULE_binom = 36
    RULE_floor = 37
    RULE_ceil = 38
    RULE_delta = 39
    RULE_func_normal = 40
    RULE_func = 41
    RULE_args = 42
    RULE_limit_sub = 43
    RULE_func_arg = 44
    RULE_func_arg_noparens = 45
    RULE_subexpr = 46
    RULE_supexpr = 47
    RULE_subeq = 48
    RULE_supeq = 49

    ruleNames =  [ u"math", u"relation", u"equality", u"expr", u"additive", 
                   u"mp", u"mp_nofunc", u"unary", u"unary_nofunc", u"postfix", 
                   u"postfix_nofunc", u"postfix_op", u"eval_at", u"eval_at_sub", 
                   u"eval_at_sup", u"exp", u"exp_nofunc", u"comp", u"comp_nofunc", 
                   u"group", u"abs_group", u"atom", u"bra", u"ket", u"angularunit", 
                   u"preprime", u"prime", u"dot", u"ddot", u"matrix", u"determinant", 
                   u"mathit", u"mathit_text", u"array", u"array_elements", 
                   u"frac", u"binom", u"floor", u"ceil", u"delta", u"func_normal", 
                   u"func", u"args", u"limit_sub", u"func_arg", u"func_arg_noparens", 
                   u"subexpr", u"supexpr", u"subeq", u"supeq" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    WS=7
    THINSPACE=8
    MEDSPACE=9
    THICKSPACE=10
    QUAD=11
    QQUAD=12
    NEGTHINSPACE=13
    NEGMEDSPACE=14
    NEGTHICKSPACE=15
    CMD_LEFT=16
    CMD_RIGHT=17
    IGNORE=18
    ADD=19
    SUB=20
    MUL=21
    DIV=22
    PM=23
    MP=24
    L_PAREN=25
    R_PAREN=26
    L_BRACE=27
    R_BRACE=28
    L_BRACE_LITERAL=29
    R_BRACE_LITERAL=30
    L_BRACKET=31
    R_BRACKET=32
    BAR=33
    R_BAR=34
    L_BAR=35
    LEFT_BRACKET=36
    RIGHT_BRACKET=37
    L_ANGLE=38
    R_ANGLE=39
    L_L_ANGLE=40
    R_R_ANGLE=41
    PERIOD=42
    BAR_VAL=43
    FUNC_LIM=44
    LIM_APPROACH_SYM=45
    FUNC_INT=46
    FUNC_SUM=47
    FUNC_PROD=48
    FUNC_EXP=49
    FUNC_LOG=50
    FUNC_LN=51
    FUNC_SIN=52
    FUNC_COS=53
    FUNC_TAN=54
    FUNC_CSC=55
    FUNC_SEC=56
    FUNC_COT=57
    FUNC_ARCSIN=58
    FUNC_ARCCOS=59
    FUNC_ARCTAN=60
    FUNC_ARCCSC=61
    FUNC_ARCSEC=62
    FUNC_ARCCOT=63
    FUNC_SINH=64
    FUNC_COSH=65
    FUNC_TANH=66
    FUNC_CSCH=67
    FUNC_SECH=68
    FUNC_COTH=69
    FUNC_ARSINH=70
    FUNC_ARCOSH=71
    FUNC_ARTANH=72
    FUNC_ARCSCH=73
    FUNC_ARSECH=74
    FUNC_ARCOTH=75
    L_FLOOR=76
    R_FLOOR=77
    L_CEIL=78
    R_CEIL=79
    I_MATH=80
    J_MATH=81
    DELTA=82
    LOWER_DELTA=83
    FUNC_GAMMA=84
    LOWER_GAMMA=85
    NABLA=86
    SIGMA=87
    LOWER_SIGMA=88
    PI=89
    ZETA=90
    BEGIN_ARR=91
    END_ARR=92
    O_INT=93
    O_TIMES=94
    O_PLUS=95
    O_MINUS=96
    O_DOT=97
    BIG_O_PLUS=98
    BIG_O_TIMES=99
    O_SLASH=100
    TILDE=101
    VEC=102
    HAT=103
    HBAR=104
    DAGGER=105
    STAR=106
    DOT=107
    DDOT=108
    PRIME=109
    CIRC=110
    LDOTS=111
    VDOTS=112
    DOTS=113
    CDOTS=114
    WIDE_HAT=115
    UNDERLINE=116
    OVERBRACE=117
    OVER_LEFTARROW=118
    NOT=119
    VAR_NOTHING=120
    BIG_VEE=121
    CO_PRODUCT=122
    NEG=123
    MAPS_TO=124
    BIG_WEDGE=125
    CURLY_VEE=126
    CURLY_WEDGE=127
    N_I=128
    SUBSET_NEQ=129
    SQ_SUBSET=130
    SQ_SUBSET_EQ=131
    SQ_SUPERSET=132
    SQ_SUPERSET_EQ=133
    COMPLEMENT=134
    SUPERSET_NEQ=135
    SQ_CUP=136
    SQ_CAP=137
    NEXISTS=138
    N_SUBSET_EQ=139
    N_SUPERSET_EQ=140
    UNDER_BRACE=141
    UNDER_SET=142
    BIG_CUP=143
    BIG_CAP=144
    LONG_MAPS_TO=145
    THEREFORE=146
    BECAUSE=147
    EMPTY_SET=148
    SUBSET=149
    SUPERSET=150
    SUBSET_EQ=151
    SUPERSET_EQ=152
    NOT_IN=153
    EXISTS=154
    FOR_ALL=155
    CUP=156
    CAP=157
    OVERLINE=158
    IN=159
    WEDGE=160
    VEE=161
    SMILE=162
    FROWN=163
    MATH_BB=164
    STACK_REL=165
    IM=166
    RE=167
    MULTI_COL=168
    MULTI_ROW=169
    FUNC_SQRT=170
    LONG_DIV=171
    CMD_TIMES=172
    CMD_CDOT=173
    CMD_DIV=174
    CMD_FRAC=175
    CMD_BINOM=176
    CMD_MATHIT=177
    UNDERSCORE=178
    CARET=179
    COLON=180
    DIFFERENTIAL=181
    PARTIAL=182
    LETTER=183
    NUMBER=184
    EQUAL=185
    NEQ=186
    LT=187
    LTE=188
    LTE_Q=189
    LTE_S=190
    GT=191
    GTE=192
    GTE_Q=193
    GTE_S=194
    LL=195
    GG=196
    LLL=197
    GGG=198
    BANG=199
    SYMBOL=200
    TEXT=201

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
            self.state = 100
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


        def EQUAL(self):
            return self.getToken(LaTeXParser.EQUAL, 0)

        def LT(self):
            return self.getToken(LaTeXParser.LT, 0)

        def LTE(self):
            return self.getToken(LaTeXParser.LTE, 0)

        def GT(self):
            return self.getToken(LaTeXParser.GT, 0)

        def GTE(self):
            return self.getToken(LaTeXParser.GTE, 0)

        def NEQ(self):
            return self.getToken(LaTeXParser.NEQ, 0)

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
            self.state = 103
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.RelationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relation)
                    self.state = 105
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 106
                    _la = self._input.LA(1)
                    if not(((((_la - 185)) & ~0x3f) == 0 and ((1 << (_la - 185)) & ((1 << (LaTeXParser.EQUAL - 185)) | (1 << (LaTeXParser.NEQ - 185)) | (1 << (LaTeXParser.LT - 185)) | (1 << (LaTeXParser.LTE - 185)) | (1 << (LaTeXParser.GT - 185)) | (1 << (LaTeXParser.GTE - 185)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 107
                    self.relation(3) 
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

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

        def getRuleIndex(self):
            return LaTeXParser.RULE_equality




    def equality(self):

        localctx = LaTeXParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_equality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.expr()
            self.state = 114
            self.match(LaTeXParser.EQUAL)
            self.state = 115
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
            self.state = 117
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
            self.state = 120
            self.mp(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.AdditiveContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                    self.state = 122
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 123
                    _la = self._input.LA(1)
                    if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 124
                    self.additive(3) 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
            self.state = 131
            self.unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 138
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.MpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mp)
                    self.state = 133
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 134
                    _la = self._input.LA(1)
                    if not(_la==LaTeXParser.MUL or _la==LaTeXParser.DIV or ((((_la - 172)) & ~0x3f) == 0 and ((1 << (_la - 172)) & ((1 << (LaTeXParser.CMD_TIMES - 172)) | (1 << (LaTeXParser.CMD_CDOT - 172)) | (1 << (LaTeXParser.CMD_DIV - 172)) | (1 << (LaTeXParser.COLON - 172)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 135
                    self.mp(3) 
                self.state = 140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            self.state = 142
            self.unary_nofunc()
            self._ctx.stop = self._input.LT(-1)
            self.state = 149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.Mp_nofuncContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mp_nofunc)
                    self.state = 144
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 145
                    _la = self._input.LA(1)
                    if not(_la==LaTeXParser.MUL or _la==LaTeXParser.DIV or ((((_la - 172)) & ~0x3f) == 0 and ((1 << (_la - 172)) & ((1 << (LaTeXParser.CMD_TIMES - 172)) | (1 << (LaTeXParser.CMD_CDOT - 172)) | (1 << (LaTeXParser.CMD_DIV - 172)) | (1 << (LaTeXParser.COLON - 172)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 146
                    self.mp_nofunc(3) 
                self.state = 151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.ADD, LaTeXParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 153
                self.unary()
                pass
            elif token in [LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACE_LITERAL, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.LEFT_BRACKET, LaTeXParser.L_ANGLE, LaTeXParser.PERIOD, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_EXP, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_CSCH, LaTeXParser.FUNC_SECH, LaTeXParser.FUNC_COTH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_ARCSCH, LaTeXParser.FUNC_ARSECH, LaTeXParser.FUNC_ARCOTH, LaTeXParser.L_FLOOR, LaTeXParser.L_CEIL, LaTeXParser.DELTA, LaTeXParser.LOWER_DELTA, LaTeXParser.FUNC_GAMMA, LaTeXParser.LOWER_GAMMA, LaTeXParser.NABLA, LaTeXParser.LOWER_SIGMA, LaTeXParser.ZETA, LaTeXParser.BEGIN_ARR, LaTeXParser.VEC, LaTeXParser.HAT, LaTeXParser.DOT, LaTeXParser.DDOT, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_BINOM, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 154
                        self.postfix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 157 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.ADD, LaTeXParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 162
                self.unary_nofunc()
                pass
            elif token in [LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACE_LITERAL, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.LEFT_BRACKET, LaTeXParser.L_ANGLE, LaTeXParser.PERIOD, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_EXP, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_CSCH, LaTeXParser.FUNC_SECH, LaTeXParser.FUNC_COTH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_ARCSCH, LaTeXParser.FUNC_ARSECH, LaTeXParser.FUNC_ARCOTH, LaTeXParser.L_FLOOR, LaTeXParser.L_CEIL, LaTeXParser.DELTA, LaTeXParser.LOWER_DELTA, LaTeXParser.FUNC_GAMMA, LaTeXParser.LOWER_GAMMA, LaTeXParser.NABLA, LaTeXParser.LOWER_SIGMA, LaTeXParser.ZETA, LaTeXParser.BEGIN_ARR, LaTeXParser.VEC, LaTeXParser.HAT, LaTeXParser.DOT, LaTeXParser.DDOT, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_BINOM, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.postfix()
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 164
                        self.postfix_nofunc() 
                    self.state = 169
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 172
            self.exp(0)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 173
                    self.postfix_op() 
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 179
            self.exp_nofunc(0)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 180
                    self.postfix_op() 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.BANG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(LaTeXParser.BANG)
                pass
            elif token in [LaTeXParser.BAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
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
            self.state = 190
            self.match(LaTeXParser.BAR)
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 191
                self.eval_at_sup()
                pass

            elif la_ == 2:
                self.state = 192
                self.eval_at_sub()
                pass

            elif la_ == 3:
                self.state = 193
                self.eval_at_sup()
                self.state = 194
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
            self.state = 198
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 199
            self.match(LaTeXParser.L_BRACE)
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
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
            self.state = 206
            self.match(LaTeXParser.CARET)
            self.state = 207
            self.match(LaTeXParser.L_BRACE)
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 208
                self.expr()
                pass

            elif la_ == 2:
                self.state = 209
                self.equality()
                pass


            self.state = 212
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
            self.state = 215
            self.comp()
            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 217
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 218
                    self.match(LaTeXParser.CARET)
                    self.state = 224
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.LEFT_BRACKET, LaTeXParser.L_ANGLE, LaTeXParser.BEGIN_ARR, LaTeXParser.DOT, LaTeXParser.DDOT, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                        self.state = 219
                        self.atom()
                        pass
                    elif token in [LaTeXParser.L_BRACE]:
                        self.state = 220
                        self.match(LaTeXParser.L_BRACE)
                        self.state = 221
                        self.expr()
                        self.state = 222
                        self.match(LaTeXParser.R_BRACE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 227
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        self.state = 226
                        self.subexpr()

             
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.state = 235
            self.comp_nofunc()
            self._ctx.stop = self._input.LT(-1)
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.Exp_nofuncContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_nofunc)
                    self.state = 237
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 238
                    self.match(LaTeXParser.CARET)
                    self.state = 244
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.LEFT_BRACKET, LaTeXParser.L_ANGLE, LaTeXParser.BEGIN_ARR, LaTeXParser.DOT, LaTeXParser.DDOT, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                        self.state = 239
                        self.atom()
                        pass
                    elif token in [LaTeXParser.L_BRACE]:
                        self.state = 240
                        self.match(LaTeXParser.L_BRACE)
                        self.state = 241
                        self.expr()
                        self.state = 242
                        self.match(LaTeXParser.R_BRACE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 247
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        self.state = 246
                        self.subexpr()

             
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.group()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.abs_group()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.func()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 257
                self.atom()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 258
                self.frac()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 259
                self.binom()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 260
                self.floor()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 261
                self.ceil()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 262
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
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.group()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.abs_group()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.atom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 268
                self.frac()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 269
                self.binom()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 270
                self.floor()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 271
                self.ceil()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 272
                self.delta()
                pass


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

        def L_BRACKET(self):
            return self.getToken(LaTeXParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(LaTeXParser.R_BRACKET, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def L_BRACE_LITERAL(self):
            return self.getToken(LaTeXParser.L_BRACE_LITERAL, 0)

        def R_BRACE_LITERAL(self):
            return self.getToken(LaTeXParser.R_BRACE_LITERAL, 0)

        def PERIOD(self):
            return self.getToken(LaTeXParser.PERIOD, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_group




    def group(self):

        localctx = LaTeXParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_group)
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(LaTeXParser.L_PAREN)
                self.state = 276
                self.expr()
                self.state = 277
                self.match(LaTeXParser.R_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(LaTeXParser.L_BRACKET)
                self.state = 280
                self.expr()
                self.state = 281
                self.match(LaTeXParser.R_BRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.match(LaTeXParser.L_BRACE)
                self.state = 284
                self.expr()
                self.state = 285
                self.match(LaTeXParser.R_BRACE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 287
                self.match(LaTeXParser.L_BRACE_LITERAL)
                self.state = 288
                self.expr()
                self.state = 289
                self.match(LaTeXParser.R_BRACE_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 291
                self.match(LaTeXParser.L_BRACE_LITERAL)
                self.state = 292
                self.expr()
                self.state = 293
                self.match(LaTeXParser.PERIOD)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 295
                self.match(LaTeXParser.PERIOD)
                self.state = 296
                self.expr()
                self.state = 297
                self.match(LaTeXParser.R_BRACE_LITERAL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 299
                self.match(LaTeXParser.L_PAREN)
                self.state = 300
                self.expr()
                self.state = 301
                self.match(LaTeXParser.PERIOD)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 303
                self.match(LaTeXParser.PERIOD)
                self.state = 304
                self.expr()
                self.state = 305
                self.match(LaTeXParser.R_PAREN)
                pass


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
            self.state = 309
            self.match(LaTeXParser.BAR)
            self.state = 310
            self.expr()
            self.state = 311
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


        def prime(self):
            return self.getTypedRuleContext(LaTeXParser.PrimeContext,0)


        def dot(self):
            return self.getTypedRuleContext(LaTeXParser.DotContext,0)


        def ddot(self):
            return self.getTypedRuleContext(LaTeXParser.DdotContext,0)


        def angularunit(self):
            return self.getTypedRuleContext(LaTeXParser.AngularunitContext,0)


        def bra(self):
            return self.getTypedRuleContext(LaTeXParser.BraContext,0)


        def ket(self):
            return self.getTypedRuleContext(LaTeXParser.KetContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_atom




    def atom(self):

        localctx = LaTeXParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 315
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 314
                    self.subexpr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(LaTeXParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.match(LaTeXParser.DIFFERENTIAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 319
                self.matrix()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 320
                self.determinant()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 321
                self.array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 322
                self.mathit()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 323
                self.prime()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 324
                self.dot()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 325
                self.ddot()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 326
                self.angularunit()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 327
                self.bra()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 328
                self.ket()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BraContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.BraContext, self).__init__(parent, invokingState)
            self.parser = parser

        def L_ANGLE(self):
            return self.getToken(LaTeXParser.L_ANGLE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BAR(self):
            return self.getToken(LaTeXParser.R_BAR, 0)

        def BAR(self):
            return self.getToken(LaTeXParser.BAR, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_bra




    def bra(self):

        localctx = LaTeXParser.BraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_bra)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(LaTeXParser.L_ANGLE)
            self.state = 332
            self.expr()
            self.state = 333
            _la = self._input.LA(1)
            if not(_la==LaTeXParser.BAR or _la==LaTeXParser.R_BAR):
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


    class KetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.KetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_ANGLE(self):
            return self.getToken(LaTeXParser.R_ANGLE, 0)

        def L_BAR(self):
            return self.getToken(LaTeXParser.L_BAR, 0)

        def BAR(self):
            return self.getToken(LaTeXParser.BAR, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_ket




    def ket(self):

        localctx = LaTeXParser.KetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ket)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            _la = self._input.LA(1)
            if not(_la==LaTeXParser.BAR or _la==LaTeXParser.L_BAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 336
            self.expr()
            self.state = 337
            self.match(LaTeXParser.R_ANGLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AngularunitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.AngularunitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def CIRC(self):
            return self.getToken(LaTeXParser.CIRC, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def NUMBER(self):
            return self.getToken(LaTeXParser.NUMBER, 0)

        def LETTER(self):
            return self.getToken(LaTeXParser.LETTER, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_angularunit




    def angularunit(self):

        localctx = LaTeXParser.AngularunitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_angularunit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            _la = self._input.LA(1)
            if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 340
            self.match(LaTeXParser.CARET)
            self.state = 341
            self.match(LaTeXParser.L_BRACE)
            self.state = 342
            self.match(LaTeXParser.CIRC)
            self.state = 343
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreprimeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.PreprimeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self):
            return self.getToken(LaTeXParser.LETTER, 0)

        def SYMBOL(self):
            return self.getToken(LaTeXParser.SYMBOL, 0)

        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def PRIME(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.PRIME)
            else:
                return self.getToken(LaTeXParser.PRIME, i)

        def getRuleIndex(self):
            return LaTeXParser.RULE_preprime




    def preprime(self):

        localctx = LaTeXParser.PreprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_preprime)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            _la = self._input.LA(1)
            if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 346
                self.match(LaTeXParser.CARET)
                self.state = 347
                self.match(LaTeXParser.L_BRACE)
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LaTeXParser.PRIME:
                    self.state = 348
                    self.match(LaTeXParser.PRIME)
                    self.state = 353
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 354
                self.match(LaTeXParser.R_BRACE)
                pass

            elif la_ == 2:
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LaTeXParser.T__0:
                    self.state = 355
                    self.match(LaTeXParser.T__0)
                    self.state = 360
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LaTeXParser.T__1:
                    self.state = 361
                    self.match(LaTeXParser.T__1)
                    self.state = 366
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.PrimeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def preprime(self):
            return self.getTypedRuleContext(LaTeXParser.PreprimeContext,0)


        def L_PAREN(self):
            return self.getToken(LaTeXParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(LaTeXParser.R_PAREN, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_prime




    def prime(self):

        localctx = LaTeXParser.PrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_prime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.preprime()
            self.state = 370
            self.match(LaTeXParser.L_PAREN)
            self.state = 371
            self.expr()
            self.state = 372
            self.match(LaTeXParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DotContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.DotContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(LaTeXParser.DOT, 0)

        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_dot




    def dot(self):

        localctx = LaTeXParser.DotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_dot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(LaTeXParser.DOT)
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.L_BRACE]:
                self.state = 375
                self.match(LaTeXParser.L_BRACE)
                self.state = 376
                self.expr()
                self.state = 377
                self.match(LaTeXParser.R_BRACE)
                pass
            elif token in [LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.LEFT_BRACKET, LaTeXParser.L_ANGLE, LaTeXParser.BEGIN_ARR, LaTeXParser.DOT, LaTeXParser.DDOT, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 379
                self.atom()
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


    class DdotContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.DdotContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DDOT(self):
            return self.getToken(LaTeXParser.DDOT, 0)

        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_ddot




    def ddot(self):

        localctx = LaTeXParser.DdotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ddot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(LaTeXParser.DDOT)
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.L_BRACE]:
                self.state = 383
                self.match(LaTeXParser.L_BRACE)
                self.state = 384
                self.expr()
                self.state = 385
                self.match(LaTeXParser.R_BRACE)
                pass
            elif token in [LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.LEFT_BRACKET, LaTeXParser.L_ANGLE, LaTeXParser.BEGIN_ARR, LaTeXParser.DOT, LaTeXParser.DDOT, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 387
                self.atom()
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

        def LEFT_BRACKET(self):
            return self.getToken(LaTeXParser.LEFT_BRACKET, 0)

        def array_elements(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.Array_elementsContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.Array_elementsContext,i)


        def RIGHT_BRACKET(self):
            return self.getToken(LaTeXParser.RIGHT_BRACKET, 0)

        def BEGIN_ARR(self):
            return self.getToken(LaTeXParser.BEGIN_ARR, 0)

        def END_ARR(self):
            return self.getToken(LaTeXParser.END_ARR, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_matrix




    def matrix(self):

        localctx = LaTeXParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(LaTeXParser.LEFT_BRACKET)
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 391
                self.match(LaTeXParser.BEGIN_ARR)


            self.state = 394
            self.array_elements()
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 395
                    self.match(LaTeXParser.T__2)
                    self.state = 396
                    self.array_elements() 
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LaTeXParser.END_ARR:
                self.state = 402
                self.match(LaTeXParser.END_ARR)


            self.state = 405
            self.match(LaTeXParser.RIGHT_BRACKET)
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

        def array_elements(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.Array_elementsContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.Array_elementsContext,i)


        def R_BAR(self):
            return self.getToken(LaTeXParser.R_BAR, 0)

        def BEGIN_ARR(self):
            return self.getToken(LaTeXParser.BEGIN_ARR, 0)

        def END_ARR(self):
            return self.getToken(LaTeXParser.END_ARR, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_determinant




    def determinant(self):

        localctx = LaTeXParser.DeterminantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_determinant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(LaTeXParser.L_BAR)
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 408
                self.match(LaTeXParser.BEGIN_ARR)


            self.state = 411
            self.array_elements()
            self.state = 416
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 412
                    self.match(LaTeXParser.T__2)
                    self.state = 413
                    self.array_elements() 
                self.state = 418
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LaTeXParser.END_ARR:
                self.state = 419
                self.match(LaTeXParser.END_ARR)


            self.state = 422
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
        self.enterRule(localctx, 62, self.RULE_mathit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(LaTeXParser.CMD_MATHIT)
            self.state = 425
            self.match(LaTeXParser.L_BRACE)
            self.state = 426
            self.mathit_text()
            self.state = 427
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
        self.enterRule(localctx, 64, self.RULE_mathit_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 429
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.NUMBER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 432 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==LaTeXParser.LETTER or _la==LaTeXParser.NUMBER):
                    break

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
        self.enterRule(localctx, 66, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(LaTeXParser.BEGIN_ARR)
            self.state = 435
            self.array_elements()
            self.state = 440
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 436
                    self.match(LaTeXParser.T__2)
                    self.state = 437
                    self.array_elements() 
                self.state = 442
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

            self.state = 443
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
        self.enterRule(localctx, 68, self.RULE_array_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.relation(0)
            self.state = 452
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 447
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.T__3 or _la==LaTeXParser.T__4:
                        self.state = 446
                        _la = self._input.LA(1)
                        if not(_la==LaTeXParser.T__3 or _la==LaTeXParser.T__4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()


                    self.state = 449
                    self.relation(0) 
                self.state = 454
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_frac)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(LaTeXParser.CMD_FRAC)
            self.state = 456
            self.match(LaTeXParser.L_BRACE)
            self.state = 457
            localctx.upper = self.expr()
            self.state = 458
            self.match(LaTeXParser.R_BRACE)
            self.state = 459
            self.match(LaTeXParser.L_BRACE)
            self.state = 460
            localctx.lower = self.expr()
            self.state = 461
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

        def CMD_BINOM(self):
            return self.getToken(LaTeXParser.CMD_BINOM, 0)

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
            return LaTeXParser.RULE_binom




    def binom(self):

        localctx = LaTeXParser.BinomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_binom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(LaTeXParser.CMD_BINOM)
            self.state = 464
            self.match(LaTeXParser.L_BRACE)
            self.state = 465
            localctx.n = self.expr()
            self.state = 466
            self.match(LaTeXParser.R_BRACE)
            self.state = 467
            self.match(LaTeXParser.L_BRACE)
            self.state = 468
            localctx.k = self.expr()
            self.state = 469
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
        self.enterRule(localctx, 74, self.RULE_floor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(LaTeXParser.L_FLOOR)
            self.state = 472
            localctx.val = self.expr()
            self.state = 473
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
        self.enterRule(localctx, 76, self.RULE_ceil)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(LaTeXParser.L_CEIL)
            self.state = 476
            localctx.val = self.expr()
            self.state = 477
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

        def LOWER_DELTA(self):
            return self.getToken(LaTeXParser.LOWER_DELTA, 0)

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
        self.enterRule(localctx, 78, self.RULE_delta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(LaTeXParser.LOWER_DELTA)
            self.state = 480
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 481
            self.match(LaTeXParser.L_BRACE)
            self.state = 482
            localctx.x = self.expr()
            self.state = 483
            localctx.y = self.expr()
            self.state = 484
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

        def LOWER_GAMMA(self):
            return self.getToken(LaTeXParser.LOWER_GAMMA, 0)

        def ZETA(self):
            return self.getToken(LaTeXParser.ZETA, 0)

        def NABLA(self):
            return self.getToken(LaTeXParser.NABLA, 0)

        def DELTA(self):
            return self.getToken(LaTeXParser.DELTA, 0)

        def LOWER_SIGMA(self):
            return self.getToken(LaTeXParser.LOWER_SIGMA, 0)

        def VEC(self):
            return self.getToken(LaTeXParser.VEC, 0)

        def HAT(self):
            return self.getToken(LaTeXParser.HAT, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_func_normal




    def func_normal(self):

        localctx = LaTeXParser.Func_normalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_func_normal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            _la = self._input.LA(1)
            if not(((((_la - 49)) & ~0x3f) == 0 and ((1 << (_la - 49)) & ((1 << (LaTeXParser.FUNC_EXP - 49)) | (1 << (LaTeXParser.FUNC_LOG - 49)) | (1 << (LaTeXParser.FUNC_LN - 49)) | (1 << (LaTeXParser.FUNC_SIN - 49)) | (1 << (LaTeXParser.FUNC_COS - 49)) | (1 << (LaTeXParser.FUNC_TAN - 49)) | (1 << (LaTeXParser.FUNC_CSC - 49)) | (1 << (LaTeXParser.FUNC_SEC - 49)) | (1 << (LaTeXParser.FUNC_COT - 49)) | (1 << (LaTeXParser.FUNC_ARCSIN - 49)) | (1 << (LaTeXParser.FUNC_ARCCOS - 49)) | (1 << (LaTeXParser.FUNC_ARCTAN - 49)) | (1 << (LaTeXParser.FUNC_ARCCSC - 49)) | (1 << (LaTeXParser.FUNC_ARCSEC - 49)) | (1 << (LaTeXParser.FUNC_ARCCOT - 49)) | (1 << (LaTeXParser.FUNC_SINH - 49)) | (1 << (LaTeXParser.FUNC_COSH - 49)) | (1 << (LaTeXParser.FUNC_TANH - 49)) | (1 << (LaTeXParser.FUNC_CSCH - 49)) | (1 << (LaTeXParser.FUNC_SECH - 49)) | (1 << (LaTeXParser.FUNC_COTH - 49)) | (1 << (LaTeXParser.FUNC_ARSINH - 49)) | (1 << (LaTeXParser.FUNC_ARCOSH - 49)) | (1 << (LaTeXParser.FUNC_ARTANH - 49)) | (1 << (LaTeXParser.FUNC_ARCSCH - 49)) | (1 << (LaTeXParser.FUNC_ARSECH - 49)) | (1 << (LaTeXParser.FUNC_ARCOTH - 49)) | (1 << (LaTeXParser.DELTA - 49)) | (1 << (LaTeXParser.FUNC_GAMMA - 49)) | (1 << (LaTeXParser.LOWER_GAMMA - 49)) | (1 << (LaTeXParser.NABLA - 49)) | (1 << (LaTeXParser.LOWER_SIGMA - 49)) | (1 << (LaTeXParser.ZETA - 49)) | (1 << (LaTeXParser.VEC - 49)) | (1 << (LaTeXParser.HAT - 49)))) != 0)):
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
        self.enterRule(localctx, 82, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 561
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.FUNC_EXP, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_CSCH, LaTeXParser.FUNC_SECH, LaTeXParser.FUNC_COTH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_ARCSCH, LaTeXParser.FUNC_ARSECH, LaTeXParser.FUNC_ARCOTH, LaTeXParser.DELTA, LaTeXParser.FUNC_GAMMA, LaTeXParser.LOWER_GAMMA, LaTeXParser.NABLA, LaTeXParser.LOWER_SIGMA, LaTeXParser.ZETA, LaTeXParser.VEC, LaTeXParser.HAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.func_normal()
                self.state = 501
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                if la_ == 1:
                    self.state = 490
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.UNDERSCORE:
                        self.state = 489
                        self.subexpr()


                    self.state = 493
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.CARET:
                        self.state = 492
                        self.supexpr()


                    pass

                elif la_ == 2:
                    self.state = 496
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.CARET:
                        self.state = 495
                        self.supexpr()


                    self.state = 499
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.UNDERSCORE:
                        self.state = 498
                        self.subexpr()


                    pass


                self.state = 508
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 503
                    self.match(LaTeXParser.L_PAREN)
                    self.state = 504
                    self.func_arg()
                    self.state = 505
                    self.match(LaTeXParser.R_PAREN)
                    pass

                elif la_ == 2:
                    self.state = 507
                    self.func_arg_noparens()
                    pass


                pass
            elif token in [LaTeXParser.LETTER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 512
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LaTeXParser.UNDERSCORE:
                    self.state = 511
                    self.subexpr()


                self.state = 514
                self.match(LaTeXParser.L_PAREN)
                self.state = 515
                self.args()
                self.state = 516
                self.match(LaTeXParser.R_PAREN)
                pass
            elif token in [LaTeXParser.FUNC_INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 518
                self.match(LaTeXParser.FUNC_INT)
                self.state = 525
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LaTeXParser.UNDERSCORE]:
                    self.state = 519
                    self.subexpr()
                    self.state = 520
                    self.supexpr()
                    pass
                elif token in [LaTeXParser.CARET]:
                    self.state = 522
                    self.supexpr()
                    self.state = 523
                    self.subexpr()
                    pass
                elif token in [LaTeXParser.ADD, LaTeXParser.SUB, LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACE_LITERAL, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.LEFT_BRACKET, LaTeXParser.L_ANGLE, LaTeXParser.PERIOD, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_EXP, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_CSCH, LaTeXParser.FUNC_SECH, LaTeXParser.FUNC_COTH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_ARCSCH, LaTeXParser.FUNC_ARSECH, LaTeXParser.FUNC_ARCOTH, LaTeXParser.L_FLOOR, LaTeXParser.L_CEIL, LaTeXParser.DELTA, LaTeXParser.LOWER_DELTA, LaTeXParser.FUNC_GAMMA, LaTeXParser.LOWER_GAMMA, LaTeXParser.NABLA, LaTeXParser.LOWER_SIGMA, LaTeXParser.ZETA, LaTeXParser.BEGIN_ARR, LaTeXParser.VEC, LaTeXParser.HAT, LaTeXParser.DOT, LaTeXParser.DDOT, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_BINOM, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                    pass
                else:
                    pass
                self.state = 533
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 528
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        self.state = 527
                        self.additive(0)


                    self.state = 530
                    self.match(LaTeXParser.DIFFERENTIAL)
                    pass

                elif la_ == 2:
                    self.state = 531
                    self.frac()
                    pass

                elif la_ == 3:
                    self.state = 532
                    self.additive(0)
                    pass


                pass
            elif token in [LaTeXParser.FUNC_SQRT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 535
                self.match(LaTeXParser.FUNC_SQRT)
                self.state = 540
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LaTeXParser.L_BRACKET:
                    self.state = 536
                    self.match(LaTeXParser.L_BRACKET)
                    self.state = 537
                    localctx.root = self.expr()
                    self.state = 538
                    self.match(LaTeXParser.R_BRACKET)


                self.state = 542
                self.match(LaTeXParser.L_BRACE)
                self.state = 543
                localctx.base = self.expr()
                self.state = 544
                self.match(LaTeXParser.R_BRACE)
                pass
            elif token in [LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD]:
                self.enterOuterAlt(localctx, 5)
                self.state = 546
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.FUNC_SUM or _la==LaTeXParser.FUNC_PROD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 553
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LaTeXParser.UNDERSCORE]:
                    self.state = 547
                    self.subeq()
                    self.state = 548
                    self.supexpr()
                    pass
                elif token in [LaTeXParser.CARET]:
                    self.state = 550
                    self.supexpr()
                    self.state = 551
                    self.subeq()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 555
                self.mp(0)
                pass
            elif token in [LaTeXParser.FUNC_LIM]:
                self.enterOuterAlt(localctx, 6)
                self.state = 557
                self.match(LaTeXParser.FUNC_LIM)
                self.state = 558
                self.limit_sub()
                self.state = 559
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
        self.enterRule(localctx, 84, self.RULE_args)
        try:
            self.state = 568
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 563
                self.expr()
                self.state = 564
                self.match(LaTeXParser.T__4)
                self.state = 565
                self.args()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 567
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
        self.enterRule(localctx, 86, self.RULE_limit_sub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LaTeXParser.T__5:
                self.state = 570
                self.match(LaTeXParser.T__5)


            self.state = 573
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 574
            self.match(LaTeXParser.L_BRACE)
            self.state = 575
            _la = self._input.LA(1)
            if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 576
            self.match(LaTeXParser.LIM_APPROACH_SYM)
            self.state = 577
            self.expr()
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LaTeXParser.CARET:
                self.state = 578
                self.match(LaTeXParser.CARET)
                self.state = 579
                self.match(LaTeXParser.L_BRACE)
                self.state = 580
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 581
                self.match(LaTeXParser.R_BRACE)


            self.state = 584
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
        self.enterRule(localctx, 88, self.RULE_func_arg)
        try:
            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 586
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 587
                self.expr()
                self.state = 588
                self.match(LaTeXParser.T__4)
                self.state = 589
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
        self.enterRule(localctx, 90, self.RULE_func_arg_noparens)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
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
        self.enterRule(localctx, 92, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 601
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.LEFT_BRACKET, LaTeXParser.L_ANGLE, LaTeXParser.BEGIN_ARR, LaTeXParser.DOT, LaTeXParser.DDOT, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 596
                self.atom()
                pass
            elif token in [LaTeXParser.L_BRACE]:
                self.state = 597
                self.match(LaTeXParser.L_BRACE)
                self.state = 598
                self.expr()
                self.state = 599
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
        self.enterRule(localctx, 94, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(LaTeXParser.CARET)
            self.state = 609
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.BAR, LaTeXParser.L_BAR, LaTeXParser.LEFT_BRACKET, LaTeXParser.L_ANGLE, LaTeXParser.BEGIN_ARR, LaTeXParser.DOT, LaTeXParser.DDOT, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 604
                self.atom()
                pass
            elif token in [LaTeXParser.L_BRACE]:
                self.state = 605
                self.match(LaTeXParser.L_BRACE)
                self.state = 606
                self.expr()
                self.state = 607
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
        self.enterRule(localctx, 96, self.RULE_subeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 612
            self.match(LaTeXParser.L_BRACE)
            self.state = 613
            self.equality()
            self.state = 614
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
        self.enterRule(localctx, 98, self.RULE_supeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 617
            self.match(LaTeXParser.L_BRACE)
            self.state = 618
            self.equality()
            self.state = 619
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
         




