# Ex3
The third assignment in OPP course

Names: Saar Barel & Almog Reuveny.

In this assignment we built a directional weighted graph in Python

Example:

![image](https://user-images.githubusercontent.com/63556870/104121082-68703e00-5344-11eb-9a0f-8ddaf7daf322.png)


In this project, we used PraiorityQueue for Dijkstra's Algorithm, mathplotlib for drawing the graph and lists+dictionary to manage the graph structure

# Structure

## DiGraph Class:

**Represents a positive directional weighted graph.** 

### DiGraph Methods:
|Name  | Description |
|--|--|
| v_size |Returns the number of vertices in this graph |
| e_size|Returns the number of edges in this graph |
| get_all_v|Return a dictionary of all the nodes in the Graph (node_id:node_data)
| all_in_edges_of_node|Return a dictionary of all the nodes connected to (into) node_id |
| all_out_edges_of_node |Return a dictionary of all the nodes connected from node_id |
| get_mc| Returns a counter for every action performed on the graph
| add_edge|Adds an edge to the graph.  |
| add_node|Adds a node to the graph. |
| remove_node|Removes a node from the graph. |
| remove_edge|Removes an edge from the graph. |


## GraphAlgo Class:

**Represents a Directed (positive) Weighted Graph Theory Algorithms.** 

### GraphAlgo Methods:

|Name  | Description |
|--|--|
| get_graph|Return the directed graph on which the algorithm works on. |
| load_from_json|Loads a graph from a json file. |
| save_to_json|Saves the graph in JSON format to a file.|
| shortest_path|Returns the shortest path from node id1 to node id2 using [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). |
| connected_component|Finds the Strongly Connected Component(SCC) that node id1 is a part of. |
| connected_components|Finds all the Strongly Connected Component(SCC) in the graph.  |
| plot_graph|Drawing the graph using [matplot.lib](https://matplotlib.org/). |


## NodeData Class:

**Represents a vertex in the graph.** 

### NodeData methods:

|Name  | Description |
|--|--|
| get_key|Return the key of the node (vertex) every node has a uniqe key. |
| get_pos|Retuns the Geo Location (x,y,z) of the node.|
| connect|Connect an edge between 2 nodes with the given wieght. |
| get_map|Returns a dictionary of all the edges connected to the node.   |

### In addition to this project we built a comparison system that compares implementations of a directional weighted graph graphs in different programing languages (java,python and more), you can see the results on the WIKI page


You can find more information about **Directed Weighted Graph** [here](https://en.wikipedia.org/wiki/Directed_graph).






