import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
# 덧셈/뺄셈/곱셉/나눗셈
operator = list(map(int,input().split()))
m = sum(operator)
dict_operator = {'+':operator[0],'-':operator[1],'*':operator[2],'//':operator[3]}
arr = [0 for _ in range(m)]
operator_lst = []
for i in dict_operator.keys():
  a = dict_operator[i]
  for j in range(a):
    operator_lst.append(i)

visited = [False for _ in range(n)]
min_ = sys.maxsize
max_ = -1 * sys.maxsize
def check(arr):
  global min_,max_
  arr_ = arr.copy()
  temp = lst[0]
  for i in range(m):
    if arr_[i] == '+':
      temp += lst[i+1]
    elif arr_[i] == '-':
      temp -= lst[i+1]
    elif arr_[i] == '*':
      temp *= lst[i+1]
    else:
      if temp < 0:
        temp = (-1*temp)//lst[i+1]
        temp *= -1
      else:
        temp //= lst[i+1]
  min_ = min(min_,temp)
  max_ = max(max_,temp)
  return

def recur(cur):
  global min_, max_
  if cur == m:
    check(arr)
    return
  for i in range(m):
    if visited[i]:
      continue
    visited[i] = True
    arr[cur] = operator_lst[i]
    recur(cur+1)
    visited[i] = False

recur(0)

print(max_)
print(min_)