split -n l/10 users.txt -d hdfs_mapper
cat hdfs_mapper00|python mapper.py|sort -k1,1|python combin.py > hdfs_combine00
cat hdfs_mapper01|python mapper.py|sort -k1,1|python combin.py > hdfs_combine01
cat hdfs_mapper02|python mapper.py|sort -k1,1|python combin.py > hdfs_combine02
cat hdfs_mapper03|python mapper.py|sort -k1,1|python combin.py > hdfs_combine03
cat hdfs_mapper04|python mapper.py|sort -k1,1|python combin.py > hdfs_combine04
cat hdfs_mapper05|python mapper.py|sort -k1,1|python combin.py > hdfs_combine05
cat hdfs_mapper06|python mapper.py|sort -k1,1|python combin.py > hdfs_combine06
cat hdfs_mapper07|python mapper.py|sort -k1,1|python combin.py > hdfs_combine07
cat hdfs_mapper08|python mapper.py|sort -k1,1|python combin.py > hdfs_combine08
cat hdfs_mapper09|python mapper.py|sort -k1,1|python combin.py > hdfs_combine09
cat hdfs_combine*|sort -k1,1 -k2,2|python reducer.py|sort -k1,1 -k2,2>age.txt
