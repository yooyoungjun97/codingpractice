# 전형적인 for 문
'''

test_list =['one', 'two', 'three']
for i in test_list:
    print(i)
'''
 
'''
#다양한 for문 사용
a=[(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first+last)
'''

'''
# marks1.py
marks=[90,25,67,45,80]
number = 0
for mark in marks:
    number = number+1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)
'''

'''
# marks2.py
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number=number+1
    if mark<60: continue
    print("%d번 학생 축하합니다. 합격입니다. " %number)
'''
'''
a=range(10)
print(a)


a=range(11)
print(a)
'''
'''
add=0
for i in range(1,11):
    add=add+i

print(add)
'''

'''
add=0
for i in range(1,101):
    add=add+i

print(add)
'''

'''
# for와 range를 이용하여 구구단 만들기

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')
'''

# result 리스트 담는 예제
'''
a=[1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)
'''
# 리스트 내포 사용하기

'''
a=[1,2,3,4]
result=[num * 3 for num in a]
print(result)
'''
    # 리스트 내포 안에 짝수만 포함
'''
a=[1,2,3,4]
result=[num * 3 for num in a if num%2==0]
print(result)
'''

