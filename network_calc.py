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
    # Calculate Density
    density = np.round(nx.density(G), 3)
    # Calculate longest path
    try:
        components = nx.connected_components(G)
        largest_component = max(components, key=len)
        subgraph = G.subgraph(largest_component)
        diameter = nx.diameter(subgraph)
    except:
        diameter = 0
    # Calculate transitivity
    triadic_closure = np.round(nx.transitivity(G), 3)
    # Calculate max degree
    try:
        degree_centrality = nx.degree_centrality(G)
        max_centrality_ind = np.argmax(list(degree_centrality.values()))
        central_node = list(degree_centrality.keys())[max_centrality_ind]
        central_node_title = df_blocks[df_blocks['id'] == central_node]['title'].values[0]
        central_node_val = np.round(list(degree_centrality.values())[max_centrality_ind], 3)
    except:
        central_node = 0
        central_node_title = ''
        central_node_val = 0
    return density, diameter, triadic_closure, central_node, central_node_title, central_node_val
