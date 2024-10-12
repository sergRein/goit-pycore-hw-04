
from pathlib import Path

def total_salary(path) -> tuple:
    #init vars
    total = 0
    count_strings = 0 
    file_path = Path(path)
    #check is path exists and its a file
    if file_path.exists() and file_path.is_file():
        #open in utf-8
        with open(path, 'r', encoding='UTF-8') as file:
            while True:
                line = file.readline()
                if not line: #if end of file
                    break
                parts = line.strip().split(',') #separete name from sallary
                if len(parts) == 2: # if name and sallary
                    try:
                        total += int(parts[1].strip()) # add to total
                        count_strings += 1 # count all users
                    except ValueError: #if error in sallary
                        print(f"Cannot convert salary to integer in line: {line.strip()}")
        
        if count_strings == 0: #if empty file
            return (0,0)
        else:
            return (total, total // count_strings) 
    else: #if no file in path
        print(f"There is no file with path {path}, check file path")
        return None

total, average = total_salary("sallary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")