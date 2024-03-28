import concurrent.futures
import json
import os.path
import time
import google.generativeai as genai


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
        self.prompt_dict = readJsonFIle('./SecondPhase/prompts.json')
        self.checks = readJsonFIle('./SecondPhase/checker_info.json')
        genai.configure(api_key=key)

        #todo move json opening to main file, after first phase is done
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

    def check(self, checker_name, data):
        prompt = self.prompt_dict[checker_name]
        return self.model.generate_content(prompt + data)

    def get_spelling(self):
        return self.spelling

    def extract_data(self, data_key):
        if data_key not in self.json["Labels"]:
            return None
        data = ""
        if isinstance(self.json["Labels"][data_key], str):
            data += self.json["Labels"][data_key] + " "
        else:
            for i in self.json["Labels"][data_key]:
                if isinstance(i, dict):
                    for key, value in i.items():
                        data += f"{key}: {value} "
                else:
                    data += " ".join(map(str, i)) + " "
        return data

    def apply_checks(self):
        start_time = time.time()
        results = {}
        for check in self.checks:
            data_key = check["data_key"]
            checker = check["Checker"]
            data = self.extract_data(data_key)
            #todo check if the tag does not appear in json file
            if data is None:
                results[checker] = ""
            else:
                result = self.check(checker, data)
                if result.text.lower() != "true" and result.text.lower() != "false" and result.text.lower() != "none":
                    raise ValueError("Invalid response")
                results[checker] = result.text
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        return results



def readJsonFIle(path):
    with open(path) as f:
        data = json.load(f)
    return data
