# 파일을 쓰기모드로 열어 출력값 적기
'''
f=open("C:/Users/9blue/Desktop/정민이와 코딩공부/파이썬 기초/chap 4/새파일.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n"% i
    f.write(data)

f.close()
'''
# 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
'''
f= open("C:/Users/9blue/Desktop/정민이와 코딩공부/파이썬 기초/chap 4/새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
'''

'''
f= open("C:/Users/9blue/Desktop/정민이와 코딩공부/파이썬 기초/chap 4/새파일.txt",'r')
data = f.read()
print(data)
f.close()
'''

# 파일에 새로운 내용 추가하기

f=open("C:/Users/9blue/Desktop/정민이와 코딩공부/파이썬 기초/chap 4/새파일.txt",'a')
for i in range(11,20):
    data = "%d번째 줄입니다\n" % i
    f.write(data)
f.close