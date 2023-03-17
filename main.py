class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __get_obj_in_linken_list(self, indx):
        obj = self.head
        count = 0
        while obj and count < indx:
            obj = obj.next
            count += 1
        return obj

    def add_obj(self, obj):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def remove_obj(self, indx):
        obj = self.__get_obj_in_linken_list(indx)

        if obj is None:
            return

        prev_obj, next_obj = obj.prev, obj.next
        if prev_obj:
            prev_obj.next = next_obj
        if next_obj:
            next_obj.prev = prev_obj

        if self.head == obj:
            self.head = next_obj
        if self.tail == obj:
            self.tail = prev_obj

    def __len__(self):
        n = 0
        h = self.head

        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, num, *args, **kwargs):
        obj = self.__get_obj_in_linken_list(num)
        return obj.data if obj else None

class ObjList:
    def __init__(self, data):
        self.__data = ''
        self.data = data
        self.__next = self.__prev = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, val):
        #if val in (ObjList, type(None)):
        self.__next = val

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, val):
        #if val in (ObjList, type(None)):
        self.__prev = val

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, val):
        #if type(val) == str:
        self.__data = val