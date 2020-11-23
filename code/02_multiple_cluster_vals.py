# Earle Brown's Novara for mixed octet (1962)
# k-means cluster analysis using multiple numbers of clusters (n_clusters)

from music21 import *
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

novara = converter.parse('/Users/drakeandersen/novara-full.xml')

# by event
event11, event12, event13, event14, event15, event21, event22, event23, event24, event25, event31, event32, event33, event34, event35, event41, event42, event43, event44, event45 = [p.pitchClass for p in novara.measures(1, 6).pitches], [p.pitchClass for p in novara.measures(8, 15).pitches], [p.pitchClass for p in novara.measures(17, 21).pitches], [p.pitchClass for p in novara.measures(23, 25).pitches], [p.pitchClass for p in novara.measures(27, 29).pitches], [p.pitchClass for p in novara.measures(31, 32).pitches], [p.pitchClass for p in novara.measures(34, 37).pitches], [p.pitchClass for p in novara.measures(39, 40).pitches], [p.pitchClass for p in novara.measures(42, 46).pitches], [p.pitchClass for p in novara.measures(48, 50).pitches], [p.pitchClass for p in novara.measures(67, 67).pitches], [p.pitchClass for p in novara.measures(69, 69).pitches], [p.pitchClass for p in novara.measures(71, 71).pitches], [p.pitchClass for p in novara.measures(73, 73).pitches], [p.pitchClass for p in novara.measures(76, 77).pitches], [p.pitchClass for p in novara.measures(79, 82).pitches], [p.pitchClass for p in novara.measures(84, 85).pitches], [p.pitchClass for p in novara.measures(87, 89).pitches], [p.pitchClass for p in novara.measures(91, 91).pitches], [p.pitchClass for p in novara.measures(93, 95).pitches]

# all events
all_events = [event11, event12, event13, event14, event15, event21, event22, event23, event24, event25, event31, event32, event33, event34, event35, event41, event42, event43, event44, event45]

# get pitch class profile for any group
def getProfile(group):
	profile = [0] * 12
	for note in group:
		for i in range(12):
			if (note == i):
				profile[i] += 1
	return profile

# run the function for all groups and store in new variables
e11, e12, e13, e14, e15, e21, e22, e23, e24, e25, e31, e32, e33, e34, e35, e41, e42, e43, e44, e45 = [getProfile(event) for event in all_events]

# update all_events
all_events = [e11, e12, e13, e14, e15, e21, e22, e23, e24, e25, e31, e32, e33, e34, e35, e41, e42, e43, e44, e45]

# convert to numpy arrays
e11, e12, e13, e14, e15, e21, e22, e23, e24, e25, e31, e32, e33, e34, e35, e41, e42, e43, e44, e45 = [np.asarray(event) for event in all_events]

# update all_events again (now that we've switched to numpy)
all_events = [e11, e12, e13, e14, e15, e21, e22, e23, e24, e25, e31, e32, e33, e34, e35, e41, e42, e43, e44, e45]

# scale to 0-1 range (relative frequency instead of absolute for easier comparison)
e11, e12, e13, e14, e15, e21, e22, e23, e24, e25, e31, e32, e33, e34, e35, e41, e42, e43, e44, e45 = [np.interp(a, (a.min(), a.max()), (0,1)) for a in all_events]

# update all_events yet again (now that we've scaled the range)
all_events = [e11, e12, e13, e14, e15, e21, e22, e23, e24, e25, e31, e32, e33, e34, e35, e41, e42, e43, e44, e45]

# combine everything into a single data frame
all_events = pd.DataFrame(np.row_stack(all_events))

# do k-means cluster analysis several times using different numbers of clusters

# n = 2
km = KMeans(n_clusters=2)
clusters_predicted2 = km.fit_predict(all_events[[0,1,2,3,4,5,6,7,8,9,10,11]])
all_events['Clusters_2'] = clusters_predicted2

# n = 3
km = KMeans(n_clusters=3)
clusters_predicted3 = km.fit_predict(all_events[[0,1,2,3,4,5,6,7,8,9,10,11]])
all_events['Clusters_3'] = clusters_predicted3

# n = 4
km = KMeans(n_clusters=4)
clusters_predicted4 = km.fit_predict(all_events[[0,1,2,3,4,5,6,7,8,9,10,11]])
all_events['Clusters_4'] = clusters_predicted4

# n = 5
km = KMeans(n_clusters=5)
clusters_predicted5 = km.fit_predict(all_events[[0,1,2,3,4,5,6,7,8,9,10,11]])
all_events['Clusters_5'] = clusters_predicted5

# n = 6
km = KMeans(n_clusters=6)
clusters_predicted6 = km.fit_predict(all_events[[0,1,2,3,4,5,6,7,8,9,10,11]])
all_events['Clusters_6'] = clusters_predicted6

# n = 7
km = KMeans(n_clusters=7)
clusters_predicted7 = km.fit_predict(all_events[[0,1,2,3,4,5,6,7,8,9,10,11]])
all_events['Clusters_7'] = clusters_predicted7

# n = 8
km = KMeans(n_clusters=8)
clusters_predicted8 = km.fit_predict(all_events[[0,1,2,3,4,5,6,7,8,9,10,11]])
all_events['Clusters_8'] = clusters_predicted8

# cluster membership for each value n given as columns at right of table

# export dataframe to Excel
all_events.to_excel("cluster_results.xlsx")

# file saved to same directory as this *.py is run from
# if run line by line in shell, saves to Documents by default
