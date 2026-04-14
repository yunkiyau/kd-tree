class KDNode:
    def __init__(self, point, axis):
        self.point = point
        self.axis = axis
        self.left = None
        self.right = None


class KDTree:
    def __init__(self, k):
        self.k = k
        self.root = None

    def insert(self, point):
        if self.root is None:
            self.root = KDNode(point, 0)
            return

        self._insert_recursive(self.root, point)

    def _insert_recursive(self, node, point):
        axis = node.axis

        if point[axis] < node.point[axis]:
            if node.left is None:
                next_axis = (axis + 1) % self.k
                node.left = KDNode(point, next_axis)
            else:
                self._insert_recursive(node.left, point)
        else:
            if node.right is None:
                next_axis = (axis + 1) % self.k
                node.right = KDNode(point, next_axis)
            else:
                self._insert_recursive(node.right, point)


if __name__ == "__main__":
    tree = KDTree(2)

    tree.insert((0, 0))
    tree.insert((1, 2))
    tree.insert((2, 0))
    tree.insert((2, 3))
    tree.insert((3, 2))

    print(tree.root.point)
    print(tree.root.right.point)