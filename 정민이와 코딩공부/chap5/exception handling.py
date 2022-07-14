'''
try:
    4/0
except ZeroDivisionError as e:
    print(e)
'''


'''
try :
    a=[1,2]
    print(a[3])
    4/0

except ZeroDivisionError : 
    print("0으로 나눌 수 없습니다.")
    
except IndexError :
    print("인덱싱할 수 없습니다.")
'''

'''
class Bird :
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()
'''

# 예외 만들기


'''
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보' :
        raise MyError()
    print(nick)

say_nick("천사")
say_nick("바보")
'''