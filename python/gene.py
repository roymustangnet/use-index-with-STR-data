# -*- coding: utf-8 -*-

import random
import mysql.connector

# 每个表中记录数
ROW_COUNTS = 50

# 建表语句
SQL_DROP_TABLE = "DROP TABLE IF EXISTS {}"
SQL_CREATE_TABLE = "CREATE TABLE {} (uid int(10), gen VARCHAR(10))"
SQL_INSERT = "INSERT INTO {} VALUES (%s, %s)"

# 18个表名
TABLE_NAME_LIST = [
    "D8S1179", "D21S11", "D7S820", "CSF1PO", "D3S1358", "TH01", "D13S317", "D16S539", "D2S1338", "D19S433",
    "vWA", "TPOX", "D18S51", "AMEL", "D5S818", "FGA", "PentaE", "PentaD",
]

conn = mysql.connector.connect(host='localhost', user='root',
                               password='', database='dnatest', use_unicode=True)
cursor = conn.cursor()

# 建表
for table in TABLE_NAME_LIST:
    sql = SQL_DROP_TABLE.format(table)
    cursor.execute(sql)
    sql = SQL_CREATE_TABLE.format(table)
    cursor.execute(sql)
conn.commit()

# # 插入随机数据
# conn.autocommit = False
# for table in TABLE_NAME_LIST:
#     sql = SQL_INSERT.format(table)
#     for i in range(50):
#         cursor.execute(sql, (i, "%2.1f" % (10 * random.random()), ))
#         cursor.execute(sql, (i, "%2.1f" % (10 * random.random()), ))
#         if i % 10000 == 0:
#             conn.commit()
# conn.commit()

cursor.close()
conn.close()
