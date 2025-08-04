import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import Package

class TestPackageClassificationExtended(unittest.TestCase):

    """ STANDARD packages """
    def test_standard_typical(self):
        pkg = Package(50, 50, 50, 10)
        self.assertEqual(pkg.classify(), "STANDARD")

    def test_standard_edge_dimensions_and_mass(self):
        pkg = Package(149, 149, 149, 19)
        # volume = 149^3 = 3,307,149 (> 1M) => BULKY => SPECIAL
        self.assertEqual(pkg.classify(), "SPECIAL")  # Corrigido

    def test_standard_below_limits(self):
        pkg = Package(100, 100, 99, 19.9)
        self.assertEqual(pkg.classify(), "STANDARD")

    """ BULKY only """
    def test_bulky_volume_limit(self):
        pkg = Package(100, 100, 100, 10)  # volume = 1_000_000
        self.assertEqual(pkg.classify(), "SPECIAL")

    def test_bulky_dimension_limit(self):
        pkg = Package(150, 100, 100, 10)
        self.assertEqual(pkg.classify(), "SPECIAL")

    def test_bulky_high_volume(self):
        pkg = Package(120, 120, 80, 5)  # volume = 1,152,000
        self.assertEqual(pkg.classify(), "SPECIAL")

    """ HEAVY only """
    def test_heavy_mass_limit(self):
        pkg = Package(40, 40, 40, 20)
        self.assertEqual(pkg.classify(), "SPECIAL")

    def test_heavy_mass_above_limit(self):
        pkg = Package(10, 10, 10, 25)
        self.assertEqual(pkg.classify(), "SPECIAL")

    """ REJECTED (heavy + bulky) """
    def test_rejected_both_conditions(self):
        pkg = Package(200, 200, 200, 25)
        self.assertEqual(pkg.classify(), "REJECTED")

    def test_rejected_volume_edge_mass_edge(self):
        pkg = Package(100, 100, 100, 20)
        self.assertEqual(pkg.classify(), "REJECTED")

    def test_rejected_by_dimension_and_mass(self):
        pkg = Package(150, 100, 100, 20)
        self.assertEqual(pkg.classify(), "REJECTED")

    """ Edge cases """
    def test_edge_volume_just_under_limit(self):
        pkg = Package(100, 100, 99, 10)  # volume = 990000
        self.assertEqual(pkg.classify(), "STANDARD")

    def test_edge_mass_just_under_limit(self):
        pkg = Package(150, 100, 100, 19.9)
        self.assertEqual(pkg.classify(), "SPECIAL")  # bulky

    def test_extreme_large_package(self):
        pkg = Package(1000, 1000, 1000, 1000)
        self.assertEqual(pkg.classify(), "REJECTED")

    def test_extreme_small_package(self):
        pkg = Package(1, 1, 1, 0.1)
        self.assertEqual(pkg.classify(), "STANDARD")

    """ Optional: Invalid input handling (assume no validation in current class) """
    def test_zero_dimension(self):
        pkg = Package(0, 50, 50, 10)
        self.assertEqual(pkg.classify(), "STANDARD")

    def test_negative_mass(self):
        pkg = Package(50, 50, 50, -5)
        self.assertEqual(pkg.classify(), "STANDARD")

    def test_negative_dimension(self):
        pkg = Package(-150, 100, 100, 10)
        self.assertEqual(pkg.classify(), "STANDARD")

if __name__ == '__main__':
    unittest.main()
