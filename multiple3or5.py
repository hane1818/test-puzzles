def multi3or5(limit):
	return [i for i in range(limit) if i%3 == 0 or i%5 == 0]

def main():
	print(sum(multi3or5(1000)))

if __name__ == '__main__':
	main()