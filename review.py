import os

import argparse
import dotenv
from openai import OpenAI

def load_prompt(input_file):
    result = ""
    with open("review_prompt.txt", "r") as f:
        result += f.read()
    with open(input_file, "r") as f:
        result += f.read()
    return result

def main(input_filepath, output_file):
    print(f"{input_filepath} --> {output_file}")
    dotenv.load_dotenv()
    client = OpenAI(api_key=os.environ['OPENAI_KEY'])

    output_data = client.responses.create(
      model='gpt-4.1',
      input=[
        {
          "role": "user",
          "content": [
            {
              "type": "input_text",
              "text": load_prompt(input_filepath)
            }
          ]
        }
      ]
    )

    #print(output_data)
    #print(output_data.output_text)

    result = output_data.output_text.replace("```csv", "").replace("```", "").strip('\n')

    with open(output_file, 'w') as f:
        f.write(result)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('input_file')
  parser.add_argument('output_file')
  args = parser.parse_args()

  main(args.input_file, args.output_file)