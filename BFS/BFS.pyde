from Spot import Spot
import Queue as queue
import time
from collections import deque


w=0
h=0
end_=[]
start = []
grid = []

total_f = 0
fuel = 500

openSet = deque()
closedSet = []
path = deque()
current = []

cols = 50
rows = 50

def setup():
    global grid, start, w, h, end_, fuel
    size(800,800)
    print("Comidas: {} Combustivel: {}".format(total_f, fuel))
    #background(101, 157, 108)
    
    w = width/cols
    h = height/rows
    
    grid = []
    for i in range(cols):
        linha = []
        for j in range(rows):
            linha.append(Spot(i, j))
        grid.append(linha)
        
    for i in range(cols):
        for j in range(rows):
            grid[i][j].addNeighbors(grid)
    
    #reset_previous()
            
    start = grid[int(random(49))][int(random(49))]
    end_ = grid[int(random(49))][int(random(49))]
    start.cost = 1
    end_.cost = 1
    
    openSet.append(start)

    
def draw():
    global grid, openSet, start, w, h, end_, closedSet, path, current, total_f, fuel

    search = True
    
    if current == end_:
        openSet.clear()
        closedSet = []
        
        if len(path) == 0:
            total_f += 1
            fuel += 50
            start = end_

            openSet.append(start)

            end_ = grid[int(random(49))][int(random(49))]
            print("Comidas: {}  Combustivel: {}".format(total_f, fuel))
            while(end_.cost == 9999):
                print("???")
                end_ = grid[int(random(49))][int(random(49))]
            reset_previous()
        else:
            search = False
    else:
        if len(openSet) > 0:
            current = openSet[0]
            if current != end_:
                openSet.popleft()
                closedSet.append(current)
                neighbors = current.neighbors
                
                for i in range(len(neighbors)):
                    neighbor = neighbors[i]
                    if not neighbor in closedSet and not neighbor in openSet and not neighbor.cost == 9999:
                        neighbor.previous = current
                        openSet.append(neighbor)
        else:
            print("NO SOLUTION")
         
     
    #######################
    pos = start
    if search == False:
        pos = path.popleft()
        fuel -= pos.cost
        if(fuel < 1):
            print("ACABOU A GASOLINA")
            noLoop()
            return
        time.sleep(0.1)
    else:
        path.clear()
        temp = current
        path.append(temp)
        
        while temp.previous:
            path.append(temp.previous)
            temp = temp.previous
        path.reverse()
    
    #########################
    
    for i in range(cols):
        for j in range(rows):
            grid[i][j].show()
    
    
    # Carro
    fill(255, 0, 0);
    beginShape();
    rect(pos.i*w, pos.j*h, h, w)
    endShape();
    

    #Comida
    beginShape();
    fill(255, 0, 200);
    rect(end_.i * w, end_.j * h, h, w)
    endShape();

    #ClosedSet
    fill(255, 255, 255, 50);
    for i in range(len(closedSet)):
        if closedSet[i] == start or closedSet[i] == end_:
            continue;
        beginShape();
        rect(closedSet[i].i * w, closedSet[i].j * h, h, w)
        endShape();
        
    #OpenSet
    fill(0, 0, 0, 50);
    for i in range(len(openSet)):
        x = openSet[i]
        if (x == start):
            continue;
        beginShape();
        rect(x.i * w, x.j * h, h, w)
        
        endShape();
    
    #Path Draw
    fill(255, 0, 0);
    noStroke();
    beginShape();
    for i in range(len(path)):
        rect(path[i].i * w + w / 2, path[i].j * h + h / 2, w/3, h/3)
    endShape();
    
        
def reset_previous():
    for i in range(49):
        for j in range(49):
            grid[i][j].previous = None
