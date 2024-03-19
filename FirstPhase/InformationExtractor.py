"""
This class will implement the information extractor
it will take the clean raw text from preprocess.py
and then called the model from Mistral.ai to extract the information

"""


class InformationExtractor:
    def __init__(self, rawText):
        self.text = rawText
        # self.model = genai.GenerativeModel('gemini-pro')

    def labelData(self):
        """
        This function will label the data using the model
        :return:
        """
        pass

import ollama
response = ollama.chat(model='mistral', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },])


