# Citizen Complaint System

## Overview
A beginner-friendly command-line Python program for recording and tracking public-service complaints. It is designed for the PROG211 Object-Oriented Programming 1 assignment.

## Features
- Add, list, and find complaints.
- Update complaint status (`Submitted`, `Under Review`, or `Resolved`).
- Uses `Citizen` and `Complaint` classes and creates objects.
- Uses one Python data structure: a dictionary keyed by complaint ID.
- Includes an instance method (`display_info`) and a class method (`show_total`).
- Uses only Python's standard library.

## Requirements
- Python 3.8 or newer.
- No third-party packages are required.

## How to run
1. Save `citizen_complaint_system.py` to your computer.
2. Open Command Prompt or a terminal in the folder containing the file.
3. Run:

   ```bash
   python citizen_complaint_system.py
   ```

   On some systems, use `python3 citizen_complaint_system.py`.

## Example workflow
1. Choose `1` to add a complaint.
2. Enter a complaint ID such as `C001`.
3. Enter an anonymous citizen reference such as `CIT001`.
4. Enter a category and a short description.
5. Choose `2` to list complaints, `3` to find one, or `4` to update its status.
6. Choose `0` to exit.

## Object-oriented programming used
- **Classes and objects:** `Citizen`, `Complaint`, and `ComplaintSystem`.
- **Attributes:** complaint ID, citizen reference, category, description, and status.
- **Instance methods:** `display_info`, `update_status`, and system operations.
- **Class method:** `Complaint.show_total`, which reports the number of complaints created during the current run.
- **Object interaction:** `ComplaintSystem` creates and manages `Citizen` and `Complaint` objects.

## Digital Public Goods (DPG) principles
- **Open-source:** the source code can be shared and adapted.
- **Inclusive and accessible:** uses a simple text menu and clear prompts.
- **Privacy-respecting:** does not ask for names, phone numbers, addresses, or national ID numbers. Users should avoid entering private details in descriptions.
- **Modular and reusable:** functionality is separated into classes and methods.

## Important limitations
- Records are held in memory and disappear when the program closes.
- This is an educational prototype, not a production government service.
- A real deployment would need secure storage, authentication, access controls, validation, backups, and a privacy review.

## Suggested GitHub submission
Upload `citizen_complaint_system.py` and `README.md` to a public repository. Include screenshots of the program running and add the course lecturer as a collaborator if required by the assignment brief.
