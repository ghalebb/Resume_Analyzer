import pandas as pd
import time
from SecondPhase.Checker import Checker
from SecondPhase.Response import Response
import json

#TODO need to change the path for both
GITHUB_DATASET_PATH = r"C:\Users\user\Desktop\Resume_Analyzer\Resume_Analyzer\labeled_resumes.csv"
RECOMMENDATION_FILE = r"C:\Users\user\Desktop\Resume_Analyzer\Resume_Analyzer\recommendation.csv"
SECRET_KEY = "AIzaSyB1-RLEHFheGAlC80C4WfGReFBRN6sccPc"


def secondPhase(labeledData, key=SECRET_KEY, misspelling=None):
    labeledData = json.loads(labeledData)
    print('labeledData', labeledData)
    checker = Checker(key, labeledData, misspelling)
    results = checker.apply_checks()
    print('results', results)
    response = Response(results, 'SecondPhase/Prompts/notes.json')
    recommendations = response.generate_notes()
    print('recommendations', recommendations)
    return recommendations


class Main:
    def __init__(self):
        self.resumes = None
        self.load_labeled_dataset()

    def load_labeled_dataset(self):
        print("Loading dataset...")
        self.resumes = pd.read_csv(GITHUB_DATASET_PATH)

    def main(self):
        combined_data = []
        for ind in self.resumes.index:
            try:
                print(f"Processing resume {ind}")
                time.sleep(0.05)
                labeled_resume = self.resumes['JSON_Content'][ind]
                recommendations = secondPhase(labeled_resume, key=SECRET_KEY)
                print('recommendations', recommendations)
                combined_data.append(
                    {
                        "Filename": ind,
                        "recommendation": str(recommendations),
                    }
                )
            except Exception as e:
                print(f"Error processing file {ind}: {e}")
            df = pd.DataFrame(combined_data)
            df.to_csv(RECOMMENDATION_FILE, index=False)


if __name__ == '__main__':
    main = Main()
    main.main()
