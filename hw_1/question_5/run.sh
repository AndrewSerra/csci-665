#!/bin/bash
# Author: Andrew Serra
# Description: Runs the python test files in the same directory

echo $(pwd)
QUESTION_DIR="/Users/andrewserra/GithubProjects/csci-665/hw_1/question_5"

pushd $QUESTION_DIR

# Clean out all output files
mkdir -p output

if [ ! -z "$(ls -A output)" ]; then
    rm ./output/*
fi

for file in *.test.py; do
    echo "Working on file ${file}..."
    FILENAME=$(basename $file)
    python3 $file >> ./output/${FILENAME}_runtimes.txt
done

popd
