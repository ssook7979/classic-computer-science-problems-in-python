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

    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)
    
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]
    
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)
    
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))
    
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))
    
    def edges_for_index(self, index:int) -> List[Edge]:
        return self._edges[index]
    
    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))
    
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc

from search.generic_search import bfs, Node, node_to_path

if __name__ == "__main__":
    city_graph: Graph[str] = Graph(["시애틀", "샌프란시스코", "로스앤젤레스", "리버사이드", "피닉스", 
                                    "시카고", "보스턴", "뉴욕", "애틀란타", "마이애미", "댈러스", "휴스톤",
                                    "디트로이트", "필라델피아", "워싱턴"])
    
    city_graph.add_edge_by_vertices("시애틀", "시카고")
    city_graph.add_edge_by_vertices("시애틀", "샌프란시스코")
    city_graph.add_edge_by_vertices("샌프란시스코", "리버사이드")
    city_graph.add_edge_by_vertices("샌프란시스코", "로스앤젤레스")
    city_graph.add_edge_by_vertices("로스앤젤레스", "리버사이드")
    city_graph.add_edge_by_vertices("로스앤젤레스", "피닉스")
    city_graph.add_edge_by_vertices("리버사이드", "피닉스")
    city_graph.add_edge_by_vertices("리버사이드", "시카고")
    city_graph.add_edge_by_vertices("피닉스", "댈러스")
    city_graph.add_edge_by_vertices("피닉스", "휴스톤")
    city_graph.add_edge_by_vertices("댈러스", "시카고")
    city_graph.add_edge_by_vertices("댈러스", "애틀란타")
    city_graph.add_edge_by_vertices("댈러스", "휴스톤")
    city_graph.add_edge_by_vertices("휴스톤", "애틀란타")
    city_graph.add_edge_by_vertices("휴스톤", "마이애미")
    city_graph.add_edge_by_vertices("마이애미", "워싱턴")
    city_graph.add_edge_by_vertices("시카고", "디트로이트")
    city_graph.add_edge_by_vertices("디트로이트", "보스턴")
    city_graph.add_edge_by_vertices("디트로이트", "워싱턴")
    city_graph.add_edge_by_vertices("디트로이트", "뉴욕")
    city_graph.add_edge_by_vertices("보스턴", "뉴욕")
    city_graph.add_edge_by_vertices("뉴욕", "필라델피아")
    city_graph.add_edge_by_vertices("필라델피아", "워싱턴")
    print(city_graph)

    bfs_result: Optional[Node[V]] = bfs("보스턴", lambda x: x == "마이애미", city_graph.neighbors_for_vertex)

    if bfs_result is None:
        print("Can't find answer with bfs")
    else:
        path: List[V] = node_to_path(bfs_result)
        print("The shortest path from Boston to Maiami: ")
        print(path)

import sys
sys.path.insert(0, '...')

from search.generic_search import bfs, Node, node_to_path

bfs_result = Optional[Node[V]] = bfs("보스턴", lambda x: x == "마이애미", city_graph.neighbors_for_vertex)
if bfs_result is None:
    print("너비 우선 탐색으로 답을 찾을 수 없습니다.")
else:
    path: List[V] = node_to_path(bfs_result)
    print("보스턴에서 마이애미까지 최단 경로: ")
    print(path)