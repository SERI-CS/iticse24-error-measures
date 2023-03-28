import csv


class CompilationError:
    def __init__(self, student_id, timestamp):
        self.timestamp = timestamp
        self.error_types = []

def process_hw_log(hw_name='hw03'):
    errors_filename = 'data-errors/' + hw_name + '-compiler-errors.csv'
    errors_file = open(errors_filename, encoding='latin-1')
    errors_reader = csv.reader(errors_file, delimiter=';')
    next(errors_reader)
    all_errors = {}  # {student_id : {timestamp : [error_types]}}
    for row in errors_reader:
        student_id, timestamp, error_message = row[0], row[1], row[4]
        timestamp = timestamp.replace('_', ':')
        linebreak_index_in_error_message = error_message.find("\n")
        error_type = error_message[:linebreak_index_in_error_message].strip()
        if student_id not in all_errors:
            all_errors[student_id] = {}
            all_errors[student_id][timestamp] = [error_type]
        elif timestamp not in all_errors[student_id]:
            all_errors[student_id][timestamp] = [error_type]
        else:
            all_errors[student_id][timestamp].append(error_type)
    errors_file.close()

    snapshots_filename = 'data-snapshots/' + hw_name + '-complete_snapshots.csv'
    snapshots_file = open(snapshots_filename)
    snapshots_reader = csv.reader(snapshots_file, delimiter=';')
    next(snapshots_reader)
    for row in snapshots_reader:
        student_id, timestamp = row[0], row[1]
        errors = []
        if student_id in all_errors and timestamp in all_errors[student_id]:
            errors = all_errors[student_id][timestamp]

        if student_id not in all_students:
            all_students[student_id] = errors
        else:
            all_students[student_id].append(errors)
    snapshots_file.close()


if __name__ == '__main__':
    all_students = {}  # student_id : [compilation_events]
    process_hw_log()
    for student_id, student_session in all_students.items():
        student_error_quotient = 0
        for i in range(len(student_session) - 1):
            current_errors = set(student_session[i])
            next_errors = set(student_session[i+1])
            error_score_per_event_pair = 0
            if current_errors and next_errors:
                error_score_per_event_pair += 8
                if not current_errors.isdisjoint(next_errors):
                    error_score_per_event_pair += 3
                error_score_per_event_pair /= 11
            student_error_quotient += error_score_per_event_pair
        #student_error_quotient /=
        print(student_id, student_error_quotient)
