'''

'''
import sys
input = sys.stdin.readline
N = int(input())
S = input().rstrip()
modular = 10**9 + 7
arr = [0,0,0]
result = 0
for i in range(N):
    # 차례대로 돌면서 해당 알파벳의 갯수를 누적합
    if S[i] == 'W':
        arr[0] += 1
    elif S[i] == 'H':
        # 앞에 있는 W의 갯수만큼 더해준다.
        arr[1] += arr[0]
    elif S[i] == 'E':
        # E가 들어올때 마다 result에 더할 수 있는지 확인
        result += arr[2]
        # 뒤에 E가 또 붙을때 마다 두배씩 늘어나기 때문에 *2
        arr[2] *= 2
        # 한번 들어오면 +W의 갯수만큼
        arr[2] += arr[1]
result %= modular
print(result)