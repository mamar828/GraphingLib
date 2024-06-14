try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class MathematicalObject:
    """
    This class implements the __r* and __i* methods for adding, subtracting, multiplying, dividing or raising to a power
    an object that contains the implementation for the standard operators.
    The __add__, __sub__, __mul__, __truediv__ and __pow__ methods must be implemented in the children class.
    """
    def __radd__(self, other: Self | float) -> Self:
        return self.__add__(other)
    
    def __iadd__(self, other: Self | float) -> Self:
        self = self.__add__(other)
        return self

    def __rsub__(self, other: Self | float) -> Self:
        return self.__sub__(other) * (-1)
    
    def __isub__(self, other: Self | float) -> Self:
        self = self.__sub__(other)
        return self

    def __rmul__(self, other: Self | float) -> Self:
        return self.__mul__(other)
    
    def __imul__(self, other: Self | float) -> Self:
        self = self.__mul__(other)
        return self
    
    def __rtruediv__(self, other: Self | float) -> Self:
        try:
            return self.__truediv__(other) ** (-1)
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero.")
    
    def __itruediv__(self, other: Self | float) -> Self:
        self = self.__truediv__(other)
        return self
    
    def __rpow__(self, other: Self | float) -> Self:
        raise NotImplementedError
    
    def __ipow__(self, other: Self | float) -> Self:
        self = self.__pow__(other)
        return self
    