def log_entries_with_keyword(log_file, keyword):
    with open(log_file, 'r') as file:
        yield f"\nThese are the lines from the {log_file} file that are matching with the {key}\n"
        for line in file:
            if keyword in line.lower():
                yield line

key = input("Provide the keyword: ")
for i in ['task_log_1.log', 'task_log_2.log']:
    for entry in log_entries_with_keyword(i, key.lower()):
        print(entry, end='')
