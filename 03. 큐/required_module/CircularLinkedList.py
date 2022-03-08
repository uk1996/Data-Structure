class ListNode:
    def __init__(self, newItem, nextNode:'ListNode'):
        self.item = newItem
        self.next = nextNode

class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode('dummy', None)
        self.__tail.next = self.__tail
        self.__numItems = 0
    
    # newItem을 i번째 자리에 삽입하는 메서드
    def insert(self, i:int, newItem):
        if (i >= 0) and (i <= self.__numItems):
            prev = self.getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            if i == self.__numItems:
                self.__tail = newNode
            self.__numItems += 1
        else:
            raise Exception(f"index {i} is out of range")

    # 연결 리스트의 끝에 원소 newItem을 추가하는 메서드
    def append(self, newItem):
        newNode = ListNode(newItem, self.__tail.next)
        self.__tail.next = newNode
        self.__tail = newNode
        self.__numItems += 1
    
    # i번째 노드를 삭제하는 메서드
    def pop(self, *args): # *args: 가변 파라미터. 인자가 없거나 -1이면 마지막 원소로 처리하기 위함
        if self.isEmpty():
            raise Exception(f"linked list is empty")
 
        if len(args) != 0:
            i = args[0]
        if (len(args) == 0) or (i == -1):
            i = self.__numItems - 1
        if (i >= 0) and (i <= self.__numItems -1):
            prev = self.getNode(i-1)
            retItem = prev.next.item
            prev.next = prev.next.next
            if i == self.__numItems - 1:
                self.__tail = prev
            self.__numItems -= 1
            return retItem
        else:
            raise Exception(f"index {i} is out of range")

    
    # 원소 x를 삭제 하는 메서드
    def remove(self, x):
        (prev, curr) = self. __findNode(x)
        if curr != None:
            prev.next = curr.next
            if curr == self.__tail:
                self.tail = prev
            self.__numItems -= 1
        else:
            raise Exception('There is no value to find.')

    # 연결 리스트가 빈 리스트인지 알려주는 메서드
    def isEmpty(self):
        return self.__numItems == 0

    # i번째 원소를 알려주는 메서드
    def get(self, *args):
        if self.isEmpty():
            raise Exception(f"linked list is empty")
        
        if len(args) != 0:
            i = args[0]
        if (len(args) == 0) or (i == -1):
            i = self.__numItems - 1
        if (i >= 0) and (i <= self.__numItems - 1):
            return self.getNode(i).item
        else:
            raise Exception(f"index {i} is out of range")
    
    # 원소 x가 리트의 몇번째 원소인지를 알려주는 메서드
    def index(self, x):
        cnt = 0
        for element in self:
            if element == x:
                return cnt
            cnt += 1
        raise Exception('There is no value to find.')

    # 원소의 수(리스트의 길이)를 리턴하는 메서드
    def size(self) ->int:
        return self.__numItems

    # 모든 원소를 지우는 메서드
    def clear(self):
        self.__tail = ListNode('dummy', None)
        self.__tail.next = self.__tail
        self.__numItems = 0
    
    # 원소 x가 몇번 나오는지 세는 메서드
    def count(self, x):
        cnt = 0
        for element in self:
            if element == x:
                cnt += 1
        return cnt
    
    # 연결 리스트 뒤에 순회 가능한 객체 붙이는 메서드
    def extend(self, a): # a는 순회 가능한 객체
        for element in a:
            self.append(element)
    
    # 연결 리스트를 복사하고 리턴하는 메서드
    def copy(self):
        a = CircularLinkedList()
        for element in self:
            a.append(element)
        return a
    
    # 연결 리스트의 순서를 역으로 뒤집는 메서드
    def reverse(self):
        __head = self.__tail.next # 더미 헤드
        prev = __head; curr = prev.next; next = curr.next
        __head.next = self.__tail; self.__tail = curr
        for _ in range(self.__numItems):
            curr.next = prev
            prev = curr; curr = next; next = next.next
        

    # 원소를 정렬해주는 메서드(파이썬 내장 리스트로 복사해서 정렬한 다음 다시 연결 리스트로 만들어준다.)
    def sort(self):
        a = []
        for element in self:
            a.append(element)
        a.sort()
        self.clear()
        self.extend(a)

    
    # 연결 리스트의 i번 노드를 알려주는 메서드
    def getNode(self, i:int) -> ListNode:
        curr = self.__tail.next # 더미 헤드
        for _ in range(i+1):
            curr = curr.next
        return curr
    
    # 원소 x를 가진 첫번째 노드와 그직전 노드를 찾아주는 메서드
    def __findNode(self, x):
        __head = prev = self.__tail.next
        curr = prev.next
        while curr != __head:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr; curr = curr.next 
        return (None, None)

    # 연결 리스트의 모든 원소를 순서대로 보여주는 메서드
    def printList(self):
        for element in self:
            print(element, end = ' ')
    
    def __iter__(self):
        return CircularLinkedListIterator(self)

class CircularLinkedListIterator:
    def __init__(self, alist):
        self.__head  = alist.getNode(-1) # 더미 헤드
        self.iterPosition = self.__head.next # 0번 노드
    
    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item