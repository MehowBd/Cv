#!/usr/bin/python
# -*- coding: utf-8 -*-

# Michał Badura, 407049

from typing import List, Dict, Set, NamedTuple
import networkx as nx


VertexID = int

AdjList = Dict[VertexID, List[VertexID]]

Distance = int

EdgeID = int


def neighbors(adjlist: AdjList, start_vertex_id: VertexID, max_distance: Distance) -> Set[VertexID]:
    color = {}
    current_distance = 0

    for i in range(1,max(adjlist)+1):
        color[i] = 'white'
    color[start_vertex_id] = 'grey'
    queue = []
    queue.append([start_vertex_id, current_distance])

    while queue:
        u,distance = queue.pop(0)
        if distance > max_distance:
          neighbor = [key for key, value in color.items() if value == 'black' and key != start_vertex_id]
          return set(neighbor)
        if u not in adjlist.keys():
            color[u] = 'black'
        else:
          for v in adjlist[u]:
            if color[v] == 'white' and v in color.keys():
                color[v] = 'grey'
                queue.append([v,distance+1])
        color[u] = 'black'
    neighbor = [key for key, value in color.items() if value == 'black' and key != start_vertex_id]
    return set(neighbor)

class TrailSegmentEntry(NamedTuple):
    Start_Vertex: VertexID
    End_Vertex: VertexID
    Edge: EdgeID
    Edge_Weight: float


Trail = List[TrailSegmentEntry]


def load_multigraph_from_file(filepath: str) -> nx.MultiDiGraph:
    """Stwórz multigraf na podstawie danych o krawędziach wczytanych z pliku.

    :param filepath: względna ścieżka do pliku (wraz z rozszerzeniem)
    :return: multigraf
    """
    multigraf = nx.MultiDiGraph()

    with open(filepath) as data:
        graf = [line.strip() for line in data if line.strip()]

        for line in graf:
            line = line.split(" ")
            line[0], line[1], line[2] = int(line[0]), int(line[1]), float(line[2])
            multigraf.add_weighted_edges_from([(line[0], line[1], line[2])])


    return multigraf

def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    """Znajdź najkrótszą ścieżkę w grafie pomiędzy zadanymi wierzchołkami.

    :param g: graf
    :param v_start: wierzchołek początkowy
    :param v_end: wierzchołek końcowy
    :return: najkrótsza ścieżka
    """
    path = nx.dijkstra_path(g, v_start, v_end)
    edges = []
    dc = {}
    for i in range(1,len(path)):
        for arg in dict(g[i][i+1]):
            dc[arg] = g[i][i+1][arg]['weight']
        edges.append(TrailSegmentEntry(Start_Vertex = i, End_Vertex = i+1, Edge = min(dc, key = dc.get), Edge_Weight = dc[min(dc, key = dc.get)]))

    return edges



def trail_to_str(trail: Trail) -> str:
    """Wyznacz reprezentację tekstową ścieżki.

    :param trail: ścieżka
    :return: reprezentacja tekstowa ścieżki
    """
    sum = 0
    str = ""
    for i in trail:
        sum += i.Edge_Weight
    for el in trail:
        if el == trail[0]:
            str += '{} -[{}: {}]-> {}'.format(el.Start_Vertex, el.Edge, el.Edge_Weight, el.End_Vertex)
        elif el == trail[-1]:
            str += ' -[{}: {}]-> {}  (total = {})'.format(el.Edge, el.Edge_Weight, el.End_Vertex, sum)
        else:
            str += ' -[{}: {}]-> {}'.format(el.Start_Vertex, el.Edge, el.Edge_Weight, el.End_Vertex)
    return str
