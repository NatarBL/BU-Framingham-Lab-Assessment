# Bland FHS Research Programmer Interview README

## General Info

**Python 3.9.7**

### Data

- **data/**
  - This directory contains folders named after years.
  - Each year-folder will contain text files with the following filename pattern:
    - `<participant_id>-<year>_<month>_<day>`
  - Each text file has a single line containing an integer between (0, 999999) inclusive (6 digit integer).
  - Each text file represents an examination for that participant on that given date.
  - For example, we could have "PT-120108_1999_10_05.txt," representing the examination for participant 120108 on 1999_10_05 with the contents as a single line containing "5."

### Files

- README.txt
- scheduled_visits.csv
- ranid_linker.json
- sln/all_files.csv
- sln/compare_files.csv
- sln/dummy_files.csv
- **main**.py
- data_operations.py
- exam_operations.py
- file_operations.py

## Instructions

1. Unzip the project and open the src folder in the terminal.
2. Run: `python __main__.py`
3. **Task 1:** Check if terminal prints 176 participants and 755 exams.
4. **Task 2:** Check if all_files.csv was generated and contains the correct rows/columns (compare to sln).
5. **Task 3:** Check if compare_files.csv was generated and contains the correct rows/columns (compare to sln).
6. **Task 4:** Check confirmed/unconfirmed folders for correct txt files and contents.
7. **Task 5:** Check if terminal prints confirmed participants: 133, confirmed exams: 251, unconfirmed participants: 162, unconfirmed exams: 504.
8. **Task 6:** Check if dummy_files.csv was generated and contains the correct rows/columns (compare to sln). Please refer to the assumptions section as the README example was different than sln/dummy_files.csv.
9. **Task 7:** Check dummy_files folder for correct txt files and contents.

Note: Install any libraries you may be missing. I beleive for this project only Numpy needs to be installed.

## Assumptions

- In Task 3 of the README, the dst column of compare_files.csv is written as:

  - "`<confirmed_files or unconfirmed_files>/120108/120108_1999_10_05.txt`"
  - In Task 6, a new column in dummy_files.csv is created using the dst from compare_files.csv as the instructions state:
    - "`confirmed_files/...`" (using compare_files.csv "dst")
  - But in sln/dummy_files.csv, the columns are in a different format than what's stated in the README:
    - "`confirmed_files/PT-015256/PT-015256_2009_03_06.txt`"
  - Since the prefix "PT-" is not used elsewhere, I believe it is appropriate to leave it out for now, but if we wanted to add it, it would be a very easy change. This is worth noting, however, since the dummy_files.csv will not align with the src column in sln/dummy_files.csv.

- Tasks 6 and 7 do not explicitly state what the contents of the files should be in the dummy_files folder since content was not a column in dummy_files.csv. Since we are copying all the other information from the original text files, I assume we are also copying the contents. Therefore, I took the content from the original confirmed_files folder using the src from dummy_files.csv.
