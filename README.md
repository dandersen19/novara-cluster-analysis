# novara-cluster-analysis
Cluster analysis of Earle Brown's composition *Novara* (1962) for mixed octet. Clusters the twenty events based on normalized pitch class distribution (profile) using k-means algorithm.

Three versions:

1. Cluster analysis using a single value for k (4 by default, to compare with 4 pages in score).
2. Cluster analysis using values in range 1-20 for k.
3. Cluster analysis outputting graph of sum of squares for "elbow" test.

If .py file run as module, Excel file saved to directory where file is saved. If run line by line, saved to Documents. Pitch data retrieval from XML file via music21 library.
