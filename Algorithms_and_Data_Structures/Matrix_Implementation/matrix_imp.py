class Matrix:

    def __init__(self, matrix, value = 0):
        if(isinstance(matrix, tuple)):
            self.rows, self.cols = matrix
            self.size = matrix
            self.matrix = [[value for col in range(self.cols)] for row in range(self.rows)]
        else:
            self.matrix = matrix
            self.rows = len(matrix)
            self.cols = len(matrix[0])

    def __len__(self):
        return(self.rows, self.cols)
    
    def __getitem__(self, row_id):
        return self.matrix[row_id]

    def __add__(self, matrix_addon):
        sum = []
        if self.__len__() == Matrix.__len__(matrix_addon):
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    el = self.matrix.__getitem__(i)[j] + Matrix.__getitem__(matrix_addon, i)[j]
                    row.append(el)
                sum.append(row)
            return Matrix(sum)
        else:
            print("Matrices have diffrent length")


    def __mul__(self, matrix_addon):
        product = []
        if self.__len__()[1] == matrix_addon.__len__()[0]:
            for i in range(self.rows):
                row = []
                for j in range(matrix_addon.__len__()[1]):
                    el = 0
                    for k in range(matrix_addon.__len__()[0]):
                        el += self.matrix[i][k] * matrix_addon[k][j]
                    row.append(el)
                product.append(row)
            return Matrix(product)
        else:
            print("Matrices have diffrent shapes")

    def __str__(self):
        pr = "["
        for row in range(self.rows):
            if row < self.rows-1:
                pr += str(self.matrix.__getitem__(row)) + "," + "\n"
            if row == self.rows-1:
                pr += str(self.matrix.__getitem__(row)) + "]"
        return pr

def transpotition(matrix):
    transposed_matrix = Matrix((len(matrix[0]), len(matrix)), 0)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            transposed_matrix[col][row] = matrix[row][col]
    return transposed_matrix
    
def main():

    macierz1 = [ [1, 0, 2],
    [-1, 3, 1] ]

    macierz2 = (2, 3)

    macierz3 = [ [3, 1],
    [2, 1],
    [1, 0]]

    a = Matrix(macierz1) 
    a_t= transpotition(macierz1)
    b = Matrix(macierz2, 1)
    c = Matrix(macierz3)
    
    print(a_t, "\n")
    print(a+b,"\n")
    print(a*c)

if __name__ == "__main__":
    main()