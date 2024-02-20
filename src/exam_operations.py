import csv
import json
from exam import Exam

def pullExams(filename, confirmedOnly=False, unconfirmedOnly=False, isDummy=False):
    """
    pullExams reads exam information from a CSV file and returns a list of Exam objects.

    :param 1: filename: str
        The name of the CSV file containing exam information.

    :param 2: confirmedOnly: bool, optional (default=False)
        If True, stores only confirmed exams; if False, stores all exams.

    :param 3: unconfirmedOnly: bool, optional (default=False)
        If True, stores only unconfirmed exams; if False, stores all exams.

    :param 4: isDummy: bool, optional (default=False)
        If True, indicates that the data is being pulled from dummy_files.

    :return: List of Exam objects
        A list containing Exam objects representing exams based on the specified criteria.
    """
    exams = [] # Store exams from file

    # Read rows from exams scheduled
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(f) # Skip first line
        for row in reader:
            id = row[0]
            date = row[1]
            ranid = 0
            days_from_exam_one = 0

            # Catches incase row we're accessing is blank
            try:
                contents = row[2]
            except IndexError:
                contents = 0
            try:
                src = row[3]
            except IndexError:
                src = ""
            try:
                dst = row[4]
            except IndexError:
                dst = ""
            try:
                is_confirmed = row[5]
            except IndexError:
                is_confirmed = "0"

            # when pulling data from dummy_files the rows have different values 
            if isDummy:
                ranid = row[0]
                days_from_exam_one = row[1]
                src = row[2]
                dst = row[3]
                is_confirmed = row[4]

            exam = Exam(id, ranid, date, days_from_exam_one, contents, src, dst, is_confirmed)

            # confirmedOnly arg allows exams to store only confirmed exams, unconfirmed exams, or both
            if confirmedOnly == True and is_confirmed == "1":
                exams.append(exam)
            elif unconfirmedOnly == True and is_confirmed == "0":
                exams.append(exam)
            elif confirmedOnly == False and unconfirmedOnly == False:
                exams.append(exam)

    return exams

def readJSON():
    """
    readJSON reads data from a JSON file and returns it as a Python dictionary.

    :return: dict
        A dictionary containing data from the JSON file.
    """
    # parse the JSON string into a Python dictionary
    with open('ranid_linker.json', 'r') as file:
        data_dict = json.load(file)

    return data_dict
    
# iterate through exams to check if successfully scheduled
def compareExams(completed_exams, scheduled_exams):
    """
    compareExams compares completed exams with scheduled exams and categorizes them as confirmed or unconfirmed.

    :param 1: completed_exams: List of Exam objects
        A list containing Exam objects representing completed exams.

    :param 2: scheduled_exams: List of Exam objects
        A list containing Exam objects representing scheduled exams.

    :return: Tuple (confirmed: List of Exam objects, unconfirmed: List of Exam objects)
        - confirmed: A list containing Exam objects representing confirmed exams.
        - unconfirmed: A list containing Exam objects representing unconfirmed exams.
    """
    confirmed = [] # stores confirmed exams
    unconfirmed = [] # stores unconfirmed exams

    # iterate through exams to create a list of confirmed and unconfirmed exams
    for completed in completed_exams:
        completedId = completed.get_participant_id()
        completedDate = completed.get_date()
        completedContents = completed.get_contents()
        completedSrc = completed.get_src()
        completeDst = "\\"+ completedSrc[13:19]+"\\"+completedSrc[13:]
        is_confirmed = 0 # temporary variable to distinguish confirmed or unconfirmed

        for scheduled in scheduled_exams:
            scheduledId = scheduled.get_participant_id()
            scheduledDate = scheduled.get_date()

            # if exam is both completed and scheduled confirm the exam
            if completedId == scheduledId and completedDate == scheduledDate:
                is_confirmed = 1
                break

        # create exam objects to add to list
        if(is_confirmed == 1):
            confirmed_exam = Exam(completedId, 0, completedDate, 0, completedContents, completedSrc, "confirmed_files"+completeDst, 1)
            confirmed.append(confirmed_exam)
        else:
            unconfirmed_exam = Exam(completedId, 0, completedDate, 0, completedContents, completedSrc, "unconfirmed_files"+completeDst, 0)
            unconfirmed.append(unconfirmed_exam)

    return confirmed, unconfirmed
