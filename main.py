import argparse
import os.path
from FirstPhase.InformationExtractor import InformationExtractor
from FirstPhase.preprocess import Preprocess
from SecondPhase.Checker import Checker
from SecondPhase.Response import Response

SECRET_KEY = "AIzaSyB1-RLEHFheGAlC80C4WfGReFBRN6sccPc"
PATH = "../resume.json"


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Recommendation system")
    parser.add_argument('-path', required=True, type=str, help='Please provide a path to a resume file')
    parser.add_argument('-key', default=SECRET_KEY, type=str, help='Please provide a key Geminia website')
    return parser.parse_args()


def check_arguments(args: argparse.Namespace):
    if args.path is None:
        raise ValueError("Please provide a path to a resume file")
    if os.path.exists(args.path) is False:
        raise ValueError("File not found")
    pass


def firstPhase(path):
    preprocess = Preprocess(path)
    cleanText, misspelling = preprocess.preprocess()
    extractor = InformationExtractor(cleanText)
    labeledData = extractor.labelData()
    return labeledData, misspelling


def secondPhase(key, labeledData, misspelling):
    checker = Checker(key, labeledData, misspelling)
    results = checker.apply_checks()
    response = Response(results, checker.get_spelling())
    recommendations = response.generate_response()
    return recommendations


def main():
    args = parse_arguments()
    check_arguments(args)
    labeledData, misspelling = firstPhase(args.path)
    recommendations = secondPhase(args.key, labeledData, misspelling)
    print(recommendations)
    pass


if __name__ == '__main__':
    main()
