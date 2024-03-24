from FirstPhase.preprocess import Preprocess
from SecondPhase.Checker import Checker
from SecondPhase.Response import Response

RESUME_RAW_TEXT_PATH = "RESUME_TEST.txt"
LABEL_DATA_PATH = r"./Test/labelDataTmp.json"
SECRET_KEY = "AIzaSyB1-RLEHFheGAlC80C4WfGReFBRN6sccPc"


def checkPreprocess():
    p = Preprocess(RESUME_RAW_TEXT_PATH)
    cleanText, misspelling = p.preprocess()
    return cleanText, misspelling


def checkInformationExtractor():
    pass


def CheckSecondPhase():
    checker = Checker(SECRET_KEY, LABEL_DATA_PATH)
    results = checker.apply_checks()
    print("This the result after calling the checker class")
    print(results)
    print('---------------------------')
    res = Response(results,"./SecondPhase/notes.json")
    recommendations = res.generate_notes()
    print(recommendations)

if __name__ == '__main__':
    # print(checkPreprocess())
    CheckSecondPhase()
