# TODO Provide comments for *ALL* lines, including the already provided ones.
# TODO Type your comments above the lines.
# TODO Replace all "pass" with proper code.
# NAME: Mantej Lamba
# ID: 2259394598
# DATE: 2022-11-23
# DESCRIPTION: Programming assignment 3 that builds on assignment 2, exposes us to working with libraries and


from Graph import *
from typing import IO, Tuple, List
# TODO
PROGRAMMER = "Add your name here"
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
    def __init__(self, member_id: int,
                 first_name: str,
                 last_name: str,
                 email: str,
                 country: str):
        pass

    def add_friend(self, friend_id) -> None:
        # Check if the friend_id is not already in the list
        pass

    def remove_friend(self, friend_id) -> None:
        # Check if the friend_id is already in the list
        pass

    def friend_list(self) -> List[int]:
        # Return friends list
        pass

    def number_of_friends(self) -> int:
        # return number of friends
        pass

    def __str__(self) -> str:
        # must be in the format as shown in the handout
        pass

    # Do not change
    def display_name(self) -> str:
        return self.first_name + " " + self.last_name

def open_file(file_type: str) -> IO:
    # file_name = input("Enter the " + file_type + " filename:\n")
    # TODO To save time, comment out the above line and uncomment the following section.
    # TODO Do not forget to return it back before submitting.
    if file_type == "profile":
        file_name = "profile_10.csv"
    else:
        file_name = "connection_10.txt"
    file_pointer = None
    while file_pointer is None:
        try:
            file_pointer = open(file_name, "r")
        except IOError:
            print(f"An error occurred while opening the file {file_name}.\n"
                  f"Make sure the file path and name are correct \nand that "
                  f"the file exist and is readable.")
            file_name = input("Enter the " + file_type + " filename:\n")

    return file_pointer


def create_network(fp: IO) -> List[List[int]]:
    size = int(fp.readline())
    network = []

    for i in range(size):
        network.append([])

    line = fp.readline()

    while line is not None and len(line) >= 3:
        split_line = line.strip().split(" ")
        member_id1 = int(split_line[0])
        member_id2 = int(split_line[1])
        if member_id2 not in network[member_id1]:
            network[member_id1].append(member_id2)
        if member_id1 not in network[member_id2]:
            network[member_id2].append(member_id1)

        network[member_id1].sort()
        network[member_id2].sort()
        line = fp.readline()

    return network

def num_in_common_between_lists(list1: List, list2: List) -> int:
    degree = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            degree += 1

    return degree


def init_matrix(size: int) -> List[List[int]]:
    matrix = []
    for row in range(size):
        matrix.append([])
        for column in range(size):
            matrix[row].append(0)

    return matrix


def calc_similarity_scores(profile_list: List[Member]) -> List[List[int]]:
    matrix = init_matrix(len(profile_list))

    for i in range(len(profile_list)):
        for j in range(i, len(profile_list)):
            degree = num_in_common_between_lists(
                profile_list[i].friends_id_list,
                profile_list[j].friends_id_list)

            matrix[i][j] = degree
            matrix[j][i] = degree

    return matrix


def recommend(member_id: int, friend_list: List[int], similarity_list: List[int]) -> int:
    max_similarity_val = -1
    max_similarity_pos = -1

    for i in range(len(similarity_list)):
        if i not in friend_list and i != member_id:
            if max_similarity_val < similarity_list[i]:
                max_similarity_pos = i
                max_similarity_val = similarity_list[i]

    return max_similarity_pos


def create_members_list(profile_fp: IO) -> List[Member]:
    profiles = []
    profile_fp.readline()
    line = profile_fp.readline()
    profile_list = line.split(',')
    while line is not None and len(profile_list) == 5:
        pass

    return profiles


def display_menu():
    print("\nPlease select one of the following options.\n")
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

    return input("Press any other key to exit.\n")


def receive_verify_member_id(size: int):
    valid = False
    while not valid:
        member_id = input(f"Please enter a member id between 0 and {size}:\n")
        if not member_id.isdigit():
            print("This is not a valid entry")
        elif not 0 <= int(member_id) < size:
            print("This member id does not exist")
        else:
            valid = True

    return int(member_id)


def add_friend(profile_list: List[Member],
               similarity_matrix: List[List[int]]) -> None:
    size = len(profile_list)
    print("For the first friend: ")
    member1 = input("Please enter a member id between 0 and 10: ")
    print("For the second friend: ")
    member2 = input("Please enter a member id between 0 and 10: ")
    if member1 == member2:
        print("You need to enter two different ids. Please try again.")
    elif member1 in profile_list[member2].friends_id_list:
        print("These two members are already friends. Please try again.")
    else:
        profile_list[member1].add_friend(member2)
        profile_list[member2].add_friend(member1)

        for i in range(size):
            if member2 in profile_list[i].friends_id_list:
                similarity_matrix[member1][i] += 1
                if member1 != i:
                    similarity_matrix[i][member1] += 1
            if member1 in profile_list[i].friends_id_list:
                similarity_matrix[member2][i] += 1
                if member2 != i:
                    similarity_matrix[i][member2] += 1

        print("The connection is added. Please check the graph.")

def remove_friend(profile_list: List[Member],
                  similarity_matrix: List[List[int]]) -> None:
    size = len(profile_list)
    print("For the first friend: ")
    member1 = receive_verify_member_id(size)

    print(f"For the second friend, select from following list: {profile_list[member1].friends_id_list}")
    member2 = receive_verify_member_id(size)
    if member1 == member2:
        print("You need to enter two different ids. Please try again.")
    elif member1 not in profile_list[member2].friends_id_list:
        print("These two members are not friends. Please try again.")
    else:
        profile_list[member1].remove_friend(member2)
        profile_list[member2].remove_friend(member1)
        for i in range(size):

            if member2 in profile_list[i].friends_id_list:
                # TODO
                # profile_list[i].friends_id_list.remove(member2)
                pass

            if member1 in profile_list[i].friends_id_list:
                # TODO
                # profile_list[i].friends_id_list.remove(member1)
                pass

        similarity_matrix[member1][member1] -= 1
        similarity_matrix[member2][member2] -= 1

        print("The connection is removed. Please check the graph.")



# This function asks for a country name and list all members from that country.
def search(profile_list: List[Member]) -> None:

    pass

# Do not change.
def add_friends_to_profiles(profile_list: List[Member],
                            network: List[List[int]]) -> None:
    for i in range(len(profile_list)):
        profile_list[i].friends_id_list = network[i]


def select_action(profile_list: List[Member],
                  network: List[List[int]],
                  similarity_matrix: List[List[int]]) -> str:
    response = display_menu()

    print(LINE)
    size = len(profile_list)

    if response in [MEMBER_INFO, NUM_OF_FRIENDS, LIST_OF_FRIENDS, RECOMMEND]:
        member_id = receive_verify_member_id(size)

    if response == MEMBER_INFO:
        # TODO Complete the code

    elif response == NUM_OF_FRIENDS:
        # TODO Complete the code
    elif response == LIST_OF_FRIENDS:
        # TODO Complete the code
    elif response == RECOMMEND:
        # TODO Complete the code
    elif response == SEARCH:
        # TODO Complete the code
    elif response == ADD_FRIEND:
        # TODO Complete the code
    elif response == REMOVE_FRIEND:
        # TODO Complete the code
    elif response == SHOW_GRAPH:
        tooltip_list = []
        for profile in profile_list:
            tooltip_list.append(profile)
        graph = Graph(PROGRAMMER,
                      [*range(len(profile_list))],
                      tooltip_list, network)
        graph.draw_graph()
        print("Graph is ready. Please check your browser.")
    elif response == SAVE:
        # TODO Complete the code
    else:
        return "Exit"

    print(LINE)

    return "Continue"


def save_changes(profile_list: List[Member]) -> None:
    pass

# Do not change
def initialization() -> Tuple[List[Member], List[List[int]], List[List[int]]]:
    profile_fp = open_file("profile")
    profile_list = create_members_list(profile_fp)

    connection_fp = open_file("connection")
    network = create_network(connection_fp)
    if len(network) != len(profile_list):
        input("Both files must have the same number of members.\n"
              "Please try again.")
        exit()

    add_friends_to_profiles(profile_list, network)
    similarity_matrix = calc_similarity_scores(profile_list)

    profile_fp.close()
    connection_fp.close()

    return profile_list, network, similarity_matrix

#  Do not change.
def main():
    print("Welcome to the network program.")
    print("We need two data files.")
    profile_list, network, similarity_matrix = initialization()
    action = "Continue"
    while action != "Exit":
        action = select_action(profile_list, network, similarity_matrix)

    input("Thanks for using this program.")


if __name__ == "__main__":
    main()