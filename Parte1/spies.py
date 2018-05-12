#!/usr/bin/python

import sys
import argparse

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
		return hash(self._x)+hash(self._y)

	def __eq__(self, other):
		return (
			self.__class__ == other.__class__ and
			self._x == other._x and
			self._y == other._y
		)

	def __ne__(self, other):
		return (
			self.__class__ != other.__class__ or
			self._x != other._x or
			self._y != other._y
		)

#	def get_distance(self, node):
#		"""Distancia euclidea"""
#		return 0

#Grafo del mapa
map_graph = {} #sera un diccionario: clave= nodo, valor= conjunto de nodos adyacentes

#O(V + E)
def BFS(map_graph, start_node, end_node):
	bfs_tree = {} #el arbol BFS
	discovered_nodes = set() #set de nodos ya visitados
	layers = [set()] #lista de capas
	layers[0]= {start_node} #capa inicial
	layer_index = 0
	new_nodes_discovered = True
#	print "BFS: map graph => " 
#	print map_graph
	#print "BFS: layers => "
	#print layers

	print start_node
	print end_node

	while new_nodes_discovered:
		new_nodes_discovered = False
		for current_layer_node_i in layers[layer_index]: #se recorre la capa actual
			next_level_nodes_set = map_graph[current_layer_node_i] #set de nodos adyacentes
			print "BFS: next level nodes set => "
			print next_level_nodes_set

			layers.append(set())
			for adj_node in next_level_nodes_set: #se recorren todos los adyacentes
				if adj_node not in discovered_nodes:
					new_nodes_discovered = True
					print "BFS: Se visita un nuevo nodo: " + str(adj_node.get_x())+', '+str(adj_node.get_y())
					layers[layer_index+1].add(adj_node) #se va armando la siguiente capa

					#print "BFS: layers => "
					#print layers

					discovered_nodes.add(adj_node)
					if current_layer_node_i not in bfs_tree:
						bfs_tree.update({current_layer_node_i:{adj_node}}) #se va armando el arbol BFS
					else:
						bfs_tree[current_layer_node_i].add(adj_node) #se va armando el arbol BFS
					if adj_node == end_node:
						return layer_index + 1
			layer_index += 1

	return -1

def load_map(map_graph):
	

def main():
	print "TP2 - Parte 1: Spy vs Spy"
	
	parser = argparse.ArgumentParser()
	parser.add_argument("spy1_x", help="x coord for spy 1", type=int)
	parser.add_argument("spy1_y", help="y coord for spy 1", type=int)
	parser.add_argument("spy2_x", help="x coord for spy 2", type=int)
	parser.add_argument("spy2_y", help="y coord for spy 2", type=int)
	parser.add_argument("airport_x", help="x coord for airport", type=int)
	parser.add_argument("airport_y", help="y coord for airport", type=int)

	args = parser.parse_args()
	
	#TODO leer grafo de mapa.coords y cargarlo en memoria
	#load_map(map_graph)
	node_i = Node(1,1) #spy 1
	node_j = Node(2,2)
	node_k = Node(3,3)
	node_l = Node(4,4) #airport
	node_m = Node(2,1) #spy 2
	node_n = Node(10,29)
	map_graph = {node_i:{node_j, node_m},
				 node_j:{node_k, node_i},
				 node_k:{node_j, node_l},
				 node_m:{node_i, node_n},
				 node_n:{node_l, node_m}}

	#spy1_edges_count = BFS(graph, spy1, airport)
	spy1_edges_count = BFS(map_graph, node_i, node_l)
	print "spy1_edges_count = "+ str(spy1_edges_count)

	#spy2_edges_count = BFS(graph, spy2, airport)
	spy2_edges_count = BFS(map_graph, node_m, node_l)
	print "spy2_edges_count = "+ str(spy2_edges_count)

	if spy1_edges_count < spy2_edges_count:
		print "Spy1 wins!"
	else:
		if spy1_edges_count > spy2_edges_count:
			print "Spy2 wins!"
		else:	
			print "The spies tie!"
	
if __name__ == "__main__":
	main()
