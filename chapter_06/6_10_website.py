from cmath import inf


def main():
    infile = open('main.html', 'w')
    name = input('Enter your name: ')
    information = input('Enter information about yourself: ')
    infile.write('<html>\n<head>\n</head>\n<body>\n')
    infile.write('\t<center>\n')
    infile.write('\t<h1>'+ name + '</h1>\n')
    infile.write('\t</center>\n')
    infile.write('<hr />\n')
    infile.write(information + '\n')
    infile.write('<hr />\n')
    infile.write('</body>\n</html>\n')
    infile.close()
main()