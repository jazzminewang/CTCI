#3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time. 

class MinStack:

    def __init__(self):
        self.numstacks = 1
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize
        self.minvals = [sys.maxint] * (stacksize * self.numstacks)

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is Full')
        self.sizes[stacknum] += 1
        if self.IsEmpty(stacknum):
            self.minvals[self.IndexOfTop(stacknum)] = item
        else:
            self.minvals[self.IndexOfTop(stacknum)] = min(
                item, self.minvals[self.IndexOfTop(stacknum) - 1])
        self.array[self.IndexOfTop(stacknum)] = item
    
    def Pop(self, stacknum): 
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)]
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def Min(self, stacknum):
        return self.minvals[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1