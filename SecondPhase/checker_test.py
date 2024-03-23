from Checker import Checker
from Response import Response

file_path = 'template.json'
GOOGLE_API_KEY = 'AIzaSyC7t6rx9qAaFR7uSRKbWxY4EdgA9fN71Qk'

checker = Checker(GOOGLE_API_KEY, file_path)
result = checker.apply_checks()
print(result)

# result = {'related_experience': 'True', 'wordCount': 'False', 'residence_location': 'False', 'email_address': 'True', 'linkedIn_account': 'False', 'phone_number': 'True', 'github': 'False', 'personal_info': 'False', 'not_related_experience': 'True', 'work_experience_order': 'False', 'volunteering': 'True', 'volunteering_description': 'True', 'technical_skills': 'True', 'soft_skills': 'False', 'education_background': 'True', 'education_center': 'True', 'education_grad_year': 'True', 'projects': 'False', 'projects_relevant': 'True', 'project_description': 'True'}
#
# notes = Response(result, 'notes.json')
# q = notes.generate_notes()
# print(q)





