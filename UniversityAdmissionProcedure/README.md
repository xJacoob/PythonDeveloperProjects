# University Admission Procedure (Algorithmic Sorting Tool)
# Project from HyperSkill
## About the Project
This algorithmic tool automates the complex process of allocating student candidates to various university departments. The project demonstrates strong skills in multi-criteria sorting, file I/O operations, and managing complex relationships between multiple objects in Python.

## Key Features
* **Multi-Criteria Sorting**: Implements custom sorting algorithms to rank candidates based on their exam scores across different subjects.
* **Data Parsing (I/O)**: Efficiently reads large sets of candidate data from raw text files and dynamically processes them.
* **Automated Allocation**: Distributes accepted students into specific departments based on their capacity and candidate rankings.
* **Report Generation**: Automatically generates output text files for each department containing the final list of admitted students.

## Project Structure
* `univeristy.py` - The main executable script that triggers the admission process.
* `Recruitment.py` - Contains the core algorithmic logic and sorting mechanisms.
* `Candidate.py` - Data model representing an individual applicant (stores scores, preferences, etc.).
* `Department.py` - Data model representing a university faculty (handles capacity and acceptance logic).
* `applicants.txt` - Raw input data containing the pool of candidates.
* `biotech.txt`, `chemistry.txt`, `engineering.txt`, `mathematics.txt`, `physics.txt` - Automatically generated output files representing the final admission lists.

## How to Run
Ensure `applicants.txt` is in the root directory, then execute:
\`\`\`bash
python univeristy.py
\`\`\`
The script will process the data and update/create the specific department `.txt` files with the results.

## Technologies Used
* Python 3
* File I/O Operations
* Object-Oriented Programming (OOP)
