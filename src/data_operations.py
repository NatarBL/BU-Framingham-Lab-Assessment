import os
import csv
from exam import Exam

# Global variables
directory = '..\src\data\.'

def collectData():
    """
    collectData iterates through the specified data folder,
    collecting participant IDs and dates of exams and creating Exam objects.

    :return: List of Exam objects
        A list containing Exam objects, each representing an exam in the data folder.
    """

    # iterate over files in that directory
    exams = [] # Create hash map (participant, count)
    for path, subdirs, files in os.walk(directory):
        for name in files:
            date = name[10:20]
            participant_id = name[3:9] # slice participants id (ex. PT-999999)
            exams.append(Exam(participant_id, 0, date, 0, "", "", "", 0))
    return exams

def countData(participants_ids):
    """
    countData takes a list of participant IDs and counts the occurrences of each participant.

    :param participants_ids: List of str
        A list containing participant IDs.

    :return: Tuple (participants: dict, examCount: int)
        - participants: A hashmap (dictionary) containing participant IDs as keys
                        and the number of occurrences as values.
        - examCount: The total count of participant IDs.
    """
    examCount = 0
    participants = {} # Create hash map (participant, count)
    for participant in participants_ids:
        examCount += 1
        if(participant in participants):
            participants[participant] += 1
        else: 
            participants[participant] = 1

    return participants, examCount

def createCSVFromDirectory(filename):
    """
    createCSVFromDirectory creates a CSV file based on files in the specified directory.

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

def createCSVFromExams(exams, filename):
    """
    createCSVFromExams creates a CSV file based on Exam objects.

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
