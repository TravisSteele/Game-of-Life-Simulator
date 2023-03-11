class Rule:
    def __init__(self, birth, survival):
        self.s = survival
        self.b = birth
    def isKill(self, cell, plane):
        return False if cell.getHood(plane).count(1) in self.s else True
    def isBorn(self, cell, plane):
        return True if cell.getHood(plane).count(1) in self.b else False

class Cell:
    def __init__(self, rule, state, position):
        self.rule = rule
        self.state = state
        self.x = position[0]
        self.y = position[1]
    def getHood(self, plane):
        return list(map(lambda x: plane[(x[0] + self.x) % len(plane)][(x[1] + self.y) % len(plane)], [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]))
    def update(self, plane):
        if self.rule.isBorn(self, plane):
            return 1
        elif self.rule.isKill(self, plane):
            return 0
        else:
            return self.state
class Plane:
    def __init__(self, pattern, rule):
        self.p = pattern
        self.rule = rule
        self.cells = self.initialize()
    def initialize(self):
        newList = []
        for i in range(len(self.p)):
            newList.append([])
            for j in range(len(self.p[i])):
                newList[i].append(Cell(self.rule, self.p[i][j], [i,j]))
        return newList
    def simulate(self):
        newList = []
        for i in range(len(self.p)):
            newList.append([])
            for j in range(len(self.p[i])):
                newList[i].append(self.cells[i][j].update(self.p))
        return Plane(newList, self.rule)
    def simulateByTick(self, tick):
        newList = []
        for i in range(len(self.p)):
            newList.append([])
            for j in range(len(self.p[i])):
                newList[i].append(self.cells[i][j].update(self.p))
        return Plane(newList, self.rule) if tick == 1 else Plane(newList, self.rule).simulateByTick(tick - 1)
    def display(self):
        r_string = "--" * len(self.p[0]) + "-"
        print("--" * len(self.p[0]) + "-")
        for i in range(len(self.p)):
                print("|" + " ".join([u'\u25a0' if self.p[i][j] == 1 else " " for j in range(len(self.p[i]))]) + "|")
                r_string += "\n" + ("|" + " ".join([u'\u25a0' if self.p[i][j] == 1 else " " for j in range(len(self.p[i]))]) + "|")#.encode('utf-8').strip()
        print("--" * len(self.p[0]) + "-")
        r_string += "\n" + ("--" * len(self.p[0])) + "-" + "\n"
        return r_string
    def __getitem__(self, i):
        return self.p[i]


board = Plane([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], Rule([3],[2,3]))

                
board.display()
while True:
    if input()!='':
        break
    board = board.simulate()
    board.display()
