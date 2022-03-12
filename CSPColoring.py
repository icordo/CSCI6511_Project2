'''
CSCI6511 Artificial Intelligence
Project 2 -- CSP Color Graph
Author: I. Cordova
'''


class Graph:
    def __init__(self, edges, vert):
        # A list of lists to represent an adjacency list
        self.adjList = {}
        for key in vert:
            self.adjList[key] = []

        for (x, y) in edges:
            self.adjList[x].append(y)
            self.adjList[y].append(x)


class FinalColor:
    def __init__(self, vert):
        self.color_list = {}
        for val in vert:
            self.color_list[val] = 0


def file_extraction(file):
    '''
    :param file: text file
    :return: max color (int), edges list (list), list of individual vertices (list)
    '''
    open_file = open(file, 'r')
    file = []
    for i in open_file:
        file.append(i)
    color = int(file[2].split()[-1])
    file = file[4:]
    edges_list = []
    vertices_list = []
    for unit in file:
        str_vert = unit.split(",")
        unit_a = int(str_vert[0])
        unit_b = int(str_vert[1].strip())
        edges_list.append([unit_a, unit_b])
        if unit_a not in vertices_list:
            vertices_list.append(unit_a)
        if unit_b not in vertices_list:
            vertices_list.append(unit_b)

    open_file.close()
    return [color, edges_list, vertices_list]


def adjacent_check(graph, color, vert_index, current_color):
    '''
    :param graph: graph includes all edges
    :param color: color results
    :param vert_index: vertice index
    :param current_color: color being checked
    :return:
    '''
    for u in graph.adjList[vertices[vert_index]]:
        if color.color_list[u] == current_color:
            return False
    return True


def color_graph(g, color, max_color, current_vertex_index, total_vert):
    '''
    :param g: graph includes all edges
    :param color: color results
    :param max_color: max colors being used
    :param current_vertex_index: vertice index
    :param total_vert: number of total vertices
    :return:
    '''

    if current_vertex_index == total_vert:
        final_graph_colored.append(color.color_list)
        return True

    for current_color in range(1, max_color + 1):
        if adjacent_check(g, color, current_vertex_index, current_color):
            color.color_list[vertices[current_vertex_index]] = current_color
            color_graph(g, color, max_color, current_vertex_index + 1, total_vert)
            #color.color_list[vertices[current_vertex_index]] = 0


def CSPColoring(file):
    # Extract important data from text file
    output = file_extraction(file)
    max_colors = output[0]
    #edges = [[0, 1], [0, 4], [0, 5], [4, 5], [1, 4], [1, 3], [2, 3], [2, 4]]
    edges = output[1]
    global vertices
    #vertices = [0,1,2,3,4,5]
    vertices = output[2]
    number_of_vertices = len(vertices)
    global final_graph_colored
    final_graph_colored = []
    final_graph = []
    for vertex in edges:
        if vertex not in final_graph and [vertex[1], vertex[0]] not in final_graph:
            final_graph.append(vertex)

    g = Graph(edges, vertices)

    color_result = FinalColor(vertices)

    # print all configurations of the graph
    color_graph(g, color_result, max_colors, 0, number_of_vertices)
    return final_graph_colored
CSPColoring("test_3.txt")