h, m = map(int, input().split())
c = int(input())
# 현재 시간을 분 단위로
total = h * 60 + m

# 요리 시간 더하기
total += c

# 다시 시와 분으로 환산
h = (total // 60) % 24
m = total % 60

print(h, m)
