import logging
import json
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

        # Probably a cleaner way of creating this dict...
        self.my_menu = {
            'Monday': {'lunch': '', 'dinner': ''},
            'Tuesday': {'lunch': '', 'dinner': ''},
            'Wednesday': {'lunch': '', 'dinner': ''},
            'Thursday': {'lunch': '', 'dinner': ''},
            'Friday': {'lunch': '', 'dinner': ''},
            'Saturday': {'lunch': '', 'dinner': ''},
            'Sunday': {'lunch': '', 'dinner': ''},
        }

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

        if logging_level not in log_levels.keys():
            raise ValueError("Invalid logging_level '{0}'".format(logging_level))

        logger.setLevel(log_levels.get(logging_level))
        self.logger = logger

    def insert_lunch_menu(self, inpt):
        """
        Inserts a list of lunches into the menu

        First item will be Monday and next Tuesday and so forth
        :param inpt: Iterator containing lunch items
        """

        self.populate_menu(self.lunch_menu, inpt)

    def insert_dinner_menu(self, inpt, file_format=None, randomize=False):
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

        if randomize:
            self.logger.debug("Randomizing food_items")
            self._randomize(food_items)

        self.logger.debug('food items is:{0}'.format(food_items))
        self.populate_menu(self.dinner_menu, food_items)

    def _randomize(self, lst):
        """
        Returns the list in random order
        """
        return random.shuffle(lst)

    def populate_menu(self, menu_dict, lst):
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
