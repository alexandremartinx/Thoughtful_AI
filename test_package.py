import unittest
from main import Package

class TestPackageClassification(unittest.TestCase):

    def test_standard_package(self):
        pkg = Package(50, 50, 50, 10)
        self.assertEqual(pkg.classify(), "STANDARD")

    def test_bulky_only(self):
        pkg = Package(200, 50, 50, 10)
        self.assertEqual(pkg.classify(), "SPECIAL")

        pkg = Package(100, 100, 100, 10)
        self.assertEqual(pkg.classify(), "SPECIAL")
    def test_heavy_only(self):
        pkg = Package(50, 50, 50, 20)
        self.assertEqual(pkg.classify(), "SPECIAL")

        pkg = Package(100, 100, 100, 25)
        self.assertEqual(pkg.classify(), "SPECIAL")

    def test_bulky_and_heavy(self):
        pkg = Package(200, 200, 200, 25)
        self.assertEqual(pkg.classify(), "REJECTED")

    def test_edge_cases(self):
        pkg = Package(149, 149, 149, 19)
        self.assertEqual(pkg.classify(), "STANDARD")

        pkg = Package(100, 100, 100, 10)
        self.assertEqual(pkg.classify(), "SPECIAL")

        pkg = Package(150, 100, 100, 10)
        self.assertEqual(pkg.classify(), "SPECIAL")

        pkg = Package(50, 50, 50, 20)
        self.assertEqual(pkg.classify(), "SPECIAL")

    def test_extreme_values(self):
        pkg = Package(1000, 1000, 1000, 1000)
        self.assertEqual(pkg.classify(), "REJECTED")

if __name__ == '__main__':
    unittest.main()
