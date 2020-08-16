from sympy.parsing.latex import parse_latex
fi = open('valid_latex', 'r')
lines = fi.readlines()
nlines = [line.strip() for line in lines]
newlines = ""
for i in nlines:
    try:
        parsed = parse_latex(i)
    except Exception as e:
        newlines += i
        newlines += '\n' + str(e) + '\n'
        newlines += "\n --- \n\n"
    print(i)
wr = open('sympyerror', 'w')
wr.writelines(newlines)
wr.close()
