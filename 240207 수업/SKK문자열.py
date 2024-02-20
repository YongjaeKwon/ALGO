'''
SKK가 포함된 가장 긴 문자열을 찾는다.
S 를 2 K를 -1로 표현.
누적합!
합이 0인 연속 부분 수열을 찾으면 된다.
S가 존재하는지 아닌지를 판별 => 어려운 부분
'''
import sys
input = sys.stdin.readline

skk = input().rstrip()
arr = [0]
for i in range(len(skk)):
  if skk[i] == 'S':
    arr.append(2)
  elif skk[i] == 'K':
    arr.append(-1)
  else:
    arr.append(0)

# S가 포함되어있는지 확인하는 누적합 배열이 필요함
count_s = [0 for _ in range(len(arr))]
for i in range(1, len(arr)):
  if arr[i] == 2:
    count_s[i] += 1
prefix_s = [0 for _ in range(len(arr))]
for i in range(1,len(count_s)):
  prefix_s[i] = prefix_s[i-1] + count_s[i]
print(prefix_s)


prefix = list(0 for _ in range(len(arr)))
for i in range(1,len(arr)):
  prefix[i] = prefix[i-1] + arr[i]
print(prefix)

max_len = -1
s = 1
e = len(prefix)-1
while s <= e:
  if prefix[e] - prefix[s] == 0 and prefix_s[e] - prefix_s[s] != 0:
    max_len = max(max_len, e - s)
  if prefix[e] - prefix[s] == 0:
    if prefix_s[e] - prefix_s[s] != 0:
      e -= 1 
    else:
      s += 1
  else:
      e -= 1
print(max_len)