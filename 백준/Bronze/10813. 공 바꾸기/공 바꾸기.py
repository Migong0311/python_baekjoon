

n, m = map(int, input().split())  # n : 바구니개수 m : 공 교체횟수

bucket = list(range(1, n + 1))  # 바구니 1번부터

for _ in range(m):
    i, j = map(int, input().split())  # i번 j번 바구니 서로 교체

    # 바구니 속 공을 교체
    bucket[i - 1], bucket[j - 1] = bucket[j - 1], bucket[i - 1]

print(*bucket)
