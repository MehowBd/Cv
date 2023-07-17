#skończone

class Matrix:

    def __init__(self, matrix, value = 0, rows = 0, cols = 0):
        if(isinstance(matrix, tuple)):
            self.rows, self.cols = matrix
            self.size = matrix
            self.matrix = [[value for col in range(self.cols)] for row in range(self.rows)]
        else:
            self.matrix = matrix
            self.rows = len(matrix)
            self.cols = len(matrix[0])

    def __len__(self):
        return (self.rows, self.cols)
    
    def __getitem__(self, row_id):
        return self.matrix[row_id]

    def __add__(self, matrix_addon):
        sum = []
        if self.__len__() == matrix_addon.__len__():
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    el = self.matrix[i][j] + matrix_addon[i][j]
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

def chio(macierz_podana, component = 1):
    macierz = Matrix(macierz_podana)

    if macierz.__len__()[0] == macierz.__len__()[1] and macierz.__len__()[0]  > 2:
        if macierz.__getitem__(0)[0] == 0:
            for col in macierz[0]:
                if col != 0:
                    break
            for i in range(macierz.__len__()[0]):
                macierz.__getitem__(i)[0], macierz.__getitem__(i)[col] = macierz.__getitem__(i)[col], macierz.__getitem__(i)[0]

            component *= -macierz.__getitem__(0)[0]**(macierz.__len__()[0]-2)
            final_form = []
            for i in range(macierz.__len__()[0]-1):
                final_row = []
                for j in range(macierz.__len__()[0]-1):
                    el = (macierz.__getitem__(0)[0]*macierz.__getitem__(i+1)[j+1] - macierz.__getitem__(0)[j+1]*macierz.__getitem__(i+1)[0])
                    final_row.append(el)
                final_form.append(final_row)
        else:
            component *= macierz.__getitem__(0)[0]**(macierz.__len__()[0]-2)
            final_form = []
            for i in range(macierz.__len__()[0]-1):
                final_row = []
                for j in range(macierz.__len__()[0]-1):
                    el = (macierz.__getitem__(0)[0]*macierz.__getitem__(i+1)[j+1] - macierz.__getitem__(0)[j+1]*macierz.__getitem__(i+1)[0])
                    final_row.append(el)
                final_form.append(final_row)
                
        if len(final_form) == 2:
            return (final_form[0][0]*final_form[1][1] -  final_form[1][0]*final_form[0][1])/component
        else:
            return chio(final_form, component)
            
def main():
    macierz = [[5 , 1 , 1 , 2 , 3],
    [4 , 2 , 1 , 7 , 3],
    [2 , 1 , 2 , 4 , 7],
    [9 , 1 , 0 , 7 , 0],
    [1 , 4 , 7 , 2 , 2]]

    macierz1 = [[1, 0, 3],
    [1, 7, 2],
    [1, 3, 2]]

    macierz2 =   [
        [0 , 1 , 1 , 2 , 3],
        [4 , 2 , 1 , 7 , 3],
        [2 , 1 , 2 , 4 , 7],
        [9 , 1 , 0 , 7 , 0],
        [1 , 4 , 7 , 2 , 2]
        ]


    print(chio(macierz))
    print(chio(macierz2))

if __name__ == "__main__":
    main()