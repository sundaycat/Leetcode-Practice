#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#

# @lc code=start
from heapq import *

'''
We can use a Max Heap to store the numbers. Instead of comparing the numbers we will compare their frequencies so that the root of the heap is always the most frequently occurring number. There are two issues that need to be resolved though:

    1. How can we keep track of the frequencies of numbers in the heap? When we are pushing a new number to the Max Heap, we don’t know how many times the number has already appeared in the Max Heap. To resolve this, we will maintain a HashMap to store the current frequency of each number. Thus whenever we push a new number in the heap, we will increment its frequency in the HashMap and when we pop, we will decrement its frequency.
    2. If two numbers have the same frequency, we will need to return the number which was pushed later while popping. To resolve this, we need to attach a sequence number to every number to know which number came first.

In short, we will keep three things with every number that we push to the heap:

    1. number: value of the number
    2. frequency: current frequency of the number when it was pushed to the heap
    3. sequenceNumber: a sequence number, to know what number came first

'''
class Element:

    def __init__(self, val, freq, sequence):

        # value of the number
        self.val = val
        # current frequence of the number when it was pushed to the heap
        self.freq = freq
        # a sequence number, to indicate which number came first
        self.sequence = sequence
    
    def __lt__(self, other):
        '''
        Note, we apply maxheap, so all freq and seq is negative when they were pass to lt. so smaller in heap means larger in reality.

            1. if frequence is not equal, return true if current one has larger frequence().
            2. if frequence is equal, return the true if current one was pushed into heap later than other.
        '''
        if self.freq != other.freq:
            return self.freq < other.freq
        else:
            return self.sequence < other.sequence
    

class FreqStack:

    def __init__(self):
        
        self.sequence = 0
        self.maxHeap = []
        self.freqMap = {}

    def push(self, val: int) -> None:

        # increase the val in dict by one
        if val not in self.freqMap:
            self.freqMap[val] = 0
        self.freqMap[val] += 1
        
        # increase the current sequence
        self.sequence += 1

        # push (val, freq, sequence) vector into max heap
        element = Element(val, -self.freqMap[val], -self.sequence)
        heappush(self.maxHeap, element)

    def pop(self) -> int:
        
        val = heappop(self.maxHeap).val

        # decrement the frequence or remove if it's the last val
        if self.freqMap[val] > 1:
            self.freqMap[val] -= 1
        else:
            del self.freqMap[val]

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# @lc code=end


# 5, 7, 5, 7, 4, 5
freqStack = FreqStack();
freqStack.push(5) # The stack is [5]
freqStack.push(7) # The stack is [5,7]
freqStack.push(5) # The stack is [5,7,5]
freqStack.push(7) # The stack is [5,7,5,7]
freqStack.push(4) # The stack is [5,7,5,7,4]
freqStack.push(5) # The stack is [5,7,5,7,4,5]
print(freqStack.pop())   # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
print(freqStack.pop())   # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
print(freqStack.pop())   # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
print(freqStack.pop())   # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
