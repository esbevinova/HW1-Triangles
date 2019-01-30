"""Ekaterina (Katya) Bevinova
   SSW-567-A
   HW01: Testing Triangle Classification
"""
import unittest

def classify_triangle(a,b,c):
    """A function that tells if the triangle is Equilateral, Isosceles, Scalene and possibly right."""

    try:
        float(a) and float(b) and float(c)

        if a == 0 or b == 0 or c == 0:
            return "Cannot have 0 as a side."
        elif (a + b <= c) or (a + c <= b) or (b + c <= a): 
            return "It is not a triangle."
        elif a == b == c:
            return "Equilateral"
        elif (a == b or b ==c or a == c) and round(a**2 + b**2) == c**2:
            return "Isosceles and Right."
        elif a == b or b ==c or a == c:
            return "Isosceles"
        elif a != b != c and a**2 + b**2 == c**2:
            return "Scalene and Right."
        elif a != b != c:
            return "Scalene"
        else:
            return "It is not a triangle."

    except ValueError:
        return "Not a valid triangle."

        
class CommonTest(unittest.TestCase):
    """A class that includes test methods that check classify_triangle() function."""

    def test_classify_triangle(self):
        """A method that tests what kind of triangle it is."""
        
        self.assertEqual(classify_triangle(4,4,4), "Equilateral")
        self.assertEqual(classify_triangle(3,4,5), "Scalene and Right.")
        self.assertEqual(classify_triangle(3,4,6), "Scalene")
        self.assertEqual(classify_triangle(4,4,6), "Isosceles")
        self.assertEqual(classify_triangle(7.071067812,7.071067812,10), "Isosceles and Right.")
        self.assertEqual(classify_triangle(3,4,9), "It is not a triangle.")
        self.assertEqual(classify_triangle(0,4,5), "Cannot have 0 as a side.")
        self.assertEqual(classify_triangle("bob", "blob", "f"), "Not a valid triangle.")
        self.assertEqual(classify_triangle("fdhs", 4, 4), "Not a valid triangle.")
        
    
def main():
    print(classify_triangle(3,4,5))

if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)

