from collections import defaultdict

# Displays the probability of rolling a certain number with two dice
combo = defaultdict(int)
for i in range(1, 7):
	for j in range(1, 7):
		roll = i + j
		combo[roll] += 1

for n in range(2, 13):
	print("%d %.2f%%" % (n, combo[n] / 36.0))