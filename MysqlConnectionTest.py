import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='zhc131180176',db='mytest')

cursor = conn.cursor()

cursor.execute('SET CHARACTER SET utf8;')

cursor.execute("select * from studentlist;")

# row_1 = cursor.fetchone();
# print(row_1)
row_2 = cursor.fetchmany(3)
print(row_2)

conn.commit()
cursor.close()



