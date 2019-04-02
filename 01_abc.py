# 如果 a+b+c=N 且 a^2+b^2=c^2（a，b，c为自然数），如何求出所有a、b、c的组合？

# a
# b
# c
# c = 1000-a-b

import time

start_time = time.time()
for a in range(0, 2001):
	for b in range(0, 2001):
		for c in range(0, 2001):
			if a+b+c == 1000 and a**2 + b**2 == c**2
				print "a, b, c:%d, %d, %d" % (a, b, c)
				print "a, b, c:%d, %d, %d" % (a, b, c)
				
# 顺序
# 条件
# 循环


# T = 1000 * 1000 * 1000 * 2
# T = 2000 * 2000 * 2000 * 2
# T = N * N * N * 2

# T(n) = n^3 *2
# T(n) = n^3 * 10

# T(n) = g(n)
# g(n) = n^3


for a in range(0, n):
	for b in range(0, n):
		c = 1000 - a - b 
		if a**2 + b**2 = c**2:
			print "a, b, c: %d, %d, %d" % (a, b, c)

T(n) = n * n * (1 + max(1, 0))
	 = n^2 * 2
	 = O(n^2)
	 
