from dataclasses import dataclass
from typing import Any, Optional, Tuple, List
from __future__ import annotations

from datastructures.avltree import AVLTree

@dataclass
class IntervalNode:
    key: Tuple[int, int]
    value: Any
    left: Optional[IntervalNode] = None
    right: Optional[IntervalNode] = None
    height: int = 1
    max_end: int = 0
    intervals_at_low: AVLTree = AVLTree()  # Tracks overlapping intervals with the same low value

class IntervalTree:
    def __init__(self):
        self._tree = AVLTree()

    def insert(self, low: int, high: int, value: Any):
        # Check if there is already an interval node with this low value
        node: Optional[IntervalNode] = self._tree.search(low)

        if node:
            # Insert into the AVL tree that manages overlapping intervals
            node.intervals_at_low.insert(high, value)
        else:
            # Create a new interval node and insert it
            new_node = IntervalNode(key=(low, high), value=value, max_end=high)
            new_node.intervals_at_low.insert(high, value)
            self._tree.insert(low, new_node)

        # Update the max_end values up the tree
        self._update_max_end(self._tree._root)

    def delete(self, low: int, high: int):
        node: Optional[IntervalNode] = self._tree.search(low)

        if node:
            # Delete from the overlapping intervals AVL tree
            try:
                node.intervals_at_low.delete(high)
            except KeyError:
                raise KeyError(f"Interval ({low}, {high}) not found.")

            # If no intervals remain at this low value, remove the interval node itself
            if node.intervals_at_low.size() == 0:
                self._tree.delete(low)

        # Update the max_end values up the tree
        self._update_max_end(self._tree._root)

    def search(self, low: int, high: int) -> Optional[Any]:
        node: Optional[IntervalNode] = self._tree.search(low)
        
        if node:
            return node.intervals_at_low.search(high)
        return None

    def range_query(self, low: int, high: int) -> List[IntervalNode]:
        result = []
        self._range_query(self._tree._root, low, high, result)
        return result

    def _range_query(self, node: Optional[IntervalNode], low: int, high: int, result: List[IntervalNode]):
        if not node:
            return

        if node.key[0] <= high and node.max_end >= low:
            # Add matching intervals
            if low <= node.key[1] and high >= node.key[0]:
                result.append(node)

            # Traverse left and right children
            self._range_query(node.left, low, high, result)
            self._range_query(node.right, low, high, result)

    def top_k(self, k: int, ascending: bool = True) -> List[IntervalNode]:
        all_nodes = self._inorder(self._tree._root)
        sorted_nodes = sorted(all_nodes, key=lambda x: x.key[1], reverse=not ascending)
        return sorted_nodes[:k]

    def _inorder(self, node: Optional[IntervalNode]) -> List[IntervalNode]:
        if not node:
            return []
        return self._inorder(node.left) + [node] + self._inorder(node.right)

    def _update_max_end(self, node: Optional[IntervalNode]) -> int:
        if not node:
            return 0

        left_max = self._update_max_end(node.left)
        right_max = self._update_max_end(node.right)
        node.max_end = max(node.key[1], left_max, right_max)
        
        return node.max_end

