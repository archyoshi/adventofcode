import sys
import os

# Set workdir to current path
os.chdir(os.path.dirname(os.path.abspath(__file__)))
WORK_DIR = os.getcwd()

def get_first_digit(line:str) -> str :
    for character in line:
        if character.isdigit():
            return character
    return ''
        
def get_last_digit(line:str) -> str :
    return get_first_digit(reversed(line))

def compute(filename:str):
    with open(filename, "r") as file:
        lines = file.readlines()
    sum=0
    for line in lines:
        digits = int(get_first_digit(line) + get_last_digit(line))
        sum+=digits
    return(sum)

def main():
    if len(sys.argv) == 2:
        print(compute(sys.argv[1]))
    else:
        print("File not provided !")
    return 0

if __name__ == '__main__':
    sys.exit(main())