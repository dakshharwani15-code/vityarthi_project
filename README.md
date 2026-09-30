**README**

_Personal Workout Tracker – A Python Command-Line Application_

**Name:** DAKSH HARWANI **Registration No.:** 26BCE11292

# 1. About the Project

**Personal Workout Tracker** is a beginner-friendly, menu-driven Python program that helps you keep a record of your daily workouts. You can add workouts, view them in a table, delete wrong entries and see a summary of how much you have exercised in each category and in the current month. All data is stored in memory during runtime, so no external libraries or files are needed.

**Author:** DAKSH HARWANI **Registration No.:** 26BCE11292

# 2. Features

- **Add workout** – enter the duration, category and an optional note; today's date is recorded automatically.
- **View workouts** – see every workout in a numbered, neatly aligned table.
- **Delete workout** – remove a wrongly entered workout by its number.
- **Summary** – category-wise totals with percentages (highest first), this month's total and the all-time total.
- **Session storage** – data is maintained in-memory for the duration of the session.
- **Input validation** – invalid durations and invalid delete numbers are rejected with clear messages.
- **Default category** – if you leave the category blank, it is stored as "Other".

# 3. Technologies Used

| **Item**  | **Details**                                                     |
| --------- | --------------------------------------------------------------- |
| Language  | Python 3 (3.6 or later, because f-strings are used)             |
| ---       | ---                                                             |
| Modules   | datetime – part of the Python standard library                  |
| ---       | ---                                                             |
| Storage   | In-memory list (data resets upon exiting the program)           |
| ---       | ---                                                             |
| Interface | Command line / terminal (text menu)                             |
| ---       | ---                                                             |

# 4. Requirements

- A computer running Windows, Linux or macOS.
- Python 3.6 or newer. To check, open a terminal and type: python --version (or python3 --version).
- A terminal or command prompt, or any Python IDE such as IDLE, VS Code or PyCharm.
- No additional packages need to be installed.

# 5. Project Structure

```
PersonalWorkoutTracker/
|-- workout_tracker.py    # main program (all the code)
|-- README.md             # this document
```

# 6. Installation and Running

1. Download or copy the file workout_tracker.py into a new folder on your computer.
2. Open a terminal or command prompt and move into that folder, for example: cd PersonalWorkoutTracker
3. Run the program with: python workout_tracker.py (on some systems use python3 workout_tracker.py).
4. The main menu appears. Type the number of the option you want and press Enter.
5. Choose 0 to exit.

# 7. Author and Licence

Developed by **DAKSH HARWANI** (Registration No. **26BCE11292**) as an academic project. This project is provided for educational purposes and may be freely used and modified for learning.
