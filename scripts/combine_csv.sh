#!/bin/zsh

touch review/openai_combined_review.csv;

for file in review/openai/*; do echo "$file"; done