class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def remove_obj(self, indx):
        temp_obj = self.head

        temp_count = 0
        while temp_obj and temp_count < indx:
            temp_obj = temp_obj.next
            temp_count += 1

        if temp_obj is None:
            return

        prev_obj, next_obj = temp_obj.prev, temp_obj.next
        if prev_obj:
            prev_obj.next = next_obj
        if next_obj:
            next_obj.prev = prev_obj

        if self.head == temp_obj:
            self.head = temp_obj
        if self.tail == temp_obj:
            self.tail = temp_obj

    def __len__(self):
        count = 0

        obj = self.head
        while obj:
            count += 1
            obj = obj.next

        return count

    def __call__(self, num, *args, **kwargs):
        count = 0
        obj = self.head

        while obj and count < num:
            print(obj.data)
            obj = obj.next
            print(obj.data)
            count += 1

        return obj.data # if link_obj else None

class ObjList:
    def __init__(self, data):
        self.__data = ''
        self.data = data
        self.__next = self.__prev = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if next in (ObjList, type(None)):
            self.__next = next

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        if prev in (ObjList, type(None)):
            self.__prev = prev

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) is str:
            self.__data = data


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
print(n)
print(s)