# novara-cluster-analysis
Cluster analysis of Earle Brown's composition *Novara* (1962) for mixed octet. Clusters the twenty events based on normalized pitch class distribution (profile) using k-means algorithm. Pitch data retrieval from XML file and processing via music21 library.

Link to composition on Earle Brown Music Foundation website: http://earle-brown.org/works/view/28

Three versions:

1. Cluster analysis using a single value for k (4 by default, to compare with 4 pages in score). Dumps results (pitch class profile for each event and cluster membership) in Excel file.
2. Cluster analysis using values in range 2-8 for k. Dumps results (pitch class profile for each event and cluster membership for each value k) in Excel file.
3. Cluster analysis using values in range 1-20 for k. Outputs graph of sum of squares for "elbow" test.

If .py file run as module, Excel file saved to directory where file is saved. If run line by line, saved to Documents. Columns = pitch class, rows = events (1-1 to 4-5 numbered 1-20).
