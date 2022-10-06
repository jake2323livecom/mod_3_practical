import re
import os


if __name__ == '__main__':

    # List of directories containing files you'd like to add numbering to.
    TARGET_DIRS = [
        '.'
    ]
    EXCLUDED_FILES = []

    # Patterns for matching specific files and headings within those files
    FILENAME_PATTERN = re.compile('^Lab_\d{1,2}')
    TASK_HEADING_PATTERN = re.compile('^# Task \d{1,3}')
    STEP_HEADING_PATTERN = re.compile('^## Step \d{1,2}')


    files = []
    for directory in TARGET_DIRS:
        for file_name in os.listdir(directory):
            if file_name not in EXCLUDED_FILES and os.path.isfile(f'{directory}/{file_name}') and FILENAME_PATTERN.match(file_name):
                files.append(f'{directory}/{file_name}')
                print(f'Matched file: {file_name}')


    for file in files:
        print(f'The current file is {file}')

        try:
            with open(file, 'r') as f:
                lines = f.readlines()
            scheme = None
        except UnicodeDecodeError:
            with(open(file, 'r', encoding = 'UTF-8')) as f:
                lines = f.readlines()
            scheme = 'UTF-8'

        task_counter = 1
        step_counter = 1

        for index, line in enumerate(lines):

            if TASK_HEADING_PATTERN.match(line):
                step_counter = 1
                lines[index] = TASK_HEADING_PATTERN.sub(f'# Task {task_counter}', line)
                task_counter += 1
            
            if STEP_HEADING_PATTERN.match(line):
                lines[index] = STEP_HEADING_PATTERN.sub(f'## Step {step_counter}', line)
                step_counter += 1





        new_content = ''.join(lines)
        if scheme:
            with open(file, 'w', encoding=scheme) as new_file:
                new_file.write(new_content)
        else:
            with open(file, 'w') as new_file:
                new_file.write(new_content)

