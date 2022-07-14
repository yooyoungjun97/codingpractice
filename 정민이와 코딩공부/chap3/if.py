# 만약 3000원 이상의 돈을 가지고 있드면 택시를 타고 그렇지 않으면 걸어가라
'''
money=2000
if money>=3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
'''

#돈이 3000원 이상 있거나 카드가 있따면 택시를 타고 그렇지 않으면 걸아가라
'''
money=2000
card=True
if money>= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
'''

# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라.
'''
pocket =['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
'''

# 주머니에 카드가 없다면 걸어가고 있다면 버스를 타고가라
'''
pocket=['paper', 'cellphone', 'money', 'airpod']
if 'card' not in pocket:
    print("걸어가라")
else:
    print("버스릍 타고 가라")
'''

#주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라
'''
pocket=['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
'''

#주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라
'''
from cgi import print_arguments


pocket=['paper', 'cellphone']
card=True
if'money' in pocket:
    print("Taxi")
elif card:
    print("Taxi")
else:
    print('walk')
'''