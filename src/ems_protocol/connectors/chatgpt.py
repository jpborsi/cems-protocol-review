"""Open AI connector implementation."""
import os

from openai import OpenAI

from ems_protocol.connectors import core


class OpenAIConnector(core.Connector):
    def __init__(self, model='gpt-4.1'):
        self.model = model
        self.client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])


    def text_prompt(self, prompt):
        output_data = self.client.responses.create(
            model=self.model,
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": prompt,
                        }
                    ]
                }
            ]
        )
        return output_data

    def file_prompt(self, input_file, prompt):
        existing_files = self.client.files.list()
        existing_file_ids = {file.filename: file.id for file in existing_files.data}

        print(existing_file_ids)
        input_filename = input_file.split('/')[-1]

        if input_filename not in existing_file_ids:
            file_id = self.client.files.create(
                file=open(input_file, 'rb'),
                purpose='user_data',
                expires_after={
                    "anchor": "created_at",
                    "seconds": 3600
                }
            ).id
        else:
            file_id = existing_file_ids[input_filename]

        output_data = self.client.responses.create(
            model=self.model,
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
                            "text": prompt
                        },
                    ]
                }
            ]
        )
        return output_data
