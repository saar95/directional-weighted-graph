# Ex3
The third assignment in OPP course

[AlmogHomo](#digraph-methods:)

- Names: Saar Barel & Almog Reuveny.

In this assignment we built a directional weighted graph in Python

Example:

![image](https://user-images.githubusercontent.com/63556870/104121082-68703e00-5344-11eb-9a0f-8ddaf7daf322.png)

There are 3 parts to the task:

-The first part: Represents a positive directional weighted graph.

 -DiGraph: Represents a positive directional weighted graph.
 
 -Node_data: Represents a Node and his attributes-key,tag,weight,info,map.
 
-The second part: 

 -GraphAlgo: Represents a Directed (positive) Weighted Graph Theory Algorithms.
 
 -The third part: In this section you can see the results of the comparisons between Python, Java (our cod for Ex2) and NetworkX. 

  The results show the running times and the differences between them.
  
  


You can find more information about **Directed Weighted Graph** [here](https://en.wikipedia.org/wiki/Directed_graph).



## DiGraph Methods:
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




## GraphAlgo Methods
|Name  | Description |
|--|--|
| get_graph|Return the directed graph on which the algorithm works on. |
| load_from_json|Loads a graph from a json file. |
| save_to_json|Saves the graph in JSON format to a file.|
| shortest_path|Returns the shortest path from node id1 to node id2 using [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). |
| connected_component|Finds the Strongly Connected Component(SCC) that node id1 is a part of. |
| connected_components|Finds all the Strongly Connected Component(SCC) in the graph.  |
| plot_graph|Drawing the graph using [matplot.lib](https://matplotlib.org/). |
