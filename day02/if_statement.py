# if_statement.py - 제어문 if문
# 제어문 중 최초로 만들어진 것
# if 조건 :
#       처리할 문장
# else : 
#       처리할 문장

age = 20

print("담배주세요")

if age > 19 :
    print("담배를 산다")
else :
    print("민증주세요")

print()
blood = "A"

if blood == "A" :
    print("소심하네요")
elif blood == "B" :
    print("돌아이네요")
elif blood == "AB" :
    print("괴팍하네요")
elif blood == "O" :
    printd("온화하네요")
else:
    print("외계인이세요?")

print()

is_adult = True
gender = 'Female'


#이중 if문으로 분기
if is_adult == True:
    print('성인입니다. 20,000원 입니다.')
    if gender == 'Male' : 
        print('남탕으로 가세요')
    else:
        print('여탕으로 가세요')
else:
    print('소인입니다. 12,000원 입니다.')

# 논리연산자 and로 분기
is_adult=False
gender = 'Male'

if is_adult == True and gender =='Male':
    print('대인,남자,20,000원')
elif is_adult==True and gender == 'FeMale' :
    print('대인,여자,20,000원')
elif is_adult==False and gender == 'Male':
    print('대인,여자,12,000원')
elif is_adult==False and gender == 'FeMale':
    print('대인,여자,12,000원')    

# and or not
print(not is_adult) # false > true
