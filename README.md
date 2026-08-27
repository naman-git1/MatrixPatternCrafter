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

* **NumPy**

## 📋 Requirements

Before running the program, make sure you have:

* NumPy

You can check whether Python is installed by running:

```bash
python --version
```

or, on some systems:

```bash
python3 --version
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/concentric-matrix-generator.git
```

Replace `your-username` with your GitHub username.

### 2. Move into the project folder

```bash
cd concentric-matrix-generator
```

### 3. Install NumPy

```bash
pip install numpy
```

If your system uses `pip3`, use:

```bash
pip3 install numpy
```

## ▶️ How to Run

Run the Python file using:

```bash
python matrix.py
```

or:

```bash
python3 matrix.py
```

The program will ask you to enter a value for `n`.

Example:

```text
Enter the value of n: 7
```

The corresponding concentric matrix will then be displayed.

## 💡 How It Works

The program first creates an `n × n` matrix using NumPy.

Each position in the matrix is checked to find its distance from the four edges:

* Top
* Left
* Bottom
* Right

The closest edge determines which layer the position belongs to.

For example, in a `7 × 7` matrix:

* The outermost layer contains `7`
* The next layer contains `6`
* The next layer contains `5`
* The center contains `4`

This process is repeated for every position in the matrix.

## 🧩 Code Structure

```text
concentric-matrix-generator/
│
├── matrix.py
├── README.md
└── requirements.txt
```

### `matrix.py`

Contains the main Python program that takes the user's input and generates the matrix.

### `README.md`

Contains the project information, setup instructions, and explanation.

### `requirements.txt`

Contains the Python packages required to run the project.

## 📦 Dependencies

The project only requires one external Python library:

```text
numpy
```

The dependency can also be installed using:

```bash
pip install -r requirements.txt
```

## 🚫 Input Validation

The program checks whether the entered value is a positive integer.

If the user enters `0` or a negative number, the program displays a message asking for a positive value instead of trying to create an invalid matrix.

## 🎯 Purpose

This project was created as a simple exercise to practice:

* Python loops
* User input
* NumPy arrays
* Matrix manipulation
* Basic problem-solving

It is a small project, but it helped me understand how a mathematical pattern can be converted into a program.
