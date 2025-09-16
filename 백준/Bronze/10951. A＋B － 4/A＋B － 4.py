import sys

for line in sys.stdin:           # 입력이 끝날 때까지 한 줄씩 읽음
    a, b = map(int, line.split())
    print(a + b)
