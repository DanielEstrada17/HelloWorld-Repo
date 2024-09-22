upper = int(input('Enter uppper bound for a check: '))

#This should go up when it goes through loops
defic_count = 0
perf_count = 0
abund_count = 0

#This is the loop body
for num in range(1, upper + 1):
    divisors = 0
    for i in range(1, num):
        if num % i == 0:
            divisors += i
    if divisors < num:  #This will make the deficient count go up
        defic_count += 1
    elif divisors == num:   #This will make the perfect count go up
        perf_count += 1
    else:
        abund_count += 1    #This will make the abundant count go up

print(f"Between 1 and {upper} there are...")
print(f"Deficient numbers: {defic_count}")
print(f"Perfect numbers: {perf_count}")
print(f"Abundant numbers: {abund_count}")


