'''
길이가 N인 수열 S가 있다.
원하는 위치에서 K번 삭제 가능
삭제한 배열중에서 짝수가 가장 긴 부분수열의 길이 구하기
'''
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
e = 0
odd_cnt = 0
answer = 0
length = 0
# s 전부 순회
for s in range(n):
  # 홀수 갯수가 k가 될때까지
  while odd_cnt <= k and e < n:
    if arr[e] % 2 == 1:
      odd_cnt += 1
    # 짝수라면 길이가 최대 + 1
    else:
      length += 1
    # e 한칸씩 이동
    e += 1
    if s == 0 and e == n:
      answer = length
      break
  
  if odd_cnt == k+1:
    answer = max(answer, length)
  # 시작점이 홀수라면 - 1
  if arr[s]%2 == 1:
    odd_cnt -= 1
  else:
    length -= 1
print(answer)