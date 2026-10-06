# Student Registration System

A simple beginner Python project that simulates a student registration system.

This project was created as a practice project to work with different Python data structures and basic data manipulation.

## Features

- Store student information
- Store student courses
- Store student scores
- Access student information using indexing
- Add a new course to a student's courses
- Add a new student
- Display all student information

## Concepts Used

- Variables
- Lists
- Dictionaries
- Sets
- Tuples
- Indexing
- for loops
- append()
- set.add()
- print()

## Data Structure

The project combines several Python data structures:

- **List** → stores multiple students
- **Dictionary** → stores information about each student
- **Set** → stores courses without duplicates
- **Tuple** → stores student scores

The overall structure is:

List → Dictionary → Set / Tuple

## Example

Each student is represented as a dictionary:

```python
{
    "name": "Ali",
    "age": 20,
    "courses": {"Python", "Math"},
    "scores": (18, 15)
}