from itertools import permutations
import itertools

class const:
    colors = ['W','Y','R','B','O','G']
    postitions = [(0, 0, 0) ,(0, 0, 1) ,(0, 0, 2) ,(0, 1, 0) ,(0, 1, 1) ,
                  (0, 1, 2) ,(0, 2, 0) ,(0, 2, 1) ,(0, 2, 2) ,(1, 0, 0) ,
                  (1, 0, 1) ,(1, 0, 2) ,(1, 1, 0) ,(1, 1, 1) ,(1, 1, 2) ,
                  (1, 2, 0) ,(1, 2, 1) ,(1, 2, 2) ,(2, 0, 0) ,(2, 0, 1) ,
                  (2, 0, 2) ,(2, 1, 0) ,(2, 1, 1) ,(2, 1, 2) ,(2, 2, 0) ,
                  (2, 2, 1) ,(2, 2, 2) ]
    faces = [[0,1,1,1,0,0], [0,0,1,1,0,0], [1,0,1,1,0,0], [0,1,1,0,0,0], [0,0,1,0,0,0], 
             [1,0,1,0,0,0], [0,1,1,0,0,1], [0,0,1,0,0,1], [1,0,1,0,0,1], [0,1,0,1,0,0], 
             [0,0,0,1,0,0], [1,0,0,1,0,0], [0,1,0,0,0,0], [0,0,0,0,0,0], [1,0,0,0,0,0], 
             [0,1,0,0,0,1], [0,0,0,0,0,1], [1,0,0,0,0,1], [0,1,0,1,1,0], [0,0,0,1,1,0], 
             [1,0,0,1,1,0], [0,1,0,0,1,0], [0,0,0,0,1,0], [1,0,0,0,1,0], [0,1,0,0,1,1], 
             [0,0,0,0,1,1], [1,0,0,0,1,1]]

class stone:   
    def createArray(self,up=None, down=None, _1=None, _2=None, _3=None, _4=None):
        self.array = [up,down,_1,_2,_3,_4]     
        self.test = False
            
    def __init__(self, a,b,c):        
        up,down,_1,_2,_3,_4 = None,None,None,None,None,None
        if a == 0:            _1 = 'R'
        if a == 2:            _3 = 'O'
        if b == 0:            _2 = 'B'
        if b == 2:            _4 = 'G'
        if c == 0:            down = 'Y'
        if c == 2:            up = 'W'
        self.createArray(up,down,_1,_2,_3,_4)
        
    
    def X_move(self):
        temp = self.array.copy()
        self.array = [temp[3],temp[5],temp[2],temp[1],temp[4],temp[0]]
        if self.test :print(self,' ',self.get_position())
    
    def Y_move(self):
        temp = self.array.copy()
        self.array = [temp[4],temp[2],temp[0],temp[3],temp[1],temp[5]]
        if self.test: print(self,' ',self.get_position())
        
    def Z_move(self):
        temp = self.array.copy()
        self.array = [temp[0],temp[1],temp[3],temp[4],temp[5],temp[2]]
        if self.test : print(self,' ',self.get_position())        
        
    def get_face(self):
        result = []
        for side in self.array:
            if side == None: result.append(0)
            else: result.append(1)
        return result
    
    
    def __str__(self):
        result = '['
        for side in self.array:
            if side == None: result +='-,'
            else: result += side+','
        return result[:-1]+']'
      
    def fil_side(side):        
        """used only inside createArray() """
        if type(side) == type('a') and side.upper() in const.colors: return side.upper()
        else: return None
            
    def get_position(self):
        temp = []
        for a in self.array:
            if a == None: temp.append(0)
            else: temp.append(1)
        return const.postitions[const.faces.index(temp)]

if __name__ == '__main__':
    a = stone(0,0,0)
    print(a)
    a.test = True
    a.Z_move()
