'''
2차원 누적합 활용??
해당 부분 배열에 서로 다른 자연수가 몇개인지
3차원 배열로 만들어서 해당 배열에 1~10까지의 숫자가 몇개 들어있나 확인하면서 푼다.
'''
import sys
input = sys.stdin.readline
n = int(input())
arr = [[0]*(n+1)]
for i in range(n):
  arr.append([0]+list(map(int,input().split())))

prefix = [[[0]*11 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,11):
      if arr[i][j] == k:
        # 해당 배열에 몇개있는지 추가
        prefix[i][j][k] += 1
      # 겹치는 부분을 제외하면서 누적합 형식으로 넣어준다
      prefix[i][j][k] += prefix[i-1][j][k] + prefix[i][j-1][k] - prefix[i-1][j-1][k]
# 이제 2차원 누적합을 구했던것 처럼 해당 쿼리가 들어왔을 때, 계산을 해준다
q = int(input())
for i in range(q):
  x1,y1,x2,y2 = map(int,input().split())
  cnt = 0
  for k in range(1,11):
    # 누적합 배열에 존재하고 있다면. cnt += 1 (1개만 있는지 확인할 필요가 없다. 존재만 한다면 그 숫자에 대해서만 +=1)
    if prefix[x2][y2][k] - prefix[x2][y1 - 1][k] - prefix[x1-1][y2][k] + prefix[x1-1][y1-1][k]:
      cnt += 1
  print(cnt)