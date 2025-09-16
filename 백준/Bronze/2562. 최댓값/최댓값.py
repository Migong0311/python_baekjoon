
find_max_arr = []

for _ in range(9):
    n = int(input())
    find_max_arr.append(n)
max_v = max(find_max_arr)
print(max_v)
print(find_max_arr.index(max_v)+1)
