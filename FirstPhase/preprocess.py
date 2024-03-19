""""
The aim of this class is to find the mistake in the spelling and
clean the text of the resume.

After that we will send the clean raw text file to the model
In order to label ( Information Extraction )
"""

import os
from spellchecker import SpellChecker
import re


class Preprocess:
    def __init__(self, path):
        if not os.path.exists(path):
            raise ValueError("File not found")
        self.path = path
        with open(self.path, "r") as file:
            self.text = file.read()
        self.misspelled = None
        self.cleanText = None

    def findMisSpelled(self):# TODO : Add more checks
        spell = SpellChecker()

        # Regular expressions for filtering emails and numbers
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        number_regex = r'\b\d+\b'
        # self.text = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@\[\]^_`{|}~]', ' ', self.text)

        words = self.text.split()
        filtered_words = [word for word in words if
                          not re.match(email_regex, word) and not re.match(number_regex, word)]

        spell.word_frequency.load_words(['gmail', 'hotmail', 'outlook'])  # Example: Adding some domain names
        self.misspelled = spell.unknown(filtered_words)
        return self.misspelled

    def cleanResume(self) -> None:
        patterns = [
            (r'https?://\S+', ' '),  # URLs
            (r'RT|cc', ' '),  # RT and cc
            (r'#\S+', ''),  # hashtags
            (r'@\S+', '  '),  # mentions
            (r'[!"#$%&\'()*+,-./:;<=>?@\[\]^_`{|}~]', ' '),  # punctuations
            (r'[^0-9A-Za-z\s]', ' '),  # non-ascii characters
            (r'\s+', ' ')  # extra whitespace
        ]
        self.cleanText = self.text
        for pattern, repl in patterns:
            self.cleanText = re.sub(pattern, repl, self.cleanText)
        self.cleanText = self.cleanText.strip()

    def preprocess(self) -> tuple[str, list[str]]:
        self.findMisSpelled()
        self.cleanResume()
        return self.cleanText, list(self.misspelled)
