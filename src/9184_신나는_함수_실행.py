import sys
input = sys.stdin.readline
arr = [[[0 for _ in range(21)] for _ in range(21)]for _ in range(21)]
for i in range(0, 21):
	for j in range(0, 21):
		for k in range(0, 21):
			if i == 0 or j == 0 or k == 0:
				arr[i][j][k] = 1
			elif i < j < k:
				arr[i][j][k] = arr[i][j][k-1] + arr[i][j-1][k-1] - arr[i][j-1][k]
			else:
				arr[i][j][k] = arr[i-1][j][k] + arr[i-1][j-1][k] + arr[i-1][j][k-1] - arr[i-1][j-1][k-1]
while (True):
	a, b, c = map(int, input().rstrip().split())
	res = 0
	if a == -1 and b == -1 and c == -1:
		break
	elif a <= 0 or b <= 0 or c <= 0:
		print("w(%d, %d, %d) = %d"%(a, b, c, 1))
	elif a > 20 or b > 20 or c > 20:
		print("w(%d, %d, %d) = %d"%(a, b, c, arr[20][20][20]))
	else:
		print("w(%d, %d, %d) = %d"%(a, b, c, arr[a][b][c]))