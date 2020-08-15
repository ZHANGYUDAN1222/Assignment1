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
    with open('places.csv','r') as s_f:
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

# for the L_menu and M_menu
def read_list(places_n,places_v):
    # for the numbers
    count_places_total=1
    # list non-visited places
    for i in places_n:
        print('*%i. %-15s in %-15s priority%5s'%(count_places_total,i[0],i[1],i[2]))
        count_places_total+=1
    # list visited places
    for z in places_v:
        print(' %i. %-15s in %-15s priority%5s'%(count_places_total,z[0],z[1],z[2]))
        count_places_total+=1

# Add
def A_menu(places,places_n):
    valid_name=False
    while valid_name==False:
        new_place=input('Name:')
        if new_place=='' or new_place==' ':
            print('Input cannot be blank')
        else:
            valid_place=True
            break
    while valid_place:
        country=input('Country:')
        if country=='' or country==' ':
            print('Input cannot be blank')
        else:
            valid_country=True
            break
    while valid_country:
        priority=input('Priority:')
        if priority=='' or priority==' ':
            print('Invalid input; enter a valid number')
        elif priority.isdigit():
            if int(priority)<=0:
                print('Number must be > 0')
            else:
                print('%s in %s (priority %i) added to Travel Tracker.'%(new_place.title(),country.title(),int(priority)))
                places_n.append([new_place.title(),country.title(),int(priority),'n'])  # store in places_n and places
                places.append([new_place.title(),country.title(),int(priority),'n'])
                break
        else:
            print('Invalid input; enter a valid number')

# Mark
def M_menu(places,places_n,places_v):
    while True:
        if len(places_n)==0:
            print('No unvisited places')
            break
        change=input('''%i places. You still want to visit %i places.
Enter the number of a place to mark as visited
>>> '''%(len(places),len(places_n)))
        if change.isdigit():
            if int(change)<=0:
                print('Number must be > 0')
            elif len(places_n) < int(change) <= len(places):
                print('That place is already visited')
                break
            elif int(change) > len(places):
                print('Invalid place number')
            else:
                m_place=places_n[int(change)-1]
                print('%s in %s visited!'%(m_place[0],m_place[1]))
                places_n.pop(int(change)-1)
                places_v.append(m_place)
                break
        else:
            print('Invalid input; enter a valid number')

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
    if menu == 'L':  # list places
        read_list(places_n, places_v)
    elif menu == 'A':  # Add
        A_menu(places, places_n)
    elif menu == 'M':  # Mark
        read_list(places_n, places_v)
        M_menu(places, places_n, places_v)

if __name__ == '__main__':
    main()
