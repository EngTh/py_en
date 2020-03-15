from src.engine import learning

date_learn = input("学习日期：")
date_review = input("复习日期：")

engine = learning(date_curr=date_learn, date_last=date_review)

DoLearn = input("是否学习：yes/no")
if DoLearn == "yes":
    engine.learnew()
    pass

DoReview = input("是否复习：yes/no")
if DoReview == "yes":
    start = int(input("起始位置："))
    engine.review(start)
    pass
