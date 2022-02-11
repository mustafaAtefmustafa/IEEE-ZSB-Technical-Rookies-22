from turtle import pos


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, data, index):
        new_node = Node(data)
        # if the list is empty make the new node the head.
        if self.head is None:
            self.head = new_node
            return
        else:
            # Checking if the wanted element is outside of the list.
            if index > self.size_of() - 1:
                print("Please enter a valid index.")
                return

            # Inserting at the front.
            if index == 0:
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
            # Inserting at the end.
            elif index == self.size_of() - 1:
                last = self.head
                while(last.next):
                    last = last.next
                last.next = new_node

            else:
                # Inserting at certain index.
                temp = self.head
                for i in range(index - 1):
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node

    def delete_at_index(self, index):
        # if the list is empty do nothing.
        if self.head is None:
            return

        # Checking if the wanted element is outside of the list.
        if index > self.size_of() - 1:
            print("Please enter a valid index.")
            return

        # if the node is the head delete it.
        if index == 0:
            self.head = self.head.next
            return

        # if the node is somewhere in the list make the previous node point at the next node then delete the current.
        position = 0
        current = self.head
        previous = self.head
        temp = self.head
        while current is not None:
            if position == index:
                temp = current.next
                break
            previous = current
            current = current.next
            position += 1
        previous.next = temp
        return

    def count_occurrences(self, current, element):
        if current is None:
            return 0
        if current.data == element:
            return 1 + self.count_occurrences(current.next, element)
        else:
            return self.count_occurrences(current.next, element)

    def size_of(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    """Building the linkedlist"""
    l = LinkedList()
    l.head = Node(1)
    second = Node(2)
    third = Node(3)
    l.head.next = second
    second.next = third

    l.print_list()
    print(f" the size is {l.size_of()}")

    """Insertion."""
    l.insert_at_index(5, 2)
    l.insert_at_index(8, 2)
    l.insert_at_index(5, 2)
# 123  --> insert 5 -->  1235 --> insert 8 -->  12835  --> insert 5 at index 2 -->  125835

    print("The list after inserting 3 nodes is: ")
    l.print_list()
    print(f" the size is {l.size_of()}")

    """Deletion."""
    l.delete_at_index(4)
    print("The list after deleting the node at index 4 is:")
    l.print_list()
    print(f" the size is {l.size_of()}")
# 123  -->  1235 -->  12835  -->  125835  --> deletion of node 3 at index 4 --> 12585

    """Counting the occurrence."""
    print(f" the count is {l.count_occurrences(l.head, 5)}")
