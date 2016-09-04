#!/usr/bin/env python3

from menuGenerator import GenMenu
import pytest

my_lunch_menu = [
    "kötbullar och Spaghetti",
    "Pannkakor",
    "Pizza",
    "Omelette",
    "Burgers",
    "Pasta",
    "Sallad",
]
my_dinner_menu = [
    "Falukorv med makaroner",
]

@pytest.fixture
def genmenu_instance():

    genmenu = GenMenu()

    # Create a lunch menu
    genmenu.insert_lunch_menu(my_lunch_menu)

    # Create a dinner menu
    genmenu.insert_dinner_menu(my_dinner_menu)

    # Generate the menu
    genmenu.generate_menu()

    return genmenu


def test_my_menu(genmenu_instance):
    assert genmenu_instance.my_menu['Monday']['lunch'] == my_lunch_menu[0]
    assert genmenu_instance.my_menu['Monday']['dinner'] == my_dinner_menu[0]