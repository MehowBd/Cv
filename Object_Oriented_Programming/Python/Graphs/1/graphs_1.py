# !/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Dict

def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    adjlist = {x + 1: [] for x in range(len(adjmat))}
    i = 1
    for row  in adjmat:
        for col in row:
            if col != 0:
                for j in range(0,col):
                    adjlist[i].append(row.index(col) + 1)
        i += 1

    for key in adjlist.copy():
        if adjlist[key] == []:
            del adjlist[key]
    return adjlist

def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    visited = []
    def dfs(G: Dict[int, List[int]], s: int, visited: List[int]):
        if s not in visited:
            visited.append(s)
            for node in G[s]:
                dfs(G, node, visited)
            return visited
    return dfs(G, s, visited)

def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    stack = []
    stack.append(s)
    visited = []
    while stack:
        s = stack.pop()
        if s not in visited:
            visited.append(s)
            for u in reversed(G[s]):
                stack.append(u)
    return visited

def dfs_acyclic(G: Dict[int, List[int]], s: int) -> List[int]:
    visited = []
    def dfs(G: Dict[int, List[int]], s: int, visited: List[int]):
        if s not in G:
            return False
        if s not in visited:
            visited.append(s)
        for node in G[s]:
            if node in visited or dfs(G, node, visited.copy()):
                return True
        return False
    return dfs(G, s, visited)

def is_acyclic(G: Dict[int, List[int]]) -> bool:
    acyclic = True
    for i in G.keys():
        if dfs_acyclic(G, i):
            acyclic = False
    return acyclic
