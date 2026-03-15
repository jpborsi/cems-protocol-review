import argparse
import os

import dotenv
from openai import OpenAI


def load_prompt(input_file):
    result = ""
    with open("exp002_prompt_review.txt", "r") as f:
        result += f.read()
    with open(input_file, "r") as f:
        result += f.read()
    return result


def run(input_filepath, output_file, iteration, client):
    output_filepath = f"{output_file}{iteration}.csv"
    print(f"{input_filepath} --> {output_filepath}")

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

    result = output_data.output_text.replace("```csv", "").replace("```", "").strip()

    with open(output_filepath, 'w') as f:
        f.write(result)


def main(input_filepath, output_file):
    dotenv.load_dotenv()
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    for i in range(5):
        run(input_filepath, output_file, i, client)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()

    main(args.input_file, args.output_file)
