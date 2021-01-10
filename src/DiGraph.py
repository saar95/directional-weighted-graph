from random import random

from Node_data import Node_data, Geo_location


class DiGraph:

    def __init__(self):
        self.nodes = {}
        self.mode_count = 0
        self.edge_count = 0

    def v_size(self) -> int:
        return len(self.nodes.keys())

    """
    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    """

    def e_size(self) -> int:
        return self.edge_count

    """
    Returns the number of edges in this graph
    @return: The number of edges in this graph
    """

    def get_all_v(self) -> dict:
        get_v = {}
        a = self.nodes
        b = self.nodes[0].get_key()
        for temp_node in self.nodes.keys():
            get_v[temp_node] = str(temp_node) + ": ""|edges out|" + " " + str(
                len(self.nodes[temp_node].get_map())) + " " + "|edges in|" + " " + str(
                len(self.all_in_edges_of_node(temp_node)))
        return get_v

    """
    This method passing all the nodes in the graph and collecting the all the edges data to a dictionary
    @return a dictionary of all the nodes in the Graph, each node is represented using a pair
    (node_id, |edges out| X |edges in| X)
    """

    def get_all_v_2(self):
        return self.nodes

    def get_mc(self) -> int:
        return self.mode_count

    """
    @Return a counter for every action performed on the graph
    """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if not self.nodes.__contains__(node_id):
            if pos is None:
                pos = Geo_location(random() * 50, random() * 50, 0)
            node_temp = Node_data(node_id, pos)
            self.nodes[node_id] = node_temp
            self.mode_count += 1
            return True
        return False

    """
    This method adding a new node to the graph by creating a node with the given key and pos.
    If there is no given pos this method giving a random pos to the node.
    If the node successfully added to the graph the method return True.
    If the node is already in the graph the method will return False.
    @param node_id node_key
    @param pos Geo_location (x,y,z)
    @return True if the node successfully added to the graph, else False
    """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.nodes.__contains__(id1) and self.nodes.__contains__(id2):
            if not (self.nodes.get(id1)).map.__contains__(id2):
                (self.nodes.get(id1)).connect(id2, weight)
                self.edge_count += 1
                self.mode_count += 1
                return True
        return False

    """
    This method adding a new edge to the graph by connecting 2 given node keys.
    If one of the node doesn't exist in the graph or there is already edge between the given nodes
    the method return false.
    If the edge successfully added to the graph the method return True.
    @param id1 src node_key
    @param id2 dest node_key
    @param weight node_weight
    @return True if edge successfully added to the graph, else False.
    """

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.nodes.__contains__(id1):
            temp_dict = {}
            for temp in self.get_all_v_2().get(id1).map.keys():
                temp_dict[temp] = self.get_all_v_2().get(id1).map[temp]
            return temp_dict

    """
    This method runs over all the nodes is the graph, and creating a new dictionary
    with all the edges connected to (into) the given node_id (-->)
    @param id1 node_key
    @return: dictionary with all the edges connected to (into) the given node_id
    """

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.nodes.__contains__(id1):
            temp_dict = {}
            for temp in self.nodes.values():
                if temp.map.__contains__(id1):
                    temp_dict[temp.get_key()] = temp.map.get(id1)
        return temp_dict

    """
    This method runs over all the nodes is the graph, and creating a new dictionary
    with all the edges connected connected from the given node_id (<--)
    @param id1 node_key
    @return: dictionary with all the edges connected to (into) the given node_id
    """

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes.keys():
            temp_dict = self.all_in_edges_of_node(node_id)
            for temp in temp_dict.keys():
                self.remove_edge(temp, node_id)
            del self.nodes[node_id]
            self.mode_count += 1
            return True
        return False

    """
    This method removes node with the given key from the graph.
    This method also go through all the nodes in the graph and delete all the edges
    which include the given node (key).
    If there is no node with the given key in the graph return False.
    @param node_id key
    @return True if the node successfully deleted, else False.
    """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self is None:
            return True
        if node_id1 in self.nodes.keys() and node_id2 in self.nodes.keys():
            if (node_id2 in self.nodes.get(node_id1).map):
                del self.nodes.get(node_id1).map[node_id2]
                self.edge_count -= 1
                self.mode_count += 1
                return True
        return False

    """
    This method removes an edge from src to dest (src -> dest) from the graph.
    If there is no such a nodes or there is already edge between the given nodes return False.
    @param node_id1 src node
    @param node_id2 dest node
    @return True if the edge successfully removed from the graph, else False
    """

    def __repr__(self):
        return f'Graph: |V|={self.nodes.__len__()},|E|={self.edge_count}'

