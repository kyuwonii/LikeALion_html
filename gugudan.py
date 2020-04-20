x=1
while (x != 0) : #2단계
    print("구구단 몇단을 계산할까요?")
    print("구구단은 정말 재미있어!!")
    x = int(input())
    if x == 0 :
        break
    if not(1<=x<=9) : #3단계
        print("잘못 입력했습니다. 1~9 사이 숫자를 입력하세요")
        continue
    else : 
        print("구구단 "+str(x)+"단을 계산합니다.") #1단계
        for i in range(1,10) :
            print(str(x)+"x"+str(i)+"="+str(x*i))
            
print("구구단을 종료합니다.")
