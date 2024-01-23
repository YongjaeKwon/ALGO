'''
카누랑 똑같은 문제.
'''
N = int(input())
A,B,C,D = [],[],[],[]
for _ in range(N):
  a,b,c,d = map(int,input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)
  
arr_AB = []
arr_CD = []

# A+B / C+D로 나눈다.
for i in range(N):
  for j in range(N):
    arr_AB.append(A[i] + B[j])
    arr_CD.append(C[i] + D[j])

# 합이 0이 되는 쌍을 찾아야 하기 떄문에 중복제거 X

# 투포인터 활용을 위해 정렬
arr_AB.sort()
arr_CD.sort()

s = 0
e = len(arr_CD) -1

cnt = 0
while s < len(arr_AB) and e >= 0:
  sum_ = arr_AB[s] + arr_CD[e]
  if sum_ < 0:
    s += 1
  elif sum_ == 0:
    # 합이 0일때는 각각에 같은 숫자가 몇개씩 있는지 확인을 해야한다.
    a, b = 1,1

    for i in range(s+1,len(arr_AB)):
      if arr_AB[i] == arr_AB[s]:
        a += 1
      else:
        break

    for i in range(e-1, -1, -1):
      if arr_CD[i] == arr_CD[e]:
        b += 1
      else:
        break
      
    cnt += a*b
    # 같은 숫자가 있는 만큼 포인터를 이동 시킨다. (연산횟수 감소)
    s += a
    e -= b
  else:
    e -=1
print(cnt)