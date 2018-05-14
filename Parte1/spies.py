#!/usr/bin/python

import sys
import argparse
import math
import heapq

class Node:
	def __init__(self, x, y):
		self._x = x
		self._y = y

	def get_x(self):
		return self._x

	def get_y(self):
		return self._y

	def __str__(self):
		return "x: " + str(self._x) + ", y: " + str(self._y)

	def __hash__(self):
		return hash((self._x, self._y))

	def __eq__(self, other):
		return (
			self._x == other._x and
			self._y == other._y
		)

	def __ne__(self, other):
		return (
			self._x != other._x or
			self._y != other._y
		)

	def get_distance(self, other):
		return math.sqrt(
				(self._x-other._x)**2 +
				(self._y-other._y)**2)

#Grafo del mapa
map_graph = {} #sera un diccionario: clave= nodo, valor= conjunto de nodos adyacentes

#O(V + E)
def BFS(map_graph, start_node, end_node):
	bfs_tree = {} #el arbol BFS
	discovered_nodes = set({start_node}) #set de nodos ya visitados
	layers = [set()] #lista de capas
	layers[0]= {start_node} #capa inicial
	layer_index = 0
	new_nodes_discovered = True

	print "******* Se ejecuta BFS ***********"
	print "Nodo inicial: " + str(start_node)
	print "Nodo final: " + str(end_node)

	while new_nodes_discovered:
		new_nodes_discovered = False
		#print "Start layer " + str(layer_index)
		for current_layer_node_i in layers[layer_index]: #se recorre la capa actual
			next_level_nodes_set = map_graph[current_layer_node_i] #set de nodos adyacentes
			#print "BFS: next level nodes set => "
			#print next_level_nodes_set

			layers.append(set())
			for adj_node in next_level_nodes_set: #se recorren todos los adyacentes
				if adj_node not in discovered_nodes:
					new_nodes_discovered = True
					#print "BFS: Se visita un nuevo nodo: " + str(adj_node.get_x())+', '+str(adj_node.get_y())
					layers[layer_index+1].add(adj_node) #se va armando la siguiente capa
					discovered_nodes.add(adj_node)
					if current_layer_node_i not in bfs_tree:
						bfs_tree.update({current_layer_node_i:{adj_node}}) #se va armando el arbol BFS
					else:
						bfs_tree[current_layer_node_i].add(adj_node) #se va armando el arbol BFS
					if adj_node == end_node:
						return layer_index + 1
		layer_index += 1

	return -1

def dijkstra(map_graph, start_node, end_node):
	nodes_distances = {} #diccionario de distancias
	nodes_distances[start_node] = 0

	print "******* Se ejecuta Dijkstra ***********"
	print "Nodo inicial: " + str(start_node)
	print "Nodo final: " + str(end_node)

	priority_queue = []
	heapq.heappush(priority_queue, (0, start_node))

	while priority_queue:
		node_tuple_i = heapq.heappop(priority_queue)
		if end_node == node_tuple_i[1]:
			#print "BFS: se visito el nodo final!"
			return node_tuple_i[0]
		#print "Nodo actual ----> " + str( node_tuple_i[1])
		next_level_nodes_set = map_graph[node_tuple_i[1]]
		for adj_node in next_level_nodes_set: #se recorren los adyacentes
			#Se actualiza la distancia al nodo adyacente de ser necesario
			new_distance = nodes_distances[node_tuple_i[1]] + adj_node.get_distance(node_tuple_i[1])
			if (adj_node not in nodes_distances) or (new_distance < nodes_distances[adj_node]):
				#Se encontro una distancia menor
				nodes_distances[adj_node] = new_distance
				heapq.heappush(priority_queue, (new_distance, adj_node))
				
	return 0

def load_map_from_file(map_graph):
	with open('mapa.coords') as fp:
		for line in fp:
			node_1,node_2 = line.split('-')
			x,y,_= node_1.split(' ')
			new_node_1 = Node(int(x),int(y))
			_,x,y= node_2.split(' ')
			new_node_2 = Node(int(x),int(y))
			if new_node_1 not in map_graph:
				map_graph.update({new_node_1:{new_node_2}})
			else:
				map_graph[new_node_1].add(new_node_2)
			if new_node_2 not in map_graph:
				map_graph.update({new_node_2:{new_node_1}})
			else:
				map_graph[new_node_2].add(new_node_1)

def check_algorithm(value):
	valid_algorithms = ['B', 'D']
	if value not in valid_algorithms:
		raise argparse.ArgumentTypeError("%s no es un algoritmo valido. Usar B o D. Ver -h" % value)
	return value

def main():
	print "TP2 - Parte 1: Spy vs Spy"
	
	parser = argparse.ArgumentParser()
	parser.add_argument("algorithm", help="algorithm to use: B for BFS, D for Dijkstra", type=check_algorithm)
	parser.add_argument("spy1_x", help="x coord for spy 1", type=int)
	parser.add_argument("spy1_y", help="y coord for spy 1", type=int)
	parser.add_argument("spy2_x", help="x coord for spy 2", type=int)
	parser.add_argument("spy2_y", help="y coord for spy 2", type=int)
	parser.add_argument("airport_x", help="x coord for airport", type=int)
	parser.add_argument("airport_y", help="y coord for airport", type=int)

	args = parser.parse_args()

	spy1 = Node(int(args.spy1_x), int(args.spy1_y))
	spy2 = Node(int(args.spy2_x), int(args.spy2_y))
	airport = Node(int(args.airport_x), int(args.airport_y))
	load_map_from_file(map_graph)

	if args.algorithm == 'B':
		spy1_edges_count = BFS(map_graph, spy1, airport)	
		spy2_edges_count = BFS(map_graph, spy2, airport)	
	else:
		spy1_edges_count = dijkstra(map_graph, spy1, airport)
		spy2_edges_count = dijkstra(map_graph, spy2, airport)

	print "Distancia del esp"+u'\u00ed'+"a 1 al aeropuerto = "+ str(spy1_edges_count)
	print "Distancia del esp"+u'\u00ed'+"a 2 al aeropuerto = "+ str(spy2_edges_count)

	if spy1_edges_count < spy2_edges_count:
		print "El esp"+u'\u00ed'+"a 1 llegar"+u'\u00e1'+ " antes al aeropuerto."
	else:
		if spy1_edges_count > spy2_edges_count:
			print "El esp"+u'\u00ed'+"a 2 llegar"+u'\u00e1'+ " antes al aeropuerto."
		else:	
			print "Los 2 esp"+u'\u00ed'+"as llegar"+u'\u00e1'+"n al mismo tiempo."

if __name__ == "__main__":
	main()
