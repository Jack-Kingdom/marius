#!/usr/bin/env bash

set -e

python -m unittest discover -s . -p "*.py" -v