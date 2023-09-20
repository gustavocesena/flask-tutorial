class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def push(self, val):
        new_node = Node(val)
        head = self
        while head.next:
            head = head.next
        head.next = new_node

    def print_nodes(self):
        head = self
        while head:
            print(head)
            head = head.next

    def add_nodes_by_list(self, list_of_nodes: list):
        new_node = Node(list_of_nodes[0])
        for val in list_of_nodes[1::]:
            new_node.push(val)
        return new_node


l = Node(8)

new_node = l.add_nodes_by_list([8, 0, 7])
new_node.print_nodes()
