import logging
import json
import sys
import random

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

    def __init__(self, logging_level='info'):
        """
        Valid logging_level: debug, info, warning, error or critical

        These values are correlated with the log levels in logging module
        """

        logger = logging.getLogger(__name__)
        formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        std_handler = logging.StreamHandler()
        std_handler.setFormatter(formatter)
        logger.addHandler(std_handler)

        log_levels = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL,
        }

        if not logging_level in log_levels.keys():
            raise ValueError("Invalid logging_level '{0}'".format(logging_level))

        logger.setLevel(log_levels.get(logging_level))
        self.logger = logger


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


    def insert_dinner_menu(self, inpt, file_format=None, random=False):
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
            food_items = list(inpt)

        if random:
            self.logger.debug("Randomizing food_items")
            GenMenu.randomize(food_items)

        self.logger.debug('food items is:{0}'.format(food_items))
        self.dinner_menu = GenMenu.populate_menu(self.dinner_menu, food_items)

    @staticmethod
    def randomize(lst):
        """
        Returns the list in random order
        """
        return random.shuffle(lst)

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
