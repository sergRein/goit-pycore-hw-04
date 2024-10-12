from colorama import Fore, Style
from pathlib import Path
import sys

def main():
    if len(sys.argv) > 1: #check arguments number
        file_path = Path(sys.argv[1]) #create path variable
        if file_path.exists() and file_path.is_dir(): #if is dir - lets read it
            read_catalog_tree(file_path)
        elif file_path.exists() and file_path.is_file(): #if its file just print it
            print_file(file_path)
        else:
            print("There is no such path in system, please provide correct path")
    else:
        print("Please set path as first argument to render files tree")


def read_catalog_tree(current_path, margin = 0):
    for elem in current_path.iterdir(): #iter input dir
        try: #try? maybe we cant acess some files or dirs
            if elem.is_file(): 
                print_file(elem,margin)
            elif elem.is_dir(): 
                print_dir(elem,margin)
                read_catalog_tree(elem, margin+1) #read dir in recursion
        except PermissionError: 
            print(Fore.RED + "Permission denied: {elem}")
        except Exception as e:
            print(Fore.RED + "Error reading {elem}: {e}")


def print_dir(dir_name, margin):
    print(Fore.BLUE + f"{' '*4*margin} {dir_name}/" + Style.RESET_ALL)


def print_file(file_name ,margin = 0):
    print(Fore.GREEN + f"{' '*4*margin} {file_name}" + Style.RESET_ALL)

if __name__ == '__main__':
    main()