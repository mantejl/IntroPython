from typing import List

def get_filename(type_of_file:str) -> str: # get filename
    filename = input("Enter the name the " + type_of_file + " file: ")
    return filename

def read_file(input_filename: str) -> List[List[str]]: # read input file
    input_file = open(input_filename, "r") # open file
    content=[]
    for line in input_file: # read in each line into content
        word_and_num = line.strip().split(" ")
        content.append(word_and_num)
    input_file.close()
    return content # return content

def write_file(list_of_words: List[List[str]], output_filename: str) -> None: # create output files
    output_filename = open(output_filename, "w") # open the file
    for line in list_of_words: # for everything in content
        new_line = (line[0] + "\n") * int(line[1]) # print name n times
        output_filename.write(new_line) # go to a new line
    output_filename.close() # close

def main():
    print("Welcome to the file expansion program.")
    input_file = get_filename("input")
    output_file = get_filename("output")
    content = read_file(input_file) # take in
    write_file(content, output_file) # create output file


if __name__ == "__main__":
    main()