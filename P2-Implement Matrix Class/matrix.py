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
        if self.h == 1:
            t = self.g[0][0]
        else:
            t=1
            for i in range(self.h):
                for j in range(self.w):
                    if i==j:
                        t*=self.g[i][j]
        return t
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        tr=0
        for i in range(self.h):
            for j in range(self.w):
                if i==j:
                    tr+=self.g[i][j]
                
        return tr

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        
        # TODO - your code here
        inverse=[]
        if self.h == 1:
            d=[1/self.g[0][0]]
            inverse.append(d)
            return Matrix(inverse)
        
        elif self.h == 2:
            d=(self.g[0][0]*self.g[1][1])-(self.g[1][0]*self.g[0][1])
            tr = self.g[0][0]+self.g[1][1]
        
        B = (d**-1)*(tr*identity(self.h)-self.g)

        return B 

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        # first get column --->[] in row format
        # second add them togather to get your matrix
        T=[]
        for j in range(self.w):
            row=[]
            for i in range(self.h):
                row.append(self.g[i][j])
            T.append(row)
               
        return Matrix(T)
        
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
        R = []
        for i in range(self.h):
            row=[]
            for j in range(self.w):
                row.append(self.g[i][j]+ other[i][j])
            R.append(row)
            
        return Matrix(R)

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
        R = []
        for i in range(self.h):
            row=[]
            for j in range(self.w):
                row.append(-self.g[i][j])
            R.append(row)     
        return Matrix(R)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        R=[]
        for i in range(self.h):
            row=[]
            for j in range(self.w):
                row.append(self.g[i][j]-other[i][j])
            R.append(row)
        return Matrix(R)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        M=[]
        for i in range(self.h):
            R=[]
            for j in range(len(other[0])):
                r = self.g[i]
                c=[]
                
                # let us get column, the objective of this function is to get you right column to do your dot product
                for d in range(other.h):
                    c.append(other[d][j])
                #r should be sth like r=[1,2,...,n]
                #c should be sth like c=[1,2,...,n]
                
                # This is a dot_product loop   
                dot_product=0
                for k in range(len(r)):
                    dot_product+=r[k]*c[k]
                R.append(dot_product)
            M.append(R)
            
        return Matrix(M)
        
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
            R=[]
            for i in range(self.h):
                row=[]
                for j in range(self.w):
                    row.append(other*self.g[i][j])
                R.append(row)  
            return Matrix(R)
            
            #   
            # TODO - your code here
            #
    