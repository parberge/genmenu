#!/usr/bin/env python

import logging
import json
import sys

class GenMenu(object):

    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

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

    def insert_lunch_menu(self, inpt):
        """
        Inserts a list of lunches into the menu

        :param lst: A list of lunches.
        First item will be Monday and next Tuesday and so forth
        """

        self.lunch_menu = GenMenu.populate_menu(self.lunch_menu, inpt)


    def insert_dinner_menu(self, inpt, file_format=None):
        """
        Inserts a list of dinners into the menu

        If file_format is not specified, an iterator is expected
        First item will be Monday and next Tuesday and so forth

        Supported file_format(s): json
        """

        if file_format == 'json':
            with open(inpt, 'r') as f:
                food_items = json.load(f)
        else:
            food_items = inpt

        self.logger.debug('food items is:{0}'.format(food_items))
        self.dinner_menu = GenMenu.populate_menu(self.dinner_menu, food_items)

    @staticmethod
    def convert_json(json_obj):
        """
        Converts the json array to a list
        """
        import json

        return json.loads(json_obj)

    @staticmethod
    def populate_menu(menu_dict, lst):
        """
        Populate a menu with the items from a list
        """

        for day, food_item in zip(GenMenu.week_days, lst):
            menu_dict[day] = food_item

        return menu_dict

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
