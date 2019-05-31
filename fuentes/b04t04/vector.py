class Vector2D:
    """A vector in a 2D euclidean space."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)

        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)

        return NotImplemented

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, scalar):
        import numbers
        if isinstance(scalar, numbers.Real):
            return Vector2D(self.x * scalar, self.y * scalar)

        return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    def __truediv__(self, scalar):
        import numbers
        if isinstance(scalar, numbers.Real):
            return Vector2D(self.x / scalar, self.y / scalar)

        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
            return self

        return NotImplemented

    def __bool__(self):
        return bool(self.x or self.y)

    def __len__(self):
        return 2

    def __getitem__(self, index):
        index = self._correct_index(index)
        return self.x if index == 0 else self.y

    def __setitem__(self, index, value):
        index = self._correct_index(index)
        if index == 0:
            self.x = value
        else:
            self.y = value

    def _correct_index(self, index):
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError
        return index

    def __contains__(self, item):
        return self.x == item or self.y == item