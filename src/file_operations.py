import os
import csv
import numpy as np
from datetime import datetime

def createDirectory(exams, createDummy=False):
    """
    createDirectory creates directories and text files based on Exam objects.

    :param 1: exams: List of Exam objects
        A list containing Exam objects representing exams.

    :param 2: createDummy: bool, optional (default=False)
        If True, creates dummy folders and files; otherwise, creates folders and files based on Exam objects.

    :no return
    """
    for exam in exams:
        # different paths/folder names needed for dummy folder
        if(createDummy):
            file_name = exam.get_dst()[24:]
            folder_path = exam.get_dst()[:24]
            try:
                with open(exam.get_src(), 'r') as file:
                    contents = file.readline() # sets contents as contents based on src
            except FileNotFoundError:
                print(f"The file '{exam.get_src()}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            # accounts for confirmation changing size of filename/folderpath string
            if(exam.get_is_confirmed() == 1):
                file_name = exam.get_dst()[23:]
                folder_path = exam.get_dst()[:23]
            else:
                file_name = exam.get_dst()[25:]
                folder_path = exam.get_dst()[:25]
            contents = exam.get_contents()

        # Create folder
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Create text file
        with open(folder_path+file_name, 'w') as file:
            file.write(contents)

def createDummyFiles(filename, json_dict, compare_files_exams):
    """
    createDummyFiles generates a CSV file with dummy file information based on Exam objects.

    :param 1: filename: str
        The name of the CSV file to be created.

    :param 2: json_dict: dict
        A dictionary containing participant IDs as keys and associated information, such as 'ranid' and 'first_exam'.

    :param 3: compare_files_exams: List of Exam objects
        A list containing Exam objects representing exams to be compared.

    :no return
    """

    # Create CSV based off of files in directory
    with open(filename, 'w', newline='') as file:

        writer = csv.writer(file)
        field = ["ranid", "days_from_exam_one", "src", "dst", "is_confirmed"]
        writer.writerow(field) # Set column titles

        for exam in compare_files_exams:
            participant_id = exam.get_participant_id()
            ranid = json_dict[participant_id]["ranid"]
            date = exam.get_date()
            days_between = countDaysBetween(str(date), str(json_dict[participant_id]["first_exam"]))
            dst = "dummy_files/"+ranid+"/"+ranid+"_"+str(days_between)+"Days.txt"
            src = exam.get_dst()
            is_confirmed = exam.get_is_confirmed()

            writer.writerow([ranid, days_between, src, dst, is_confirmed]) # Write data into CSV


def countDaysBetween(date1, date2):
    """
    countDaysBetween calculates the difference in days between two dates.

    :param 1: date1: str
        The first date in the format YYYYMMDD.

    :param 2: date2: str
        The second date in the format YYYYMMDD.

    :return: int
    """
    # Convert strings to datetime objects
    date_format = "%Y%m%d"
    date1_obj = datetime.strptime(date1, date_format)
    date2_obj = datetime.strptime(date2, date_format)

    # Calculate the difference in days
    delta = date2_obj - date1_obj
    return abs(delta.days)  # Use abs to ensure a positive result
