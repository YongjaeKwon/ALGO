'''
길이가 N인 수열 S가 있다.
원하는 위치에서 K번 삭제 가능
삭제한 배열중에서 짝수가 가장 긴 부분수열의 길이 구하기
'''
import sys
input = sys.stdin.readline

n,k = int(input().split())
arr = list(map(int,input().split()))

odd_cnt = 0
for i in range(k):