# 10개의 수를 입력받아 42로 나눈 나머지의 서로 다른 개수를 구한다
remain_42 = []                      # 모든 나머지 저장
unique_remains = []                 # 서로 다른 나머지만 저장

for _ in range(10):                 # 10개 입력
    n = int(input())                # 정수 입력
    remain_42.append(n % 42)        # 42로 나눈 나머지를 저장

for r in remain_42:                 # 저장된 나머지를 하나씩 보며
    if r not in unique_remains:     # 아직 등장하지 않았다면
        unique_remains.append(r)    # 새로 추가

print(len(unique_remains))          # 서로 다른 나머지 개수 출력
