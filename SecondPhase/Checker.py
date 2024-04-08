PROMPT_DICT_PATH = r'C:\Users\user\Desktop\Resume_Analyzer\Resume_Analyzer\SecondPhase\Prompts\prompts.json'
CHECKES_PATH = r'C:\Users\user\Desktop\Resume_Analyzer\Resume_Analyzer\SecondPhase\Prompts\checker_info.json'

import json
import time
import google.generativeai as genai
import os

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
        self.prompt_dict = readJsonFIle(PROMPT_DICT_PATH)
        self.checks = readJsonFIle(CHECKES_PATH)
        genai.configure(api_key=key)
        # self.json = readJsonFIle(pathOrJson)
        if type(pathOrJson) == str:
            if not os.path.exists(pathOrJson):
                raise ValueError("File not found")
            self.labels = readJsonFIle(pathOrJson)
        else:
            self.labels = pathOrJson
        self.model = genai.GenerativeModel('gemini-pro')
        print('self.checks', self.checks)
        print('selfprompt_dict', self.prompt_dict)


    def check(self, checker_name, data):
        prompt = self.prompt_dict[checker_name]
        if prompt:
            print(prompt)
            print(data)
            return self.model.generate_content(prompt + data)


    # def get_labels(self):
    #     return self.labels

    # def get_spelling(self):
    #     return self.spelling

    def extract_data(self, data_key):
        if self.labels.get(data_key):
            data = ""
            if isinstance(self.labels[data_key], str):
                data += self.labels[data_key] + " "
            else:
                for i in self.labels[data_key]:
                    if isinstance(i, dict):
                        for key, value in i.items():
                            data += f"{key}: {value} "
                    else:
                        data += " ".join(map(str, i)) + " "
            return data
        else:
            print(f'{data_key} do not exist! ')
            return None

    def apply_checks(self):
        start_time = time.time()
        results = {}
        for check in self.checks:
            data_key = check["data_key"]
            checker = check["Checker"]
            data = self.extract_data(data_key)
            if data:
                result = self.check(checker, data)
                print('result: ', result)
                print('text: ', result.text)
                if not result.text:
                    raise ValueError("Invalid response")
                elif result.text.lower() != "true" and result.text.lower() != "false" and result.text.lower() != "none":
                    raise ValueError("Invalid response")
                # result_text = str(result.result) if hasattr(result.result, '__str__') else None
                results[checker] = result.text
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        return results



def readJsonFIle(path):
    with open(path) as f:
        data = json.load(f)
    return data





# //answer only with True or False, Given the following number, check if the number is between 300 - 600, if it is answer True, Answer False otherwise. the number is: