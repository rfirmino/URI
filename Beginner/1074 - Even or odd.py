n = int(input())
for i in range(n):
	x = int(input())
	if x == 0:
		print("NULL")
	elif x < 0:
		if x & 1:
			print("ODD NEGATIVE")
		else:
			print("EVEN NEGATIVE")
	elif x > 0:
		if x & 1:
			print("ODD POSITIVE")
		else:
			print("EVEN POSITIVE")
