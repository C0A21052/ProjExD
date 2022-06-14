


from locale import ABDAY_1
import random 
import datetime

def shutudai(a):
    Q_list = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    print = ("問題："+ "\n" + Q_list[a])
    



def kaito(a):
    A_list = [["ますお","マスオ"],["わかめ","ワカメ"],["甥","おい","甥っ子","おいっこ"]]
    ans = input("答えるんだ：")
    if ans in A_list[a]:
        print("正解！！！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    a1 = random.randint(0,2)
    shutudai(a1)
    kaito(a1)


