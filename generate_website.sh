#!/bin/bash

cd python_files

sudo python bundle.py -all
sudo python generateIndex.py

cd ..

s3cmd sync ./ s3://bladenelson.com