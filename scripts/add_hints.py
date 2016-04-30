import csv
import os

# adds hints to the levels listed in lixlfpack.csv
# lixlfpack.csv must have semicolon as column separator
# run this script from within the root folder of the pack

ratings = {1 : "Simple",
           2 : "Quirky",
           3 : "Cunning",
           4 : "Daunting",
           5 : "Vicious",
           6 : "Hopeless"}

if not os.path.exists('temp'):
    for r in ratings.values():
        os.makedirs('temp/' + r)

with open('lixlfpack.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        lvpath = ratings[int(row[5])] + '/' + row[1]
        lv = open(lvpath, 'r')
        out = open('temp/' + lvpath, 'w')
        for line in lv:
            out.write(line)
            if line.startswith("$ENGLISH "):
                out.write("\n")
                i = 8
                while (i < len(row) and row[i] != '' and row[i] != '.'):
                    out.write("$HINT_ENGLISH " + row[i] + '\n')
                    i += 1
        out.close()
        lv.close()

