#!/usr/bin/env python

from menuGenerator import GenMenu
import pytest
import os

my_lunch_menu = ['Köttbullar', 'hamburgare' ]
my_dinner_menu = ['Pizza', 'Pasta carbonara' ]


def test_logging_debug():
    test_instance = GenMenu(logging_level='debug')
    # Defined in the logging class
    debug_int_value = 10
    assert test_instance.logger.getEffectiveLevel() == debug_int_value
    assert 0

@pytest.fixture
def genmenu_instance():
    genmenu_obj = GenMenu()
    genmenu_obj.insert_lunch_menu(my_lunch_menu)
    genmenu_obj.insert_dinner_menu(my_dinner_menu)
    return genmenu_obj

def test_lunch_dict(genmenu_instance):
    assert isinstance(genmenu_instance.lunch_menu, dict)
    for day in genmenu_instance.week_days:
        assert day in genmenu_instance.lunch_menu

def test_dinner_dict(genmenu_instance):
    assert isinstance(genmenu_instance.dinner_menu, dict)
    for day in genmenu_instance.week_days:
        assert day in genmenu_instance.dinner_menu

def test_insert_lunch_menu(genmenu_instance):
    assert my_lunch_menu[0] == genmenu_instance.lunch_menu['Monday']
    assert my_lunch_menu[1] == genmenu_instance.lunch_menu['Tuesday']

def test_insert_dinner_menu(genmenu_instance):
    assert my_dinner_menu[0] == genmenu_instance.dinner_menu['Monday']
    assert my_dinner_menu[1] == genmenu_instance.dinner_menu['Tuesday']

def test_generate_menu(genmenu_instance):
    assert isinstance(genmenu_instance.my_menu, dict)
    genmenu_instance.generate_menu()
    assert my_lunch_menu[0] == genmenu_instance.my_menu['Monday']['lunch']
    assert my_dinner_menu[0] == genmenu_instance.my_menu['Monday']['dinner']

def test_insert_dinners_with_json_file():
    base_dir = os.path.dirname(__file__)
    test_file = os.path.join(base_dir, 'test_dinners.json')
    genmenu_instance = GenMenu()
    genmenu_instance.insert_dinner_menu(test_file, file_format='json')
    assert genmenu_instance.dinner_menu['Monday'] == 'Pizza'
    assert genmenu_instance.dinner_menu['Tuesday'] == 'Pasta carbonara'
