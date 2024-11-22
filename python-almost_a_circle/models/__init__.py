def __init__(self, width, height, x=0, y=0, id=None):
    """Initialize a new Rectangle instance."""
    super().__init__(id)
    if not isinstance(width, int):
        raise TypeError("width must be an integer")
    if not isinstance(height, int):
        raise TypeError("height must be an integer")
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if not isinstance(y, int):
        raise TypeError("y must be an integer")
    if width <= 0:
        raise ValueError("width must be > 0")
    if height <= 0:
        raise ValueError("height must be > 0")
    if x < 0:
        raise ValueError("x must be >= 0")
    if y < 0:
        raise ValueError("y must be >= 0")
    self.width = width
    self.height = height
    self.x = x
    self.y = y 
