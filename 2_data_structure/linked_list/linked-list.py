# my LinkedList on Python

# Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

# Linkedlist class
class Linkedlist(object):
    def __init__(self, head = None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while(item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def delete_at(self, id):
        if id > self.count - 1:
            return
        if id == 0:
            self.head = self.head.next()
        else:
            idTmp = 0
            node = self.head
            while idTmp < id-1:
                node = node.get_next()
                idTmp += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

# create a new linkedlist with new data
itemlist = Linkedlist()
itemlist.insert(30)
itemlist.insert(40)
itemlist.insert(10)
itemlist.insert(15)
itemlist.dump_list()

# test get and find in the linkedlist
# print("Item count: ", itemlist.get_count())
# print("Finding item: ", itemlist.find(13))
# print("Finding item: ", itemlist.find(26))

# test delete from the linkedlist
itemlist.delete_at(3)
print("Item count: ", itemlist.get_count())
print("Find item: ", itemlist.find(30))
itemlist.dump_list()


