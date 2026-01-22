# modules.py - 모듈 내장함수 확인
# import 모듈명

import math # 수학관련된 함수와 데이터 담고있는 모듈

pi = 3.141592

radius = 10

result = radius * radius * pi
print('원의 넓이는 '+str(result))

result = radius*radius*math.pi
print('원의 넓이는 '+str(result))
