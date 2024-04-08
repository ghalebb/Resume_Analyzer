from SecondPhase.Checker import Checker
from SecondPhase.Response import Response

RESUME_RAW_TEXT_PATH = "../SecondPhase/Prompts/template.json"
# LABEL_DATA_PATH = r"./Test/labelDataTmp.json"
LABEL_DATA_PATH = "../SecondPhase/Prompts/template.json"
SECRET_KEY = "AIzaSyC7t6rx9qAaFR7uSRKbWxY4EdgA9fN71Qk"

NOTES_PATH = '../SecondPhase/Prompts/notes.json'

def append_data(result):
    with open("output.txt", "w") as f:
        f.write(str(result))
        print('succeed')


def CheckSecondPhase():
    checker = Checker(SECRET_KEY, LABEL_DATA_PATH)
    results = checker.apply_checks()
    print("This the result after calling the checker class")
    print(results)
    print('---------------------------')
    res = Response(results,NOTES_PATH)
    recommendations = res.generate_notes()
    print(recommendations)
    return recommendations

if __name__ == '__main__':
    # print(checkPreprocess())
    recommendations = CheckSecondPhase()
    append_data(str([RESUME_RAW_TEXT_PATH, LABEL_DATA_PATH,recommendations]))
