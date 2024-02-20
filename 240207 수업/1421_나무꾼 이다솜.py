'''
나무를 자를 때 c원
목재상에서 살때 한단위에 w원
k개의 나무 길이 l => k * l * w원
=> 다솜이가 벌수 있는 가장 큰 돈
'''
n, c, w = map(int,input().split())
tree = []
for i in range(n):
  tree.append(int(input()))
M = max(tree)
answer = -1
# 완전탐색. (1~최대길이만큼 다 잘라서 계산)
for i in range(1,M+1):
  temp = 0
  for j in tree:
    # 몫과 나머지
    div = j // i
    mod = j % i
    
    # 나무를 자르는 비용을 나머지가 있나 없나로 나눈다.
    if mod:
      cost = div * c
    else:
      # 나머지가 없다는 소리는 몫 -1 만큼 잘랐다는 소리이다. (딱 맞춰 떨어지기 때문에)
      cost = (div - 1) * c
    revenue = (div * i * w) - cost
    # 이윤이 날 때만 더한다.
    if revenue > 0:
      temp += revenue
  answer = max(answer,temp)

print(answer)
  