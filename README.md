# Package Sorting Challenge

This is a Python implementation for the Thoughtful Robotic Automation Factory sorting challenge. The goal is to classify packages based on their **dimensions** and **mass** into three categories.

### A package is considered:
- **Bulky** if:
  - Volume (Width × Height × Length) ≥ 1,000,000 cm³ **OR**
  - Any dimension (width, height, or length) ≥ 150 cm
- **Heavy** if:
  - Mass ≥ 20 kg

---

## 📂 Classification Stacks

| Category    | Description                                      |
|-------------|--------------------------------------------------|
| `STANDARD`  | Not bulky and not heavy                          |
| `SPECIAL`   | Either bulky **or** heavy                        |
| `REJECTED`  | Both bulky **and** heavy                         |



The solution uses a `Package` class with the following methods:

class Package:
    def __init__(width, height, length, mass)
    def is_bulky() -> bool
    def is_heavy() -> bool
    def classify() -> str  # Returns "STANDARD", "SPECIAL", or "REJECTED"
