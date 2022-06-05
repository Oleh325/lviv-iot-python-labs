from Model.LinkedListStack import Node, StackLinkedList

def main():
    node1 = Node(1, 2)
    node2 = Node(2, 3)
    node3 = Node(5, 4)
    node4 = Node(8, 7)
    node5 = Node(6, 9)
    stack = StackLinkedList()
    stack.add_node(node1)
    stack.add_node(node2)
    stack.add_node(node3)
    stack.add_node(node4)
    stack.add_node(node5)
    print("Stack: ")
    print(stack)
    print("After removing two nodes: ")
    stack.remove_node()
    stack.remove_node()
    print(stack)
    print("Adding two last nodes: ")
    print(stack.add())
    print("\nSearching for node 1 + 2*i: ")
    print(stack.find(1, 2))
    print("\nSearching for node 6 + 9*i: ")
    print(stack.find(6, 9))
    print("\nLast(top) node: ")
    stack.print_top()
    print("\nStack size: ")
    print(stack.size())

    

if __name__ == '__main__':
    main()