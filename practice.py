n = int(input())
x = n
for i in range(2,n+1):
	if i * i > n:
		break
	if x == 1:
		break
	while x%i == 0:
		print(i)
		x//=i
# 루트 n보다 큰 소인수가 있다면 n에 아직 남아있기 때문에
if x != 1:
	print(x)
