# 1번
'''
a=80
b=75
c=55
d=a+b+c
print(d/3)
'''
#2번
'''
number=13

if number % 2 == 0 :
    print("even")
elif number % 2 == 1:
    print("odd")
'''

#3번
'''
pin ="881120-1068234"
yyyymmdd=pin[0:6]
num=pin[7:]
print(yyyymmdd)
print(num)
'''

#4번
'''
pin ="881120-1068234"
print(pin[7])
'''
#5번

'''
a='a:b:c:d'
b=a.replace(':','#')
print(b)
'''

#6번
'''
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)
'''

#7번
'''
a=['Life','is','too','short']
result=a[0]+a[1]+a[2]+a[3]
print(result)
'''

#8번
'''
a=(1,2,3)
a=a+(4,)
print(a)
'''

#9번
# a=dict()
# print(a)
# a[[1]]='python' -> 딕셔너리는 변하는 값을 쓸수 없다.

# 10번
'''
from unittest import result


a={'a':90, 'b':80, 'c':70}
result = a.pop('b')
print(a)
print(result)
'''

#11번
'''
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
print(aSet)
b=list(aSet)
print(b)
'''

#12번
a=b=[1,2,3]
a[1]=4
print(b)
