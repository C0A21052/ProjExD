
import random
import datetime

al = 5
ak = 10
aj = 2
def main(a):
    global a
    st = datetime.datetime.now()
    for _ in range(al):
        seikai = shutudai()
        kaitou(seikai)
    ed = datetime.datetime.now()
    print(f"{(ed-st).seconds}秒かかりました")

def shutudai(b):
    global b
    alp_list = [chr(ord("a")+i) for i in range(26)]
    all_char_lst = random.sample(alp_list, ak)
    print(f"対象文字：{all_char_lst}")
    abs_char_lst = random.sample(XXXX, YYYY)
    print(f"欠損文字：{abs_char_lst}")
    pre_char_lst = [ZZZZ]
    print(f"表示文字：{pre_char_lst}")


def kaitou(seikai):
    global seiseki
    num = int(input("欠損文字はいくつあるでしょうか？"))
    if num != aj:
        print("不正解です、またチャレンジしてね")
        return 0
    else:
        print("正解です。それでは具体的に欠損文字を一つずつ入力してください")
        for i  in range(aj):
            c = input()
if __name__ == "__main__":
    shutudai()
    kaitou()


