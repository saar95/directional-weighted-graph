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
        ga = graph_algo_creator()
        self.assertEqual(5, ga.get_graph().v_size())
        self.assertEqual(6, ga.get_graph().e_size())
        graph = DiGraph()
        test_graph = GraphAlgo(graph)
        self.assertEqual(0, test_graph.get_graph().v_size())
        self.assertEqual(0, test_graph.get_graph().e_size())
        test_graph = ga.get_graph()
        self.assertEqual(5, test_graph.v_size())
        self.assertEqual(6, test_graph.e_size())
        ga.get_graph().remove_node(1)
        self.assertEqual(4, ga.get_graph().v_size())
        test_graph = ga.get_graph()
        self.assertEqual(4, test_graph.v_size())

    def test_load_from_json(self):
        ga = graph_algo_creator()
        ga.save_to_json('../Test/load_test')
        ga1 = DiGraph()
        dwga_test = GraphAlgo(ga1)
        self.assertNotEqual(dwga_test.get_graph().get_mc(), ga.get_graph().get_mc())
        self.assertNotEqual(dwga_test.get_graph().v_size(), ga.get_graph().v_size())
        self.assertNotEqual(dwga_test.get_graph().e_size(), ga.get_graph().e_size())
        dwga_test.load_from_json('../Test/load_test')
        self.assertEqual(dwga_test.get_graph().get_mc(), ga.get_graph().get_mc())
        self.assertEqual(dwga_test.get_graph().v_size(), ga.get_graph().v_size())
        self.assertEqual(dwga_test.get_graph().e_size(), ga.get_graph().e_size())
        ga_dict = ga.get_graph().all_in_edges_of_node(2)
        dwga_dict = dwga_test.get_graph().all_in_edges_of_node(2)
        for temp in ga_dict:
            self.assertEqual(ga_dict[temp], dwga_dict[temp])

    def test_save_to_json(self):
        ga = graph_algo_creator()
        self.assertTrue(ga.save_to_json('../Test/save_test'))

    def test_shortest_path(self):
        dwga = GraphAlgo()
        dwga.load_from_json('../data/A5')
        dist, path_list = dwga.shortest_path(47, 19)
        self.assertEqual(17.693921758901507, dist)
        check_list = [47, 46, 44, 43, 42, 41, 40, 39, 15, 16, 17, 18, 19]
        for check in path_list:
            self.assertEqual(check_list.pop(0), check)
        dwga.get_graph().add_edge(47, 15, 2)
        dist, path_list = dwga.shortest_path(47, 19)
        self.assertEqual(8.000357917488648, dist)
        check_list = [47, 15, 16, 17, 18, 19]
        for check in path_list:
            self.assertEqual(check_list.pop(0), check)
        dwga.get_graph().remove_node(19)
        dist, path_list = dwga.shortest_path(47, 19)
        self.assertEqual(float('inf'), dist)
        self.assertEqual([], path_list)

    def test_connected_component(self):
        ga = graph_algo_creator()
        ga.get_graph().add_node(6)
        ga.get_graph().add_node(7)
        ga.get_graph().add_node(8)
        ga.get_graph().add_node(9)
        ga.get_graph().add_edge(2, 5, 7)
        ga.get_graph().add_edge(5, 2, 12)
        ga.get_graph().add_edge(4, 7, 1)
        ga.get_graph().add_edge(7, 9, 12)
        ga.get_graph().add_edge(9, 8, 2)
        ga.get_graph().add_edge(6, 8, 2)
        ga.get_graph().add_edge(8, 6, 2)
        ga.get_graph().add_edge(8, 4, 2)
        cc_list = ga.connected_component(1)
        check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for check in cc_list:
            self.assertEqual(check_list.pop(0), check)
        ga.get_graph().remove_edge(4, 7)
        cc_list = ga.connected_component(1)
        check_list = [1, 2, 3, 4, 5, 6]
        for check in cc_list:
            self.assertEqual(check_list.pop(0), check)

    def test_connected_components(self):
        ga = graph_algo_creator()
        ga.get_graph().add_node(6)
        ga.get_graph().add_node(7)
        ga.get_graph().add_node(8)
        ga.get_graph().add_node(9)
        ga.get_graph().add_edge(2, 5, 7)
        ga.get_graph().add_edge(5, 2, 12)
        ga.get_graph().add_edge(4, 7, 1)
        ga.get_graph().add_edge(7, 9, 12)
        ga.get_graph().add_edge(9, 8, 2)
        ga.get_graph().add_edge(6, 8, 2)
        ga.get_graph().add_edge(8, 6, 2)
        ga.get_graph().add_edge(8, 4, 2)
        cc_lists = ga.connected_components()
        check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for temp_list in cc_lists:
            for check in temp_list:
                self.assertEqual(check_list.pop(0), check)
        ga.get_graph().remove_edge(4, 7)
        ga.get_graph().remove_edge(2, 5)
        ga.get_graph().remove_edge(5, 2)
        ga.get_graph().add_edge(8, 9, 1)
        ga.get_graph().add_edge(9, 7, 1)
        check_list1 = [1, 2, 3, 4]
        check_list2 = [5]
        check_list3 = [6, 7, 8, 9]
        cc_lists = ga.connected_components()
        self.assertTrue(check_list1 in cc_lists)
        self.assertTrue(check_list2 in cc_lists)
        self.assertTrue(check_list3 in cc_lists)

    def test_plot_graph(self):
        pass


if __name__ == '__main__':
    unittest.main()
