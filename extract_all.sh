#!/bin/zsh

for file in raw_protocol/*; do
  if [ ! -f text_protocol/${file:t:r}.md ]; then
    uv run extract.py $file text_protocol/${file:t:r}.md;
  fi
done