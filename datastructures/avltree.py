from __future__ import annotations
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
        return f'{"\n".join([f'{desc} {"".join(str(trav))}' for desc, trav in zip(descriptions, traversals)])}\n\n{str(self)}' 
 

    def insert(self, key: K, value: V) -> None:
        raise NotImplementedError
    
    def search(self, key: K) -> V | None:
        raise NotImplementedError

    def delete(self, key: K) -> None:
        raise NotImplementedError

    def inorder(self, visit: Callable[[V], None] | None=None) -> List[K]:
        raise NotImplementedError

    def preorder(self, visit: Callable[[V], None]| None=None) -> List[K]:
        raise NotImplementedError

    def postorder(self, visit: Callable[[V], None]| None=None) -> List[K]:
        raise NotImplementedError

    def bforder(self, visit: Callable[[V], None]| None=None) -> List[K]:
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError
    
    #potential helper function
    #def _balance_factor(node: AVLNode) -> int: return _height(node.left) - _height(node.right)

    def _balance_tree(self, node: AVLNode) -> AVLNode:
        raise NotImplementedError
        # LL:
        #   do a right rotation on node, 
        #   then return node
        # RR:
        #   do a left rotation on node,
        #   then return node
        # LR: 
        #   do a left rotation on node.left
        #   do a right rotation on node
        #   then return node
        # RL:
        #   do a right rotation on node.right
        #   do a left rotation on node
        #   then return node

        # Else: 
        #   no rotations needed! 
        #   just return the node
    # def _rotate_left(self, node: AVLNode) -> AVLNode:
    # 	set new_root to node.right
    #   	set new_left_subtree to new_root.left
        
    #     set new_root.left to node
    #     set node.right to new_left_subtree
        
    #     then return new_root
      
 	# def _rotate_right(self, node: AVLNode) -> AVLNode:
    # 	...
