# modules.py - 모듈 내장함수 확인
# import 모듈명

import math # 수학관련된 함수와 데이터 담고있는 모듈

pi = 3.141592

radius = 10

result = radius * radius * pi
print('원의 넓이는 '+str(result))

result = radius*radius*math.pi
print('원의 넓이는 '+str(result))

print(math.sqrt(16))
print(math.floor(4.3))
print(math.ceil(4.3))

import datetime

print(datetime.datetime.now)

## 내장함수
print(len('Hello'))
print(len([1,2,3,4,5,6]))

print(type(1))
print(type(pi))
print(type([1,2,3,4]))
print(type('hello'))

print(int('80')) # 정수형으로 된 문자열만 변환가능
print(float('4.6')) # 정수형, 싨형 모두 변환가능
print(str(3.141592)) 