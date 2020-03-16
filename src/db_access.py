import pypyodbc

from src.word import word


class vocabulary_database(object):
    last = "19700101"
    date = "19700101"

    def __init__(self):
        self.path = u'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + r"./db/en_us.accdb"
        self.db = pypyodbc.win_connect_mdb(self.path)
        self.cur = self.db.cursor()
        pass

    def GetReviewList(self):
        sql = "SELECT * FROM TOEFL where 添加日期=" + self.last
        try:
            self.cur.execute(sql)
            self.TodayList = self.cur.fetchall()
        except:
            self.TodayList = []
        if self.TodayList == []:
            return False
        else:
            return [word(en_us=self.TodayList[i][0], zh_cn=self.TodayList[i][1]) for i in range(0, len(self.TodayList))]
        pass

    def InsertAWord(self, single_word: word):
        sql = "Insert Into " + "TOEFL" + " Values ('" + single_word.en_us + "','" + single_word.zh_cn + "'," + self.date + ")"
        try:
            self.cur.execute(sql)
            self.db.commit()
            return True
        except:
            return False
        pass

    def SetDate(self, date, before):
        self.date = date
        self.last = before
        pass

    pass
