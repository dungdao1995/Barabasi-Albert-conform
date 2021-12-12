# Barabasi-Albert-conform
# Introduction
Consider a network of N red and N blue nodes. The probability that there is a link between nodes of identical color is p and the probability that there is a link between nodes of different color is q (p + q = 1). If p > q, the nodes exhibit a tendency to connect to nodes of the same color. For q = 0 the network has at least two components, containing nodes with the same color.
The student is requested to implement a code which simulates a modified Barabasi-Albert conform to the following workflow:
1. Create a seed network composed of 4 blue nodes and 4 red nodes
2. At each time step add a new node. Its color is randomly selected depending on a parameter r (0≤r≤1): ifr=0allnodeswillbeblue,ifr=1allnodeswillbered,intermediatevalues will determine different percentages. For example, if r = 0.1 only 10% of nodes will be red. Hint: create a sequence of N − 8 colors (red or blue) coherent with the chosen value of r
3. Depending on the value of p, and consequently of q, each new node will be connected to some nodes of the same color and some others of the other color
4. When the network is complete, store the degree distribution
5. Plot the degree distributions corresponding to 4 different values of p for a fixed value of r
6. Plot the degree distributions corresponding to 4 different values of r for a fixed value of p
