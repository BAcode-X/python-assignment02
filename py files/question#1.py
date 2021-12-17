# Question 1:
# A function that takes 2 tuples as arguments and returns a dictionary in which the keys are elements of the first tuple and the values are elements of the second tuple.

def combine(tup1, tup2):
    dic = dict(zip(tup1, tup2))
    return dic

if __name__ == '__main__':
    tup1 = ('a', 'b', 'c')
    tup2 = (1, 2, 3)
    print(combine(tup1, tup2))