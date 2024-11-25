from typing import List, Tuple, Protocol

class Node:
    # Placeholder for the Node class, assuming it contains at least a name or position
    def __init__(self, name: str):
        self.name = name
    # Add any other attributes as necessary (like position if using Euclidean distance)

class IGraph(Protocol):
    def add_node(self, node: Node) -> None:
        """Adds a node to the graph."""
        pass

    def add_edge(self, start: Node, end: Node, weight: float) -> None:
        """Adds a weighted edge between two nodes."""
        pass

    def get_neighbors(self, node: Node) -> List[Tuple[Node, float]]:
        """Returns a list of neighbors and weights for a given node."""
        pass

class IHeuristicFunction(Protocol):
    def estimate(self, current: Node, goal: Node) -> float:
        """Returns the heuristic estimate from the current node to the goal."""
        pass

class IAStar(Protocol):
    def find_path(self, graph: IGraph, start: Node, goal: Node, heuristic: IHeuristicFunction) -> List[Node]:
        """Executes the A* algorithm to find the optimal path from start to goal."""
        pass

# Implementing stubs for the classes that will use these interfaces

class Graph(IGraph):
    def add_node(self, node: Node) -> None:
        pass

    def add_edge(self, start: Node, end: Node, weight: float) -> None:
        pass

    def get_neighbors(self, node: Node) -> List[Tuple[Node, float]]:
        return []

class HeuristicFunction(IHeuristicFunction):
    def estimate(self, current: Node, goal: Node) -> float:
        return 0.0

class AStar(IAStar):
    def find_path(self, graph: IGraph, start: Node, goal: Node, heuristic: IHeuristicFunction) -> List[Node]:
        return []

# Additional utility classes and methods might be implemented later, as needed.
