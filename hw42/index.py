from node import Node

class UnsortedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    # add item to the start of the list   
    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    # add item to the end of the list
    def append(self, item):
        if self.is_empty():
            self.add(item)

        else:
            current = self._head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(Node(item))

    # add item to a specific position
    def insert(self, item, position):
        new_item = Node(item)
        current_node = self._head
        current_position = 0

        if current_position == position:
            self.add(item)
        else:
            while(current_node != None and current_position+1 != position):
                current_position = current_position+1
                current_node = current_node.get_next()
 
            if current_node != None:
                new_item.set_next(current_node.get_next())
                current_node.set_next(new_item)
            else:
                pass

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    # remove item from the end of the list
    def pop(self):
        if self.is_empty():
            return None
        
        current = self._head
        previous = None
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        if previous is None:
            self._head = None
        else:
            previous.set_next(None)
        return current.get_data()

    # return item index or -1 if items doesn't exist in list
    def index(self, item):
        current = self._head
        index = 0
        while current is not None:
            if current.get_data() == item:
                return index
            current = current.get_next()
            index += 1
        return -1

    def slice(self, start, stop):
        new_list = UnsortedList()
        current = self._head
        index = 0
        while current is not None and index < stop:
            if index >= start:
                new_list.append(current.get_data())
            current = current.get_next()
            index += 1
        return new_list

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    
if __name__ == "__main__":
    my_list = UnsortedList()

    my_list.add(31)
    my_list.add(54)
    my_list.add(10)
    my_list.add(15)

    my_list.append(9)
    my_list.insert(6, 1)
    my_list.remove(31)

    my_list.pop()

    # print(my_list.index(54))

    print(my_list)
    print(my_list.slice(1,3))
