# 230512 공지사항
# A 학급에 총 10명의 학생이 있다.
# 학생들의 중간고사 점수 : [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수 구하시오.

s = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum = 0

# for i in s:
#     sum += i
# print(f"{sum/len(s)}")

for i in s:
    sum += i
print(sum/10)