from SecondPhase.Checker import Checker

file_path = '../Prompts/template.json'
GOOGLE_API_KEY = ''

checker = Checker(GOOGLE_API_KEY, file_path)
result = checker.apply_checks()
print(result)
