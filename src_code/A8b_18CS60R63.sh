echo " we are creating occ.txt "
split -n l/10 occ/users.txt occ/hdfs_mapper -d
cat occ/hdfs_mapper00|python occ/mapper.py|sort -k1,1n|python occ/combin.py > occ/hdfs_combine00
cat occ/hdfs_mapper01|python occ/mapper.py|sort -k1,1n|python occ/combin.py > occ/hdfs_combine01
cat occ/hdfs_mapper02|python occ/mapper.py|sort -k1,1n|python occ/combin.py > occ/hdfs_combine02
cat occ/hdfs_mapper03|python occ/mapper.py|sort -k1,1n|python occ/combin.py > occ/hdfs_combine03
cat occ/hdfs_mapper04|python occ/mapper.py|sort -k1,1n|python occ/combin.py > occ/hdfs_combine04
cat occ/hdfs_mapper05|python occ/mapper.py|sort -k1,1n|python occ/combin.py > occ/hdfs_combine05
cat occ/hdfs_mapper06|python occ/mapper.py|sort -k1,1n|python occ/combin.py > occ/hdfs_combine06
cat occ/hdfs_mapper07|python occ/mapper.py|sort -k1,1n|python occ/combin.py > occ/hdfs_combine07
cat occ/hdfs_mapper08|python occ/mapper.py|sort -k1,1n|python occ/combin.py > occ/hdfs_combine08
cat occ/hdfs_mapper09|python occ/mapper.py|sort -k1,1n|python occ/combin.py > occ/hdfs_combine09
cat occ/hdfs_combine*|sort -k1,1n -k2,2n|python occ/reducer.py|sort -k1,1n -k2n,2>occ.txt


echo " we are creating age.txt "
split -n l/10 age/users.txt age/hdfs_mapper -d
cat age/hdfs_mapper00|python age/mapper.py|sort -k1,1n|python age/combin.py > age/hdfs_combine00
cat age/hdfs_mapper01|python age/mapper.py|sort -k1,1n|python age/combin.py > age/hdfs_combine01
cat age/hdfs_mapper02|python age/mapper.py|sort -k1,1n|python age/combin.py > age/hdfs_combine02
cat age/hdfs_mapper03|python age/mapper.py|sort -k1,1n|python age/combin.py > age/hdfs_combine03
cat age/hdfs_mapper04|python age/mapper.py|sort -k1,1n|python age/combin.py > age/hdfs_combine04
cat age/hdfs_mapper05|python age/mapper.py|sort -k1,1n|python age/combin.py > age/hdfs_combine05
cat age/hdfs_mapper06|python age/mapper.py|sort -k1,1n|python age/combin.py > age/hdfs_combine06
cat age/hdfs_mapper07|python age/mapper.py|sort -k1,1n|python age/combin.py > age/hdfs_combine07
cat age/hdfs_mapper08|python age/mapper.py|sort -k1,1n|python age/combin.py > age/hdfs_combine08
cat age/hdfs_mapper09|python age/mapper.py|sort -k1,1n|python age/combin.py > age/hdfs_combine09
cat age/hdfs_combine*|sort -k1,1n -k2,2n|python age/reducer.py|sort -k1,1n -k2n,2>age.txt


echo " we are creating mov.txt "
split -n l/10 ratings.txt -d hdfs_mapper
cat hdfs_mapper00|python mapper.py|sort -k1,1n|python combin.py > hdfs_combine00
cat hdfs_mapper01|python mapper.py|sort -k1,1n|python combin.py > hdfs_combine01
cat hdfs_mapper02|python mapper.py|sort -k1,1n|python combin.py > hdfs_combine02
cat hdfs_mapper03|python mapper.py|sort -k1,1n|python combin.py > hdfs_combine03
cat hdfs_mapper04|python mapper.py|sort -k1,1n|python combin.py > hdfs_combine04
cat hdfs_mapper05|python mapper.py|sort -k1,1n|python combin.py > hdfs_combine05
cat hdfs_mapper06|python mapper.py|sort -k1,1n|python combin.py > hdfs_combine06
cat hdfs_mapper07|python mapper.py|sort -k1,1n|python combin.py > hdfs_combine07
cat hdfs_mapper08|python mapper.py|sort -k1,1n|python combin.py > hdfs_combine08
cat hdfs_mapper09|python mapper.py|sort -k1,1n|python combin.py > hdfs_combine09
echo "we are creating mov.txt"
cat hdfs_combine*|sort -k1,1n -k2,2n|python reducer.py|sort -k1,1n -k2,2n|python reducer2.py|sort -k1,1n -k2n,2>mov.txt
echo "we are creating norm_mov.txt"
python normalise.py
echo "we are creating score.txt"
python score.py
echo "we are creating closest_friend.txt"
cat score.txt|sort -k1,1n -k3,3nr -k2,2n|python closest_friend.py|python final_reducer.py>closest_friend.txt
