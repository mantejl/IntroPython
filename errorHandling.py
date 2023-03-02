# Mantej Lamba
# Error handling and working with dictionaries

from typing import IO, Dict


def open_file() -> IO:
    file_pointer = None
    while file_pointer is None:
        try:
            file_pointer = open(input("Enter name of file: "))
        except IOError as e:
            print("An error occured, please check the filename")
    return file_pointer


# returns a dictionary, where keys the word
# are mapped to the numbers
def read_file(input_file_pointer: IO) -> Dict[str, int]:
    content = {}
    for line in input_file_pointer:
        word_and_num = line.strip().split(" ")
        if len(word_and_num) != 2 or not word_and_num[1].isdigit(): # checking if it contains a word and digit
            print(line, "not formatted well")
        else:
            content[word_and_num[0]] = word_and_num[1] # adding the data to the dictionary
    return content


def write_file(dict_of_words: Dict[str, int]) -> None:
    output_filename = input("Enter the name of the output file: ")
    output_file = open(output_filename, "w")
    for i in dict_of_words: # iterating through dictionary of words
        line = (i + "\n") * int(dict_of_words[i]) # reading the items
        output_file.write(line) # writing them
    output_file.close() # closing the file 
    print(output_filename + " has been created.")


# No change is needed in main. Just add comments.
def main():
    print("Welcome to the File Expansion program.")
    input_file_pointer = open_file()
    file_contents = read_file(input_file_pointer)
    write_file(file_contents)


if __name__ == "__main__":
    main()