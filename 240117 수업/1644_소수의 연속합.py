'''
에라토스테네스의 체로 4백만 까지의 소수를 구한다.
이를 arr에 넣어준 후, 투포인터로 s,e를 0,1으로 두고 합이 가능한지 판별.
arr[s]의 값이 N보다 커지는 경우 break
'''
is_Prime = [True for _ in range(4000001)]
is_Prime[0] = False
is_Prime[1] = False
for i in range(2,4000001):
  if not is_Prime:
    continue
  for j in range(i*i,4000001,i):
    is_Prime[j] = False

arr = []
for i in range(4000001):
  if is_Prime[i]:
    arr.append(i)

N = int(input())
s, e = 0, 1
cnt = 0
while s < e and e <= N:
  if arr[s] > N:
    break
  # arr의 s~e-1번까지의 합
  temp = sum(arr[s:e])
  if temp > N:
    s += 1
  elif temp == N:
    cnt += 1
    s += 1
  else:
    e += 1
print(cnt)