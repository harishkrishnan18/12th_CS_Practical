num = []
for i in range(1, 11):
    num.append(i)
print("Numbers from 1 to 10...\n", num)
for j, i in enumerate(num):
    if(i%2 == 1):
        del num[j]
print("The values after removed odd numbers...\n", num)
