from spellchecker import SpellChecker
import json
import re
import os
import pandas as pd
import google.generativeai as genai
from PROMPTS import *

GITHUB_DATASET_PATH = "https://raw.githubusercontent.com/hussamsalamh/dataset/main/data2.csv"


class ResumeDatasetManager:
    def __init__(self, dataset_path=GITHUB_DATASET_PATH):
        self.dataset_path = dataset_path
        self.resumes = None
        self.load_dataset()

    def load_dataset(self):
        print("Loading dataset...")
        self.resumes = pd.read_csv(GITHUB_DATASET_PATH)


def load_gemini_model():
    genai.configure(api_key=SECRET_KEY_GEMINI)
    model = genai.GenerativeModel('gemini-pro')
    return model


def find_mis_spelled(rawText):
    spell = SpellChecker()
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    number_regex = r'\b\d+\b'
    words = rawText.split()
    filtered_words = [word for word in words if
                      not re.match(email_regex, word) and not re.match(number_regex, word)]

    spell.word_frequency.load_words(['gmail', 'hotmail', 'outlook'])  # Example: Adding some domain names
    misspelled = spell.unknown(filtered_words)
    return misspelled


def clean_text(text):
    patterns = [
        ('https?://\S+', ' '),  # URLs
        ('RT|cc', ' '),  # RT and cc
        ('#\S+', ''),  # hashtags
        ('@\S+', '  '),  # mentions
        ('[!"#$%&\'()*+,-./:;<=>?@\[\]^_`{|}~]', ' '),  # punctuations
        ('[^0-9A-Za-z\s]', ' '),  # non-ascii characters
        ('\s+', ' ')  # extra whitespace
    ]
    cleaned_text = text
    for pattern, repl in patterns:
        cleaned_text = re.sub(pattern, repl, cleaned_text)
    cleaned_text = cleaned_text.lower()
    cleaned_text = cleaned_text.strip()
    return cleaned_text


class ResumeProcessor:
    def __init__(self):
        self.model = load_gemini_model()
        self.personal_info = None
        self.skills = None
        self.work_exp = None
        self.education = None
        self.volunteer_info = None
        self.project_into = None

    def findSkills(self, text):
        self.skills = self.model.generate_content(SKILLS_PROMPT + text).text

    def findEducation(self, text):
        self.education = self.model.generate_content(EDU_PROMPT + text).text

    def findWorkExp(self, text):
        self.work_exp = self.model.generate_content(WORK_EXP_PROMPT + text).text

    def findPersonalInfo(self, text):
        self.personal_info = self.model.generate_content(PERSON_INFO_PROMPT + text).text

    def findVolunteerInfo(self, text):
        self.volunteer_info = self.model.generate_content(VOLUNTEER_PROMPT + text).text

    def findProjectsInfo(self, text):
        self.project_into = self.model.generate_content(PROJECTS_PROMPT + text).text
    @staticmethod
    def save_processed_data(processed_data, output_path):
        with open(output_path, 'w') as file:
            json.dump(processed_data, file, indent=4)


def process_and_save(model, output_directory, resume, index):
    cleaned_text = resume  # clean_text(resume)
    model.findSkills(cleaned_text)
    model.findEducation(cleaned_text)
    model.findWorkExp(cleaned_text)
    model.findPersonalInfo(cleaned_text)
    model.findVolunteerInfo(cleaned_text)
    model.findProjectInfo(cleaned_text)

    processed_data = {
        "skills": model.skills,
        "education": model.education,
        "work_exp": model.work_exp,
        "personal_info": model.personal_info,
        "volunteer_info": model.volunteer_info,
        "project_info": model.project_into
    }

    outputPath = os.path.join(output_directory, f"processed_resume_{index}.json")
    model.save_processed_data(processed_data, outputPath)
