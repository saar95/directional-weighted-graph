import json
from random import random
from typing import List
import matplotlib.pyplot as plt
from DiGraph import DiGraph
from GraphInterface import GraphInterface
from queue import PriorityQueue
from queue import Queue

from Node_data import Geo_location

"""This  class represents a Directed (positive) Weighted Graph Theory Algorithms"""

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
        for temp_node in self.graph.get_all_v_2().values():
            edge_dict = self.graph.all_out_edges_of_node(temp_node.get_key())
            for temp in edge_dict:
                temp_dict = {}
                temp_dict["src"] = temp_node.get_key()
                temp_dict["w"] = self.get_graph().get_all_v_2().get(temp_node.get_key()).get_map().get(temp)
                temp_dict["dest"] = temp
                edges.append(temp_dict)
        nodes = []
        for temp in self.graph.get_all_v_2().values():
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

    """
    This method save the directed weighted graph to a file with the given name
    The graph will be saved in specific JSON format
    @param file_name - the file name (may include a relative path).
    @return True if the save succeed, else False
     """

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
                if len(temp_node) == 2:
                    str = temp_node["pos"]
                    pos_list = str.split(",")
                    pos_x = pos_list.pop(0)
                    pos_y = pos_list.pop(0)
                    pos_z = pos_list.pop(0)
                    pos = Geo_location(pos_x, pos_y, pos_z)
                else:
                    pos = Geo_location(random() * 50, random() * 50, 0)
                new_graph_algo.get_graph().add_node(temp_node["id"], pos)
            for temp_edge in edges:
                new_graph_algo.get_graph().add_edge(temp_edge["src"], temp_edge["dest"], temp_edge["w"])
            self.set_graph(new_graph)
            return True
        return False

    """"
    This method build a new graph from the given file_name (JSON file)
    If the the node don't have position in the JSON file, the method will gave them random position.
    @param file_name the file name (may include a relative path).
    @return True if the load succeed, else False
    """

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.res_info()
        if self.get_graph() is None:
            return float('inf'), []
        if id1 not in self.get_graph().get_all_v_2().keys() or id2 not in self.get_graph().get_all_v_2().keys():
            return float('inf'), []
        short_path_list = []
        used_list = []
        p_queue = PriorityQueue()
        p_queue.put(self.get_graph().get_all_v_2().get(id1))
        used_list.append(self.get_graph().get_all_v_2().get(id1))
        self.get_graph().get_all_v_2().get(id1).set_weight(0)
        while not p_queue.empty():
            temp_node = p_queue.get()
            p_queue.put(temp_node)
            a = temp_node.get_key()
            if temp_node.get_info() == "":
                temp_node.set_info("1")
                if a == id2:
                    break
                for temp_edge in self.get_graph().all_out_edges_of_node(temp_node.get_key()):
                    temp_edge = self.get_graph().get_all_v_2().get(temp_edge)
                    if temp_edge.get_info() == "":
                        temp_weight = self.get_graph().get_all_v_2().get(temp_node.get_key()).get_map().get(
                            temp_edge.get_key())
                        if temp_weight != 999999 and temp_weight + temp_node.get_weight() < temp_edge.get_weight():
                            temp_edge.set_weight(temp_weight + temp_node.get_weight())
                            if temp_edge not in used_list:
                                p_queue.put(temp_edge)
                                used_list.append(temp_edge)
            p_queue.get()
        weight = self.get_graph().get_all_v_2().get(id2).get_weight()
        if weight == 999999:
            self.res_info()
            return float('inf'), []
        short_path_list.append(self.get_graph().get_all_v_2().get(id2).get_key())
        self = self.redirect()
        self.list_maker(self.get_graph().get_all_v_2().get(id2), short_path_list)
        short_path_list.reverse()
        short_path = (weight, short_path_list)
        self = self.redirect()
        self.res_info()
        return short_path

    """This method run over all the nodes connected between from src to dest (-->) and all their neighbors and 
    changing the tags of the nodes according to this calculation: my tag = my neighbor's smallest tag+the edge 
    between me and my neighbor. The calculation using PriorityQueue to find the lowest weight neighbor. Then turn the 
    graph over and run it again from the end to the beginning to find the list If there is no path between 2 given 
    nodes return (float('inf'),[]) @param id1: The start node id @param id2: The end node id @return: The distance of 
    the shortest path, a list of the nodes ids that the path goes through, if there is no path return (float('inf'),[]) 
    """

    def res_info(self):
        for temp_node in self.get_graph().get_all_v_2().values():
            temp_node.set_info("")
            temp_node.set_weight(999999)
            temp_node.set_tag(0)

    """
    This method run over all the nodes in the given graph
    resets all the node date including tag,info and weight.
    """

    def list_maker(self, src, short_path_list):
        for temp_edge in self.get_graph().all_out_edges_of_node(src.get_key()):
            temp_edge = self.get_graph().get_all_v_2().get(temp_edge)
            if self.get_graph().get_all_v_2().get(src.get_key()).get_map().get(temp_edge) != 999999:
                src_weight = self.get_graph().get_all_v_2().get(src.get_key()).get_weight()
                dest_weight = self.get_graph().get_all_v_2().get(temp_edge.get_key()).get_weight()
                edge_weight = self.get_graph().get_all_v_2().get(src.get_key()).get_map().get(temp_edge.get_key())
                if src_weight == dest_weight + edge_weight:
                    short_path_list.append(temp_edge.get_key())
                    self.list_maker(temp_edge, short_path_list)

    def redirect(self):
        new_graph = DiGraph()
        new_graph_algo = GraphAlgo(new_graph)
        for temp_node in self.get_graph().get_all_v_2().values():
            new_graph_algo.get_graph().add_node(temp_node.get_key())
            new_graph_algo.get_graph().get_all_v_2().get(temp_node.get_key()).set_weight(
                self.get_graph().get_all_v_2().get(temp_node.get_key()).get_weight())
        for temp_node in self.get_graph().get_all_v_2().values():
            for temp_edge in self.get_graph().get_all_v_2().get(temp_node.get_key()).get_map().keys():
                new_weight = self.get_graph().get_all_v_2().get(temp_node.get_key()).get_map().get(temp_edge)
                new_graph_algo.get_graph().add_edge(temp_edge, temp_node.get_key(), new_weight)
        return new_graph_algo

    """
    This method create a new copy of the given graph but reversed
    mean all the edges are reversed.
    @return reversed copy of directed_weighted_graph
    """

    def connected_component(self, id1: int) -> list:
        self.res_info()
        connected_component = []
        if id1 not in self.get_graph().get_all_v_2().keys() or self.get_graph() is None:
            return connected_component
        visited = [self.get_graph().get_all_v_2().get(id1).get_key()]
        redirect_visited = [self.get_graph().get_all_v_2().get(id1).get_key()]
        node_q = Queue()
        node_q.put(self.get_graph().get_all_v_2().get(id1))
        self.get_graph().get_all_v_2().get(id1).set_info("1")
        while not node_q.empty():
            head_node = node_q.get()
            for node_temp in self.get_graph().all_out_edges_of_node(head_node.get_key()):
                node_temp = self.get_graph().get_all_v_2().get(node_temp)
                if node_temp.get_info() == "":
                    node_q.put(node_temp)
                    visited.append(node_temp.get_key())
                    node_temp.set_info("1")
        self.res_info()
        self = self.redirect()
        node_q.put(self.get_graph().get_all_v_2().get(id1))
        self.get_graph().get_all_v_2().get(id1).set_info("1")
        while not node_q.empty():
            head_node = node_q.get()
            for node_temp in self.get_graph().all_out_edges_of_node(head_node.get_key()):
                node_temp = self.get_graph().get_all_v_2().get(node_temp)
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
        connected_component.sort()
        return connected_component

    """
    This method starts at the first node in the graph, changes his tag to 0 than move all over his neighbors and 
    changes their tags to 0 and so on till the last node in the graph and add them to a list. 
    Then the method resets all the nodes tag and turns all the edges in the graph using redirect function.
    And run again from the same node, changing all his neighbors tag to 0 and so on and add them to another list.
    Finally we loop through the lists, the binding component will consist of the nodes in both lists.
    @param id1: The node key
    @return: The list of nodes in the SCC
    """

    def connected_components(self) -> List[list]:
        final_list = []
        cc_list = []
        if self.get_graph() is None:
            return final_list
        for temp_node in self.get_graph().get_all_v_2().values():
            if temp_node.get_tag() != 1:
                cc_list = self.connected_component(temp_node.get_key())
                for temp in cc_list:
                    self.get_graph().get_all_v_2().get(temp).set_tag(1)
                if cc_list not in final_list:
                    final_list.append(cc_list)
        self.res_info()
        return final_list

    """
    Call connected_component function for each node in the graph.
    @return: The list of all SCC in the graph
    """

    def plot_graph(self) -> None:
        node_id = []
        node_x = []
        node_y = []
        for temp_node in self.get_graph().get_all_v_2().values():
            node_id.append(temp_node.get_key())
            node_x.append(temp_node.get_pos().get_x())
            node_y.append(temp_node.get_pos().get_y())
        fig, ax = plt.subplots()
        ax.scatter(node_x, node_y, 140, "blue")
        for temp_node in self.get_graph().get_all_v_2().values():
            for temp_edge in self.get_graph().all_out_edges_of_node(temp_node.get_key()):
                temp_edge = self.get_graph().get_all_v_2().get(temp_edge)
                src = (temp_node.get_pos().get_x(), temp_node.get_pos().get_y())
                dest = (temp_edge.get_pos().get_x(), temp_edge.get_pos().get_y())
                plt.annotate("", dest, src,
                             arrowprops=dict(facecolor='red', edgecolor="red", width=0.3, headwidth=2.5, shrink=0.028),
                             horizontalalignment='right', verticalalignment='top',
                             )
        for i, txt in enumerate(node_id):  # text=nodeid i=index
            ax.annotate(txt, (node_x[i] + 0.8, node_y[i] + 0.8), color="black")
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        ax.set_title("Ex3 - Directed Wighted Graph")
        plt.show()

        """
        This method drawing the graph using matplotlib, this method collects all the nodes and edges data
        (Geo location and keys) and drawing them.
        """
