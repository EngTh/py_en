import pypyodbc

path = u'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + r"B:\\OneDrive\\University\\2019-2020\\2_Second_Term\\背单词\en_us.accdb"
db = pypyodbc.win_connect_mdb(path)
cur = db.cursor()
sql = "SELECT * FROM TOEFL where 添加日期=20200314"
cur.execute(sql)
b = cur.fetchall()
a = 0
sql = "Insert Into " + "TOEFL" + " Values ('testa','n,测试一下',20200404)"
cur.execute(sql)
db.commit()
c = 0
