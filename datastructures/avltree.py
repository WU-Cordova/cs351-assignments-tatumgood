from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import Generic, Callable, List, Optional, Sequence, Tuple
from datastructures.iavltree import K, V, IAVLTree

#version 1
# class AVLNode(Generic[K, V]):
#     def __init__(self, key: K, value:V, left: Optional[AVLNode]=None, right: Optional[AVLNode]=None):
#         self._key = key 
#         self._value = value 
#         self._left = left
#         self._right = right
#         self._height = 1

#     @property
#     def key(self) -> K: return self._key

#     @key.setter
#     def key(self, new_key: K) -> None: self._key = new_key

#version 2
@dataclass
class AVLNode(Generic[K,V]):
    def __init__(self, key: K, value:V, left: Optional[AVLNode]=None, right: Optional[AVLNode]=None):
        self.key = key
        self.value = value 
        self.left = left
        self.right = right
        self._height = 1

# node = AVLNode(None, None)
# print (node.key)
# node.key = new_key

class AVLTree(IAVLTree[K,V], Generic[K, V]):
    def __init__(self, starting_sequence: Optional[Sequence[Tuple]]=None):
        self._root = None

        for key, value in starting_sequence or []:
            self.insert(key, value)

    def __str__(self) -> str:
        def draw_tree(node: Optional[AVLNode], level: int=0) -> None:
            if not node:
                return 
            draw_tree(node.right, level + 1)
            level_outputs.append(f'{" " * 4 * level} -> {str(node.value)}')
            draw_tree(node.left, level + 1)
        level_outputs: List[str] = []
        draw_tree(self._root)
        return '\n'.join(level_outputs)
    
    def __repr__(self) -> str:
        descriptions = ['Breadth First: ', 'In-order: ', 'Pre-order: ', 'Post-order: ']
        traversals = [self.bforder(), self.inorder(), self.preorder(), self.postorder()]
        return "".join([desc + " " + "".join(str(trav).replace("\\", "\\\\")) for desc, trav in zip(descriptions, traversals)]) + "\n\n" + str(self)
        #return f'{"\n".join([f" {desc} {"".join(str(trav).replace("\\", "\\\\"))}" for desc, trav in zip(descriptions, traversals)])}\n\n{str(self)}' 
        #return f'{"\n".join([f'{desc} {"".join(str(trav))}' for desc, trav in zip(descriptions, traversals)])}\n\n{str(self)}' 

    def insert(self, key: K, value: V) -> None:
        self._root = self._insert(self._root, key, value)
    
    def _insert(self, node: Optional[AVLNode], key: K, value: V) -> Optional[AVLNode]:
        if node is None:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value #if key already exists
            raise ValueError(f"Key {key} already exists in the tree.")

        node._height = 1 + max(self._height(node.left), self._height(node.right))

        return self._balance_tree(node)
    
    def search(self, key: K) -> V | None:
        return self._search(self._root, key)
    
    def _search(self, node: Optional[AVLNode], key: K) -> V | None:
        if node is None:
            return None
        elif key == node.key:
            return node.value
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key: K) -> None:
        self._root = self._delete(self._root, key)

    def _delete(self, node: Optional[AVLNode], key: K) -> Optional[AVLNode]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key) 

        else:  # Node found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node has two children: find the successor
            successor = self._find_successor(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self._delete(node.right, successor.key)

        # Update height and balance the tree
        node._height = 1 + max(self._height(node.left), self._height(node.right))
        return self._balance_tree(node)

    def _find_successor(self, node: AVLNode) -> AVLNode:
        if node.left is None:
            return node
        return self._find_successor(node.left)
    
    # def inorder(self, visit: Callable[[V], None] | None=None) -> List[K]:
    #     keys: List[K] = []
    #     stack = []
    #     node = self._root

    #     while node or stack:
    #         while node:
    #             stack.append(node)
    #             node = node.left

    #         node = stack.pop()
    #         keys.append(node.key)
    #         if visit:
    #             visit(node.value)
    #         node = node.right

    #     return keys

    def inorder(self, visit: Callable[[V], None] | None=None) -> List[K]:
        def _inorder(node: Optional [AVLNode])-> AVLNode:
            if not node:
                return
            _inorder(node.left)
            keys.append(node.key)
            if visit:
                visit(node.value)
            _inorder(node.right)
        
        keys: List[K] = []
        _inorder(self._root)
        return keys
    
    # def inorder(self, visit: Callable[[V], None] | None=None) -> List[K]:
    #     def _inorder(node: Optional[AVLNode]) -> None:
    #         if node:
    #             _inorder(node.left)
    #             keys.append(node.key)
    #             if visit:
    #                 visit(node.value)
    #             _inorder(node.right)

    #     keys: List[K] = []
    #     _inorder(self._root)
    #     return keys

    def preorder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        def _preorder(node: Optional[AVLNode]) -> None:
            if node:
                keys.append(node.key)
                if visit:
                    visit(node.value)
                _preorder(node.left)
                _preorder(node.right)

        keys: List[K] = []
        _preorder(self._root)
        return keys

    def postorder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        def _postorder(node: Optional[AVLNode]) -> None:
            if node:
                _postorder(node.left)
                _postorder(node.right)
                keys.append(node.key)
                if visit:
                    visit(node.value)

        keys: List[K] = []
        _postorder(self._root)
        return keys

    def bforder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        if not self._root:
            return []
        
        keys: List[K] = []
        queue = deque()
        queue.append(self._root)

        while queue:
            node = queue.popleft()
            keys.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if visit:
                visit(node.value)
        return keys

    def size(self) -> int:
        def _size(node: Optional[AVLNode]) -> int:
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self._root)
    
    def _height(self, node: Optional[AVLNode]) -> int:
        return node._height if node else 0 #was erroring for two days because I forgot a "_"
    #potential helper function

    def _balance_factor(self, node: AVLNode) -> int: 
        return self._height(node.left) - self._height(node.right)

    def _balance_tree(self, node: AVLNode) -> AVLNode:
        balance_factor = self._balance_factor(node)

        # LL: do a right rotation on node, then return node
        if balance_factor > 1 and self._balance_factor(node.left) >= 0:  
            return self._rotate_right(node)
        # RR: do a left rotation on node, then return node
        elif balance_factor < -1 and self._balance_factor(node.right) <= 0:  
            return self._rotate_left(node)
        # LR: do a left rotation on node.left, do a right rotation on node, then return node
        elif balance_factor > 1 and self._balance_factor(node.left) < 0:  
            # node.left = self._rotate_right(node.left)
            # return self._rotate_left(node)
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # RL: do a right rotation on node.right, do a left rotation on node,  then return node
        elif balance_factor < -1 and self._balance_factor(node.right) > 0:  
            # node.right = self._rotate_left(node.right)
            # return self._rotate_right(node)
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        
        # Else:  no rotations needed!  just return the node
        return node

    
    def _rotate_left(self, node: AVLNode) -> AVLNode:
        new_root = node.right
        new_left_subtree = new_root.left

        new_root.left = node
        node.right = new_left_subtree

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        new_root = node.left
        new_right_subtree = new_root.right

        new_root.right = node
        node.left = new_right_subtree

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root
