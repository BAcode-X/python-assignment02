# Question 2:
# write a function that can draw an arrow with asterisks

def drawPattern(n):
    for i in range(n):
        print(' '*(n-i-1)+'*'*(i*2+1))
    for i in range(n//2 + 1):
        print(' '*2 + '*'*n)

if __name__ == '__main__':
    drawPattern(5)