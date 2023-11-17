# 230512 공지사항
# for문을 사용해 1~1000까지 자연수 중 3의 배수의 합 구하기

sum = 0

for i in range(1, 1001):
    if i % 3 == 0:
        sum = sum + i
print(sum)