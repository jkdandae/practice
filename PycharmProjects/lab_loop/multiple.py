user_input=1
while user_input!=0:
    print("구구단 몇 단을 계산할까요")
    user_input = int(input())
    print("구구단", user_input,"단을 계산합니다")
    j=1
    while j<10:
        cal = j * user_input
        print(user_input, "X", j, "=", cal)
        j+=1
print("구구단 게임을 종료합니다")
