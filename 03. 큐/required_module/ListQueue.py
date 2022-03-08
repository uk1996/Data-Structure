class ListQueue:
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, x):
        self.__queue.append(x)
    
    def dequeue(self):
        return self.__queue.pop(0)
    
    def front(self):
        return self.__queue[0]
    
    def isEmpty(self):
        return len(self.__queue) == 0
    
    def dequeueAll(self):
        self.__queue.clear()
    
    def printQueue(self):
        print('Queue from front:', end = ' ')
        for value in self.__queue:
            print(value, end = ' ')
        print()