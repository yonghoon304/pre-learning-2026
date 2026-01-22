# functions.py - 함수
# def 함수명({파라미터}) :
#   함수내코드
# 매개변수 == parameter == argument

# print()
# print('hello python')
# print(str(10))

# 함수 정의(매개변수가 없음)
def sayhello() :
    print('hello')
    return None

    # pass = 코드 오류 방지 기능
sayhello()


# 함수 정의(매개변수)
def sayHello(name):
    print('hello~ im '+name )

# 매개변수 사용2 + 반환
def add(x,y) : 
    result = x+y
    return result

# 매개변수 없이 반환하는 함수
def process() :
    result = 'Done'
    return result

sayHello('최용훈')

print(add(int(input('x=')),int(input('y='))))

print(process())