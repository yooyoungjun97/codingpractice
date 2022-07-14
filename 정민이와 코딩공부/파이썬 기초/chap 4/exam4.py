# 1번 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수(is_odd)를 작성해보자
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

# print(is_odd(3))

# 4번 다음중 출력 결과가 다른 것 한 개를 고르시오.
#1) print("you" "need" "python")
#2) print("you"+"need"+"python")
#3) print("you", "need", "python")
#4) print("".join(["you" "need" "python"]))
# 3번

# 6번 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해보자.
user_input = input("저장할 내용을 입력하세요: ")
f=open('test.txt','a')
f.write(user_input)
f.write("\n")
f.close()