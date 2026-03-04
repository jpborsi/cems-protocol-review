#!/bin/zsh

for file in text_protocol/*; do
  if [ ! -f review/openai/gpt-4_1/${file:t:r}.csv ]; then
    uv run review.py $file review/openai/gpt-4_1/${file:t:r}.csv;
  fi
done