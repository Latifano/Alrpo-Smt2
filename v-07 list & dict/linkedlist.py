class SingleLInkedList:
    class Node:
        def __init__(self, elemen, link=None):
            self.element = elemen
            self.nextNode = link

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        result = " "
        pointer = self.head
        while pointer != None:
            result = result + str(pointer.element) + " "
            pointer = pointer.nextNode
        return result

    def add(self, element):
        newNode = self.Node(element)
        newNode.nextNode = self.head
        self.head = newNode
        self.size += 1

    def __len__(self):
        return self.size


def main():
    myList = SingleLInkedList()
    myList.add(10)
    myList.add(20)
    myList.add(30)
    print(str(myList))
    print(len(myList))


main()
