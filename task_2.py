from pathlib import Path

def get_cats_info(path) -> list:
    #init vars
    cats = []
    file_path = Path(path)
    #check is path exists and its a file
    if file_path.exists() and file_path.is_file():
        #open in utf-8
        with open(path, 'r', encoding='UTF-8') as file:
            lines = file.readlines() #try another method for read file line by line
            for line in lines: 
                cat_info = line.strip().split(',') #separete all data
                if len(cat_info) == 3: # if complete info for cat
                    cats.append({'id': cat_info[0], 'name': cat_info[1], 'age': cat_info[2]})
                else:
                    print(f"Info in line: {line.strip()} is incomplete")
        
        return cats
    else: #if no file in path
        print(f"There is no file with path {path}, check file path")
        return None


cats = get_cats_info('cats.txt')
print(cats)