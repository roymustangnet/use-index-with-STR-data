#多表查询的SQL语句
SELECT uid
FROM (SELECT uid, COUNT(1) AS cnt
    FROM (
        SELECT distinct(uid)
        FROM D8S1179
        WHERE gen = '3.1' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM D21S11
        WHERE gen = '8.6' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM D7S820
        WHERE gen = '6.3' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM CSF1PO
        WHERE gen = '4.7' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM D3S1358
        WHERE gen = '2.9' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM TH01
        WHERE gen = '9.9' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM D13S317
        WHERE gen = '7.6' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM D16S539
        WHERE gen = '7.1' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM D2S1338
        WHERE gen = '5.4' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM D19S433
        WHERE gen = '8.0' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM vWA
        WHERE gen = '4.6' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM TPOX
        WHERE gen = '3.0' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM D18S51
        WHERE gen = '8.9' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM AMEL
        WHERE gen = '5.6' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM D5S818
        WHERE gen = '3.6' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM FGA
        WHERE gen = '7.6' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM PentaE
        WHERE gen = '0.6' or gen = '13'
        UNION ALL
        SELECT distinct(uid)
        FROM PentaD
        WHERE gen = '3.0' or gen = '13'
    ) t1
    GROUP BY uid
    ) t2
WHERE cnt >= 17;