import random

a = [random.randrange(0,101) for x in range(random.randrange(3, 21))]
b = [random.randrange(0,101) for x in range(random.randrange(3, 21))]

print("Elements in 'a': %s " % (str(a)))
print("Elements in 'b': %s " % (str(b)))

c = [x for x in a if x in b]
print("Elements in both (c): %s" % (str(c)))