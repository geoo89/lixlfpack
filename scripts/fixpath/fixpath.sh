#!/bin/sh
# looks into the replay file for the level path
# only based on the filename without path, it changes the path to
# single/lixlfpack/[rating]/[filename]
# needs lixlfpack.csv and ratings.sed to run
sed 's%[^;]*;\([^;]*\);[^;]*;[^;]*;[^;]*;\([1-6]\);.*$%s:\1:single/lixlfpack/\2/\1:%' lixlfpack.csv > lvlist
sed -i -r -f ratings.sed lvlist
echo 's:\$FILENAME.*/([^/]*.txt):$FILENAME \\1:g' > adjustpath.sed
cat lvlist >> adjustpath.sed
sed -i -r -f adjustpath.sed *.txt
