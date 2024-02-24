#!/usr/bin/python3
"""This is a Rectangle Class"""


class Rectangle:
    """A Rectangle
       Arguments:
            number_of_instances  calculates the number
            of instances of this class
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Constructor for Rectangle
           Takes two values to intiate the width and height
           Attributes:
                width   width value of the rectangle
                height  height value of the rectangle
                number_of_instances  calculates the number of
                instances of this class incremented by the number of instances
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        """A getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter for the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """A getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter for the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of this object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = []
            for i in range(self.__height):
                for j in range(self.__width):
                    rect.append('#')
                if i != self.__height - 1:
                    rect.append("\n")
            return ("".join(rect))

    def __repr__(self):
        """Return a string representation of this object as a string."""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Deletes this object
            and decrements the number of instances
        """
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1
        print("Bye rectangle...")
