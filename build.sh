#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install Django==4.1.x djangorestframework djongo
