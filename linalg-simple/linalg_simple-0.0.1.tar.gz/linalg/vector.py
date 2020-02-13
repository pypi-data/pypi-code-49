from math import acos, degrees, pi, sqrt
from decimal import Decimal, getcontext

# Set precision level for Decimals class
getcontext().prec = 30


class Vector(object):

    """Vector class for storing vectors and calculating basic vector operations
    
    Args:
        coordinates (int, float)

    Attributes:
        coordinates (Decimal)
        dimensions (int)
    
    Returns:
        Vector object -- an object with coordinates and number of dimentsions
    """

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector"
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = "No unique orthogonal component"
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = "No unique parallel component"
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = "Only defined in two or three dimensions"

    # Constructor for a Vector object
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be non empty!")

        except TypeError:
            raise TypeError("The coordinates must be an iterable!")

    def __add__(self, v):
        """Function to add two vectors by operator overload (plus sign)

        Args:
            Vector object
        
        Returns:
            Vector object - the sum of two vectors
        """
        return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        """Function to subtract two vectors by operator overload (minus sign)

        Args:
            Vector object
        
        Returns:
            Vector object - the difference of two vectors
        """
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    def times_scalar(self, c):
        """Function to multiply a vector with a scalar

        Args:
            Scalar (int, float)
        
        Returns:
            Vector object - the scaled vector
        """
        return Vector([x * Decimal(c) for x in self.coordinates])

    def magnitude(self):
        """Function to calculate the magnitude (length) of a vector

        Args:
            None
        
        Returns:
            Decimal object - magnitude (length) of the vector
        """
        sum_of_squares = sum([x ** 2 for x in self.coordinates])
        return (sum_of_squares) ** Decimal(0.5)

    def normalized(self):
        """Function to calculate the unit vector (normalization) of a vector

        Args:
            None
        
        Returns:
            Vector object - returns the unit vector of a vector
        """
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal(1.0) / magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, v):
        """Function to calculate the dot product of two vectors

        Args:
            Vector object
        
        Returns:
            Decimal object - dot product of two vectors
        """
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, rad=True):
        """Function to calculate the angle between two vectors

        Args:
            Vector object
            rad (bool) - whether the angle is returned in rads or degrees
        
        Returns:
            float - angle between two vectors
        """
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_rads = acos(u1.dot(u2))
            if rad:
                return angle_in_rads
            else:
                return angle_in_rads * 180.0 / pi

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute an angle with the zero vector")
            else:
                raise e

    def is_zero(self, tolerance=1e-10):
        """Function to check, if a vector's magnitude is zero

        Args:
            tolerance (float) - cut off point to correct for precision errors
        
        Returns:
            bool - whether the vector is zero or not
        """
        return self.magnitude() < tolerance

    def is_orthogonal_to(self, v, tolerance=1e-10):
        """Function to check if two vectors are orthogonal (90°) to each other

        Args:
            Vector object
            tolerance (bool) - cut off poiont to correct for precision errors
        
        Returns:
            bool - whether the vectors are orthogonal to each other
        """
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        """Function to check if two vectors are parallel (0°) to each other

        Args:
            Vector object
        
        Returns:
            bool - whether the vectors are parallel to each other
        """
        return (
            self.is_zero()
            or v.is_zero()
            or self.angle_with(v) == 0
            or self.angle_with(v) == pi
        )

    def component_parallel_to(self, basis):
        """Function to calculate the projection of a vector onto a basis vector

        Args:
            Vector object - basis vector
        
        Returns:
            vector object - projection vector (parallel component of vector)
        """
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_orthogonal_to(self, basis):
        """Function to calculate the orthogonal component of a vector

        Args:
            Vector object - basis vector
        
        Returns:
            Vector object - orthogonal vector component
        """
        try:
            projection = self.component_parallel_to(basis)
            return self - projection

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def cross(self, v):
        """Function to calculate the cross product of two vectors

        Args:
            Vector object
        
        Returns:
            Vector object - cross product
        """
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [
                y_1 * z_2 - y_2 * z_1,
                -(x_1 * z_2 - x_2 * z_1),
                x_1 * y_2 - x_2 * y_1,
            ]
            return Vector(new_coordinates)

        except ValueError as e:
            msg = str(e)
            # If input vectors are 2D, then add another dimension and
            # calculate the cross product
            if msg == "not enough values to unpack (expected 3, got 2)":
                self_embedded_in_R3 = Vector(self.coordinates + ("0",))
                v_embedded_in_R3 = Vector(v.coordinates + ("0",))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (
                # If input vectors are 1D or 4D and above, raise an exception
                msg == "too many values to unpack (expected 3)"
                or msg == "not enough values to unpack (expected 3, got 1)"
            ):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def area_of_parallelogram_with(self, v):
        """Function to calculate the parallelogram between two vectors

        Args:
            Vector object
        
        Returns:
            Decimal object - area of parallelogram (length of cross product)
        """
        cross_product = self.cross(v)
        return cross_product.magnitude()

    # Calculate the area of a triangle spanned by two vectors
    def area_of_triangle_with(self, v):
        """Function to calculate the triangle between two vectors

        Args:
            Vector object
        
        Returns:
            Decimal object - area of triangle (half length of cross product)
        """
        return self.area_of_parallelogram_with(v) / Decimal("2.0")

    # Define the inner representation of a Vector object
    def __repr__(self):
        return f"Vector: {self.coordinates}"

    # Define the string output format of a Vector object
    def __str__(self):
        coordinates = [round(float(x), 3) for x in self.coordinates]
        return f"Vector: {coordinates}"

    # Define the 'equals' (==) method
    def __eq__(self, v):
        return self.coordinates == v.coordinates
