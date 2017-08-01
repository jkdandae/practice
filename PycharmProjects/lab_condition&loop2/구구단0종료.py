a=1
while a is 1:
    index=1
    print("구구단 몇 단을 계산할까요(1~9)?")
    input_number=int(input())
    if 1<=input_number<=9:
        print("구구단 ", input_number,"단을 계산합니다.")
        for i in range(1,10):
            print(str(input_number),"X",str(i)," = ", str(i*input_number))
    elif input_number>9:
        print("1~9까지의 숫자를 입력해 주세요.")
    else:
        print("구구단 게임을 종료합니다.")
        exit()
