# Concentric Number Matrix Generator 🔢

A simple Python project that uses **NumPy** to generate a concentric number matrix based on a number entered by the user.

For example, when `n = 7`, the program generates a matrix where the outer layer contains `7`, the next layer contains `6`, and the numbers continue decreasing towards the center.

## 📌 Example

For `n = 7`, the output looks like:

```text
7 7 7 7 7 7 7
7 6 6 6 6 6 7
7 6 5 5 5 6 7
7 6 5 4 5 6 7
7 6 5 5 5 6 7
7 6 6 6 6 6 7
7 7 7 7 7 7 7
```

## 🛠️ Technologies Used

* Python
* NumPy

## 📋 Requirements

The project requires:

* NumPy


## ▶️ How to Run

Run the main Python file:

```bash
python matrix.py
```

The program will ask you to enter a value for `n`.

Example:

```text
Enter the value of n: 7
```

The corresponding concentric number matrix will then be displayed.

## 💡 How It Works

The program first creates an `n × n` matrix using NumPy.

For every position in the matrix, it checks its distance from the four edges:

* Top
* Left
* Bottom
* Right

The closest edge determines which layer that position belongs to.

For example, in a `7 × 7` matrix:

* The outermost layer contains `7`
* The next layer contains `6`
* The next layer contains `5`
* The center contains `4`

This process is repeated for every position in the matrix.

## 🧩 Project Structure

```text
concentric-matrix-generator/
│
├── Matrix pattern generation.py
├── README.md
```

### `Matrix pattern generation.py`

Contains the main program that takes user input and generates the concentric number matrix.

### `README.md`

Contains the project description, installation instructions, usage, and other information.


## 📦 Dependencies

The project uses:

```text
numpy
```

To install it manually:

```bash
pip install numpy
```

## 🚫 Input Validation

The program checks whether the entered value is a positive integer.

If the user enters `0` or a negative number, the program displays a message asking for a positive value instead of creating an invalid matrix.

## 🎯 Purpose

This project was created as a simple exercise to practice:

* Python loops
* User input
* NumPy arrays
* Matrix manipulation
* Basic problem-solving

It demonstrates how a mathematical pattern can be turned into a working program using Python and NumPy.
