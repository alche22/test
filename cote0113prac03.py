# N = row 수
# 구조가 행이 N개인 배열의 리스트 입출력

# 3
# 1 2 3
# 3 2 1 
# 2 2 2

import sys
input = sys.stdin.readline
row = []
N = int(input().strip())
# row = list(map(int,input().strip()))
for i in range(N):
    row_data = list(map(int,input().split()))
    row.append(row_data)

print(row)