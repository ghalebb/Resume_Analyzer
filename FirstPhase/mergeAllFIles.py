import json
import pandas as pd
import os
import re


def clean(input_string):
    pattern = r'\b(no|not|none|never|n\'t)\b'
    if re.search(pattern, input_string.lower(), re.IGNORECASE):
        return []
    return input_string


class cleaner:
    def __init__(self, folder_path, output_csv_file):
        self.output_csv_file = output_csv_file
        self.folder_path = folder_path

    def list_files(self):
        return [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]

    def jsons_to_csv(self):
        """
        Combine multiple JSON files into a single CSV file.

        Parameters:
        - json_filenames: List of paths to the JSON files.
        - output_csv_file: Path to the output CSV file.
        """
        combined_data = []
        json_files = self.list_files()
        for filename in json_files:
            try:
                with open(os.path.join(self.folder_path, filename), 'r') as file:
                    # Read the JSON content
                    json_content = json.load(file)
                    json_content['volunteer_info'] = clean(
                        json_content['volunteer_info']
                    )
                    json_content['skills'] = json_content['skills'].split(',')
                    json_content['work_exp'] = clean(json_content['work_exp'])

                    combined_data.append({
                        "Filename": filename.split('.')[0].split('_')[-1],
                        "JSON_Content": json.dumps(json_content)
                    })
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

        df = pd.DataFrame(combined_data)
        df.to_csv(self.output_csv_file, index=False)

    def main(self):
        self.jsons_to_csv()


if __name__ == '__main__':
    folder_path = r'C:\Users\user\Desktop\Resume_Analyzer\Resume_Analyzer\FirstPhase\labeled_data'
    output_csv_file = r'C:\Users\user\Desktop\Resume_Analyzer\Resume_Analyzer\phase_one_results.csv'
    cleaner = cleaner(folder_path, output_csv_file)
    cleaner.main()
