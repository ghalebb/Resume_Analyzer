import json
import os.path

import google.generativeai as genai
from google.generativeai.types import GenerateContentResponse


class Checker:
    """"
    checks structure is the follow
    [
    { "CheckerName": "" , "data_key": ["PersInfo",etc..], "check_function": check_residence},
    { "CheckerName": "" , "data_key": ["PersInfo",etc..], "check_function": check_residence},
    { "CheckerName": "" , "data_key": ["PersInfo",etc..], "check_function": check_residence},
    ]
    """

    def __init__(self, key, pathOrJson, misspelling=None):
        genai.configure(api_key=key)
        if type(pathOrJson) is str:
            if not os.path.exists(pathOrJson):
                raise ValueError("File not found")
            self.json = readJsonFIle(pathOrJson)
        else:
            self.json = pathOrJson
        self.labels = self.json["Labels"]

        # This could be passed inside the json file and as a list
        if misspelling is not None:
            self.spelling = misspelling
        else:
            self.spelling = self.json["Spelling"]

        self.model = genai.GenerativeModel('gemini-pro')
        self.checks = [
            {"Checker": "residence Location", "data_key": ["PersInfo"]},
            {"Checker": "email address", "data_key": ["PersInfo"]},
            {"Checker": "linkedIn account", "data_key": ["PersInfo"]},
            {"Checker": "phone number", "data_key": ["PersInfo"]},
            {"Checker": "github", "data_key": ["PersInfo"]},
        ]

    prompt_dict = {
        "residence Location": "Make sure that the following text has no address or any location mentioned. Answer by true or false only. The text",
        "email address": "Check if the following text includes an email address.  Answer with true or false only. The text: ",
        "linkedIn account": "Given the following text, check if it includes LinkedIn address. Answer with true or false only. The text: ",
        "phone number": "Given the following text, check if it includes a phone number. Answer with true or false only. The text: ",
        "github": "Given the following text, check if it includes github address. Answer with true or false only. The text: ",

    }

    def get_labels(self):
        return self.labels

    def get_spelling(self):
        return self.spelling

        ## TODO : Add more checks here

    def check_function(self, prompt, data):
        return self.model.generate_content(prompt + data)

    def apply_checks(self):
        results = {}
        for check in self.checks:
            data_keys = check["data_key"]
            checker = check["Checker"]
            data = ""
            for data_key in data_keys:
                data += self.json["Labels"][data_key] + " "
            result = self.check_function(self.prompt_dict[checker], data)
            if result.text.lower() != 'true' and result.text.lower() != 'false':
                raise ValueError("Invalid response")
            results[checker] = result.text
        return results


def readJsonFIle(path):
    with open(path) as f:
        data = json.load(f)
    return data
