'''
This is the file which helps the model to localize the state it feels it is in for any task as such.

Firstly we will try to use gpt-4v and check if we are able to localize properly 

Key inputs for it to take actions : (for deciding the task )
1) Your prompt - either in the form of text, or your audio(text)
2) memory patters - from past actions ( tidious or tough things which can be guessed from memory)
3) prediction - 
		example - buying pizza requires you to actually navigate to the pizza site 

Input( for the model) :
1) observation - current screenshot 
2) trajectory of actions - 
3) understanding of state - inferred from 1,2 

'''
# import torch
# from torch_geometric.data import Data

# edge_index = torch.tensor([[0, 1, 1, 2],
#                            [1, 0, 2, 1]], dtype=torch.long)
# x = torch.tensor([[-1], [0], [1]], dtype=torch.float)
# print(edge_index)
# #print(x)
# #data = Data(x=x, edge_index=edge_index)
# data = Data(x=x, edge_index=edge_index.t().contiguous())
# #Data(edge_index=[2, 4], x=[3, 1])
# print(Data)
# print(data.num_nodes)
# #print(Data.edges)

# trying out the graph using nx
import networkx as nx
G = nx.DiGraph()

G.add_nodes_from([0], type='home_screen')
G.add_nodes_from([1], type='valorant')
G.add_nodes_from([2], type='youtube')
G.add_edge(1, 2)
G.add_edges_from([(2, 1), (0, 1)])

print(G.nodes)
print(G.edges)
print(G.nodes[1])
#G.add_edge(2, 3, action='click')

def add_interaction(G, prev_state, state , action, type):
    if G.has_node(state):
        G.add_edge(prev_state, state, action=action)
    else:
        G.add_node(state, type=type)
        G.add_edge(prev_state, state, action=action)

add_interaction(G, 2, 3, 'click', 'valorant')
add_interaction(G, 2, 4, 'double_click', 'notepad')
add_interaction(G, 2, 5, 'type', 'valorant_b')
add_interaction(G, 5, 0, 'type', 'valorant_b')
print(G.nodes[0])
import matplotlib.pyplot as plt
subax1 = plt.subplot(121)
nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
plt.show()

