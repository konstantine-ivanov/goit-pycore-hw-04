import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True) #autorese of styles

def print_tree(path: Path, space: str = ""):
    pass




def coloring(folder, space=""): #folder parcing and items coloring
    try:
        for item in folder.iterdir(): #step by step check

            if item.is_dir(): 
                print(space + Fore.BLUE + item.name)
                coloring(item, space + "    ") #recursion call if item is folder
            else:
                print(space + Fore.GREEN + item.name)

    except FileNotFoundError:
        print(space + Fore.RED + "File not found")




def main():
    if len(sys.argv) < 2: #check if path  entered
        print(Fore.RED + 'No folder path entered')
        sys.exit()
    
    path = Path(sys.argv[1])

    if not path.exists(): #check if path exists
        print(Fore.RED + "Path does not exist")
        sys.exit(1)
    
    if not path.is_dir(): #check if path is a directory
        print(Fore.RED + "This is not a directory")
        sys.exit(1)

    coloring(path)

if __name__ == "__main__":
    main()