infile = open('jan.dat')
outfile = open('JanUCI.csv','w')

doclines = infile.readlines()
infile.close()

for i in range(len(doclines)):
    line = doclines[i].strip().split(' ')[1:]
    for elt in line:
        pieces = elt.split(':')
        outfile.write(str(i+1) + ' ' + pieces[0] + ' ' + pieces[1] + '\n')
    
outfile.close()
