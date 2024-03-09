#!/bin/bash
# Author: Andrew Serra
# Description: Runs the python test files in the same directory

echo $(pwd)
QUESTION_DIR="/Users/andrewserra/GithubProjects/csci-665/hw_3/question_4"
FILENAME=$1
pushd $QUESTION_DIR

for case_num in {1..3}
do
    start_time=$(date +%s)
    result=$(cat inputs/input-1.$case_num | python3 $FILENAME)
    end_time=$(date +%s)
    output=$(cat outputs/answer-1.$case_num)

    if [[ $result = $output ]]; then
        elapsed=$(( end_time - start_time ))
        echo "Test ${case_num}: SUCCESS"
        echo "Time elapsed ${elapsed}"
    else
        echo "Test ${case_num}: FAIL"
        echo "---- Output:   " $result
        echo -e "---- Expected: " $output "\n"
    fi
done

popd
