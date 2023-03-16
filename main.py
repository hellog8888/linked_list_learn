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
        if indx == 0:
            temp_obj = self.head.prev
            temp_obj.prev = None
            self.head = temp_obj

        temp_count = 0
        if indx > 1:
            link_obj = self.head.next
            while temp_count < indx:
                temp_count += 1
                link_obj = link_obj.next
            prev_obj = link_obj.prev
            prev_obj.next = link_obj.next
            next_obj = link_obj.next
            next_obj.prev = link_obj.prev
            link_obj.next = None
            link_obj.prev = None

    def __len__(self):
        count = 1

        if self.head is None:
            return 0

        link_obj = self.head.next
        while link_obj is not self.tail:
            count += 1
            link_obj = link_obj.next

        return count

    def __call__(self, num, *args, **kwargs):
        count = 0

        if num == 0:
            return self.head.data

        if num == 1:
            return self.head.next.data

        if num > 1:
            link_obj = self.head.next
            while link_obj is not self.tail:
                count += 1
                link_obj = link_obj.next

            return link_obj.data


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