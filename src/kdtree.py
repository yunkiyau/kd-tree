import random
import time

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

    @staticmethod
    def _distance_squared(p1, p2):
        return sum((a - b) ** 2 for a, b in zip(p1, p2))

    def _validate_point(self, point):
        if len(point) != self.k:
            raise ValueError(f"Expected point of dimension {self.k}, got {len(point)}")

    def insert(self, point):
        self._validate_point(point)

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

    def search(self, point):
        self._validate_point(point)
        return self._search_recursive(self.root, point)

    def _search_recursive(self, node, point):
        if node is None:
            return False

        if node.point == point:
            return True

        axis = node.axis

        if point[axis] < node.point[axis]:
            return self._search_recursive(node.left, point)
        else:
            return self._search_recursive(node.right, point)

    def nearest_neighbour(self, target):
        self._validate_point(target)

        if self.root is None:
            return None

        best = {"point": None, "dist": float("inf")}
        self._nn_recursive(self.root, target, best)
        return best["point"]

    def _nn_recursive(self, node, target, best):
        if node is None:
            return

        dist = self._distance_squared(node.point, target)

        if dist < best["dist"]:
            best["point"] = node.point
            best["dist"] = dist

        axis = node.axis

        if target[axis] < node.point[axis]:
            good_side = node.left
            bad_side = node.right
        else:
            good_side = node.right
            bad_side = node.left

        self._nn_recursive(good_side, target, best)

        axis_dist = (target[axis] - node.point[axis]) ** 2
        if axis_dist < best["dist"]:
            self._nn_recursive(bad_side, target, best)
    
    @staticmethod
    def brute_force_nearest(points, target):
        best_point = None
        best_dist = float("inf")

        for p in points:
            dist = KDTree._distance_squared(p, target)
            if dist < best_dist:
                best_point = p
                best_dist = dist

        return best_point



