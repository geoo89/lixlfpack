f = open("run")
d = dict()
for line in f:
    if line[0] == 'm':
        pieces = line.split(' ')
        name = pieces[-1].strip('\'\n')
        if not name in d:
            d[name] = 1
        else:
            d[name] += 1
        for piece in pieces[0:-1]:
            print(piece, end=' ')
        if d[name] == 1:
            print('\'' + name[0:-4] + '.txt\'')
        else:
            print('\'' + name[0:-4] + str(d[name]) + '.txt\'')
