import json
from random import random
from typing import List
import matplotlib.pyplot as plt
from DiGraph import DiGraph
from GraphInterface import GraphInterface
from queue import PriorityQueue
from queue import Queue

from Node_data import Geo_location


class GraphAlgo:
    def __init__(self, graph=None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def set_graph(self, graph):
        self.graph = graph

    def save_to_json(self, file_name: str) -> bool:
        final_dict = {}
        if self.graph is None:
            with open(file_name, 'w') as outfile:
                json.dump(final_dict, outfile)
            return True
        edges = []
        for temp_node in self.graph.get_all_v().values():
            edge_dict = self.graph.all_out_edges_of_node(temp_node.get_key())
            for temp in edge_dict:
                temp_dict = {}
                temp_dict["src"] = temp_node.get_key()
                temp_dict["w"] = self.get_graph().get_all_v().get(temp_node.get_key()).get_map().get(temp)
                temp_dict["dest"] = temp
                edges.append(temp_dict)
        nodes = []
        for temp in self.graph.get_all_v().values():
            temp_dict = {}
            temp_dict["pos"] = str(temp.get_pos().get_x()) + ',' + str(temp.get_pos().get_y()) + ',' + str(
                temp.get_pos().get_z())
            temp_dict["id"] = temp.get_key()
            nodes.append(temp_dict)
        final_dict["Edges"] = edges
        final_dict["Nodes"] = nodes
        with open(file_name, 'w') as outfile:
            json.dump(final_dict, outfile)
            return True
        return False

    def load_from_json(self, file_name: str) -> bool:
        i = 0
        with open(file_name) as json_file:
            final_dict = json.load(json_file)
            edges = []
            edges = final_dict["Edges"]
            nodes = []
            nodes = final_dict["Nodes"]
            new_graph = DiGraph()
            new_graph_algo = GraphAlgo(new_graph)
            for temp_node in nodes:
                if len(temp_node) == 2:
                    str=temp_node["pos"]
                    pos_list=str.split(",")
                    pos_x=pos_list.pop(0)
                    pos_y = pos_list.pop(0)
                    pos_z = pos_list.pop(0)
                    pos=Geo_location(pos_x, pos_y, pos_z)
                else:
                    pos = Geo_location(random()*50, random()*50, 0)
                new_graph_algo.get_graph().add_node(temp_node["id"], pos)
            for temp_edge in edges:
                new_graph_algo.get_graph().add_edge(temp_edge["src"], temp_edge["dest"], temp_edge["w"])
            self.set_graph(new_graph)
            return True
        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.get_graph() is None:
            return float('inf'), []
        if id1 not in self.get_graph().get_all_v().keys() or id2 not in self.get_graph().get_all_v().keys():
            return float('inf'), []
        short_path_list = []
        used_list = []
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
        self = self.redirect()
        self.list_maker(self.get_graph().get_all_v().get(id2), short_path_list)
        short_path_list.reverse()
        short_path = (weight, short_path_list)
        self = self.redirect()
        self.res_info()
        return short_path

    def res_info(self):
        for temp_node in self.get_graph().get_all_v().values():
            temp_node.set_info("")
            temp_node.set_weight(999999)
            temp_node.set_tag(0)

    def list_maker(self, src, short_path_list):
        for temp_edge in self.get_graph().all_out_edges_of_node(src.get_key()):
            temp_edge = self.get_graph().get_all_v().get(temp_edge)
            if self.get_graph().get_all_v().get(src.get_key()).get_map().get(temp_edge) != 999999:
                src_weight = self.get_graph().get_all_v().get(src.get_key()).get_weight()
                dest_weight = self.get_graph().get_all_v().get(temp_edge.get_key()).get_weight()
                edge_weight = self.get_graph().get_all_v().get(src.get_key()).get_map().get(temp_edge.get_key())
                if src_weight == dest_weight + edge_weight:
                    short_path_list.append(temp_edge.get_key())
                    self.list_maker(temp_edge, short_path_list)

    def redirect(self):
        new_graph = DiGraph()
        new_graph_algo = GraphAlgo(new_graph)
        for temp_node in self.get_graph().get_all_v().values():
            new_graph_algo.get_graph().add_node(temp_node.get_key())
            new_graph_algo.get_graph().get_all_v().get(temp_node.get_key()).set_weight(
                self.get_graph().get_all_v().get(temp_node.get_key()).get_weight())
        for temp_node in self.get_graph().get_all_v().values():
            for temp_edge in self.get_graph().get_all_v().get(temp_node.get_key()).get_map().keys():
                new_weight = self.get_graph().get_all_v().get(temp_node.get_key()).get_map().get(temp_edge)
                new_graph_algo.get_graph().add_edge(temp_edge, temp_node.get_key(), new_weight)
        return new_graph_algo

    def connected_component(self, id1: int) -> list:
        self.res_info()
        connected_component = []
        if id1 not in self.get_graph().get_all_v().keys() or self.get_graph() is None:
            return connected_component
        visited = [self.get_graph().get_all_v().get(id1).get_key()]
        redirect_visited = [self.get_graph().get_all_v().get(id1).get_key()]
        node_q = Queue()
        node_q.put(self.get_graph().get_all_v().get(id1))
        self.get_graph().get_all_v().get(id1).set_info("1")
        while not node_q.empty():
            head_node = node_q.get()
            for node_temp in self.get_graph().all_out_edges_of_node(head_node.get_key()):
                node_temp = self.get_graph().get_all_v().get(node_temp)
                if node_temp.get_info() == "":
                    node_q.put(node_temp)
                    visited.append(node_temp.get_key())
                    node_temp.set_info("1")
        self.res_info()
        self = self.redirect()
        node_q.put(self.get_graph().get_all_v().get(id1))
        self.get_graph().get_all_v().get(id1).set_info("1")
        while not node_q.empty():
            head_node = node_q.get()
            for node_temp in self.get_graph().all_out_edges_of_node(head_node.get_key()):
                node_temp = self.get_graph().get_all_v().get(node_temp)
                if node_temp.get_info() == "":
                    node_q.put(node_temp)
                    redirect_visited.append(node_temp.get_key())
                    node_temp.set_info("1")
        self.res_info()
        self = self.redirect()
        connected_component = []
        for x in visited:
            if x in redirect_visited:
                connected_component.append(x)
        self.res_info()
        self = self.redirect()
        return connected_component

    def connected_components(self) -> List[list]:
        final_list = []
        cc_list = []
        if self.get_graph() is None:
            return final_list
        for temp_node in self.get_graph().get_all_v().values():
            cc_list = self.connected_component(temp_node.get_key())
            final_list.append(cc_list)
        return final_list

    def plot_graph(self) -> None:
        node_id=[]
        node_x=[]
        node_y=[]
        for temp_node in self.get_graph().get_all_v().values():
            node_id.append(temp_node.get_key())
            node_x.append(temp_node.get_pos().get_x())
            node_y.append(temp_node.get_pos().get_y())
        fig, ax = plt.subplots()
        ax.scatter(node_x, node_y,220,"blue")
        for temp_node in self.get_graph().get_all_v().values():
            for temp_edge in self.get_graph().all_out_edges_of_node(temp_node.get_key()):
                temp_edge=self.get_graph().get_all_v().get(temp_edge)
                src =(temp_node.get_pos().get_x(),temp_node.get_pos().get_y())
                dest=(temp_edge.get_pos().get_x(),temp_edge.get_pos().get_y())
                plt.annotate("",src,dest, arrowprops=dict(facecolor='red',edgecolor="red", width=0.5,headwidth=5, shrink=0.028),
            horizontalalignment='right', verticalalignment='top',
            )
        for i, txt in enumerate(node_id): #text=nodeid i=index
            ax.annotate(txt, (node_x[i] - 0.3,node_y[i] - 0.3),color="white")
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        ax.set_title("Ex3 - Directed Wighted Graph")
        plt.show()


if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_edge(5, 4, 1)
    graph.add_edge(4, 5, 1)
    print(graph.add_edge(1, 2, 88))
    print(graph.add_edge(2, 4, 6))
    print(graph.add_edge(4, 2, 9))
    print(graph.add_edge(4, 1, 12))
    print(graph.add_edge(1, 3, 4))
    print(graph.add_edge(3, 2, 1))
    graph_algo = GraphAlgo(graph)
    graph_algo.shortest_path(1, 4)
    b = graph_algo.connected_components()
    graph_algo.plot_graph()

    # graph_algo.save_to_json("test.txt")
    # graph_algo.load_from_json("test.txt")
