#!/bin/bash

set -e

git add .
git commit -m "backup"
git push origin ALL_STEPS

echo "==========> Pushed to github."