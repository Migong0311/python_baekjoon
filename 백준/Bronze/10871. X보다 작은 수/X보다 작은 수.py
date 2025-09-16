n,m = map(int,input().split())
arr = list(map(int,input().split()))
result_arr = []

for i in range(n):
    if arr[i] < m:
        result_arr.append(arr[i])
print(*result_arr)