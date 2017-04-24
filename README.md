# use-index-with-STR-data

# 说明
生成460000条STR数据，用于测试不同存储方式的速度

# 建立数据的方法
 - 用DB/sql.txt中的SQL建表
 - 用python/main.py生成CSV数据和DB数据（在STR数据表中）
 - 用python/gene.py生成位点表
 - 用DB/insert_data.sql中的SQl语句，将STR中的数据分别插入到对应的STR位点表中

# 查询方法
 - 用DB/query.sql中的SQL语句进行模糊查询