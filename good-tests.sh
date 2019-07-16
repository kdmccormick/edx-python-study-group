#!/bin/sh

set -e

pytest test_1.py
pytest test_2.py
# pytest test_3.py # purposefully broken
pytest test_4.py
# pytest test_5.py # purposefully broken
pytest test_6.py
pytest test_7.py
pytest test_8.py
