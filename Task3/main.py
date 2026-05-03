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
    if len(sys.argv) < 2:
        print('No folder path entered')
    if not path.exists():
        print('No')        

    path = Path(sys.argv[1])




coloring(Path('Task3/picture'))