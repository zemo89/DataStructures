class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def insert_from_tail(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.size += 1

    def add_in_lst(self):
        global x
        x = []
        current = self.head
        while current != None:
            x.append(str(current.data))
            current = current.next
        
    def convert_to_string(self):
        global s
        s = ''
        for i in x:
            s = s + i
        print(s)
class LinkedList1:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def insert_from_tail_first(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.size += 1

    def add_in_lst_first(self):
        global y
        y = []
        current = self.head
        while current != None:
            y.append(str(current.data))
            current = current.next
    def convert_to_string_first(self):
        global d
        d = ''
        for i in y:
            d = d + i
        print(d)
class Arithematic(LinkedList1):
    def add(self):
        print(int(s)+int(d))

l = LinkedList()
a = Arithematic()
l.insert_from_tail(9)
l.insert_from_tail(7)
l.add_in_lst()
a.insert_from_tail_first(7)
a.insert_from_tail_first(8)
l.convert_to_string()
a.add_in_lst_first()
a.convert_to_string_first()
a.add()
