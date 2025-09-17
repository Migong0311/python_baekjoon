student = set(range(1, 31))  # 1~30 전체학생
submit = set()  # 제출 학생집합

for _ in range(28):
    n = int(input())  # 28명 입력
    submit.add(n)  # 제출자 추가

missing = sorted(student - submit)  # 전체학생번호에서 제출자의 차이를 계산 후 정렬
print(missing[0])
print(missing[1])
