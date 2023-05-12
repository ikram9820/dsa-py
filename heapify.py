
class Heap:
    @classmethod
    
    def heapify(cls,array):
        cls.array = array
        lastparentIndex = len(array)//2-1
        for i in range(lastparentIndex,-1,-1):
            cls.doheapify(i)


    @classmethod
    def doheapify(cls,index):
        largerIndex=index
        leftIndex = index*2+1
        if leftIndex<len(cls.array) and \
        cls.array[leftIndex]>cls.array[largerIndex]:
            largerIndex = leftIndex
        rightIndex = index*2+2
        if rightIndex<len(cls.array) and \
        cls.array[rightIndex]>cls.array[largerIndex]:
            largerIndex = rightIndex
        
        if index == largerIndex: return 
        cls.swap(index,largerIndex)
        cls.doheapify(largerIndex)

    @classmethod
    def swap(cls,first,second):
        cls.array[first],cls.array[second] = cls.array[second],cls.array[first]


if __name__ == '__main__':
    array = [3,1,6,3,7,2,8,9,5,1]
    Heap.heapify(array)
    print(array)



