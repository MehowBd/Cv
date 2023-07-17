# Michał Badura, 407049

import graphs_2
import networkx as nx

from unittest import TestCase


class graph2_test(TestCase):

    def test_weight_sum(self):
        graph = nx.MultiDiGraph()
        graph.add_weighted_edges_from([(1, 2, 0.5), (2, 3, 0.4), (2, 3, 0.3), (1, 3, 1.0)])
        sum = 0
        for i in graphs_2.find_min_trail(graph,1,3):
            sum += i.Edge_Weight
        minimum = nx.dijkstra_path_length(graph, 1, 3)
        self.assertEqual(sum, minimum)
