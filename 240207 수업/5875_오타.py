import sys
input = sys.stdin.readline

S = input().rstrip()
answer = 0
n = len(S)
arr = [0] * n

for i in range(n):
    if S[i] == '(':
        arr[i] = 1
    else:
        arr[i] = -1
        
prefix = arr.copy()
suffix = arr.copy()

for i in range(1, n):
    prefix[i] += prefix[i-1]

for i in range(n-1,0,-1):
    suffix[i-1] += suffix[i]

# 닫는 괄호가 더 많을 경우
if prefix[-1] == -2:
    for i in range(n):
        # 닫는 괄호마다 +1
        if S[i] == ')':
            answer += 1
        # 처음으로 여는 괄호가 많아지는 지점에서 수정이 불가
        if prefix[i] == -1:
            break
        
# 여는 괄호가 더 많을 경우
elif prefix[-1] == 2: 
    for i in range(n-1,0,-1):
        # 여는 괄호마다 +1
        if S[i] == '(':
            answer += 1
        # 처음으로 닫는 괄호가 많아지는 지점에서 수정이 불가
        if suffix[i] == 1:
            break

print(answer)
