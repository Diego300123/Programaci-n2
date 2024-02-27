def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes_in_list(primes):
    primes = []
    for num in list1:
        if is_prime(num):
            primes.append(num)
    return primes

def sum_and_avg(number_list):
    total = 0
    for numbers in number_list:
        total = total + numbers
    average = total / len(number_list)
    return total, average


list1 = [1,3,7,9,13,24,37,51]
primes = primes_in_list(list1)
print("The primes are: ", primes)
print(sum_and_avg(list1))