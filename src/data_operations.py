import os
import csv
import re
from exam import Exam
from collections import Counter


# Global variables
directory = '..\src\data\.'

def collect_data():
    """
    collect_data iterates through the specified data folder,
    collecting participant IDs and dates of exams and creating Exam objects.

    :return: List of Exam objects
        A list containing Exam objects, each representing an exam in the data folder.
    """

    # iterate over files in that directory
    exams = [] # Create hash map (participant, count)
    for path, subdirs, files in os.walk(directory):
        for name in files:
            date = re.sub("", "", re.search("^[^_]*_(.*)\.[^.]*$", name).group(1).upper()) # regex to find date (ex. 2020_01_01)
            participant_id = re.sub("", "", re.search("^[^_]*", name).group(0).upper()) # regex to find participants id (ex. PT-999999)
            exams.append(Exam(participant_id, 0, date, 0, "", "", "", 0))
    return exams

def count_data(participants_ids):
    """
    count_data takes a list of participant IDs and counts the occurrences of each participant.

    :param participants_ids: List of str
        A list containing participant IDs.

    :return: Tuple (participants: dict, exam_count: int)
        - participants: A hashmap (dictionary) containing participant IDs as keys
                        and the number of occurrences as values.
        - exam_count: The total count of participant IDs.
    """
    return Counter(participants_ids), len(Counter(participants_ids))

def create_CSV_from_directory(filename):
    """
    create_CSV_from_directory creates a CSV file based on files in the specified directory.

    :param 1: filename: str
        The name of the CSV file to be created.

    :param 2: directory: str
        The path to the directory containing files to be included in the CSV.

    :no return
    """
    # Create CSV based off of files in directory
    with open(filename, 'w', newline='') as file:

        writer = csv.writer(file)
        field = ["participant_id", "date", "contents", "filepath"]
        writer.writerow(field) # Set column titles

        # Iterate through sub-directories
        for path, subdirs, files in os.walk(directory):
            for name in files:

                # create data for columns
                participant_id = name[0:9]
                date = name[10:14]+name[15:17]+name[18:20]
                filelocation = os.path.join(path, name)
                filepath = filelocation[7:12]+filelocation[14:]

                with open(filelocation) as file:
                    contents = file.read().rstrip()

                # write data into CSV
                writer.writerow([participant_id, date, contents, filepath])

def create_CSV_from_exams(exams, filename):
    """
    create_CSV_from_exams creates a CSV file based on Exam objects.

    :param 1: exams: List of Exam objects
        A list containing Exam objects representing exams.

    :param 2: filename: str
        The name of the CSV file to be created.

    :no return
    """

    # create CSV based off of files in directory
    with open(filename, 'w', newline='') as file:

        writer = csv.writer(file)
        field = ["participant_id", "date", "contents", "src", "dst", "is_confirmed"]
        writer.writerow(field) # Set column titles

        # iterate through exams
        for exam in exams:
            participant_id = exam.get_participant_id()
            ranid = exam.get_ranid()
            date = exam.get_date()
            days_from_exam_one = exam.get_days_from_exam_one()
            contents = exam.get_contents()
            src = exam.get_src()
            dst = exam.get_dst()
            is_confirmed = exam.get_is_confirmed()

            # write data into CSV
            writer.writerow([participant_id, date, contents, src, dst, is_confirmed])
