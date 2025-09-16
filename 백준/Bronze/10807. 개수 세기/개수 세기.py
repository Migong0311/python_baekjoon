n = int(input())
arr = list(map(int,input().split()))
v = int(input())
result_arr = []

for i in range(n):
    if arr[i] == v:
        result_arr.append(arr[i])
print(len(result_arr))