
#딕셔너리 쌍 추가
'''
a={1:'a'}
a[2]='b'
a['name']='pey'
a[3]=[1,2,3]
print(a)
'''

#딕셔너리 쌍 삭제
'''
del(a[1])
print(a)
'''

#딕셔너리에서 key를 사용해 value값 얻기
'''
grade={'pey':10, 'julliet':99}
# print(grade['pey'])
# print(grade['julliet'])
'''

'''
a={1:'a', 2:'b'}
# print(a[1])
# print(a[2])
'''

#key 리스트 만들기

a={'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# print(a.keys())
#for k in a.keys():
#    print(k)
# print(list(a.keys()))
# print(a.values())

#key,value 쌍 얻기
# print(a.items())

#key:value 쌍 모두 지우기
'''
a.clear()
print(a)
'''

#key로 value 얻기(get)
'''
a={'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# print(a.get('name'))
print(a.get('phone'))
'''

#해당key가 딕셔너리 안에 있는지 조사하기(in)
'''
a={'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print('name' in a)
print('email' in a)
'''

#연습문제
a={'name':'홍길동', 'birth':'1128', 'age':'30'}
print(a)