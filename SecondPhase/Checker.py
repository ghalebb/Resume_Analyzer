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
        if type(pathOrJson) == str:
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
            {"Checker": "residenceLocation", "data_key": ["PersInfo"], "check_function": self.checkResidence},
        ]

    def get_labels(self):
        return self.labels

    def get_spelling(self):
        return self.spelling

    def checkResidence(self, data: str) -> GenerateContentResponse:
        PROMPT = "Check the string that between brackets if it contain a residence location, and if it contain only say yes " \
                 "otherwise say no. The string is : "
        # Simulate checking the personal info string
        return self.model.generate_content(PROMPT + data)

    ## TODO : Add more checks here

    def apply_checks(self):

        results = {}
        for check in self.checks:
            data_keys = check["data_key"]
            check_function = check["check_function"]
            checker = check["Checker"]
            data = ""
            for data_key in data_keys:
                data += self.json["Labels"][data_key] + " "
            result = check_function(data)
            if result.text != "yes" and result.text != "no":
                raise ValueError("Invalid response")
            results[checker] = result.text
        return results


"""
{ 
Checker "residenceLocation" : Yes or No , 





}


"""



def readJsonFIle(path):
    with open(path) as f:
        data = json.load(f)
    return data
