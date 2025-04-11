# 📦 Package Sorting System

This project simulates a **robotic arm** for sorting packages based on their dimensions and mass, according to Thoughtful test rules.

## 📌 Objective

Sort incoming packages into the correct stack:

- A package is **bulky** if:
  - Volume ≥ 1,000,000 cm³, or
  - Any dimension ≥ 150 cm.
- A package is **heavy** if:
  - Mass ≥ 20 kg.

## 🧠 Rules

| Condition                     | Stack     |
|------------------------------|-----------|
| Not bulky and not heavy      | `STANDARD` |
| Bulky or heavy               | `SPECIAL`  |
| Bulky and heavy          | `REJECTED` |

## 🚀 Usage

### ✅ Requirements

- Python 3.6+

### 🔧 Run a package check:

```bash
python main.py --width 100 --height 100 --length 100 --mass 10
````
- Expected Output:
```bash
Result: SPECIAL
````

### 🧪 Run tests:

```bash
python main.py --test
````
- Expected Output:
```bash
Passed: sort(100, 100, 99, 19) ==> 'STANDARD'
Passed: sort(150, 10, 10, 19) ==> 'SPECIAL'
...
📊 Results:
8 Passed
0 Failed
```
