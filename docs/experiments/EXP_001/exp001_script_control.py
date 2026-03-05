import os

import argparse
import dotenv
from openai import OpenAI

def load_prompt():
  with open("extract_prompt.txt", "r") as f:
    return f.read()

def main(input_filepath, output_file):
    print(f"{input_filepath} --> {output_file}")
    dotenv.load_dotenv()
    client = OpenAI(api_key=os.environ['OPENAI_KEY'])
    existing_files = client.files.list()
    existing_file_ids = {file.filename: file.id for file in existing_files.data}

    print(existing_file_ids)
    input_filename = input_filepath.split('/')[-1]

    if input_filename not in existing_file_ids:
      file_id = client.files.create(
        file=open(input_filepath, 'rb'),
        purpose='user_data',
        expires_after={
          "anchor": "created_at",
          "seconds": 3600
        }
      ).id
    else:
      file_id = existing_file_ids[input_filename]

    print(file_id)

    output_data = client.responses.create(
      model='gpt-4.1',
      input=[
        {
          "role": "user",
          "content": [
            {
              "type": "input_file",
              "file_id": file_id,
            },
            {
              "type": "input_text",
              "text": load_prompt()
            },
          ]
        }
      ]
    )

    #print(output_data)
    #print(output_data.output_text)

    result = output_data.output_text.replace("```markdown", "").replace("```", "")

    with open(output_file, 'w') as f:
        f.write(result)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('input_file')
  parser.add_argument('output_file')
  args = parser.parse_args()

  main(args.input_file, args.output_file)