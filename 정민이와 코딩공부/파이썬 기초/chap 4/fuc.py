#def
'''
def add(a,b):
    return a+b

a=3
b=4
c=add(a,b)
print(c)
'''
# def2
'''
def add(a,b):
    result=a+b
    return result

a= add(3,4)
print(a)
'''

# 입력값이 없는 함수
'''
def say():
    return 'Hi'

a = say()
print(a)
'''

#결과 값이 없는 함수
'''
def add(a,b):
    print("%d,%d의 합은 %d입니다." % (a,b,a+b))

# print(add(3,4))

a= add(3,4)
'''
#매개변수 지정하여 호출하기
'''
def add(a,b):
    return a+b
result = add(b=5, a=3)
print(result)
'''

# 여러 개의 입력 값을 받는 함수 만들기

'''
def add_many(*args):
    result = 0
    for i in args : 
        result = result + i
    return result

result = add_many(1,2,3)
print(result)
'''

'''

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args : 
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args : 
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)
    
'''

#매개변수에 초깃값 미리 설정하기
'''
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27, True)
'''

#함수 안에서 선언한 변수의 효력범위
'''
a=1
def vartest(a):
    a=a+1

vartest(a)
print(a)
'''

#함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. 리턴 사용하기




a = 1
def vartest(a):
    a=a+1  
    return a
a= vartest(a)
print(a)