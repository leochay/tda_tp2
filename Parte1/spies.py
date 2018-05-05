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

#	def get_distance(self, node):
#		"""Distancia euclidea"""
#		return 0

#Grafo del mapa
map_graph = {}
discovered_nodes = {} #set de nodos ya visitados
layers = [] #las capas del arbol BFS
bfs_tree = {} #el arbol BFS

def BFS(start_node, end_node):
	layer_index = 0
	layers[0].add({start_node}) #capa inicial

	#build the next layer
	for node_i in layers[layer_index]:
		next_level_nodes = map_graph[node_i] #set of adjacent nodes
		for adj_node in next_level_nodes:
			if adj_node not in discovered_nodes:
				print str(adj_node.get_x())+', '+str(adj_node.get_y())
				layers[layer_index+1].add(adj_node)
				discovered_nodes.add(adj_node)
		layer_index += 1

	#return distance

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
	#print str(args.spy1_x) + " " + str(args.spy1_y)
	
	#leer grafo de mapa.coords y cargarlo en memoria

	node_i = Node(1,1) #spy 1
	node_j = Node(2,2)
	node_k = Node(3,3)
	node_l = Node(4,4) #airport
	node_m = Node(2,1) #spy 2
	node_n = Node(10,29)
	map_graph = {node_i:{node_j, node_l},
				 node_j:{node_k},
				 node_k:{node_l},
				 node_m:{node_n},
				 node_n:{node_l}}
	
	#spy1_edges_count = BFS(spy1, airport)
	#spy2_edges_count = BFS(spy2, airport)
#	spy1_edges_count = BFS(node_i, node_l)
#	spy2_edges_count = BFS(node_m, node_l)
	"""
	if spy1_edges_count < sp2_edges_count:
		print "Spy1 wins!"
	else:
		if spy1_edges_count > sp2_edges_count:
			print "Spy2 wins!"
		else:	
			print "The spies tie!"
	"""
if __name__ == "__main__":
	main()
