# Grama: cost = 1
# Lama: cost = 5
# Agua: cost = 10
# Obstaculo: cost = 9999

class Spot():
    def __init__(self, i, j):
        # position
        self.i = i
        self.j = j
        
        # cost
        self.cost = 1
        
        if random(1) < 0.6:
            self.cost = 5
            if random(1) < 0.4:
                self.cost = 10
                if random(1) < 0.4:
                    self.cost = 9999
        
        # neighbors
        self.neighbors = []
        
        #
        self.previous = None
        
        
        
        
    def show(self):
        if self.cost == 1:
            fill(101, 157, 108)
        elif self.cost == 5:
            fill(192, 157, 108)
        elif self.cost == 10:
            fill(137, 157, 255)
        elif self.cost == 9999:
            fill(0)
        rect(self.i*16, self.j*16, 16, 16)
            
    def addNeighbors(self, grid):
        i = self.i
        j = self.j
        
        if i < 49: #cols
            self.neighbors.append(grid[i+1][j])
            
        if i > 0:
            self.neighbors.append(grid[i-1][j])
            
        if j < 49: #rows
            self.neighbors.append(grid[i][j+1])
            
        if j > 0:
            self.neighbors.append(grid[i][j-1])
