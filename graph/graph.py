from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V')

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)
    
    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))
    
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1
    
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())
