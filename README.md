# Python file management exercise

## General Info

**Python 3.9.7**

## Tasks:

- 1.) Search these files and report the overall number of participants and number of exams
	- there should be 176 participants and 755 exams;
- 2.) Generate a CSV named "all_files.csv" with the following columns:
	- participant_id: the participant's ID
		- "PT-120108"
	- date: the date of the examination in YYYYMMDD format
		- "19991005"
	- contents: the integer found in the text file
		- some integer
	- filepath: relative path to the file
		- "data/1999/120108_1999_10_05.txt"

- Please see "sln/all_files.csv" for the correct CSV, as a point of comparison to check your work.

- Please see "scheduled_visits.csv"
	- it contains a participant_id and a date column
	- these are the participant_id + date combinations that we should have files for
	- there will be files that are NOT in this CSV and some that are in the CSV
	- this is intentional and is meant to approximately simulate the reality of data files not matching to the record of the data we should have
		- side note: this could happen for many reasons (scheduled_visits record hasn't been updated yet, data files were misnamed, etc.)

- 3.) Compare the files found in data/ to the participant_id and dates found in "scheduled_visits.csv" and prepare for copying of the files. All confirmed files should go to a folder named confirmed_files/ and all unconfirmed files should go to a folder named unconfirmed_files/
	- Generate a CSV named "compare_files.csv"
	- compare_files.csv should have the following columns:
		- participant_id:
			- "PT-120108"
		- date:
			- "19991005"
		- contents:
			- some integer from the txt file contents
		- src:
			- "data/1999/120108_1999_10_05.txt"
		- dst:
			- "<confirmed_files or unconfirmed_files>/120108/120108_1999_10_05.txt"
		- is_confirmed:
			- 1 if in scheduled_visits.csv, 0 otherwise.

- Please see "sln/compare_files.csv" as a point of comparison to check your work

- 4.) Copy files to appropriate locations
	- Use compare_files.csv to copy the files

- 5.) Report the overall number of participants and number of exams for both confirmed and unconfirmed exams.
	- The confirmed exams should have 133 participants with 251 exams
	- The unconfirmed exams should include 162 participants with 504 exams
	- Write a function to print out the above numbers based on your files.

	- Please note that the confirmed participants and unconfirmed participants can overlap (e.g., a participant could have confirmed exam(s) and unconfirmed exam(s)), which means that we don't expect the number of participants with confirmed exams and unconfirmed exams to add up to 176.
	- However, the number of exams should total 755 (251 + 504)

- 6.) Create a copy of all the confirmed text files and replace the participant ID with a predefined random ID (ranid) and replace the date with the number of days between that date and the participant's first exam.
	- Oftentimes, to protect sensitive participant data, we must replace the real participant ID with a random ID series and we have to replace the date with the number of days between that date and the participant's first exam date.
	- This further protects the original participant identifier and removes the exact date of the exam, while still retaining the relative timing between different data points collected from the participant.

	- Use ranid_linker.json to load the mapping between the participant id ("pt_id") and the random ID ("ranid") and the first exam date ("first_exam")

	- Generate a CSV named "dummy_files.csv" by using "compare_files.csv" as an input.
	- dummy_files.csv should have the following columns:
		- ranid:
			- "555-0106157" (the random ID)
		- days_from_exam_one:
			- 437 (the number of days between "first_exam" and "date")
		- src:
			- confirmed_files/... (using compare_files.csv "dst")
		- dst:
			- dummy_files/555-0106157/555-0106157_437Days.txt
			- dummy_files/<ranid>/<ranid>_<days_from_exam_one>Days.txt
		- is_confirmed:
			- retain this column from compare_files.csv - note that we only want confirmed files (is_confirmed=1)

	- Please see "sln/dummy_files.csv" as a point of comparison to check your work.

- 7.) Copy files to appropriate locations.
	- use dummy_files.csv to copy the files.

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
