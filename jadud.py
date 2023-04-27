"""
Purpose: Compute Jadud's error quotient (EQ) for every student based on their compilation logs and errors.

* Input/prerequisites: CSV files, one with all compilation events, the other with all compilation errors and/or
runtime exceptions. Join attribute: student_id.
* Output: Jadud's EQ for every individual student_id in the logs.

Author: Valdemar Švábenský <valdemar@upenn.edu>, University of Pennsylvania, 2023.
Reviewed by: TODO: We need to assign a code reviewer.
License: MIT.

===== UNIT TEST DOCUMENTATION =====

For testing, use the files 'hwtestfile-complete_snapshots.csv' and 'hwtestfile-compiler-errors.csv'.
The files were designed as follows:

Student A compiled at times 3, 4. Made no errors.
Student B compiled at times 1, 3, 5. Made errors in 1, 5 (not consecutive, different error types).
Student C compiled at times 1, 3, 4. Made errors in 1, 4 (not consecutive, same error types).
Student D compiled at times 5, 6. Made errors in 5, 6 (consecutive, different error types).
Student E compiled at times 4, 5. Made errors in 4, 5 (consecutive, same error types).
Student F compiled at times 1, 3, 4. Made errors in 1, 3, 4 (consecutive, first pair same error, second pair same error).
Student G compiled at times 1, 3, 4. Made errors in 1, 3, 4 (consecutive, first pair same error, second pair different error).
Student H compiled at times 1, 3, 4. Made errors in 1, 3, 4 (consecutive, first pair different error, second pair same error).
Student I compiled at times 1, 3, 4. Made errors in 1, 3, 4 (consecutive, first pair different error, second pair different error).

Expected output for the Jadud's EQ:
A 0.0
B 0.0
C 0.0
D 0.7272727272727273
E 1.0
F 1.0
G 0.8636363636363636
H 0.8636363636363636
I 0.7272727272727273
"""

import csv
import pandas as pd


def prepare_data_row(row, error_category):
    """
    Process a single line from a CSV file with compiler errors OR runtime errors.

    This function is called only from the function process_data_errors_exceptions() below.

    :param row: obj. Pointer to a line from a CSV reader.
    :param error_category: str. Compiler errors ('compiler-errors') or runtime errors ('exceptions').
    :return: tuple. Unique error defined by the student ID, timestamp, and the full error message.
    """
    assert error_category in ['compiler-errors', 'exceptions']
    student_id = row[0]
    timestamp = row[1].replace('_', ':')  # For compatibility with a different timestamp format in the snapshot files
    error = None

    if error_category == 'compiler-errors':
        error_message = row[4]
        linebreak_index_in_error_message = error_message.find('\n')  # Error messages may span multiple lines, we want only the first
        if linebreak_index_in_error_message == -1:  # There is no new line, the message fits a single line
            linebreak_index_in_error_message = len(error_message)
        error = error_message[:linebreak_index_in_error_message].strip()
    elif error_category == 'exceptions':
        error = row[3] + ' ' + row[4] + ' ' + row[5] + ' ' + row[6]  # Exception is uniquely identified by these fields
    return student_id, timestamp, error


def process_data_errors_exceptions(hw_name, error_category):
    """
    Read a single CSV file from the folder `data-compiler-errors` or 'data-exceptions' for one homework,
    and process this file to represent it in a dictionary with the following structure:
    { student_id : { timestamp : [errors] } }, where all entries are of type str.
    This dictionary represents all unique errors/exceptions a given student made at a given time.

    For example:
    {
        'student_A' : { 't1' : ['error_X', 'error_Y'] }
        'student_B' : { 't1' : ['error_X', 'error_X', 'error_Z'], 't2' : ['error_Y'] }
    }

    This function is called only from the function process_data_snapshots() below.

    :param hw_name: str. Number of the homework assignment, e.g. '03'.
    :param error_category: str. Compiler errors ('compiler-errors') or runtime errors ('exceptions').
    :return: dict. Dictionary with the structure described above.
    """
    assert error_category in ['compiler-errors', 'exceptions']
    filename = 'data-' + error_category + '/hw' + hw_name + '-' + error_category + '.csv'
    file_handle = open(filename, encoding='latin-1')
    reader = csv.reader(file_handle, delimiter=';')
    next(reader)  # Skip the CSV header
    all_errors = {}  # The dictionary

    for row in reader:
        student_id, timestamp, error = prepare_data_row(row, error_category)
        if student_id not in all_errors:
            all_errors[student_id] = {}
            all_errors[student_id][timestamp] = [error]
        elif timestamp not in all_errors[student_id]:
            all_errors[student_id][timestamp] = [error]
        else:
            all_errors[student_id][timestamp].append(error)
    file_handle.close()
    return all_errors


def process_data_snapshots(hw_name, error_category):
    """
    Read a single CSV file from the folder `data-snapshots` for one particular homework,
    and process this file to represent it in a dictionary with the following structure:
    { student_id : [compilation_events] }, where:
        * student_id is of type str, and
        * [compilation_events] is a list of lists representing compilation events, where:
            * [] is a successful compilation event (without any errors), and
            * a non-empty list contains strings that indicate errors occurring during that compilation event.
    Together, each list represents the whole student programming session.

    For example:
    {
        'student_A' : [ ['error_X', 'error_Y'], [], [] ]
        'student_B' : [ ['error_X', 'error_X', 'error_Z'], ['error_Y'], [], [], ['error_Z'] ]
    }

    This function is called only from the function compute_jadud_eq() below.

    :param hw_name: str. Number of the homework assignment, e.g. '03'.
    :param error_category: str. Compiler errors ('compiler-errors') or runtime errors ('exceptions').
    :return: dict. Dictionary with the structure described above.
    """
    assert error_category in ['compiler-errors', 'exceptions']
    all_errors = process_data_errors_exceptions(hw_name, error_category)
    filename = 'data-snapshots/hw' + hw_name + '-complete_snapshots.csv'
    file_handle = open(filename)
    reader = csv.reader(file_handle, delimiter=';')
    next(reader)  # Skip the CSV header
    all_students = {}  # The dictionary

    for row in reader:
        student_id, timestamp = row[0], row[1]
        errors = []  # Empty list indicates a successful compilation event (i.e., no errors)
        if student_id in all_errors and timestamp in all_errors[student_id]:  # all_errors is used only at this place
            errors = all_errors[student_id][timestamp]  # This student made 1 or more errors during this timestamp
        if student_id not in all_students:
            all_students[student_id] = []
        all_students[student_id].append(errors)
    file_handle.close()
    return all_students


def compute_jadud_eq(hw_name='03', error_category='compiler-errors'):
    """
    Calculate the Jadud's error quotient (EQ) for each student in the logs for the given homework files.
    The algorithm is described in the following publication on page 6:
        Matthew C. Jadud. 2006. Methods and tools for exploring novice compilation behaviour.
        In Proceedings of the second international workshop on Computing education research (ICER '06).
        ACM, New York, NY, USA, 73–84. https://dl.acm.org/doi/pdf/10.1145/1151588.1151600

    :param hw_name: str. Number of the homework assignment, e.g. '03'.
    :param error_category: str. Compiler errors ('compiler-errors') or runtime errors ('exceptions').
    :return: dict. Dictionary with the structure { student_id : jadud_eq_for_this_hw }.
    """
    all_students = process_data_snapshots(hw_name, error_category)
    all_scores_per_student = {}
    for student_id, student_session in all_students.items():
        student_total_eq = 0
        num_event_pairs_per_student = 0
        for i in range(len(student_session) - 1):  # 1. COLLATE: Create consecutive pairs from the events in the session
            num_event_pairs_per_student += 1
            current_event_errors = set(student_session[i])  # Create a set to ignore multiple errors of the same type
            next_event_errors = set(student_session[i + 1])

            eq_per_event_pair = 0  # Error score (quotient) for the pair of the current and next event
            if current_event_errors and next_event_errors:  # 2. CALCULATE: Score the event pair according to the algorithm
                eq_per_event_pair += 8  # Both events ended in (at least one) error
                if not current_event_errors.isdisjoint(next_event_errors):
                    eq_per_event_pair += 3  # Both events included the same error type
                eq_per_event_pair /= 11  # 3. NORMALIZE: Divide the score assigned to each pair by 11

            student_total_eq += eq_per_event_pair  # 4a. AVERAGE: Sum the scores...

        assert num_event_pairs_per_student > 0, 'This should not happen because it indicates no compilation events.'
        student_total_eq /= num_event_pairs_per_student  # 4b. AVERAGE: ... and divide by the number of pairs
        assert 0 <= student_total_eq <= 1, 'The EQ must be between 0 and 1'
        all_scores_per_student[student_id] = student_total_eq

    return all_scores_per_student


def get_results(error_category='compiler-errors'):
    """
    Compute Jadud's EQs for all students in all log files and export the EQs into CSV files.

    :param error_category: str. Compiler errors ('compiler-errors') or runtime errors ('exceptions').
    :return: None.
    """
    df_all = pd.DataFrame(columns=['student_id']).set_index('student_id')
    for hw_name in ['03', '04', '05', '06', '07', '08']:
        all_scores_per_student = compute_jadud_eq(hw_name, error_category)
        df_hw = pd.DataFrame.from_dict(all_scores_per_student, columns=['jadud_hw_' + hw_name], orient='index')
        df_all = df_all.join(df_hw, how='outer')

    # Output results and compute descriptive statistics
    filename = 'results/jadud-' + error_category
    df_all.to_csv(filename + '.csv', encoding='utf-8', index_label='student_id')
    df_all.describe().to_csv(filename + '-per-homework.csv', encoding='utf-8')
    df_all.apply(pd.Series.describe, axis=1).to_csv(filename + '-per-student.csv', encoding='utf-8')


if __name__ == '__main__':
    get_results('compiler-errors')
    get_results('exceptions')
