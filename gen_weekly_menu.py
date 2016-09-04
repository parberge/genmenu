#!/usr/bin/env python3

from menuGenerator import GenMenu

my_lunch_menu = [
    'Lunch på föris',
    'Lunch på föris',
    'Lunch på föris',
    'Lunch på föris',
    'Lunch på föris',
    'Lunch på föris',
    'Lunch på föris',
]

my_dinner_menu = [
    'Pyttipanna',
    'Lasagne (rester)',
    'Lax med rotfrukter',
    'Gnocchi med frästa grönsaker',
    'Potatissoppa',
]

menu = GenMenu()

menu.insert_lunch_menu(my_lunch_menu)

menu.insert_dinner_menu(my_dinner_menu)

menu.generate_menu()

for day in menu.week_days:
    print('%s' % day)
    menu_for_day = menu.my_menu[day]
    print('Lunch: %s' % menu_for_day.get('lunch'))
    print('Dinner: %s' % menu_for_day.get('dinner'))
    print()

