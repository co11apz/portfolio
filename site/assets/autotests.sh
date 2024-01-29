#!/bin/bash
pwd
cd ../../
pwd
cd autotests/tests
pwd
echo "Hello from autotests.sh"
pytest -s -v test_main_page.py
