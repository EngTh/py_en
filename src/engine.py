from src.common import clr_scr
from src.db_access import vocabulary_database
from src.word import word


class learning(object):
    db = vocabulary_database()

    def __init__(self, date_curr, date_last):
        self.db.SetDate(date=date_curr, before=date_last)
        pass

    def review(self, start: int):
        wordVector_left = self.db.GetReviewList()
        wordVector_onre = []
        countVector_display = []
        countVector_recite = []
        indexVector = []
        counter = 0

        for i in range(0, start):
            del wordVector_left[0]
            counter = counter + 1
            pass

        wordVector_onre.insert(0, wordVector_left[0])
        countVector_display.insert(0, 0)
        countVector_recite.insert(0, 0)
        indexVector.insert(0, counter)
        del wordVector_left[0]

        while wordVector_onre != []:
            while len(wordVector_onre) < 20:
                if wordVector_left != []:
                    counter = counter + 1
                    wordVector_onre.insert(len(wordVector_onre), wordVector_left[0])
                    countVector_display.insert(len(wordVector_onre), 0)
                    countVector_recite.insert(len(wordVector_onre), 0)
                    indexVector.insert(len(wordVector_onre), counter)
                    del wordVector_left[0]
                else:
                    break
                    pass
                pass
            for i in range(0, len(wordVector_onre)):
                if countVector_display[i] < 3:
                    clr_scr()
                    wordVector_onre[i].PlayOral()
                    print("**********单词复习**********")
                    print("当前序号：" + str(indexVector[i]))
                    print("en_us:" + wordVector_onre[i].en_us)
                    print("zh_cn:" + wordVector_onre[i].zh_cn)
                    print("当前 显示次数：" + str(countVector_display[i]))
                    print("***************************")
                    tempstr_enus = input("请输入英文：")
                    # tempstr_zhcn = input("请输入中文：")
                    # if tempstr_enus == wordVector_onre[i].en_us and (wordVector_onre[i].zh_cn.find(tempstr_zhcn) != -1):
                    if tempstr_enus == wordVector_onre[i].en_us:
                        print("通过")
                        countVector_display[i] = countVector_display[i] + 1
                        input()
                        pass
                    else:
                        print("失败")
                        countVector_display[i] = 0
                        input()
                        pass
                elif countVector_recite[i] < 2:
                    clr_scr()
                    print("**********单词复习**********")
                    print("当前序号：" + str(indexVector[i]))
                    print("zh_cn:" + wordVector_onre[i].zh_cn)
                    print("当前 背诵次数：" + str(countVector_recite[i]))
                    print("***************************")
                    tempstr_enus = input("请输入英文：")
                    if tempstr_enus == wordVector_onre[i].en_us:
                        print("通过")
                        wordVector_onre[i].PlayOral()
                        countVector_recite[i] = countVector_recite[i] + 1
                        input()
                        pass
                    else:
                        print("失败")
                        wordVector_onre[i].PlayOral()
                        print("en_us:" + wordVector_onre[i].en_us)
                        print("zh_cn:" + wordVector_onre[i].zh_cn)
                        countVector_recite[i] = 0
                        input()
                        pass
                    pass
                pass
            flag = False
            for i in range(0, len(wordVector_onre)):
                if countVector_recite[i] == 2:
                    flag = True
            while flag:
                for i in range(0, len(wordVector_onre)):
                    if countVector_recite[i] == 2:
                        del wordVector_onre[i]
                        del countVector_display[i]
                        del countVector_recite[i]
                        del indexVector[i]
                        break
                        pass
                    pass
                flag = False
                for i in range(0, len(wordVector_onre)):
                    if countVector_recite[i] == 2:
                        flag = True
                        pass
                    pass
            pass
        return

    def learnew(self):
        while True:
            clr_scr()
            print("**********创建新单词**********")
            tempstr_enus = input("en_us:")
            if tempstr_enus == "break_out":
                return
            tempstr_zhcn = input("zh_cn:")
            print("**********新单词确认**********")
            print("en_us:" + tempstr_enus)
            print("zh_cn:" + tempstr_zhcn)
            print("**********新单词确认**********")
            command = input("[yes/no]:")
            if command == "y":
                try:
                    self.db.InsertAWord(word(en_us=tempstr_enus, zh_cn=tempstr_zhcn))
                except:
                    print("插入失败")
                print("插入完成")
                input()
            else:
                print("插入取消")
                input()
                continue
                pass
            pass
        pass

    pass
