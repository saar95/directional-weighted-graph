import unittest

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def graph_algo_creator():
    graph = DiGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 3, 4)
    graph.add_edge(3, 2, 1)
    graph.add_edge(2, 4, 6)
    graph.add_edge(4, 2, 9)
    graph.add_edge(4, 1, 12)
    graph_algo = GraphAlgo(graph)
    return graph_algo

class MyTestCase(unittest.TestCase):

    def test_get_graph(self):
        ga=graph_algo_creator()
        self.assertEqual(True, False)

    def test_load_from_json(self):
        self.assertEqual(True, False)

    def test_save_to_json(self):
        self.assertEqual(True, False)

    def test_shortest_path(self):
        self.assertEqual(True, False)

    def test_connected_component(self):
        self.assertEqual(True, False)

    def test_connected_components(self):
        self.assertEqual(True, False)

    def test_plot_graph(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
