total = int(input())
n = int(input())
item_sum = 0
for _ in range(1, n + 1):
    a, b = map(int, input().split())
    item_sum += a * b

if item_sum == total:
    print('Yes')
else:
    print('No')

