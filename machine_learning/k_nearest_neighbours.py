#!/usr/bin/env python3
# encoding: utf-8

# k_means_clust.py	# This file's Name

#from editor import *			# Idea From David Beazley working "en vivo"
								# Toutes les Libraries indispensables

# Dans le Terminal: PS1="\$ " ===> Un prompt minimal!!!

from pprint import pprint		# A importer toujours...car tres utile
# print ("dir() === Indispensables en direct dans le Terminal"); pprint(dir())	


__ref__ = """
# ===  References  ===
# Reworked by < ZZ > : --- on : --- 12/8/19, 20:32

LES REFERENCES SONT OBLIGATOIRES...
https://github.com/kilimandjaro2/Python

Created by ZZ - 3/5/18, 7:13 PM.
Copyright (c) 2018 __MyCompanyName__. All free rights .

"""

__doc__ = """
# ===  Documentation  ===
# Template  minimum
	  traiter les sources avec ypf
	  https://yapf.now.sh/
(Yet another Python formatter)
# ===========================

=== Procedure a suivre: ===
# <Indispensable>

0/Presentation:
Une seule file qui est auto-suffisante, car elle comporte tout a la fois:
	-Le programme
	-Le lancement de L'Execution
	-Le resultat de l'Execution
tout cela sans quitter notre Editeur favori: BBEDIT!

1/Edition
Pour un maximum de clarte:
	Faire le menage dans les noms de folders et de files (en particulier, des files identiques en .py et .ipynd doivent porter des noms identiques(seule change l'extension)
	
Puis Editer dans BBEDITun job en se servant de ce Template.

2/Runs et Tests
En plus il comporte, via le "if __name__ == '__main__', un moyen de le tester "in extenso" ou de le garder tel quel pour des Imports.

3/Les sorties
Elles sont incorporees a cette file, via un "Cut and paste" dans la variable "output"

4/Une fois totalement edite, la file est incorporee dans Jupyter via un "Cut and paste"

5/Corrections minimes
Apres suppression du "Shebang", ce job runs  directement dans un Notebook sous Jupyter

6/Autre solulion (preferable), l'Import
Il est preferable de faire un import des noms de domaine du fichier  .py, car ainsi on ne conserve qu'un exemplaire de source unique.


Et aussi...

Cas de recuperation d'anciens codes:
====================================
1/3 Examen du contenu:
	deux blancs pour l'indentation ===> 1 tabulation

2/3   2to3 for Converting Python 2 scripts to Python 3
	Ref: la Doc de Python3:
		https://docs.python.org/2/library/2to3.html
		
	explications:
	https://pythonprogramming.net/converting-python2-to-python3-2to3/
	et
	Outil:   2to3 on Line:
	https://www.pythonconverter.com/


3/3	YAPF (Yet another Python formatter)
	https://yapf.now.sh/

"""


def first():
	"""<first() Documentation>"""

	print("""< # Entering"first"   > """)
	print("""< # Doing hard Work...   > """)
	print("""< # END of "first"	> """)
	return
	   
	   
	   
	   
import numpy as np
from collections import Counter
from sklearn import datasets
from sklearn.model_selection import train_test_split

data = datasets.load_iris()

X = np.array(data["data"])
y = np.array(data["target"])
classes = data["target_names"]

X_train, X_test, y_train, y_test = train_test_split(X, y)


def euclidean_distance(a, b):
	"""
	Gives the euclidean distance between two points
	>>> euclidean_distance([0, 0], [3, 4])
	5.0
	>>> euclidean_distance([1, 2, 3], [1, 8, 11])
	10.0
	"""
	return np.linalg.norm(np.array(a) - np.array(b))


def classifier(train_data, train_target, classes, point, k=5):
	"""
	Classifies the point using the KNN algorithm
	k closest points are found (ranked in ascending order of euclidean distance)
	Params:
	:train_data: Set of points that are classified into two or more classes
	:train_target: List of classes in the order of train_data points
	:classes: Labels of the classes
	:point: The data point that needs to be classifed

	>>> X_train = [[0, 0], [1, 0], [0, 1], [0.5, 0.5], [3, 3], [2, 3], [3, 2]]
	>>> y_train = [0, 0, 0, 0, 1, 1, 1]
	>>> classes = ['A','B']; point = [1.2,1.2]
	>>> classifier(X_train, y_train, classes,point)
	'A'
	"""
	data = zip(train_data, train_target)
	# List of distances of all points from the point to be classified
	distances = []
	for data_point in data:
		distance = euclidean_distance(data_point[0], point)
		distances.append((distance, data_point[1]))
	# Choosing 'k' points with the least distances.
	votes = [i[1] for i in sorted(distances)[:k]]
	# Most commonly occuring class among them
	# is the class into which the point is classified
	result = Counter(votes).most_common(1)[0][0]
	return classes[result]


if __name__ == "__main__":
	print(classifier(X_train, y_train, classes, [4.4, 3.1, 1.3, 1.4]))


output = """
setosa
logout
"""