import numpy as np
from data_operations import collect_data, count_data, create_CSV_from_exams, create_CSV_from_directory
from file_operations import create_directory, create_dummy_files
from exam_operations import pull_exams, read_JSON, compare_exams

def main ():

    ## TASK 1 ##
    # collect data from the 'data' folder
    print("\n### PART 1 ###")
    files_ids = [exam.get_participant_id() for exam in collect_data()]

    # count the number of participants and exams
    participants_count = len(count_data(files_ids)[0])
    exam_count = count_data(files_ids)[1]

    # display the results
    print("Number of participants:", participants_count)
    print("Number of exams:", exam_count)

    ## TASK 2 ## 
    # create a CSV file from the files in the 'data' folder
    print("\n### PART 2 ###")
    create_CSV_from_directory('all_files.csv') # Could collect_data() to create list of exam objects and then create_CSV_from_exams()
    print("Generated all_files.csv")

    ## TASK 3 ## 
    # pull exams data from CSV files and compare them
    print("\n### PART 3 ###")
    completed_exams = pull_exams('all_files.csv')
    scheduled_exams = pull_exams('scheduled_visits.csv')

    # categorize exams as confirmed or unconfirmed and generate a new CSV
    confirmed = compare_exams(completed_exams, scheduled_exams)[0]
    unconfirmed = compare_exams(completed_exams, scheduled_exams)[1]
    combined = np.concatenate((confirmed, unconfirmed))
    create_CSV_from_exams(combined, "compare_files.csv")
    print("Generated compare_files.csv")

    ## TASK 4 ## 
    # create directories and copy files based on confirmation status
    print("\n### PART 4 ###")
    create_directory(combined)
    print("Copied files from compare_files into confirmed and unconfirmed folders.")

    ## TASK 5 ## 
    # count the number of confirmed and unconfirmed participants and exams
    print("\n### PART 5 ###")
    confirmed_files = pull_exams('compare_files.csv', True, False, False)
    confirmed_files_ids = [exam.get_participant_id() for exam in confirmed_files]
    confirmed_participants_count = len(count_data(confirmed_files_ids)[0])
    confirmed_exam_count = count_data(confirmed_files_ids)[1]
    print("Confirmed participants:", confirmed_participants_count)
    print("Confirmed exams:", confirmed_exam_count)

    unconfirmed_files = pull_exams('compare_files.csv', False, True, False)
    unconfirmed_files_ids = [exam.get_participant_id() for exam in unconfirmed_files]
    unconfirmed_participants_count = len(count_data(unconfirmed_files_ids)[0])
    unconfirmed_exam_count = count_data(unconfirmed_files_ids)[1]
    print("Unconfirmed participants:", unconfirmed_participants_count)
    print("Unconfirmed exams:", unconfirmed_exam_count)

    ## TASK 6 ## 
    # read data from a JSON file, create dummy files, and generate a new CSV
    print("\n### PART 6 ###")
    json_dict = read_JSON()
    create_dummy_files("dummy_files.csv", json_dict, confirmed_files)
    print("Generated dummy_files.csv")

    ## TASK 7 ## 
    # pull data from the dummy files, create directories, and copy files into the dummy folder
    print("\n### PART 7 ###")
    confirmed_files = pull_exams('dummy_files.csv', False, False, True)
    create_directory(confirmed_files, True)
    print("Copied files from dummy_files.csv into dummy folder.\n")
 
if __name__ == '__main__':
    main()
