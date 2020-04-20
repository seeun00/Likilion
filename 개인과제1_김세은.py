#1876053 김세은 1-1

liondict = { "은진": "이대여대 멋사 대표님", "연주": "이화여대 멋사 회장님", "두희": "멋사 대장", "유진": "이화여대 멋사 튜터님" }

for name in liondict :          #반복문
    print("다음은 누구에 대한 설명일까요?")
    print(liondict[name])
    print("(1)은진 (2)연주 (3)두희 (4)유진")
    a=input()

    if (a==name):               #정답과 input값 비교
        print("정답입니다!\n")
    else :
        print("오답입니다!\n")
