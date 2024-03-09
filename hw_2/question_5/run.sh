#!/bin/bash
# Author: Andrew Serra
# Description: Runs the python test files in the same directory

echo $(pwd)
QUESTION_DIR="/Users/andrewserra/GithubProjects/csci-665/hw_2/question_5"

pushd $QUESTION_DIR

for case_num in {1..12}
do
    result=$(cat inputs/input-3.$case_num | python3 flood.py)
    output=$(cat outputs/answer-3.$case_num)

    if [[ $result = $output ]]; then
        echo "Test ${case_num}: SUCCESS"
    else
        echo "Test ${case_num}: FAIL"
        echo "---- Output:   " $result
        echo -e "---- Expected: " $output "\n"
    fi
done

popd
