#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: May.30.2022
# program genertate numbers, puts them
# into a list then displays it

import constants
import random


def main():

    # initlizing sum and counter
    counter = 0
    sum = 0

    # declaring empty list
    list_of_num = []

    for counter in range(constants.MAX_SIZE):
        list_of_num.append(random.randint
                           (constants.MIN_NUM, constants.MAX_NUM))

        sum = sum + list_of_num[counter]
        print("{} is added to the list at position {}"
              . format(list_of_num[counter], counter))

    # calculates the average and displays it
    # sees if array is full
    for counter in range(1):
        average = sum / constants.MAX_SIZE

        # print the averge
        print("")
        print("The average is {}".format(average))


if __name__ == "__main__":
    main()
