odd = set([x*2+1 for x in range(0, 5)])
primes = set()
for i in range(2, 10):
    for num in range(0, 11):
        if num > 1:
            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                primes.add(num)
print("Odd:", odd)
print("Prime:", primes)
print("Union:", odd.union(primes))
print("Intersection:", odd.intersection(primes))
print("Difference:", odd.difference(primes))
print("Symmetric Difference:", odd.symmetric_difference(primes))
