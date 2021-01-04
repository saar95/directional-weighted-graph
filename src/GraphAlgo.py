import json
from DiGraph import DiGraph
from GraphInterface import GraphInterface


class GraphAlgo:
    def __init__(self, graph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def save_to_json(self, file_name: str) -> bool:
        edges = []
        for temp_node in self.graph.get_all_v().values():
            edge_dict = self.graph.all_out_edges_of_node(temp_node.get_key())
            for temp in edge_dict:
                temp_dict = {}
                temp_dict["src"] = temp_node.get_key()
                temp_dict["w"] = graph.nodes.get(temp_node.get_key()).map.get(temp)
                temp_dict["dest"] = temp
                edges.append(temp_dict)
        nodes = []
        for temp in self.graph.get_all_v().values():
            temp_dict = {}
            temp_dict["pos"] = str(temp.get_pos().get_x()) + ',' + str(temp.get_pos().get_y()) + ',' + str(
                temp.get_pos().get_z())
            temp_dict["id"] = temp.get_key()
            nodes.append(temp_dict)
        final_dict = {}
        final_dict["Edges"] = edges
        final_dict["Nodes"] = nodes
        print(final_dict)
        with open(file_name, 'w') as outfile:
            json.dump(final_dict, outfile)
            return True
        return False

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name) as json_file:
            data = json.load(json_file)


if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    print(graph.add_edge(0, 1, 5))
    print(graph.add_edge(2, 1, 2))
    print(graph.add_edge(0, 3, 2))
    print(graph.add_edge(5, 1, 2))

    graph_algo = GraphAlgo(graph)
    graph_algo.save_to_json("test.txt")
