#!/bin/bash
#colors
pink='\033[0;35m'
nc='\033[0m'
target=17

echo -e "${pink}Welcome to the Number Guessing game!"
echo "I'm thinking of a number between 1 and 20..."

read -p "Take a guess: " guess

if [ "$guess" -eq "$target" ]; then
    echo "Correct!"
else 
    echo -e "Incorrect!${nc}"
fi

