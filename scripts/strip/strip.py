import os

# strips the levels from all replays within the folder this script is placed in

for i in os.listdir(os.getcwd()):
    if i.endswith(".txt"):
        f = open(i)
        f2 = open(i + '2', 'w')
        for line in f:
            if line.startswith("$BUILT 2"):
                break
            else:
                f2.write(line)
        f.close()
        f2.close()

    else:
        continue