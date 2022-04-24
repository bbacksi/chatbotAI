import pymysql

db = pymysql.connect(host='localhost', user='root', db='python', password='asdf', charset='utf8')
curs = db.cursor()

sql = "select * from sample";

curs.execute(sql)

rows = curs.fetchall()
print(rows)

db.commit()
db.close()