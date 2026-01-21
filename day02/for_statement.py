# for_statement.py - for반복문
# 밑으로 복사하는 단축어 alt shift 방향키

print(range(5))
print(list(range(5)))

for i in range(5) :  # range(0,5) => 0,1,2,3,4까지
    print(i,end=" ")
print()

for i in range(1,6) : # 1,2,3,4,5
    print(i,end=" ")
print()
for i in range(5,0,-1) : # 5,4,3,2,1
    print(i,end=" ")
print()

print('구구단')
for i in range(2,10) :
    print(str(i)+"단 시작")
    for j in range(2,10):
        print(str(i)+" x "+str(j)+" = "+str(i*j),end= " ")
    print()
    
#성적판별

score = int(input("성적 입력"))

if  score>=90:
    print("A학점")
elif  score>=80:
    print("B학점")
elif  score>=70:
    print("C학점")
else:
    print("F학점")