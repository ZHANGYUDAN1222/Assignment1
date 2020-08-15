"""
Replace the contents of this module docstring with your own details
Name:Yudan Zhang
Date started: 30/07/2020
GitHub URL:https://github.com/JCUS-CP1404/assignment-1-travel-tracker-ZHANGYUDAN1222
"""
from operator import itemgetter
import csv

# transfer csv to list
def csv_to_list(places,places_n,places_v):
    with open('places.csv',newline='') as s_f:
        s_f_lines=s_f.readlines()
        for lines in s_f_lines:
            lines_list=lines.strip().split(',')
            # store list in list
            lines_list[2]=int(lines_list[2])
            places.append(lines_list)
            # store according to n / v
            if lines_list[3]=='n':
                places_n.append(lines_list)
            else:
                places_v.append(lines_list)
    return places, places_n, places_v



def main():
    print("Travel Tracker 1.0 - by <Yudan Zhang>")
    places = []
    places_v = []
    places_n = []

    places, places_n, places_v = csv_to_list(places, places_n, places_v)

    print("Travel Tracker 1.0 - by <Yudan Zhang>")
    places_n.sort(key=itemgetter(2))
    places_v.sort(key=itemgetter(2))
    menu = input('''Menu:
L - List places
A - Add new place
M - Mark a place as visited
Q - Quit
>>> ''').upper()

if __name__ == '__main__':
    main()
