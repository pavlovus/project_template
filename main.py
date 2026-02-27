from app.io.input import *
from app.io.output import *

def main():
    res1 = input_from_console("Enter anything: ")
    output_to_console(res1)
    output_to_file(res1, "data/res1.txt")

    res2 = input_from_file("data/test.txt")
    output_to_console(res2)
    output_to_file(res2, "data/res2.txt")

    res3 = input_from_file_with_pandas("data/test.txt")
    output_to_console(res3)
    output_to_file(res3, "data/res3.txt")

if __name__ == '__main__':
    main()