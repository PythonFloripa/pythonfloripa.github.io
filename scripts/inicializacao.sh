#!/bin/bash

virtualenv .venv
. .venv/bin/activate
pip install -U pip setuptools wheel
pip install -r requirements.txt
cd site_python_floripa
nikola auto
