# NAME: Mantej Lamba
# ID: 2259394598
# DATE: 2022-10-10
# DESCRIPTION: working with strings and lists

from typing import List

TILE = "_" # global variable because we need to keep this constant
PLAYER = "&"

def display_fight_floor(size: int) -> None: # print out the floor
    for p1_idx in range(size):
        for p2_idx in range(p1_idx+1, size):
            floor = [TILE] * size # create empty floot
            floor[p1_idx] = PLAYER # insert players into floor
            floor[p2_idx] = PLAYER
            if comply_with_rules(floor):
                print("".join(floor)) # convert to string before print

def comply_with_rules(floor: List[str]) -> bool: # only print what works with floor
    chunks = "".join(floor).split(PLAYER) # create chunks of empty floor space
    for chunk in chunks:
        if (len(chunk) < 1):
            return False # if enough floor space then return time
    return True

def main():
    floor_size = int(input("Floor size: "))
    display_fight_floor(floor_size)

if __name__ == "__main__":
    main()
