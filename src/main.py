import json
import time
from random import random

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from Node_data import Geo_location


def file_name(args):
    pass


if __name__ == '__main__':

    with open("../new/G_10000_80000_0.json") as json_file:
        final_dict = json.load(json_file)
        edges = []
        edges = final_dict["Edges"]
        nodes = []
        nodes = final_dict["Nodes"]
        g = nx.DiGraph()
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
            g.add_node(temp_node["id"])
        for temp_edge in edges:
            g.add_edge(temp_edge["src"], temp_edge["dest"])
        start_time = time.perf_counter()
        a=nx.dijkstra_path(g, 0, 7584)
        end_time = time.perf_counter()
        print(end_time - start_time)
        start_time = time.perf_counter()
        a=nx.number_strongly_connected_components(g)
        end_time = time.perf_counter()
        print(end_time - start_time)






