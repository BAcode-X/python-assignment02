# Question 4:
# list tuple of elements that give the sum

from itertools import combinations

def factorize(value, factors):
    ans = [i for i in combinations(range(1, 10), factors) if sum(i) == value]
    return ans

if __name__ == '__main__':
    print(factorize(13, 2))
    print(factorize(10, 3))
    print(factorize(25, 3))