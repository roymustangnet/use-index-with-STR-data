# -*- coding: utf-8 -*-

import random
import mysql.connector

def random_pick(some_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item

FIELD_LIST = ['SAMPLE_ID',
              'D8S1179_1', 'D8S1179_2', 'D21S11_1', 'D21S11_2', 'D7S820_1', 'D7S820_2',
              'CSF1PO_1', 'CSF1PO_2', 'D3S1358_1', 'D3S1358_2', 'TH01_1', 'TH01_2',
              'D13S317_1', 'D13S317_2', 'D16S539_1', 'D16S539_2', 'D2S1338_1', 'D2S1338_2',
              'D19S433_1', 'D19S433_2', 'vWA_1', 'vWA_2', 'TPOX_1', 'TPOX_2',
              'D18S51_1', 'D18S51_2', 'AMEL_1', 'AMEL_2', 'D5S818_1', 'D5S818_2',
              'FGA_1', 'FGA_2', 'PentaE_1', 'PentaE_2', 'PentaD_1', 'PentaD_2'
              ]

TBL_NAME = 'STR'
D8S1179_LIST = [8    , 9    , 10   , 11   , 12   , 12.1 , 13   , 14   , 15   , 
                16   , 17   , 18]
D8S1179_DIST = [0.000, 0.000, 0.140, 0.128, 0.140, 0.000, 0.221, 0.174, 0.140, 
                0.047, 0.012, 0.000]
D21S11_LIST  = [24.2 , 24.3 , 25   , 25.2 , 25.3 , 26   , 26.2 , 27   , 28   , 
                28.2 , 29   , 29.2 , 29.3 , 30   , 30.2 , 30.3 , 31   , 31.2 , 
                32   , 32.1 , 32.2 , 33   , 33.1 , 33.2 , 34   , 34.1 , 34.2 ,
                35   , 35.2 , 36   , 36.1 , 37   , 37.2 , 38   , 38.2 , 39   ]
D21S11_DIST  = [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.024, 
                0.024, 0.262, 0.000, 0.000, 0.321, 0.000, 0.000, 0.119, 0.048, 
                0.048, 0.000, 0.083, 0.000, 0.000, 0.060, 0.000, 0.000, 0.012, 
                0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000]
D7S820_LIST  = [6    , 6.3  , 7    , 7.3  , 8    , 8.1  , 9    , 10   , 10.1 , 
                10.3 , 11   , 11.1 , 11.3 , 12   , 13   , 13.1 , 14   , 15]    
D7S820_DIST  = [0.000, 0.000, 0.000, 0.000, 0.125, 0.000, 0.025, 0.200, 0.000, 
                0.000, 0.438, 0.000, 0.000, 0.200, 0.013, 0.000, 0.000, 0.000]
CSF1PO_LIST  = [6    , 7    , 8    , 9    , 10   , 11   , 12   , 13   , 14   ,
                15   ]
CSF1PO_DIST  = [0.000, 0.012, 0.000, 0.036, 0.238, 0.333, 0.286, 0.083, 0.012, 
                0.000]
D3S1358_LIST = [6    , 9    , 11   , 12   , 13   , 14   , 15   , 15.2 , 16   ,
                17   , 18   , 19   , 20   ]
D3S1358_DIST = [0.000, 0.000, 0.000, 0.000, 0.000, 0.023, 0.442, 0.000, 0.279,
                0.221, 0.035, 0.000, 0.000]
TH01_LIST    = [5    , 6    , 7    , 8    , 9    , 9.3  , 10   , 11   , 12   ]
TH01_DIST    = [0.000, 0.105, 0.267, 0.058, 0.488, 0.058, 0.023, 0.000, 0.000]
D13S317_LIST = [7    , 8    , 9    , 10   , 11   , 12   , 13   , 14   , 15   , 
                16   ]
D13S317_DIST = [0.000, 0.233, 0.128, 0.174, 0.244, 0.151, 0.058, 0.012, 0.000, 
                0.000]
D16S539_LIST = [5    , 8    , 9    , 10   , 11   , 12   , 13   , 14   , 15   ]
D16S539_DIST = [0.000, 0.000, 0.274, 0.131, 0.298, 0.226, 0.071, 0.000, 0.000]
D2S1338_LIST = [11   , 13   , 14   , 15   , 16   , 17   , 18   , 19   , 20   , 
                21   , 21.2 , 22   , 23   , 24   , 25   , 26   , 27    ]
D2S1338_DIST = [0.000, 0.000, 0.000, 0.000, 0.000, 0.128, 0.140, 0.128, 0.105, 
                0.000, 0.000, 0.047, 0.174, 0.209, 0.070, 0.000, 0.000]
D19S433_LIST = [9    , 9.2  , 10   , 11   , 11.2 , 12   , 12.2 , 13   , 13.2 , 
                14   , 14.2 , 15   , 15.2 , 16   , 16.2 , 17   , 17.2 , 18   , 
                18.2]
D19S433_DIST = [0.000, 0.000, 0.000, 0.000, 0.000, 0.035, 0.000, 0.279, 0.012, 
                0.326, 0.151, 0.035, 0.163, 0.000, 0.000, 0.000, 0.000, 0.000, 
                0.000]
vWA_LIST     = [11   , 12   , 13   , 14   , 15   , 16   , 17   , 18   , 19   , 
                20   , 21   , 22   ]
vWA_DIST     = [0.000, 0.000, 0.000, 0.244, 0.012, 0.151, 0.244, 0.233, 0.093, 
                0.023, 0.000, 0.000]
TPOX_LIST    = [6    , 7    , 8    , 9    , 10   , 11   , 12   , 13   ]
TPOX_DIST    = [0.000, 0.000, 0.547, 0.093, 0.047, 0.279, 0.023, 0.012]
D18S51_LIST  = [9    , 10   , 10.2 , 11   , 11.2 , 12   , 12.2 , 13   , 13.1 , 
                13.2 , 14   , 14.2 , 15   , 15.2 , 16   , 16.2 , 17   , 17.2 , 
                18   , 18.2 , 19   , 19.2 , 20   , 21   , 21.2 , 22   , 23   ,
                24   , 25   , 28   ]
D18S51_DIST  = [0.000, 0.012, 0.000, 0.000, 0.000, 0.024, 0.000, 0.195, 0.000, 
                0.000, 0.268, 0.000, 0.220, 0.000, 0.085, 0.000, 0.024, 0.000, 
                0.073, 0.000, 0.024, 0.000, 0.037, 0.012, 0.000, 0.012, 0.012, 
                0.000, 0.000, 0.000]
AMEL_LIST    = ['X'  , 'Y'  ]
AMEL_DIST    = [0.500, 0.500]
D5S818_LIST  = [7    , 8    , 9    , 10   , 11   , 12   , 13   , 14   , 15   , 
                16   ]
D5S818_DIST  = [0.035, 0.000, 0.105, 0.128, 0.349, 0.209, 0.163, 0.012, 0.000, 
                0.000]
FGA_LIST     = [16   , 16.2 , 17   , 17.2 , 18   , 18.2 , 19   , 19.2 , 20   , 
                20.2 , 20.3 , 21   , 21.2 , 22   , 22.2 , 22.3 , 23   , 23.2 , 
                23.3 , 24   , 24.2 , 24.3 , 25   , 25.2 , 26   , 27   , 27.1 , 
                27.2 , 28   , 28.1 , 29   , 30   , 30.2 , 31.2 , 33   , 33.2 , 
                33.3 , 43.2 , 45.2 , 46.2]
FGA_DIST     = [0.000, 0.000, 0.000, 0.000, 0.026, 0.000, 0.064, 0.000, 0.115, 
                0.000, 0.000, 0.128, 0.000, 0.090, 0.000, 0.000, 0.269, 0.000, 
                0.000, 0.128, 0.013, 0.000, 0.064, 0.000, 0.090, 0.000, 0.000, 
                0.013, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 
                0.000, 0.000, 0.000, 0.000]
PentaE_LIST  = [5    , 7    , 8    , 9    , 10   , 11   , 12   , 13   , 14   , 
                15   , 16   , 17   , 18   , 19   , 20   , 21   , 22   , 23   ,
                24]
PentaE_DIST  = [0.024, 0.000, 0.000, 0.024, 0.049, 0.171, 0.122, 0.037, 0.073, 
                0.098, 0.122, 0.146, 0.049, 0.049, 0.012, 0.012, 0.000, 0.012, 
                0.000]
PentaD_LIST  = [2.2  , 3.2  , 5    , 6    , 7    , 8    , 9    , 10   , 11   ,
                12   , 13   , 14   , 15   , 16   , 17] 
PentaD_DIST  = [0.000, 0.000, 0.000, 0.024, 0.024, 0.024, 0.317, 0.134, 0.122, 
                0.232, 0.085, 0.037, 0.000, 0.000, 0.000]

STR_LIST_DIST = [[D8S1179_LIST, D8S1179_DIST],
                 [D21S11_LIST , D21S11_DIST ],
                 [D7S820_LIST , D7S820_DIST],
                 [CSF1PO_LIST , CSF1PO_DIST],
                 [D3S1358_LIST, D3S1358_DIST],
                 [TH01_LIST   , TH01_DIST],
                 [D13S317_LIST, D13S317_DIST],
                 [D16S539_LIST, D16S539_DIST],
                 [D2S1338_LIST, D2S1338_DIST],
                 [D19S433_LIST, D19S433_DIST],
                 [vWA_LIST    , vWA_DIST],
                 [TPOX_LIST   , TPOX_DIST],
                 [D18S51_LIST , D18S51_DIST],
                 [AMEL_LIST   , AMEL_DIST],
                 [D5S818_LIST , D5S818_DIST],
                 [FGA_LIST    , FGA_DIST],
                 [PentaE_LIST , PentaE_DIST],
                 [PentaD_LIST , PentaD_DIST]]

# 根据STR的名称，以一定的概率生成对应的STR值
def generateSTR(str_name):
  strs = {'D8S1179':0, 'D21S11':1, 'D7S820':2,
          'CSF1PO':3, 'D3S1358':4, 'TH01':5,
          'D13S317':6, 'D16S539':7, 'D2S1338':8,
          'D19S433':9, 'vWA':10, 'TPOX':11,
          'D18S51':12, 'AMEL':13, 'D5S818':14,
          'FGA':15, 'PentaE':16, 'PentaD':17}
  # STR的数据值和其概率分布
  str_pair = STR_LIST_DIST[strs[str_name]]
  return random_pick(str_pair[0], str_pair[1])

# 生成STR数据，并存储到CSV文件中
def generate_csv_data():
  title = ["D8S1179", "D21S11", "D7S820",
      "CSF1PO", "D3S1358", "TH01",
      "D13S317", "D16S539", "D2S1338", 
      "D19S433", "vWA", "TPOX",
      "D18S51", "AMEL", "D5S818",
      "FGA", "PentaE", "PentaD"]

  with open('./sample_data.csv', 'w') as the_file:
      the_file.write(','.join(title)+'\n')
  for cycle in range(46):
    block = []
    for i in range(10000):
      vlist = []
      for str_name in title:
        str_value = "{}/{}".format(generateSTR(str_name),generateSTR(str_name))
        vlist.append(str_value)
      line = ",".join(vlist)
      block.append(line)
    
    block = "\n".join(block)
    with open('./sample_data.csv', 'a') as the_file:
      the_file.write(block+'\n')

# 生成STR数据，并存储到数据库中
def generate_DB_data():
  conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='dnatest', use_unicode=True)
  cursor = conn.cursor()
  title = ["D8S1179", "D21S11", "D7S820",
      "CSF1PO", "D3S1358", "TH01",
      "D13S317", "D16S539", "D2S1338", 
      "D19S433", "vWA", "TPOX",
      "D18S51", "AMEL", "D5S818",
      "FGA", "PentaE", "PentaD"]
  sql = """
      INSERT INTO STR (D8S1179_1, D8S1179_2, D21S11_1, D21S11_2, D7S820_1, D7S820_2,
      CSF1PO_1, CSF1PO_2, D3S1358_1, D3S1358_2, TH01_1, TH01_2,
      D13S317_1, D13S317_2, D16S539_1, D16S539_2, D2S1338_1, D2S1338_2,
      D19S433_1, D19S433_2, vWA_1, vWA_2, TPOX_1, TPOX_2,
      D18S51_1, D18S51_2, AMEL_1, AMEL_2, D5S818_1, D5S818_2,
      FGA_1, FGA_2, PentaE_1, PentaE_2, PentaD_1, PentaD_2) VALUES (
      %s,%s,%s,%s,%s,%s,
      %s,%s,%s,%s,%s,%s,
      %s,%s,%s,%s,%s,%s,
      %s,%s,%s,%s,%s,%s,
      %s,%s,%s,%s,%s,%s,
      %s,%s,%s,%s,%s,%s)
  """  
  for cycle in range(46):
      values_lists = []
      for i in range(10000):
        vlist = []
        for str_name in title:
          # 生成两个数据
          vlist.append("{}".format(generateSTR(str_name)))
          vlist.append("{}".format(generateSTR(str_name)))
        values_lists.append(vlist)
      cursor.executemany(sql, values_lists)
      conn.commit()
  if cursor is not None:
      cursor.close()
  if conn is not None:
      conn.close()

# 生成STR数据，并保存到数据库和CSV文件中
def generate_csv_db_data():
  title = ["D8S1179", "D21S11", "D7S820",
      "CSF1PO", "D3S1358", "TH01",
      "D13S317", "D16S539", "D2S1338", 
      "D19S433", "vWA", "TPOX",
      "D18S51", "AMEL", "D5S818",
      "FGA", "PentaE", "PentaD"]
  # 生成CSV文件的头部
  with open('./sample_data.csv', 'w') as the_file:
    the_file.write('\n'+','.join(title))

  conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='dnatest', use_unicode=True)
  cursor = conn.cursor()
  sql = """
      INSERT INTO STR (D8S1179_1, D8S1179_2, D21S11_1, D21S11_2, D7S820_1, D7S820_2,
      CSF1PO_1, CSF1PO_2, D3S1358_1, D3S1358_2, TH01_1, TH01_2,
      D13S317_1, D13S317_2, D16S539_1, D16S539_2, D2S1338_1, D2S1338_2,
      D19S433_1, D19S433_2, vWA_1, vWA_2, TPOX_1, TPOX_2,
      D18S51_1, D18S51_2, AMEL_1, AMEL_2, D5S818_1, D5S818_2,
      FGA_1, FGA_2, PentaE_1, PentaE_2, PentaD_1, PentaD_2) VALUES (
      %s,%s,%s,%s,%s,%s,
      %s,%s,%s,%s,%s,%s,
      %s,%s,%s,%s,%s,%s,
      %s,%s,%s,%s,%s,%s,
      %s,%s,%s,%s,%s,%s,
      %s,%s,%s,%s,%s,%s)
  """ 

  for cycle in range(46):
      values_lists = []
      block = []
      for i in range(10000):
        vlist = []
        vlist2 = []
        for str_name in title:
          v1 = generateSTR(str_name)
          v2 = generateSTR(str_name)
          vlist.append( "{}".format(v1))
          vlist.append( "{}".format(v2))
          str_value = "{}/{}".format(v1,v2) #"13/14"形式的STR数据
          vlist2.append(str_value)
        values_lists.append(vlist)
        # 生成1行的STR数据
        line = ",".join(vlist2)
        block.append(line)

      block = "\n".join(block)
      with open('./sample_data.csv', 'a') as the_file:
        the_file.write('\n'+block)

      cursor.executemany(sql, values_lists)
      conn.commit()

  if cursor is not None:
      cursor.close()
  if conn is not None:
      conn.close()



if __name__ == '__main__':
  generate_csv_db_data()
