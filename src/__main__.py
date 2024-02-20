import numpy as np
from data_operations import collectData, countData, createCSVFromExams, createCSVFromDirectory
from file_operations import createDirectory, createDummyFiles
from exam_operations import pullExams, readJSON, compareExams

def main ():

    ## TASK 1 ##
    # collect data from the 'data' folder
    print("\n### PART 1 ###")
    files_ids = [exam.get_participant_id() for exam in collectData()]

    # count the number of participants and exams
    participantsCount = len(countData(files_ids)[0])
    examCount = countData(files_ids)[1]

    # display the results
    print("Number of participants:", participantsCount)
    print("Number of exams:", examCount)

    ## TASK 2 ## 
    # create a CSV file from the files in the 'data' folder
    print("\n### PART 2 ###")
    createCSVFromDirectory('all_files.csv')
    print("Generated all_files.csv")

    ## TASK 3 ## 
    # pull exams data from CSV files and compare them
    print("\n### PART 3 ###")
    completed_exams = pullExams('all_files.csv')
    scheduled_exams = pullExams('scheduled_visits.csv')

    # categorize exams as confirmed or unconfirmed and generate a new CSV
    confirmed = compareExams(completed_exams, scheduled_exams)[0]
    unconfirmed = compareExams(completed_exams, scheduled_exams)[1]
    combined = np.concatenate((confirmed, unconfirmed))
    createCSVFromExams(combined, "compare_files.csv")
    print("Generated compare_files.csv")

    ## TASK 4 ## 
    # create directories and copy files based on confirmation status
    print("\n### PART 4 ###")
    createDirectory(combined)
    print("Copied files from compare_files into confirmed and unconfirmed folders.")

    ## TASK 5 ## 
    # count the number of confirmed and unconfirmed participants and exams
    print("\n### PART 5 ###")
    confirmed_files = pullExams('compare_files.csv', True, False, False)
    confirmed_files_ids = [exam.get_participant_id() for exam in confirmed_files]
    confirmed_participants_count = len(countData(confirmed_files_ids)[0])
    confirmed_exam_count = countData(confirmed_files_ids)[1]
    print("Confirmed participants:", confirmed_participants_count)
    print("Confirmed exams:", confirmed_exam_count)

    unconfirmed_files = pullExams('compare_files.csv', False, True, False)
    unconfirmed_files_ids = [exam.get_participant_id() for exam in unconfirmed_files]
    unconfirmed_participants_count = len(countData(unconfirmed_files_ids)[0])
    unconfirmed_exam_count = countData(unconfirmed_files_ids)[1]
    print("Unconfirmed participants:", unconfirmed_participants_count)
    print("Unconfirmed exams:", unconfirmed_exam_count)

    ## TASK 6 ## 
    # read data from a JSON file, create dummy files, and generate a new CSV
    print("\n### PART 6 ###")
    json_dict = readJSON()
    createDummyFiles("dummy_files.csv", json_dict, confirmed_files)
    print("Generated dummy_files.csv")

    ## TASK 7 ## 
    # pull data from the dummy files, create directories, and copy files into the dummy folder
    print("\n### PART 7 ###")
    confirmed_files = pullExams('dummy_files.csv', False, False, True)
    createDirectory(confirmed_files, True)
    print("Copied files from dummy_files.csv into dummy folder.\n")
 
if __name__ == '__main__':
    main()
