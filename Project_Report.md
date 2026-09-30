# PROJECT REPORT
**Personal Workout Tracker – A Python Command-Line Application**  
**Name:** Daksh Harwani &nbsp;&nbsp;&nbsp;&nbsp; **Registration No.:** 26BCE11292

---

## Abstract
This report covers how I designed, built, and tested a Personal Workout Tracker, a small command-line program written in Python. You type in a duration in minutes, a category, and an optional note, and the program temporarily stores it in memory during your session. You can then list your workouts, delete the ones you entered wrongly, and see a summary with totals for each category, each category's share of the whole, this month's exercise, and the overall total. I used only the standard library. Along the way, the project gave me hands-on practice with lists, exception handling, dictionaries, sorting, and formatted output. The result is a tool that is actually useful for keeping an eye on your fitness routine.

## 1. Introduction
Most people know they should keep track of their physical activity, but few actually stick with it. Writing everything down by hand gets boring quickly, and the fitness apps that do the job often have far more features than a person needs. I wanted something much smaller, so this tracker sticks to three things: adding a workout quickly, tracking it for the current session, and showing a clear summary. It runs from a simple menu and needs no internet or accounts.

## 2. Problem Statement
Ordinary people rarely have an easy, offline way to record their daily workouts and then see totals by category and by month. Notes on paper or in a phone memo do no arithmetic for you. Spreadsheets take time to set up. Commercial apps usually want an account and a connection to the internet. This project tries to fill that gap with a tool that is quick to learn and quick to use.

## 3. Objectives
- Let the user record a workout with a duration, category, and note, with the date added automatically.
- Keep the data in memory (session storage) while the program runs.
- Check what the user types so that bad input cannot crash the program.
- Show all workouts in a clear, numbered table.
- Let the user delete an entry that was entered by mistake.
- Give a summary by category, for the current month and for all time.
- Keep the code simple, split into small functions, and well commented.

## 4. System Requirements
| **Type** | **Requirement** |
| :--- | :--- |
| **Hardware** | Any computer capable of running Python 3; 1 GB RAM |
| **Operating system** | Windows, Linux or macOS |
| **Software** | Python 3.6 or later; a text editor or IDE (IDLE, VS Code, PyCharm) |
| **Libraries** | `datetime` (standard library only) |
| **Input / Output** | Keyboard and terminal screen |

## 5. System Design

### 5.1 Overall Architecture
The program is built in two simple parts. The **user interface layer** is the text menu, which is displayed by `main()`. The **logic layer** holds one function for each job: `add_workout`, `view_workouts`, `delete_workout`, and `show_summary`. While the program is running, the workouts live in a list in memory. 

### 5.2 Data Structure
Every workout is stored as a Python dictionary with four keys, and all the workouts together form a list of these dictionaries.

| **Field** | **Type** | **Description** |
| :--- | :--- | :--- |
| **date** | String (YYYY-MM-DD) | Date of the workout, taken from the system clock in ISO format |
| **duration** | Float | Minutes exercised; must be greater than zero |
| **category** | String | Title-cased category such as Cardio, Strength, Flexibility or Other |
| **note** | String | Optional free-text remark |

### 5.3 Program Flow
At start-up, an empty list is created. After that, the main loop keeps showing the menu, takes the user's choice, and calls the function that matches it. This continues until the user enters `0`. 

## 6. Module Description
| **Function** | **Purpose** | **Key techniques** |
| :--- | :--- | :--- |
| `add_workout()` | Takes input, validates it, and builds a record | `try`/`except`, `strip`, `title`, `isoformat` |
| `view_workouts()` | Prints a formatted table of all records | `enumerate`, f-string alignment |
| `delete_workout()` | Removes a chosen record after showing the list | `int()`, `list.pop`, range check |
| `show_summary()` | Computes category totals, percentages and month/all-time totals | dictionary `get`, sorted with `key`, `startswith` |
| `main()` | Displays the menu and dispatches to functions | `while` loop, `if-elif` chain |

## 7. Implementation Details

### 7.1 Adding a Workout
The duration is first read as plain text and then converted using `float()`. If that fails, the program catches the `ValueError` and asks for a proper number. A separate check then turns down anything that is zero or negative. For the category, `strip()` and `title()` are applied so that "cardio" and "CARDIO" both end up as "Cardio", and if the user leaves it empty the category becomes "Other". The date comes from `date.today().isoformat()`.

### 7.2 Viewing Workouts
The header and every row are printed with f-string format specifiers, for example `{i:<5}` (left-aligned, width 5) and `{w['duration']:>15.2f}` (right-aligned, width 15, two decimal places). Because of these widths, the columns stay lined up whatever the values are. I used `enumerate(workouts, start=1)` so that the serial numbers begin at 1 instead of 0, which is easier for a person to read.

### 7.3 Deleting a Workout
The program shows the full list first so the user can see which number belongs to which workout. The number that is entered is converted to an integer and checked to be between 1 and the total number of records. The entry is then removed with `pop(number - 1)`, because Python counts list positions from 0. 

### 7.4 Generating the Summary
To build the summary, I use a dictionary called `totals` and add each duration to its category with `totals.get(category, 0) + duration`. Adding up its values gives the grand total. For the monthly figure, the program takes the first seven characters of today's ISO date (for example 2026-09) and adds up every workout whose date begins with them. The categories are then sorted from highest to lowest duration using `sorted()` with a lambda key function, and each percentage is worked out as category total divided by grand total, multiplied by 100.

## 8. Testing
I tested the program by hand, trying both correct and incorrect input. The main test cases and what happened in each are given below.

| **No.** | **Test case** | **Input** | **Expected result** | **Result** |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Add valid workout | 45, Cardio, Run | Workout added to list | Pass |
| 2 | Non-numeric duration | abc | Error message, back to menu | Pass |
| 3 | Zero duration | 0 | "Duration must be greater than 0." | Pass |
| 4 | Negative duration | -30 | "Duration must be greater than 0." | Pass |
| 5 | Blank category | (Enter) | Stored as Other | Pass |
| 6 | View with no data | Option 2 | "No workouts yet." | Pass |
| 7 | Delete valid number | 1 | Entry removed | Pass |
| 8 | Delete invalid number | 99 | "No workout with that number." | Pass |
| 9 | Delete non-numeric | x | "Please enter a whole number." | Pass |
| 10 | Summary with data | Option 4 | Correct totals and percentages | Pass |
| 11 | Invalid menu choice | 7 | "Invalid choice, try again." | Pass |

## 9. Results and Discussion
Every test case gave the result I expected. The program responds instantly and did not crash on any wrong input I tried. The categories were grouped properly in the summary, and the percentages added up to about 100. Because the design is so simple, the code is easy to follow and to extend.

## 10. Limitations
- The interface is text-only.
- An existing entry cannot be edited. It has to be deleted and typed in again.
- The monthly total only works for the current month, and there is no way to pick another one.
- The program resets when closed (no permanent data storage).

## 11. Future Scope
- Adding JSON file or database storage to persist workouts permanently.
- Editing entries, plus searching and filtering by date range or category.
- Exporting reports to CSV or PDF, and showing charts with Matplotlib.
- A graphical version using Tkinter, or a web version using Flask.

## 12. Conclusion
The Personal Workout Tracker does what I set out to do: it records, displays, deletes, and summarises personal workouts during a session. It is simple, dependable, and works fully offline. For me, the project was good practice in Python basics and in going through the whole process of designing, coding, testing, and documenting a small program.
