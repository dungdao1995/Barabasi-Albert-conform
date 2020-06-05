import networkx as nx
import matplotlib.pyplot as plt 
import random

#=======Draw Degree Distribution ======
def plot_degree(degree,p,r):
    plt.bar(list(degree.keys()), degree.values(), color='#0504aa')
    plt.xlabel('K')
    plt.ylabel('Number of Node')
    plt.title('Degree distribution with p = '+str(p) +' and r = '+ str(r))

#========Create Graph =======
def create_network(N,r,p):
    G = nx.Graph() #Create a new GRAPH
    red_nodes = [] #List of Red nodes
    blue_nodes = [] #List of Blue nodes
    degree_list = {} #Save the degree value for each node
    degree_dist = {} # Degree distribution
    
    #Append 4 nodes for each 
    for i in range(0,4):
        red_nodes.append(i) 
    for j in range(4,8):
        blue_nodes.append(j)
    
    #Add new nodes from N
    for i in range(8,N):
        rand_node = random.random()
        if rand_node <= r:
            red_nodes.append(i)
        else:
            blue_nodes.append(i)

    #Add node to Graph
    G.add_nodes_from(red_nodes)
    G.add_nodes_from(blue_nodes)        
    #Add egdes
    for i in range(0,N):
        for j in range(i,N):
            rand = random.random()
            if (j!=i) and (rand < p):
                if ((i in red_nodes) and (j in red_nodes)) or ((i in blue_nodes) and (j in blue_nodes)):
                    G.add_edge(i,j)
            elif (j!=i) and (rand > p):
                if ((i in red_nodes) and (j in blue_nodes)) or ((j in red_nodes) and (i in blue_nodes)):
                    G.add_edge(i,j)

    
    #Saving the degree value for each node in the dictionary
    for i in G.nodes:
        degree_list[i] = G.degree[i]
    
    #Saving the degree distribution in the dictionary
    for i in range(max(degree_list.values())+1):
        degree_dist[i] = 0
        for j in degree_list:
            if degree_list[j] == i:
                degree_dist[i] += 1
    return degree_dist

#=======TEST========
def test():
    print("1. Enter the number of Node, r and p")
    print("2. Enter 4 different values of p for a fixed value of r and number of nodes")
    print("3. Enter 4 different values of r for a fixed value of r and number of nodes")
    test = int(input("Choose the number of test which you want to test:"))
    if test == 1:
        N = int(input("Enter the number of nodes: "))
        p = float(input("Enter the probability p: "))
        r = float(input("Enter the random number r: "))
        degree = create_network(N,r,p)
        plot_degree(degree,p,r)
        plt.show()
    elif test == 2:
        N = int(input("Enter the number of nodes: "))
        r = float(input("Enter the random number r: "))
        p = []
        for i in range(4):
            j = float(input("Enter the probability p["+str(i)+']= '))
            p.append(j)
        for i in range(4):
            degree = create_network(N,r,p[i])
            plt.subplot(2,2,i+1)
            plot_degree(degree,p[i],r)
        plt.show()
    elif test == 3:
        N = int(input("Enter the number of nodes: "))
        p = float(input("Enter the probability p: "))
        r = []
        for i in range(4):
            j = float(input("Enter the random number r["+str(i)+']= '))
            r.append(j)
        for i in range(4):
            degree = create_network(N,r[i],p)
            plt.subplot(2,2,i+1)
            plot_degree(degree,p,r[i])
        plt.show()
    else:
        return None

test()