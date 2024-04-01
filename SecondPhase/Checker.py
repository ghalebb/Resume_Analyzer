import json
import time
import google.generativeai as genai

PROMPT_DICT_PATH = r'C:\Users\Hussam Salamh\Desktop\Projects\Resume_Analyzer\SecondPhase\Prompts\prompts.json'
CHECKES_PATH = r'C:\Users\Hussam Salamh\Desktop\Projects\Resume_Analyzer\SecondPhase\Prompts\checker_info.json'


class Checker:
    """"
    checks structure is the follow
    [
    { "CheckerName": "" , "data_key": ["PersInfo",etc..], "check_function": check_residence},
    { "CheckerName": "" , "data_key": ["PersInfo",etc..], "check_function": check_residence},
    { "CheckerName": "" , "data_key": ["PersInfo",etc..], "check_function": check_residence},
    ]
    """

    def __init__(self, key, labeledData, misspelling=None):
        self.prompt_dict = readJsonFIle(PROMPT_DICT_PATH)
        self.checks = readJsonFIle(CHECKES_PATH)
        genai.configure(api_key=key)

        self.labels = labeledData

        # This could be passed inside the json file and as a list
        if misspelling is not None:
            self.spelling = misspelling

        self.model = genai.GenerativeModel('gemini-pro')

    def check(self, checker_name, data):
        prompt = self.prompt_dict[checker_name]
        return self.model.generate_content(prompt + data)

    def get_spelling(self):
        return self.spelling

    def extract_data(self, data_key):
        if data_key not in self.labels:
            return None
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

    def apply_checks(self):
        start_time = time.time()
        results = {}
        for check in self.checks:
            data_key = check["data_key"]
            checker = check["Checker"]
            data = self.extract_data(data_key)
            # todo check if the tag does not appear in json file
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
