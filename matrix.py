import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        #print(self.g)
        
        if self.h == 1:
            return self.g[0][0]
        
        if self.h == 2:
            return self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0;
        
        for i in range(self.h):
            trace = trace + self.g[i][i]
            
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        Inv = zeroes(self.w, self.h)
        # TODO - your code here
        if self.h == 1:
            Inv.g[0][0] = 1/self.g[0][0]
        
        if self.h == 2:
            Inv[0][0] = (1/self.determinant()) * self.g[1][1]
            Inv[0][1] = (-1/self.determinant()) * self.g[0][1]
            Inv[1][0] = (-1/self.determinant()) * self.g[1][0]
            Inv[1][1] = (1/self.determinant()) * self.g[0][0]
            
            #return [ [(1/self.determinant()) * self.g[1][1], (-1/self.determinant()) * self.g[0][1]],
            #         [(-1/self.determinant()) * self.g[1][0], (1/self.determinant()) * self.g[0][0]]
            #       ]
        return Inv

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        T = zeroes(self.w, self.h)
        
        for i in range(self.h):
            for j in range(self.w):
                T[j][i] = self.g[i][j]
                
        return T

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        matrix_sum = zeroes(self.h, self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                matrix_sum[i][j] = self.g[i][j] + other.g[i][j]
        
        return matrix_sum

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #

        matrix_neg = zeroes(self.h, self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                matrix_neg[i][j] = -self.g[i][j]
        
        return matrix_neg
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        
        matrix_diff = zeroes(self.h, self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                matrix_diff[i][j] = self.g[i][j] - other.g[i][j]
        
        return matrix_diff

    def get_row(self, row):
        return self.g[row]

    def get_column(self, column_number):
        column = []
    
        for i in range(len(self.g)):
            column.append(self.g[i][column_number])
        
        return column

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        #print("grid size before: ", len(self.g), len(self.g[0]), len(other.g), len(other.g[0]))
        #print(self.h, self.w, other.h, other.w)
        matrix_prod = zeroes(len(self.g), len(other.g[0]))
        #print("grid size after: ", len(self.g), len(self.g[0]), len(other.g), len(other.g[0]))
        #print(self.h, self.w, other.h, other.w)
        for i in range(self.h):
            for j in range(other.w):
                dotproductsum = 0
                for k in range(len(self.get_row(i))):
                    #print("I: ", i)
                    #print("J: ", j)
                    #print("K: ", k)
                    dotproductsum = dotproductsum + self.get_row(i)[k] * other.get_column(j)[k]
                matrix_prod[i][j] = dotproductsum

        return matrix_prod
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #pass
            #   
            # TODO - your code here
            #
            matrix_rmul = zeroes(self.h, self.w)
        
            for i in range(self.h):
                for j in range(self.w):
                    matrix_rmul[i][j] = other * self.g[i][j]
        
        return matrix_rmul
            