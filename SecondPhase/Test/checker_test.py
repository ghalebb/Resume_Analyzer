from SecondPhase.Checker import Checker
from SecondPhase.Response import Response
import json

# file_path = r'C:\Users\user\Desktop\Resume_Analyzer\Resume_Analyzer\SecondPhase\Prompts\try_resume.json'
GOOGLE_API_KEY = 'AIzaSyC7t6rx9qAaFR7uSRKbWxY4EdgA9fN71Qk'

# data = {'skills': ['Document management', ' Project Management', ' Process Management', ' Filing', ' Minutes and reports preparation', ' Call handling', ' MIS reporting', ' Liaising', ' Ad-Hoc Admin tasks', ' Invoices', ' bills', ' receipts verification', ' Filing records', ' Correspondence management', ' Minutes of meeting', ' Meeting calendar', ' Distribution of documents', ' Tracking and retrieval of documents and drawings', ' Expedite the return of documents', ' Register', ' log', ' distribute', ' track', ' issue', ' maintain and control office and site project documents and drawings', ' Coordinate the activities of Document Control', ' Perform document control & Quality management activities', ' Maintain procedures for maintaining documents and manage change control of documents', ' Reporting on the performance of the document control system', ' Ensure that Project Team and contractors comply with the document management system process and procedures', ' Work closely and liaise with contractors’ document control group', ' Assist with the implementation', ' management & administration of the electronic management system', ' Maintain document logs', ' Receiving and distributing all documents', ' Receiving and distributing project documents and drawings based on the Document Distribution Matrix', ' Receiving', ' record', ' log', ' scan and distribute all project documents', ' Ensure the correct stamping all documents or drawings', ' Scan and store the approved shop drawings in the database', ' Ensuring meetings are effectively organized and minutes recorded', ' Maintaining effective records and administration', ' Communication and correspondence', ' Circulating agendas and reports'], 'education': '["Edu1":{"degree":"Bachelor of Commerce","university":"Salem","graduationDate":"2002"}]', 'work_exp': '[{"name":"ISG ME"},{"name":"Ali Ghurair CEW"},{"name":"Ali Mousa"},{"name":"CDM Smith"},{"name":"Dubai Properties"},{"name":"Parsons Overseas Limited"},{"name":"Dutco Balfour Beatty LLC"}]', 'personal_info': '[\n {"label":"person","ID":"1","Email":"ad3snu@r.postjobfree.com","Name":"Nagajothy. P"}\n]', 'volunteer_info': '[]'}
# checker = Checker(GOOGLE_API_KEY, data)
# result = checker.apply_checks()
# print('result: ', result)

result = {'residence_location': 'False', 'email_address': 'True', 'linkedIn_account': 'False', 'phone_number': 'False', 'github': 'False', 'personal_info': 'False', 'related_experience': 'True', 'not_related_experience': 'None', 'work_experience_order': 'False', 'volunteering': 'False', 'volunteering_description': 'False', 'technical_skills': 'False', 'soft_skills': 'True', 'education_background': 'False', 'education_center': 'True', 'education_grad_year': 'True'}
notes_file = r"C:\Users\user\Desktop\Resume_Analyzer\Resume_Analyzer\SecondPhase\Prompts\notes.json"
response = Response(result, 'SecondPhase/Prompts/notes.json')
recommendations = response.generate_notes()
print('recommendations', recommendations)


