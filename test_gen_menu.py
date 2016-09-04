#!/usr/bin/env python

from menuGenerator import GenMenu
import pytest

my_lunch_menu = ['Köttbullar']
my_dinner_menu = ['Pizza']

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

def test_insert_dinner_menu(genmenu_instance):
    assert my_dinner_menu[0] == genmenu_instance.dinner_menu['Monday']

def test_generate_menu(genmenu_instance):
    assert isinstance(genmenu_instance.my_menu, dict)
    genmenu_instance.generate_menu()
    assert my_lunch_menu[0] == genmenu_instance.my_menu['Monday']['lunch']
    assert my_dinner_menu[0] == genmenu_instance.my_menu['Monday']['dinner']
