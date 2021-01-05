import json
from DiGraph import DiGraph
from GraphInterface import GraphInterface
from queue import PriorityQueue


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
                temp_dict["w"] = graph.nodes.get(temp_node.get_key()).get_map().get(temp)
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
        with open(file_name, 'w') as outfile:
            json.dump(final_dict, outfile)
            return True
        return False

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name) as json_file:
            final_dict = json.load(json_file)
            edges = []
            edges = final_dict["Edges"]
            nodes = []
            nodes = final_dict["Nodes"]
            new_graph = DiGraph()
            new_graph_algo = GraphAlgo(new_graph)
            for temp_node in nodes:
                new_graph_algo.get_graph().add_node(temp_node["id"], temp_node["pos"])
            for temp_edge in edges:
                new_graph_algo.get_graph().add_edge(temp_edge["src"], temp_edge["dest"], temp_edge["w"])
            return True
        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.get_graph().get_all_v().keys() or id2 not in self.get_graph().get_all_v().keys():
            return float('inf'), []
        short_path_list = []
        used_list=[]
        p_queue = PriorityQueue()
        p_queue.put(self.get_graph().get_all_v().get(id1))
        used_list.append(self.get_graph().get_all_v().get(id1))
        self.get_graph().get_all_v().get(id1).set_weight(0)
        while not p_queue.empty():
            temp_node = p_queue.get()
            p_queue.put(temp_node)
            a = temp_node.get_key()
            if temp_node.get_info() == "":
                temp_node.set_info("1")
                if a == id2:
                    break
                for temp_edge in self.get_graph().all_out_edges_of_node(temp_node.get_key()):
                    temp_edge = self.get_graph().get_all_v().get(temp_edge)
                    if temp_edge.get_info() == "":
                        temp_weight = self.get_graph().get_all_v().get(temp_node.get_key()).get_map().get(
                            temp_edge.get_key())
                        if temp_weight != 999999 and temp_weight + temp_node.get_weight() < temp_edge.get_weight():
                            temp_edge.set_weight(temp_weight + temp_node.get_weight())
                            if temp_edge not in used_list:
                                p_queue.put(temp_edge)
                                used_list.append(temp_edge)
            p_queue.get()
        weight = self.get_graph().get_all_v().get(id2).get_weight()
        if weight == 999999:
            self.res_info()
            return float('inf'), []
        short_path_list.append(self.get_graph().get_all_v().get(id2).get_key())
        self=self.redirect()
        self.list_maker(self.get_graph().get_all_v().get(id2),short_path_list)
        short_path_list.reverse()
        self.res_info()
        short_path = (weight, short_path_list)
        self=self.redirect()
        return short_path

    def res_info(self):
        for temp_node in self.get_graph().get_all_v().values():
            temp_node.set_info("")
            temp_node.set_weight(999999)
            temp_node.set_tag(0)

    def list_maker(self, src, short_path_list):
        for temp_edge in self.get_graph().all_out_edges_of_node(src.get_key()):
            temp_edge = self.get_graph().get_all_v().get(temp_edge)
            if self.get_graph().get_all_v().get(src.get_key()).get_map().get(temp_edge)!=999999:
                src_weight=self.get_graph().get_all_v().get(src.get_key()).get_weight()
                dest_weight=self.get_graph().get_all_v().get(temp_edge.get_key()).get_weight()
                edge_weight=self.get_graph().get_all_v().get(src.get_key()).get_map().get(temp_edge.get_key())
                if src_weight == dest_weight+edge_weight:
                    short_path_list.append(temp_edge.get_key())
                    self.list_maker(temp_edge, short_path_list)

    def redirect(self):
        new_graph = DiGraph()
        new_graph_algo = GraphAlgo(new_graph)
        for temp_node in self.get_graph().get_all_v().values():
            new_graph_algo.get_graph().add_node(temp_node.get_key())
            new_graph_algo.get_graph().get_all_v().get(temp_node.get_key()).set_weight(self.get_graph().get_all_v().get(temp_node.get_key()).get_weight())
        for temp_node in self.get_graph().get_all_v().values():
            for temp_edge in self.get_graph().get_all_v().get(temp_node.get_key()).get_map().keys():
                new_weight = self.get_graph().get_all_v().get(temp_node.get_key()).get_map().get(temp_edge)
                new_graph_algo.get_graph().add_edge(temp_edge, temp_node.get_key(), new_weight)
        return new_graph_algo



if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    print(graph.add_edge(1, 2, 88))
    print(graph.add_edge(2, 4, 6))
    print(graph.add_edge(4, 2, 9))
    print(graph.add_edge(4, 1, 12))
    print(graph.add_edge(1, 3, 4))
    print(graph.add_edge(3, 2, 1))
    graph.remove_node(4)
    graph_algo = GraphAlgo(graph)
    a = graph_algo.shortest_path(1, 4)
    print(a)
    graph_algo.save_to_json("test.txt")
    graph_algo.load_from_json("test.txt")
