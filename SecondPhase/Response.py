import json
import os

class Response:
    def __init__(self, result_json, notes_file):
        """
        Initialize the Response object with results from checks and spelling errors.

        :param result_json: JSON object containing the results of various checks
        :param notes_file: notes_file path

        result_json = {'related_experience': 'True',
                        'wordCount': 'False',
                        'residence_location': 'True',
                        'email_address': 'True',
                        'linkedIn_account': 'False',
                        'phone_number': 'True',
                        'github': 'False',
                        'personal_info': 'False',
                        'not_related_experience': 'True',
                        'work_experience_order': 'False',
                        'volunteering': 'False',
                        'volunteering_description': 'True',
                        'technical_skills': 'False',
                        'soft_skills': 'False',
                        'education_background':
                        'True', 'education_center':
                        'True', 'education_grad_year':
                        'True', 'projects': 'False',
                        'projects_relevant': 'True',
                        'project_description': 'True'}

        """
        self.result_json = result_json
        self.notes_file = notes_file

    def generate_notes(self):
        notes = readJsonFile(self.notes_file)
        generated_notes = []
        for key in self.result_json.keys():
            if self.result_json[key].lower() == notes[key]['desired_answer'].lower():
                generated_notes.append(notes[key]['if_success'] + '\n')

            # todo handle cases where the tag does not appear

            elif self.result_json[key].lower() == 'none':
                # figure this out!!
                pass
            else:
                generated_notes.append(notes[key]['if_fail'] + '\n')
        return " ".join(generated_notes)


def readJsonFile(path):
    with open(r'C:\Users\user\Desktop\Resume_Analyzer\Resume_Analyzer\SecondPhase\Prompts\notes.json') as f:
        data = json.load(f)
    return data



