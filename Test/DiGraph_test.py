import unittest

from DiGraph import DiGraph


def graph_creator():
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
    return graph


class MyTestCase(unittest.TestCase):

    def test_v_size(self):
        d_graph = graph_creator()
        self.assertEqual(d_graph.v_size(), 5)
        d_graph.add_node(1)
        self.assertEqual(d_graph.v_size(), 5)
        d_graph.add_node(11)
        self.assertEqual(d_graph.v_size(), 6)
        d_graph.remove_node(11)
        self.assertEqual(d_graph.v_size(), 5)
        d_graph.remove_node(11)
        self.assertEqual(d_graph.v_size(), 5)

    def test_e_size(self):
        d_graph = graph_creator()
        self.assertEqual(d_graph.e_size(), 6)
        d_graph.add_edge(5,1,5)
        d_graph.add_edge(5, 2, 5)
        self.assertEqual(d_graph.e_size(), 8)
        d_graph.add_edge(5, 2, 5)
        self.assertEqual(d_graph.e_size(), 8)
        d_graph.remove_edge(5,2)
        self.assertEqual(d_graph.e_size(), 7)

    def test_get_all_v(self):
        d_graph = graph_creator()
        i = 1
        for temp in d_graph.get_all_v_2():
            self.assertEqual(i, temp)
            i += 1

    def test_all_in_edges_of_node(self):
        d_graph = graph_creator()
        all_in = d_graph.all_in_edges_of_node(2)
        self.assertEqual(2, all_in[1])
        self.assertEqual(1, all_in[3])
        self.assertNotEqual(19, all_in[4])

    def test_all_out_edges_of_node(self):
        d_graph = graph_creator()
        all_out = d_graph.all_out_edges_of_node(4)
        self.assertEqual(9, all_out[2])
        self.assertEqual(12, all_out[1])

    def test_get_mc(self):
        d_graph = graph_creator()
        mc = d_graph.get_mc()
        self.assertEqual(11, mc)
        d_graph.add_node(17, (5, 5, 5))
        mc = d_graph.get_mc()
        self.assertEqual(12, mc)

    def test_add_edge(self):
        d_graph = graph_creator()
        self.assertFalse(d_graph.add_edge(1, 2, 2))
        self.assertEqual(11, d_graph.get_mc())
        all_out = d_graph.all_out_edges_of_node(5)
        self.assertEqual(all_out, {})
        d_graph.add_edge(5, 4, 17)
        all_out = d_graph.all_out_edges_of_node(5)
        self.assertNotEqual(all_out)
        d_graph.add_edge(5, 4, 17)
        self.assertEqual(12, d_graph.get_mc())

    def test_add_node(self):
        d_graph = graph_creator()
        self.assertEqual(5, d_graph.v_size())
        d_graph.add_node(20)
        self.assertEqual(6, d_graph.v_size())
        d_graph.add_node(20)
        self.assertEqual(6, d_graph.v_size())
        self.assertTrue(d_graph.remove_node(20))
        self.assertEqual(5, d_graph.v_size())

    def test_remove_node(self):
        d_graph = graph_creator()
        self.assertEqual(5, d_graph.v_size())
        self.assertTrue(d_graph.add_node(20))
        self.assertTrue(d_graph.add_node(21))
        self.assertTrue(d_graph.add_node(22))
        self.assertEqual(8, d_graph.v_size())
        self.assertTrue(d_graph.remove_node(22))
        self.assertEqual(7, d_graph.v_size())
        self.assertFalse(d_graph.remove_node(22))
        self.assertEqual(7, d_graph.v_size())
        d_graph.add_edge(20, 21, 1)
        d_graph.add_edge(20, 1, 2)
        self.assertEqual(8, d_graph.e_size())
        self.assertTrue(d_graph.remove_node(20))
        self.assertEqual(6, d_graph.e_size())
        self.assertTrue(d_graph.add_node(20))
        d_graph.add_edge(21, 20, 1)
        d_graph.add_edge(1, 20, 2)
        self.assertEqual(8, d_graph.e_size())
        self.assertTrue(d_graph.remove_node(20))
        self.assertEqual(6, d_graph.e_size())
        self.assertFalse(d_graph.remove_node(20))

    def test_remove_edge(self):
        d_graph = graph_creator()
        self.assertEqual(6, d_graph.e_size())
        d_graph.add_node(20)
        d_graph.add_node(21)
        d_graph.add_edge(20, 21, 1)
        self.assertEqual(7, d_graph.e_size())
        d_graph.add_edge(20, 21, 1)
        self.assertEqual(7, d_graph.e_size())
        d_graph.add_edge(21, 20, 1)
        self.assertTrue(d_graph.remove_edge(20, 21))
        self.assertEqual(7, d_graph.e_size())
        self.assertFalse(d_graph.remove_edge(20, 21))
        self.assertEqual(7, d_graph.e_size())
        self.assertTrue(d_graph.remove_edge(21, 20))
        self.assertEqual(6, d_graph.e_size())


if __name__ == '__main__':
    unittest.main()
