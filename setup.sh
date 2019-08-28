#!/bin/bash

set -e

sudo yum install npm -y
npm install -g c9
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --user
pip3 install boto3 --user
pip3 install opencv-python --user

echo "==========> Dependencies installed successfully."