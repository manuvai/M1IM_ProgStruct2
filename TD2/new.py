
    

class Matrix:

    def __str__(self) -> str:
        res = ''
        for line in self.liste:
            temp = ''
            for case in line:
                temp += str(case)

            res += temp + '\n'
        return res

    def __init__(self, values: list) -> None:
        self.liste = []
        y = 0
        for line in values:
            new_line = []
            x = 0
            for el in line:
                damier = self.Case(x, y, el, self)
                new_line.append(damier) 
                x+=1 
            y+=1 
            self.liste.append(new_line)  

    def evolve(self):
        new_liste = []
        for line in self.liste:
            temp = []
            for case in line:
                evolved = case.evolve()
                temp.append(evolved)

            new_liste.append(temp)

        self.liste = new_liste
        count = 0
        for i in range(len(new_liste)):
            for j in range(len(new_liste)):
                if (new_liste[i][j].isInsect()):
                    count += (2 ** (j + (i) * 5))
        print(count)

    def getVoisin(self, x, y):
        def __upper(matrix, x, y):
            if (y == 0):
                return None
            return matrix.liste[y - 1][x]
        
        def __left(matrix, x, y):
            if (x == 0):
                return None
            return matrix.liste[y][x - 1]
        
        def __right(matrix, x, y):
            if (x >= (len(matrix.liste) - 1)):
                return None
            
            return matrix.liste[y][x + 1]
        def __down(matrix, x, y):
            if (y >= (len(matrix.liste) - 1)):
                return None
            
            return matrix.liste[y + 1][x]
        
        return [
            __upper(self, x, y),
            __right(self, x, y),
            __down(self, x, y),
            __left(self, x, y),
        ]
    
    def copy(self):
        liste = []

        matrix = Matrix(liste)

        for line in self.liste:
            temp_line = []
            for el in line: 
                temp_line.append(Matrix.Case(el.x, el.y, el.value, matrix))

            liste.append(temp_line)
        matrix.liste = liste

        return matrix
    
    def __eq__(self, that: object) -> bool:
        isEqual = True

        for i in range(len(self.liste)):
            for j in range(len(self.liste[i])):

                self_case = self.liste[i][j]
                that_case = that.liste[i][j]
                if (self_case.value != that_case.value):
                    isEqual = False
        
        return isEqual

    class Case:

        def __str__(self) -> str:
            return str(self.value)
        
        def __init__(self,x, y, value, matrix) -> None:
            self.value = value
            self.x = x
            self.y = y
            self.matrix = matrix

        def evolve(self):
            voisins = self.getVoisins()
            new_case = Matrix.Case(self.x, self.y, self.value, self.matrix)

            count = 0
            for v in voisins:
                if (not v is None and v.isInsect()):
                    count += 1
            
            if (self.isInsect() and (count != 1)):
                new_case.value = '.'
            elif (not self.isInsect() and (count == 1 or count == 2)):
                new_case.value = '#'

            return new_case
        
        def isInsect(self):
            return self.value == '#'

        def getVoisins(self):
            return self.matrix.getVoisin(self.x, self.y)

liste = [
    '.#..#',
    '#.#.#',
    '##..#',
    '##.##',
    '#...#',
]

matrice = Matrix(liste)
print(matrice, '\n')
temp_matrice = [matrice.copy()]
i = 0
isLoop = False
while (i < 100 and not isLoop):
    matrice.evolve()
    print(matrice, '\n')

    for mat in temp_matrice:
        if (mat.__eq__(matrice)):
            isLoop = True
    temp_matrice.append(matrice.copy())
    i+=1
