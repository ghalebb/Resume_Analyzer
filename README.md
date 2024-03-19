Resume Analyzer
Overview
The Resume Analyzer is a tool designed to empower graduates seeking high-tech jobs by enhancing their resumes through personalized recommendations. By utilizing advanced machine learning algorithms, the tool analyzes resumes for content relevance, formatting, and adherence to industry standards. The goal is to increase graduates' competitiveness in the job market and streamline the recruitment process for employers.

**Classes Description - FirstPhase
  *Preprocess
  
The Preprocess class is responsible for the initial cleaning and preparation of the resume text. It detects misspelled words and removes unwanted characters and formats. This step ensures that the resume is in a suitable state for further analysis. In clean stage, we remove URLs, mentions, hashtags, and punctuations to clean the resume text.


  *InformationExtractor
  
The InformationExtractor class takes the cleaned resume text and uses a machine learning model to label different sections of the resume, such as education, experience, skills, and projects.

**Classes Description - SecondPhase
  *Checker
The Checker class receives the labeled resume data and checks it against predefined criteria to identify any issues. Each check corresponds to a specific resume guideline, such as unnecessary personal information, and formatting.
  
  *Response
The Response class compiles the results from the Checker class into a user-friendly format, detailing the analysis findings and providing specific recommendations for improving the resume.
