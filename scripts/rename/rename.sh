#!/bin/sh
# renames a replay to [levelname]-[playername][number].txt
# requires nodupes.py
find *.txt | xargs -n 1 grep -iHE '(FILENAME)|(PLAYER)' > names
sed -i "s:\:\$FILENAME.*/: :g" names
tr '\r\n' '%' < names > namesnolr
tr -s '%' < namesnolr > names # now it should work for any linebreak
rm -f namesnolr
sed -i 's:\([^%]*\)%\([^%]*\)%:\1 \2\n:g' names
sed -i "s:.txt [^ ]*PLAYER 0 Garden :-:g" names
sed -i "s:$:.txt\':g" names
sed -i "s:^:mv \':g" names
sed -i "s:txt :txt\' \':g" names
echo '#!/bin/sh' > run
cat names >> run
python3 nodupes.py > run.sh
rm -f names
rm -f run
chmod +x run.sh
./run.sh
rm -f run.sh