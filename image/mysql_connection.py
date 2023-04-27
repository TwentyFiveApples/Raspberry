import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', db='info')

sql = 'select*from student_info'

with conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        result = cur.fetchall()
        for data in result:
            print(data)
