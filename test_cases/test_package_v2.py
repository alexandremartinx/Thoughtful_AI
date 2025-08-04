import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import Package

"""
This revised version of the package classification logic fixes a critical issue in the original implementation 
related to the ordering of conditional checks in the `classify` method.

Original Bug Explanation:
In the original version, the classification logic incorrectly prioritized the "bulky" condition over 
the "rejected" condition. This caused packages that were **both bulky and heavy** to be classified 
as "SPECIAL" instead of "REJECTED".

For example:
- A package with dimensions (100, 100, 100) and weight 25 was being classified as "SPECIAL"
  because the code detected it as bulky (volume ≥ 1,000,000 cm³) and returned early, 
  **without checking if it was also heavy (weight ≥ 20 kg).**
- According to the rules, any package that is both bulky and heavy must be classified as "REJECTED".

Fix Implemented:
In this version, the order of the conditions in the `classify` method has been changed to:
1. Check if the package is **both bulky and heavy** → return "REJECTED"
2. If not, check if it is only **bulky or heavy** → return "SPECIAL"
3. Otherwise → return "STANDARD"

This ensures that the logic strictly follows the classification hierarchy:
REJECTED > SPECIAL > STANDARD

This change resolves the test failure in `test_edge_cases` and ensures compliance with the 
specified classification rules.
"""


class TestPackageClassificationV2(unittest.TestCase):

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
        self.assertEqual(pkg.classify(), "REJECTED")

    def test_bulky_and_heavy(self):
        pkg = Package(200, 200, 200, 25)
        self.assertEqual(pkg.classify(), "REJECTED")

    def test_edge_cases(self):
        pkg = Package(149, 149, 149, 19)
        self.assertEqual(pkg.classify(), "SPECIAL")

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
