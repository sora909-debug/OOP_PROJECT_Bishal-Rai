# OOP_PROJECT_Bishal-Rai
# Student Grading System

## Overview

This is a simple console-based Student Grading System written in Python. It allows users to manage student records, assign subject marks, and view student reports with calculated averages and grades.

## Features

* Add new students with ID and name
* Assign subject marks to students
* Automatically calculate grades based on marks
* View all students with their subjects and average marks

## Project Structure

* **main.py** – Entry point with menu-driven interface
* **grading.py** – Core grading system logic
* **person.py** – Defines `Person` and `Student` classes
* **subject.py** – Defines `Subject` class and grading logic

## How It Works

1. Run the program
2. Choose options from the menu:

   * Add student
   * Add subject marks
   * View student report
3. The system calculates grades and averages automatically

## Grading Criteria

* 90+ → A+
* 80–89 → A
* 70–79 → B+
* 60–69 → B
* 50–59 → C
* Below 50 → F

## Requirements

* Python 3.x

## Run the Program

```bash
python main.py
```

## Notes

* Marks are stored as floating-point numbers
* Each student can have multiple subjects
* Data is stored temporarily (no database or file storage)

## Future Improvements

* Save data to file/database
* Edit/delete student records
* GUI interface
* Input validation improvements

---

Simple, clean, and beginner-friendly project for understanding object-oriented programming in Python.
