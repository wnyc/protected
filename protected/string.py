class ProtectedString(str):
    def __repr__(self):
        return '<Protected String #%d ***********>' % (id(self),)

    def __add__(self, other):
        return ProtectedString(str.__add__(self, other))

    def __radd__(self, other):
        return ProtectedString(str.__add__(other, self))

    def __mod__(self, other):
        return ProtectedString(str.__mod__(self, other))

    def __rmod__(self, other):
        return ProtectedString(str.__rmod__(self, other))

    def __concat__(self, other):
        return ProtectedString(str,__concat__(self, other))
