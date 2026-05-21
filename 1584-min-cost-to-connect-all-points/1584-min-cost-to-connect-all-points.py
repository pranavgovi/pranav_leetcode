class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, total_nodes):
                self.parent = [node for node in range(total_nodes)]
                self.rank = [0]*total_nodes
            
            def find(self, node):
                #find the parent of this node
                if self.parent[node]!=node:
                    self.parent[node]=self.find(self.parent[node])

                return self.parent[node]
            
            def union(self, pt1, pt2):
                parent1, parent2 = self.find(pt1), self.find(pt2)
                if parent1==parent2:
                    #cannot be combined
                    return False

            #if they are not equal we can just attach
                if self.rank[parent1]>self.rank[parent2]:
                    self.parent[parent2]= parent1
                elif self.rank[parent1]<self.rank[parent2]:
                    self.parent[parent1]= parent2
                else:
                    self.rank[parent1]+=1
                    self.parent[parent2]= parent1
                return True
        def kruskal(points):
            
            edges = []
            n=len(points)
            u = UnionFind(n)
            for i in range(n-1):
                for j in range(i+1, n):
                    x1, y1  = points[i]
                    x2,y2 = points[j]
                    wt = abs(x1-x2)+ abs(y1-y2)
                    edges.append([wt, i, j])

            tot_edges=0
            tot_cost=0
            edges.sort()
            for ind,edge in enumerate(edges):
                weight, pt1,pt2 = edge
                if u.union(pt1, pt2):
                    #if this is tru tehy can be combined as an edge
                    tot_edges+=1
                    tot_cost+=weight
                
                if tot_edges==n-1:
                    return tot_cost
            return 0
        return kruskal(points)