sqoop import \
--connect
jdbc:mysql://database-lab5.c3f4g2yxdyve.us-east-1.rds.amazonaws.com/happy
\
--username admin \
--password Ct123456 \
--table happy2018 \
--target-dir /user/hadoop/lab5 \
--split-by id
