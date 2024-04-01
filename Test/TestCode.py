from SecondPhase.Checker import Checker
from SecondPhase.Response import Response

RESUME_RAW_TEXT_PATH = "RESUME_TEST.txt"
LABEL_DATA_PATH = r"./Test/labelDataTmp.json"
SECRET_KEY = "AIzaSyB1-RLEHFheGAlC80C4WfGReFBRN6sccPc"


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
    res = Response(results,"./SecondPhase/Prompts/notes.json")
    recommendations = res.generate_notes()
    print(recommendations)
    return recommendations

if __name__ == '__main__':
    # print(checkPreprocess())
    recommendations = CheckSecondPhase()
    append_data(str([RESUME_RAW_TEXT_PATH, LABEL_DATA_PATH,recommendations]))
