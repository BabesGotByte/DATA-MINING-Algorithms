import math
import time
import random
import sys
import matplotlib.pyplot as plt


class Point(object):
	def __init__(self, location):
		self.visited = False
		self.noise = False
		self.incluster = False
		self.location = location

def import_data(file):
	data = []
	f = open(str(file), 'r')
	for line in f:
		current = line.split()	#enter your own delimiter like ","
		for j in range(0,len(current)):
			current[j] = int(current[j])
		data.append(Point(current))
	print("finished importing data")
	return data

def print_data_matrix(data):
	for i in data:
		print(i.location)

def distance(point1, point2):
	list1 = point1.location
	list2 = point2.location
	distance = 0
	for i in range(0,len(list1)):
		distance += abs(list1[i] - list2[i]) ** 2
	return math.sqrt(distance)

def calaculate_distance_matrix(data):
	distance_matrix =[]
	for i in range(0,len(data)):
		current = []
		for j in range(0,len(data)):
			current.append(distance(data[i], data[j]))
		distance_matrix.append(current)
	return distance_matrix

def regional_query(P, data , distance_matrix , epsilon):
	neighbour = []
	for i in range(0,len(data)):
		if data[i] == P:
			for j in range(0,len(data)):
				if distance_matrix[i][j] < epsilon:
					neighbour.append(data[j])
			break
	return neighbour

def expand_cluster(P, neighbor_pts, Cluster, epsilon, MinPts, data, distance_matrix):
	Cluster.append(P)
	P.incluster = True
	for P_neigh in neighbor_pts:
		if P_neigh.visited != True:
			P_neigh.visited = True
			neighbor_pts_in = regional_query(P_neigh, data , distance_matrix , epsilon)
			if len(neighbor_pts_in) >= MinPts:
				neighbor_pts = neighbor_pts_in + neighbor_pts
		if P_neigh.incluster != True:
			Cluster.append(P_neigh)


def dbscan(data, epsilon, MinPts):
	C = []
	distance_matrix = calaculate_distance_matrix(data)
	for P in data:
		#print P.location

		if P.visited == True:	
			continue
		P.visited = True
		neighbor_pts = regional_query(P, data, distance_matrix, epsilon)
		#print neighbor_pts
		if len(neighbor_pts) < MinPts:
			P.noise = True
		else:
			C.append([])
			expand_cluster(P, neighbor_pts, C[-1], epsilon, MinPts, data, distance_matrix)
	return C

def color(cluster_number):
	colors = []
	for i in range(0,cluster_number):
		colors.append("#%06x" % random.randint(0,0xFFFFFF))
	return colors

def graphic(final):
	colors = color(len(final))
	plt.ion()
	plt.figure()
	i = 0
	for cluster in final:
		dum = []
		for point in cluster:
			dum.append(point.location)
		x_ = [x for [x,y] in dum]
		y_ = [y for [x,y] in dum]
		#print(colors[i])
		plt.plot(x_, y_ , colors[i] , marker='o', ls='')
		i += 1
	plt.gca().set_aspect('equal', adjustable='box')
	plt.axis('equal')
	plt.show(block=False)
	plt.pause(10)
	plt.close()


def print_cluster(final):
	for i in range(0,len(final)):
		print("cluster ", i+1)
		print_data_matrix(final[i])



if __name__ == '__main__':
	data = import_data(sys.argv[1])
	epsilon = 1000
	min_pts = 50
	start = time.time()
	final = dbscan(data, epsilon, min_pts)
	print_cluster(final)
	print(time.time() - start, "seconds elapsed")
	graphic(final)

