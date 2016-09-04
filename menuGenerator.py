#!/usr/bin/env python

# Ask for the schools week menu and store it

# Create a list (and later on, a database) with user defined dinners

# Output a week menu with dinners that's not the same base food as the lunch from school


class GenMenu(object):

    week_days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ]

    lunch_menu = dict.fromkeys(week_days)
    dinner_menu = dict.fromkeys(week_days)

    my_menu = {
        'Monday': {'lunch': '', 'dinner': ''},
        'Tuesday': {'lunch': '', 'dinner': ''},
        'Wednesday': {'lunch': '', 'dinner': ''},
        'Thursday': {'lunch': '', 'dinner': ''},
        'Friday': {'lunch': '', 'dinner': ''},
        'Saturday': {'lunch': '', 'dinner': ''},
        'Sunday': {'lunch': '', 'dinner': ''},
    }

    def insert_lunch_menu(self, lst):
        """
        Inserts a list of lunches into the menu

        :param lst: A list of lunches.
        First item will be Monday and next Tuesday and so forth
        """
        lst_copy = list(lst)
        for item in lst:
            for day in self.week_days:
                if lst_copy:
                    lunch = lst_copy.pop(0)
                else:
                    lunch = None

                if lunch:
                    self.lunch_menu[day] = lunch


    def insert_dinner_menu(self, lst):
        """
        Inserts a list of dinners into the menu

        :param lst: A list of dinners
        First item will be Monday and next Tuesday and so forth
        """
        lst_copy = list(lst)
        for item in lst:
            for day in self.week_days:
                if lst_copy:
                    dinner = lst_copy.pop(0)
                else:
                    dinner = None

                if dinner:
                    self.dinner_menu[day] = dinner


    def generate_menu(self):
        """
        Generates the menu from lunch and dinner dicts
        """
        for k in self.lunch_menu:
            if self.lunch_menu[k]:
                self.my_menu[k]['lunch'] = self.lunch_menu[k]

        for k in self.dinner_menu:
            if self.dinner_menu[k]:
                self.my_menu[k]['dinner'] = self.dinner_menu[k]