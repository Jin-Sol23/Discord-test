# 230512 공지사항
# 문제 : for문을 사용하여 다음과 같이 별(*)을 표시하는
# 프로그램을 작성해 보자.

# 예상 출력 값 :
# *
# **
# ***
# ****
# *****

# sum = 0
# for i in range(0, 5):
#     sum = i + 1
#     print("*"*sum)

for i in range(1, 6, 1):
    print("*"*i)