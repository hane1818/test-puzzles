def combination(n, m):
	table = [[0 for i in range(m)] for j in range(n)]
	for i in range(0, n):
		for j in range(0, m):
			if j == 0:
				table[i][j] = i+1
			elif i == j:
				table[i][j] = 1
			else:
				table[i][j] = table[i-1][j] + table[i-1][j-1]

	return table[n-1][m-1]

def main():
	print("C(40,10) =",combination(40, 10))
	print("C(990,33) =",combination(990, 33))

if __name__ == '__main__':
	main()