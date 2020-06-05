import matplotlib.pyplot as plt
import random
import numpy as np

#===========PLOT=============
def plot_degree(degree,p,r):
    plt.bar(list(degree.keys()), degree.values(), color='#0504aa')
    plt.xlabel('K')
    plt.ylabel('Pk')
    plt.title('Degree distribution with p = '+str(p) +' and r = '+ str(r))

#=========GRAPH Class===========
class Graph:
    
    def __init__(self, graph = None):
        self.__vlist = [] 
        if graph == None:
            self.__graph = []
        else:
            self.__graph = graph
            for i in self.__graph:
                for j in range(2):
                    if i[j] not in self.__vlist :
                        self.__vlist .append(i[j])            
            
    def vertex_count(self):
        return len(self.__vlist)

    def vertices(self):
        return self.__vlist  
    
    def edge_count(self):
        return len(self.__graph)
    
    def edges(self):
        return self.__graph
    
    def get_edge(self,u,v):
        for i in self.__graph:
            if i[0] == u and i[1] == v: 
                return i
            
    def degree(self,v,out=True):
        count = 0
        if out:
            for i in self.__graph:
                if i[0] == v:
                    count += 1
        else:
            for i in self.__graph:
                for j in range(2):
                    if i[j]==v:
                        count+=1        
        return count
    
    def incident_edges(self,v,out=True):
        edge = []
        if out:
            for i in self.__graph:
                if i[0] == v:
                    edge.append(i)
        else:
            for i in self.__graph:
                for j in range(2):
                    if i[j]==v:
                        edge.append(i)
        return edge
    
    def insert_vertex(self, x = None):
        if x != None:
            if x not in self.__vlist:
                self.__vlist.append(x)
    
    def insert_edge(self,u,v,x = None):
        if u not in self.__vlist:
            self.__vlist.append(u)
        if v not in self.__vlist:
            self.__vlist.append(v)
        e = (u,v,x)    
        if e not in self.__graph:
            self.__graph.append((u,v,x))
        
    def remove_vertex(self,v):
        if v in self.__vlist:
            self.__vlist.remove(v)
            
        new_graph = []   
        for i in self.__graph:
            if i[0]!=v and i[1]!=v:
                new_graph.append(i)
                
        self.__graph = new_graph            
    
    def remove_edge(self,e):
        for i in self.__graph:
            if i == e:
                self.__graph.remove(e)

def Preferential_Att(G,node_list):
    PA = []
    sum = 0
    for i in node_list:
        sum += G.degree(i, out=False)
    for i in node_list:
        PA.append(G.degree(i, out=False)/sum)
        
    return PA

#==========Create GRAPH===================            
def create_network(N,r,p):
    m = 4 # the value of links which new nodes will have
    G = Graph() #Create a new GRAPH
    red_nodes = [] #List of Red nodes
    blue_nodes = [] #List of Blue nodes

    degree_list = {} #Save the degree value for each node
    degree_dist = {} # Degree distribution
    
    #Append 4 nodes for each 
    for i in range(0,4):
        red_nodes.append(i)
        G.insert_vertex(i) 
    for j in range(4,8):
        blue_nodes.append(j)
        G.insert_vertex(j)

    #Add egdes
    for i in range(0,8):
        for j in range(i,8):
            rand = random.random()
            if (j!=i) and (rand < p):
                if ((i in red_nodes) and (j in red_nodes)) or ((i in blue_nodes) and (j in blue_nodes)):
                    G.insert_edge(i,j)
            elif (j!=i) and (rand > p):
                if ((i in red_nodes) and (j in blue_nodes)) or ((j in red_nodes) and (i in blue_nodes)):
                    G.insert_edge(i,j)
    
    #Add new nodes from N
    for i in range(8,N):
        #Growth
        rand_node = random.random()
        if rand_node <= r:
            red_nodes.append(i) 
        else:
            blue_nodes.append(i)
            
        #Preferential attachment    
        sameColor = int(m*p)
        diffColor = int(m*(1-p))
        
        if i in red_nodes:
            #Connect to the SAME RED nodes
            PA_red = Preferential_Att(G,red_nodes)
            red_connect = np.random.choice(red_nodes,sameColor,replace=False,p = PA_red)
            for j in red_connect:
                G.insert_edge(i,j)
            #Connect to the OTHER BLUE nodes
            PA_blue = Preferential_Att(G,blue_nodes)
            blue_connect = np.random.choice(blue_nodes,diffColor,replace=False,p = PA_blue)
            for j in blue_connect:
                G.insert_edge(i,j)
        else: 
             #Connect to the SAME Blue nodes
            PA_blue = Preferential_Att(G,blue_nodes)
            blue_connect = np.random.choice(blue_nodes,sameColor,replace=False,p = PA_blue)
            for j in blue_connect:
                G.insert_edge(i,j)
            #Connect to the OTHER RED nodes
            PA_red = Preferential_Att(G,red_nodes)
            red_connect = np.random.choice(red_nodes,diffColor,replace=False,p = PA_red)
            for j in red_connect:
                G.insert_edge(i,j)           
            
    #Saving the degree value for each node in the dictionary
    for i in G.vertices():
        degree_list[i] = G.degree(i, out=False)
    
    #Saving the degree distribution in the dictionary
    for i in range(max(degree_list.values())+1):
        degree_dist[i] = 0
        for j in degree_list:
            if degree_list[j] == i:
                degree_dist[i] += 1
    #Calculating Pk           
    for i in degree_dist:
        degree_dist[i] = degree_dist[i]/N
    
    return degree_dist

#===========TEST===================
def test():
    print("1. Enter the number of Node, r and p")
    print("2. Enter 4 different values of p for a fixed value of r and number of nodes")
    print("3. Enter 4 different values of r for a fixed value of p and number of nodes")
    print("We should choose the value of P = 0.125,0.25,0.5...Because m =8 and m*p need to be Integer")
    test = int(input("Choose the number of test which you want to test: "))
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