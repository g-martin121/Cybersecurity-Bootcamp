#!/bin/bash
# Lets create an until loop that takes a variable and adds 1 till it reachs 10
# Have the script echo out what are current number is



# Start with the number 1
# Keep doing this UNTIL the number is greater than 10

number=1
until [ $number -eq 11 ]; do
echo "The number is now: $number"
number=$((number + 1))
done
