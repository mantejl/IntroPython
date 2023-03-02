# TODO Provide comments for *ALL* lines, including the already provided ones.
# TODO Type your comments above the lines.
# TODO Replace all "pass" with proper code.
# NAME: Mantej Lamba
# ID: 2259394598
# DATE: 2022-11-23
# DESCRIPTION: Programming assignment 3 that builds on assignment 2, exposes us to working with libraries and understanding how
# to work with tuples, lists, file IO and constants

#importing proper libraries that are needed for the code
from Graph import *
from typing import IO, Tuple, List
# TODO
# constants declared
PROGRAMMER = "Mantej Lamba"
MEMBER_INFO = "1"
NUM_OF_FRIENDS = "2"
LIST_OF_FRIENDS = "3"
RECOMMEND = "4"
SEARCH = "5"
ADD_FRIEND = "6"
REMOVE_FRIEND = "7"
SHOW_GRAPH = "8"
SAVE = "9"

LINE = "\n*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*\n"


# TODO Complete the class.
class Member:

    # constructor for the member class
    def __init__(self, member_id: int,
                 first_name: str,
                 last_name: str,
                 email: str,
                 country: str):
        # setting the variables correclty
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.country = country

    def add_friend(self, friend_id) -> None:
        # Check if the friend_id is not already in the list
        if (friend_id not in self.friends_id_list):
            self.friends_id_list.append(friend_id)

    def remove_friend(self, friend_id) -> None:
        # Check if the friend_id is already in the list
        if (friend_id not in self.friends_id_list):
            self.friends_id_list.remove(friend_id)

    def friend_list(self) -> List[int]:
        # Return friends list
        return self.friends_id_list

    def number_of_friends(self) -> int:
        # return number of friends
        return len(self.friends_id_list)

    def __str__(self) -> str:
        # must be in the format as shown in the handout
        # creating a big string and concatenating them together
        finalStr = self.first_name + " " + self.last_name + "\n" +  self.email + "\nFrom " + \
                   self.country + "Has " + str(self.number_of_friends()) + " friends. \n"
        return finalStr

    # Do not change
    def display_name(self) -> str:
        # returning the full name in the proper format
        return self.first_name + " " + self.last_name

def open_file(file_type: str) -> IO:
    # asking what file the user would like to open
    file_name = input("Enter the " + file_type + " filename:\n")
    # TODO To save time, comment out the above line and uncomment the following section.
    # TODO Do not forget to return it back before submitting.
    # if file_type == "profile":
    #     file_name = "profile_10.csv"
    # else:
    #     file_name = "connection_10.txt"
    # creating a file pointer
    file_pointer = None
    # keeping the loop running as long as the file pointer is none
    while file_pointer is None:
        # trying to open the file
        try:
            file_pointer = open(file_name, "r")
        except IOError:
            # if the file is unable to open, then show this error message and aks user to input file name again
            print(f"An error occurred while opening the file {file_name}.\n"
                  f"Make sure the file path and name are correct \nand that "
                  f"the file exist and is readable.")
            file_name = input("Enter the " + file_type + " filename:\n")
    # returning file pointer
    return file_pointer

# create network function
def create_network(fp: IO) -> List[List[int]]:
    # storing the first line as an int in size
    size = int(fp.readline())
    # empty list called network
    network = []

    # adding another list in each list index to create a 2D list
    for i in range(size):
        network.append([])

    # reading the next line in the file
    line = fp.readline()

    # while loop as long as the line isnt none and the length is >= 3
    while line is not None and len(line) >= 3:
        # stripping the line of spaces
        split_line = line.strip().split(" ")
        # storing the member id as ints from split_line
        member_id1 = int(split_line[0])
        member_id2 = int(split_line[1])
        # if member_id2 is not in the network of member_id1, then we will add it
        if member_id2 not in network[member_id1]:
            network[member_id1].append(member_id2)
        # if member_id1 is not in the network of member_id2, then we will add it
        if member_id1 not in network[member_id2]:
            network[member_id2].append(member_id1)

        # sorting the networks of member id 1 and member id 2
        network[member_id1].sort()
        network[member_id2].sort()
        # reading the next line
        line = fp.readline()

    # returning the network
    return network

def num_in_common_between_lists(list1: List, list2: List) -> int:
    # declaring degree variable
    degree = 0
    # iterating through the length of list 1
    for i in range(len(list1)):
        # if any elements in list 1 are in list 2, then we increment degree
        if list1[i] in list2:
            degree += 1

    # returning degree
    return degree


def init_matrix(size: int) -> List[List[int]]:
    # intializing list called matrix
    matrix = []
    # iterating through the size
    for row in range(size):
        # adding a list to the matrix to make it 2D
        matrix.append([])
        # iterating through the size
        for column in range(size):
            # adding a 0 to each row
            matrix[row].append(0)

    # returning the matrix
    return matrix


def calc_similarity_scores(profile_list: List[Member]) -> List[List[int]]:
    # calling init_matrix function on the length of profile list
    matrix = init_matrix(len(profile_list))

    # iterating through the length of profile list
    for i in range(len(profile_list)):
        # iterating from i to the length of profile list
        for j in range(i, len(profile_list)):
            # calling the num_in_common_between_lists function between the two friends id list of profile list i and j
            degree = num_in_common_between_lists(
                profile_list[i].friends_id_list,
                profile_list[j].friends_id_list)

            # setting the matrix values to degree
            matrix[i][j] = degree
            matrix[j][i] = degree
    # returning matrix
    return matrix


def recommend(member_id: int, friend_list: List[int], similarity_list: List[int]) -> int:
    # declaring two variables to -1
    max_similarity_val = -1
    max_similarity_pos = -1

    # iterating through the length of similarity_list
    for i in range(len(similarity_list)):
        # checking if i is not in the friend list and if i is not equal to member id
        if i not in friend_list and i != member_id:
            # checking if the i'th value of similarity list is greater than max similarity val
            if max_similarity_val < similarity_list[i]:
                # if it is then we set the two variables to i and similarity list [i]
                max_similarity_pos = i
                max_similarity_val = similarity_list[i]

    # returning the max smiliarity position
    return max_similarity_pos


def create_members_list(profile_fp: IO) -> List[Member]:
    # creating a list called profiles
    profiles = []
    # reading the line
    profile_fp.readline()
    # reading the line again
    line = profile_fp.readline()
    # splitting the line with ","
    profile_list = line.split(',')
    # looping through while the line is not none and length of profile list = 5
    while line is not None and len(profile_list) == 5:
        # creating a member obj
        memObj = Member(profile_list[0], profile_list[1], profile_list[2], profile_list[3], profile_list[4])
        # adding that member object to the profiles list
        profiles.append(memObj)
        # reading the next line
        line = profile_fp.readline()
        # splitting it with ","
        profile_list = line.split(',')
    # returning the list of profiles
    return profiles


def display_menu():
    # printing out the menu options header
    print("\nPlease select one of the following options.\n")
    # printing out the menu options
    print(MEMBER_INFO + ". Show a member's information \n" +
          NUM_OF_FRIENDS + ". Show a member's number of friends\n" +
          LIST_OF_FRIENDS + ". Show a member's list of friends\n" +
          RECOMMEND + ". Recommend a friend for a member\n" +
          SEARCH + ". Search members by country\n" +
          ADD_FRIEND + ". Add friend\n" +
          REMOVE_FRIEND + ". Remove friend\n" +
          SHOW_GRAPH + ". Show graph\n" +
          SAVE + ". Save changes\n"
    )

    # returning the input of what key the user presses
    return input("Press any other key to exit.\n")


def receive_verify_member_id(size: int):
    # creating boolean called valid == false
    valid = False
    # while valid is true
    while not valid:
        # storing the input in member_id
        member_id = input(f"Please enter a member id between 0 and {size}:\n")
        # if the input is not a digit
        if not member_id.isdigit():
            print("This is not a valid entry")
            # if the member id is not within the size
        elif not 0 <= int(member_id) < size:
            print("This member id does not exist")
            # if neither of these conditions are met then we set valid to true
        else:
            valid = True
    # returning the member id as an int
    return int(member_id)


def add_friend(profile_list: List[Member],
               similarity_matrix: List[List[int]]) -> None:
    # storing length of the profile list in size
    size = len(profile_list)
    # asking for the member id of the first friend
    print("For the first friend: ")
    # getting the member id and storing it in member1
    member1 = int(input("Please enter a member id between 0 and 10: "))
    # asking for the member id of the second friend
    print("For the second friend: ")
    # getting the member id and storing it in member2
    member2 = int(input("Please enter a member id between 0 and 10: "))
    # if member1 is equal to member2
    if member1 == member2:
        # printing out the two different ids
        print("You need to enter two different ids. Please try again.")
        # else if member 1 is in the friend id list of member 2
    elif member1 in profile_list[member2].friends_id_list:
        # printing out message
        print("These two members are already friends. Please try again.")
    else:
        # else adding the two friends to each other
        profile_list[member1].add_friend(member2)
        profile_list[member2].add_friend(member1)
        # iterating through the range of size
        for i in range(size):
            # if member 2 is in friends id list in profile list
            if member2 in profile_list[i].friends_id_list:
                # increase the similarity matrix value by one
                similarity_matrix[member1][i] += 1
                # if member 1 is not equal to i
                if member1 != i:
                    # similarity matrix value is incremented by one
                    similarity_matrix[i][member1] += 1
            # if member 1 is in the friend id list
            if member1 in profile_list[i].friends_id_list:
                # then we increment similarity matrix value by 1
                similarity_matrix[member2][i] += 1
                # if member 2 is not i
                if member2 != i:
                    # then we increment similarity matrix value by 1
                    similarity_matrix[i][member2] += 1
        # print out that the connection is added
        print("The connection is added. Please check the graph.")

def remove_friend(profile_list: List[Member],
                  similarity_matrix: List[List[int]]) -> None:
    # storing the length of profile list in size
    size = len(profile_list)
    # asking for the first friend
    print("For the first friend: ")
    # checking if the member id is valid
    member1 = receive_verify_member_id(size)
    # asking for the second friends
    print(f"For the second friend, select from following list: {profile_list[member1].friends_id_list}")
    # verifying if member 2 is valid
    member2 = receive_verify_member_id(size)
    # if they are equal to each other
    if member1 == member2:
        # ask again
        print("You need to enter two different ids. Please try again.")
        # if member 1 is not in the friend id list
    elif member1 not in profile_list[member2].friends_id_list:
        # ask again
        print("These two members are not friends. Please try again.")
    else:
        # else we remove member 1 from member 2 and vice versa
        profile_list[member1].remove_friend(member2)
        profile_list[member2].remove_friend(member1)
        # iterating through the range of size
        for i in range(size):
            # if member 2 is in the friends id list
            if member2 in profile_list[i].friends_id_list:
                # TODO
                # then we remove member 2
                profile_list[i].friends_id_list.remove(member2)

            # if member 1 is in the friends id list
            if member1 in profile_list[i].friends_id_list:
                # TODO
                # then we remove member 1
                profile_list[i].friends_id_list.remove(member1)

        # set the similarity matrix values of member 1 and 2 to -1
        similarity_matrix[member1][member1] -= 1
        similarity_matrix[member2][member2] -= 1

        # printing confirmation message
        print("The connection is removed. Please check the graph.")



# This function asks for a country name and list all members from that country.
def search(profile_list: List[Member]) -> None:
    # getting input
    country = input("Please enter a country name: ")
    # iterating through profile list
    for member in profile_list:
        # lower casing the input
        memCountry = member.country.lower()
        # stripping it and comparing it
        if (memCountry.strip("\n") == country.lower()):
            # if it's equal, then we print
            print(member.display_name())

# Do not change.
def add_friends_to_profiles(profile_list: List[Member],
                            network: List[List[int]]) -> None:
    # iterating through the length of profile list
    for i in range(len(profile_list)):
        # setting the friends id list value to the specific value in network
        profile_list[i].friends_id_list = network[i]


def select_action(profile_list: List[Member],
                  network: List[List[int]],
                  similarity_matrix: List[List[int]]) -> str:
    # showing the menu
    response = display_menu()
    # printing the options
    print(LINE)
    # getting the length of profile list
    size = len(profile_list)
    # if the response is one of the constants
    if response in [MEMBER_INFO, NUM_OF_FRIENDS, LIST_OF_FRIENDS, RECOMMEND]:
        # verifying the member id
        member_id = receive_verify_member_id(size)
        # creating memeber object
        memberObj = profile_list[member_id]

    # if it's equal to the first constant
    if response == MEMBER_INFO:
        # TODO Complete the code
        # printing the objext
        print(memberObj)
        # if it's equal to the second constant
    elif response == NUM_OF_FRIENDS:
        # TODO Complete the code
        # printing name and number of friends
        print(memberObj.first_name + " has " + str(memberObj.number_of_friends()) + " Friends.")
        # if it's equal to the third constant
    elif response == LIST_OF_FRIENDS:
        # TODO Complete the code
        # iterating through the friends list and printing the names
        for i in memberObj.friends_id_list:
            print (profile_list[i].member_id + " " + profile_list[i].display_name())
            # if it's equal to the fourth constant
    elif response == RECOMMEND:
        # TODO Complete the code
        # calling the recommend function
        rec = recommend(member_id, memberObj.friend_list(), similarity_matrix[member_id])
        # printing it out in a proper format
        print ("The suggested friend for " + profile_list[member_id].display_name() + " is " +
               profile_list[rec].display_name() + " with id " + str(rec) + ".")
        # if it's equal to the fifth constant
    elif response == SEARCH:
        # TODO Complete the code
        # searching the profile list
        search(profile_list)
        # if it's equal to the sixth constant
    elif response == ADD_FRIEND:
        # TODO Complete the code
        # adding friend with the function
        add_friend(profile_list,similarity_matrix)
        # if it's equal to the seventh constant
    elif response == REMOVE_FRIEND:
        # TODO Complete the code
        # calling remove friend with the function
        remove_friend(profile_list, similarity_matrix)
    # if it's equal to the eigth constant
    elif response == SHOW_GRAPH:
        # creating a list called tool tip
        tooltip_list = []
        # iterating through the profile list
        for profile in profile_list:
            # adding it to the tooltip list
            tooltip_list.append(profile)
        # creating the graph
        graph = Graph(PROGRAMMER,
                      [*range(len(profile_list))],
                      tooltip_list, network)
        # drawing the graph
        graph.draw_graph()
        # printing the output message
        print("Graph is ready. Please check your browser.")
        # if it's equal to the ninth constant
    elif response == SAVE:
        # TODO Complete the code
        # calling the save changes function
        save_changes(profile_list)
    else:
        # returning exit
        return "Exit"
    # printing the line
    print(LINE)
#   # returning continue
    return "Continue"


def save_changes(profile_list: List[Member]) -> None:
    # asking for file name
    file_name = input("Please enter a filename: ")
    # opening file
    filePtr = open(file_name, "w")
    # writing the number of users
    user = len(profile_list)
    filePtr.write(user + "\n")
    # creating list for friend dictionary
    friendDictionary = []
    # iterating through profile list
    for mem in profile_list:
        # iterating through the range of friends
        for friend in range(mem.number_of_friends()):
            # if the friend combo does not exist in the list (avoid repeats like the file format)
            if (str(mem.member_id) + str(mem.friend_list()[friend]) not in friendDictionary):
                # then we add it to the dictionary
                friendDictionary.append(str(mem.friend_list()[friend]) + str(mem.member_id))
                # and write it to the file
                filePtr.write(str(mem.member_id) + " " + str(mem.friend_list()[friend]) + "\n")
    # closing the file
    filePtr.close()
    # printing final message
    print("All changes are saved in " + file_name + ".")




# Do not change
def initialization() -> Tuple[List[Member], List[List[int]], List[List[int]]]:
    # open file
    profile_fp = open_file("profile")
    # create the member list from profile
    profile_list = create_members_list(profile_fp)
    # opening the file
    connection_fp = open_file("connection")
    # creating the network
    network = create_network(connection_fp)
    # if the length is not equal to profile list
    if len(network) != len(profile_list):
        # then we ask for input again
        input("Both files must have the same number of members.\n"
              "Please try again.")
        exit()

    # adding friends to the profiles
    add_friends_to_profiles(profile_list, network)
    # finding the similarity scores
    similarity_matrix = calc_similarity_scores(profile_list)
    # closing the profile
    profile_fp.close()
    connection_fp.close()
    # returning the profile list, network, similarity matrix
    return profile_list, network, similarity_matrix

#  Do not change.
def main():
    # welcome message
    print("Welcome to the network program.")
    # data file messages
    print("We need two data files.")
    # initiliazing
    profile_list, network, similarity_matrix = initialization()
    # setting action to continue
    action = "Continue"
    # while it is not continue
    while action != "Exit":
        # we call select action
        action = select_action(profile_list, network, similarity_matrix)
    # after program is done, print this
    input("Thanks for using this program.")

# main call
if __name__ == "__main__":
    main()