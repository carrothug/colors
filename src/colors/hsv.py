class HSV:
    """A color represented in HSV"""

    def __init__(self, h=int, s=int, v=int):
        """Initialize a HSV color

        :param h: Hue
        :type hue: int
        :param s: Saturation
        :type s: int
        :param v: Value, or brightness
        :type v: int
        """
        self.h = h
        self.s = s
        self.v = v
