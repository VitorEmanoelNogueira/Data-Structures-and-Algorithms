class UnionFind:
    def __init__(self, n):
        # Each element is initially its own parent
        self.parent = list(range(n))
        self.rank = [0] * n 
        
    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]   
    
    def union(self, x, y):
        # find the sets parents
        p_x = self.find(x)
        p_y = self.find(y)
        
        
        if p_x == p_y:
            return # already in the same set
        
        # Union by rank
        if self.rank[p_x] < self.rank[p_y]:
            self.parent[p_x] = p_y
        elif self.rank[p_x] > self.rank[p_y]:
         self.parent[p_y] = p_x
        else:
            self.parent[p_y] = p_x
            self.rank[p_x] += 1
            
                        
if __name__ == "__main__":
    uf = UnionFind(10)
    uf.union(0,1)
    uf.union(0,2)
    uf.union(3,4)
    uf.union(5,6)
    print(uf.find(1))
    print(uf.find(2))
    print(uf.find(4))
    print(uf.find(6))
    print("------------")
    uf.union(5,1)
    uf.union(3,2)
    print(uf.find(1))
    print(uf.find(2))
    print(uf.find(4))
    print(uf.find(5))
    print(uf.find(6))
    