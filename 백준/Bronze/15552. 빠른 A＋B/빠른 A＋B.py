import sys

input = sys.stdin.readline   # input을 빠른 입력으로 바꿈

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(a + b)
