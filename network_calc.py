import networkx as nx
import numpy as np

def calc_density(df_blocks, df_links):
    # Get nodes
    nodes = df_blocks['id'].to_list()
    # Get edges
    edge_start = df_links['starting_block'].to_list()
    edge_end = df_links['ending_block'].to_list()
    edges = tuple(zip(edge_start, edge_end))
    # Create Graph
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    density = np.round(nx.density(G), 3)
    return density
