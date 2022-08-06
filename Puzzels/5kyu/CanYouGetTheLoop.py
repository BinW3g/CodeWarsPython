# codewars challenge link
# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863

def loop_size(node):
    if node.next == node:
        return 1
    nodes = list()
    while node.next not in nodes:
        nodes.append(node)
        node = node.next
    first_node_of_loop = nodes.index(node.next) - 1
    return len(nodes) - first_node_of_loop


class Node:
    next = None


if __name__ == '__main__':
    node1 = Node()
    node1.next = node1
    print(loop_size(node1) == 1)

    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(loop_size(node1) == 3)

    nodes = [Node() for _ in range(0, 50)]
    for node, next_node in zip(nodes, nodes[1:]):
        node.next = next_node
    nodes[49].next = nodes[21]
    print(loop_size(nodes[0]) == 29)
