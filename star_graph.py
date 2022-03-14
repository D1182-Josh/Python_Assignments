    #TASK
 
#There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connet the center node with every other node. You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph. 
    Example 1: 
        Input : edges = [[1,2], [2,3], [4,2]]
        Output : 2

#        Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is center.

    Example 2:
        Input: edges = [[1,2],[5,1],[1,3],[1,4]]
        Output: 1

      #SOLUTION1

edges = [[1,2],[2,3],[4,2]]

max([j for i in edges for j in i ], key=[j for i in edges for j in i ].count)

    #SOLUTION2

num = list(map(int, input().split()))
liste = []
if len(num) % 2 == 0 :
  for i in range(0,len(num) // 2 +1,2) :
    liste += [[num[i],num[i+1]]]
  for i in range(len(liste)-1) :
    if len(set(liste[i]) - set(liste[i+1])) == 1 :
      print(liste)
    else :
      print("yıldız oluşturmaya uygun bir sayı dizesi giriniz")
else :
  print("yıldız oluşturmaya uygun bir sayı dizesi giriniz")

    #SOLUTION3

      
