class ListNode:
    def __init__(self, newItem, nextNode:'ListNode'):
        self.item = newItem
        self.next = nextNode

class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0
    
    # newItem을 i번째 자리에 삽입하는 메서드
    def insert(self, i:int, newItem):
        if (i >= 0) and (i <= self.__numItems):
            prev = self.__getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        else:
            raise Exception(f"index {i} is out of range")

    # 연결 리스트의 끝에 원소 newItem을 추가하는 메서드
    def append(self, newItem):
        prev = self.__getNode(self.__numItems - 1)
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1
    
    # i번째 노드를 삭제하는 메서드
    def pop(self, i:int):
        if (i >= 0) and (i <= self.__numItems-1):
            prev = self.__getNode(i-1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            self.__numItems -= 1
            return retItem
        else:
            raise Exception(f"index {i} is out of range")
    
    # 원소 x를 삭제 하는 메서드
    def remove(self, x):
        (prev, curr) = self. __findNode(x)
        if curr != None:
            prev.next = curr.next
            self.__numItems -= 1

    # 연결 리스트가 빈 리스트인지 알려주는 메서드
    def isEmpty(self):
        return self.__numItems == 0

    # i번째 원소를 알려주는 메서드
    def get(self, i):
        if self.isEmpty():
            raise Exception(f"linked list is empty")
        if (i >= 0) and (i <= self.__numItems - 1):
            return self.__getNode(i).item
        else:
            raise Exception(f"index {i} is out of range")
    
    # 원소 x가 리트의 몇번째 원소인지를 알려주는 메서드
    def index(self, x):
        curr = self.__head.next # 0번 노드: 더미 헤드 다음 노드
        for index in range(self.__numItems):
            if curr.item == x:
                return index
            else:
                curr = curr.next
        raise Exception('The element you want to find does not exist.')

    # 원소의 수(리스트의 길이)를 리턴하는 메서드
    def size(self) ->int:
        return self.__numItems

    # 모든 원소를 지우는 메서드
    def clear(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0
    
    # 원소 x가 몇번 나오는지 세는 메서드
    def count(self, x):
        cnt = 0
        curr = self.__head.next
        while curr != None:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        return cnt
    
    # 연결 리스트 뒤에 연결 리스트를 붙이는 메서드
    def extend(self, a): # a는 연결 리스트
        for index in range(a.size()):
            self.append(a.get(index))
    
    # 연결 리스트를 복사하고 리턴하는 메서드
    def copy(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a
    
    # 연결 리스트의 순서를 역으로 뒤집는 메서드
    def reverse(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.insert(0, self.get(index))
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))

    # 원소를 정렬해주는 메서드(파이썬 내장 리스트로 복사해서 정렬한 다음 다시 연결 리스트로 만들어준다.)
    def sort(self):
        curr = self.__head.next
        a = []
        while curr != None:
            a.append(curr.item)
            curr = curr.next
        a.sort()
        self.clear()
        for index in range(len(a)):
            self.append(a[index])

    
    # 연결 리스트의 i번 노드를 알려주는 메서드
    def __getNode(self, i:int) -> ListNode:
        curr = self.__head # 더미 헤드
        for index in range(i+1):
            curr = curr.next
        return curr
    
    # 원소 x를 가진 첫번째 노드와 그직전 노드를 찾아주는 메서드
    def __findNode(self, x):
        prev = self.__head
        curr = prev.next
        while curr != None:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr; curr = curr.next 
        return (None, None)

    # 연결 리스트의 모든 원소를 순서대로 보여주는 메서드
    def printList(self):
        curr = self.__head.next # 0번 노드
        while curr != None:
            print(curr.item, end=' ')
            curr = curr.next
    
    # i ~ j번 원소를 프린트 메서드
    def printInterval(self, i:int, j:int):
        if self.isEmpty():
            raise Exception(f"linked list is empty")
        
        if (i >= 0) and (i <= self.__numItems - 1) and (j >= 0) and (j <= self.__numItems - 1):
            interval = j-i
            curr = self.__getNode(i)
            print(curr.item, end=' ')
            for _ in range(interval):
                curr = curr.next
                print(curr.item, end=' ')
        elif i > j:
            raise Exception('j must be bigger than or equal to i.')
        else:
            raise Exception('index is out of range')