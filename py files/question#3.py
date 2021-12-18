# Question 3:
# create an XorGate class

class XorGate:
    num_inputs = 5
    
    def output(self, inputVector):
        ans = int(inputVector[0])
        if ans not in [0, 1]:
            raise ValueError('Input must be a binary number')
        for i in inputVector[1:]:
            if ans not in [0, 1]:
                raise ValueError('Input must be a binary number')
            ans = ans ^ int(i)
        return ans

if __name__ == '__main__':
    x = XorGate()
    print(x.output('10010'))