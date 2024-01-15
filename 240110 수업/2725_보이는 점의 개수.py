'''
(0,0)에서 (x,y)까지 보이는 점의 개수
(0,1) (1,0) (1,1) (1,2) (2,1) (1,2) (1,3) (3,1) (4,1) (1,4) (3,4) (4,3) 
=> 기울기에 중복이 없어야한다.
'''
import sys
input = sys.stdin.readline
def get_gcd(a,b):
    if b == 0:
        return a
    while a%b !=0:
        a, b = b, a%b
    return b

C = int(input())
arr = [0 for _ in range(1001)]
# N이 최소 1이기 때문에 (0,0)에서 1을 볼때 최소 3개의 점을 볼 수 있다. (1,0) (0,1) (1,1)
arr[1] = 3

for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        # 기울기가 1인건 이미 처리 했음.
        if i == j:
            continue
        # 최대 공약수가 1인 친구들을 찾으면 된다.
        if get_gcd(i, j) == 1:
            cnt += 2
    arr[i] = arr[i-1] + cnt
for _ in range(C):
    print(arr[int(input())])

