from dataclasses import dataclass, fields


@dataclass(repr=True, slots=True)
class Point2D:
    _x: int
    _y: int
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value