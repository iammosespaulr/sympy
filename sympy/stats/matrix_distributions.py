from sympy import S, Basic, exp, multigamma, pi
from sympy.core.sympify import sympify, _sympify
from sympy.matrices import (ImmutableMatrix, Inverse, Trace, Determinant,
                            MatrixSymbol, MatrixBase, Transpose, MatrixSet)
from sympy.stats.rv import (_value_check, RandomMatrixSymbol, NamedArgsMixin, PSpace,
                            _symbol_converter)


class MatrixPSpace(PSpace):
    """
    Represents probability space for
    Matrix Distributions
    """
    def __new__(cls, sym, distribution, dim_n, dim_m):
        sym = _symbol_converter(sym)
        dim_n, dim_m = _sympify(dim_n), _sympify(dim_m)
        if not (dim_n.is_integer and dim_m.is_integer):
            raise ValueError("Dimensions should be integers")
        return Basic.__new__(cls, sym, distribution, dim_n, dim_m)

    distribution = property(lambda self: self.args[1])
    symbol = property(lambda self: self.args[0])

    @property
    def value(self):
        return RandomMatrixSymbol(self.symbol, self.args[2], self.args[3], self)

    def compute_density(self, expr, *args):
        rms = expr.atoms(RandomMatrixSymbol)
        if len(rms) > 1 or (not isinstance(expr, RandomMatrixSymbol)):
            raise NotImplementedError("Currently, no algorithm has been "
                    "implemented to handle general expressions containing "
                    "multiple matrix distributions.")
        return self.distribution.pdf(expr)


def rv(symbol, cls, args):
    args = list(map(sympify, args))
    dist = cls(*args)
    dist.check(*args)
    dim = dist.dimension
    pspace = MatrixPSpace(symbol, dist, dim[0], dim[1])
    return pspace.value


class MatrixDistribution(Basic, NamedArgsMixin):
    """
    Abstract class for Matrix Distribution
    """
    def __new__(cls, *args):
        args = list(map(sympify, args))
        return Basic.__new__(cls, *args)

    @staticmethod
    def check(*args):
        pass

    def __call__(self, expr):
        if isinstance(expr, list):
            expr = ImmutableMatrix(expr)
        return self.pdf(expr)


########################################
#--------Matrix Distributions----------#
########################################

#-------------------------------------------------------------------------------
# Matrix Gamma distribution ----------------------------------------------------

class MatrixGammaDistribution(MatrixDistribution):

    _argnames = ('alpha', 'beta', 'scale_matrix')

    @staticmethod
    def check(alpha, beta, scale_matrix):
        if not isinstance(scale_matrix , MatrixSymbol):
            _value_check(scale_matrix.is_positive_definite, "The shape "
                "matrix must be positive definite.")
        _value_check(scale_matrix.is_square, "Should "
        "be square matrix")
        _value_check(alpha.is_positive, "Shape parameter should be positive.")
        _value_check(beta.is_positive, "Scale parameter should be positive.")

    @property
    def set(self):
        k = self.scale_matrix.shape[0]
        return MatrixSet(k, k, S.Reals)

    @property
    def dimension(self):
        return self.scale_matrix.shape

    def pdf(self, x):
        alpha , beta , scale_matrix = self.alpha, self.beta, self.scale_matrix
        p = scale_matrix.shape[0]
        if isinstance(x, list):
            x = ImmutableMatrix(x)
        if not isinstance(x, (MatrixBase, MatrixSymbol)):
            raise ValueError("%s should be an isinstance of Matrix "
                    "or MatrixSymbol" % str(x))
        sigma_inv_x = - Inverse(scale_matrix)*x / beta
        term1 = exp(Trace(sigma_inv_x))/((beta**(p*alpha)) * multigamma(alpha, p))
        term2 = (Determinant(scale_matrix))**(-alpha)
        term3 = (Determinant(x))**(alpha - S(p + 1)/2)
        return term1 * term2 * term3

def MatrixGamma(symbol, alpha, beta, scale_matrix):
    """
    Creates a random variable with Matrix Gamma Distribution.

    The density of the said distribution can be found at [1].

    Parameters
    ==========

    alpha: Positive Real number
        Shape Parameter
    beta: Positive Real number
        Scale Parameter
    scale_matrix: Positive definite real square matrix
        Scale Matrix

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density, MatrixGamma
    >>> from sympy import MatrixSymbol, symbols
    >>> a, b = symbols('a b', positive=True)
    >>> M = MatrixGamma('M', a, b, [[2, 1], [1, 2]])
    >>> X = MatrixSymbol('X', 2, 2)
    >>> density(M)(X).doit()
    3**(-a)*b**(-2*a)*exp(Trace(Matrix([
    [-2/3,  1/3],
    [ 1/3, -2/3]])*X)/b)*Determinant(X)**(a - 3/2)/(sqrt(pi)*gamma(a)*gamma(a - 1/2))
    >>> density(M)([[1, 0], [0, 1]]).doit()
    3**(-a)*b**(-2*a)*exp(-4/(3*b))/(sqrt(pi)*gamma(a)*gamma(a - 1/2))


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Matrix_gamma_distribution

    """
    if isinstance(scale_matrix, list):
        scale_matrix = ImmutableMatrix(scale_matrix)
    return rv(symbol, MatrixGammaDistribution, (alpha, beta, scale_matrix))

#-------------------------------------------------------------------------------
# Wishart Distribution ---------------------------------------------------------

class WishartDistribution(MatrixDistribution):

    _argnames = ('n', 'scale_matrix')

    @staticmethod
    def check(n, scale_matrix):
        if not isinstance(scale_matrix , MatrixSymbol):
            _value_check(scale_matrix.is_positive_definite, "The shape "
                "matrix must be positive definite.")
        _value_check(scale_matrix.is_square, "Should "
        "be square matrix")
        _value_check(n.is_positive, "Shape parameter should be positive.")

    @property
    def set(self):
        k = self.scale_matrix.shape[0]
        return MatrixSet(k, k, S.Reals)

    @property
    def dimension(self):
        return self.scale_matrix.shape

    def pdf(self, x):
        n, scale_matrix = self.n, self.scale_matrix
        p = scale_matrix.shape[0]
        if isinstance(x, list):
            x = ImmutableMatrix(x)
        if not isinstance(x, (MatrixBase, MatrixSymbol)):
            raise ValueError("%s should be an isinstance of Matrix "
                    "or MatrixSymbol" % str(x))
        sigma_inv_x = - Inverse(scale_matrix)*x / S(2)
        term1 = exp(Trace(sigma_inv_x))/((2**(p*n/S(2))) * multigamma(n/S(2), p))
        term2 = (Determinant(scale_matrix))**(-n/S(2))
        term3 = (Determinant(x))**(S(n - p - 1)/2)
        return term1 * term2 * term3

def Wishart(symbol, n, scale_matrix):
    """
    Creates a random variable with Wishart Distribution.

    The density of the said distribution can be found at [1].

    Parameters
    ==========

    n: Positive Real number
        Represents degrees of freedom
    scale_matrix: Positive definite real square matrix
        Scale Matrix

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density, Wishart
    >>> from sympy import MatrixSymbol, symbols
    >>> n = symbols('n', positive=True)
    >>> W = Wishart('W', n, [[2, 1], [1, 2]])
    >>> X = MatrixSymbol('X', 2, 2)
    >>> density(W)(X).doit()
    2**(-n)*3**(-n/2)*exp(Trace(Matrix([
    [-1/3,  1/6],
    [ 1/6, -1/3]])*X))*Determinant(X)**(n/2 - 3/2)/(sqrt(pi)*gamma(n/2)*gamma(n/2 - 1/2))
    >>> density(W)([[1, 0], [0, 1]]).doit()
    2**(-n)*3**(-n/2)*exp(-2/3)/(sqrt(pi)*gamma(n/2)*gamma(n/2 - 1/2))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Wishart_distribution

    """
    if isinstance(scale_matrix, list):
        scale_matrix = ImmutableMatrix(scale_matrix)
    return rv(symbol, WishartDistribution, (n, scale_matrix))

#-------------------------------------------------------------------------------
# Matrix Normal distribution ---------------------------------------------------

class MatrixNormalDistribution(MatrixDistribution):

    _argnames = ('location_matrix', 'scale_matrix_1', 'scale_matrix_2')

    @staticmethod
    def check(location_matrix, scale_matrix_1, scale_matrix_2):
        if not isinstance(scale_matrix_1 , MatrixSymbol):
            _value_check(scale_matrix_1.is_positive_definite, "The shape "
                "matrix must be positive definite.")
        if not isinstance(scale_matrix_2 , MatrixSymbol):
            _value_check(scale_matrix_2.is_positive_definite, "The shape "
                "matrix must be positive definite.")
        _value_check(scale_matrix_1.is_square, "Scale matrix 1 should be "
        "be square matrix")
        _value_check(scale_matrix_2.is_square, "Scale matrix 2 should be "
        "be square matrix")
        n = location_matrix.shape[0]
        p = location_matrix.shape[1]
        _value_check(scale_matrix_1.shape[0] == n, "Scale matrix 1 should be"
        " of shape %s x %s"% (str(n), str(n)))
        _value_check(scale_matrix_2.shape[0] == p, "Scale matrix 2 should be"
        " of shape %s x %s"% (str(p), str(p)))

    @property
    def set(self):
        n, p = self.location_matrix.shape
        return MatrixSet(n, p, S.Reals)

    @property
    def dimension(self):
        return self.location_matrix.shape

    def pdf(self, x):
        M , U , V = self.location_matrix, self.scale_matrix_1, self.scale_matrix_2
        n, p = M.shape
        if isinstance(x, list):
            x = ImmutableMatrix(x)
        if not isinstance(x, (MatrixBase, MatrixSymbol)):
            raise ValueError("%s should be an isinstance of Matrix "
                    "or MatrixSymbol" % str(x))
        term1 = Inverse(V)*Transpose(x - M)*Inverse(U)*(x - M)
        num = exp(-Trace(term1)/S(2))
        den = (2*pi)**(S(n*p)/2) * Determinant(U)**S(p)/2 * Determinant(V)**S(n)/2
        return num/den

def MatrixNormal(symbol, location_matrix, scale_matrix_1, scale_matrix_2):
    """
    Creates a random variable with Matrix Normal Distribution.

    The density of the said distribution can be found at [1].

    Parameters
    ==========

    location_matrix: Real ``n x p`` matrix
        Represents degrees of freedom
    scale_matrix_1: Positive definite matrix
        Scale Matrix of shape ``n x n``
    scale_matrix_2: Positive definite matrix
        Scale Matrix of shape ``p x p``

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy import MatrixSymbol
    >>> from sympy.stats import density, MatrixNormal
    >>> M = MatrixNormal('M', [[1, 2]], [1], [[1, 0], [0, 1]])
    >>> X = MatrixSymbol('X', 1, 2)
    >>> density(M)(X).doit()
    2*exp(-Trace((Matrix([
    [-1],
    [-2]]) + X.T)*(Matrix([[-1, -2]]) + X))/2)/pi
    >>> density(M)([[3, 4]]).doit()
    2*exp(-4)/pi

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Matrix_normal_distribution

    """
    if isinstance(location_matrix, list):
        location_matrix = ImmutableMatrix(location_matrix)
    if isinstance(scale_matrix_1, list):
        scale_matrix_1 = ImmutableMatrix(scale_matrix_1)
    if isinstance(scale_matrix_2, list):
        scale_matrix_2 = ImmutableMatrix(scale_matrix_2)
    args = (location_matrix, scale_matrix_1, scale_matrix_2)
    return rv(symbol, MatrixNormalDistribution, args)
