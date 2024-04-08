RESUME_TEST = "Developer <span class=\"hl\">Developer</span> Developer - TATA CONSULTANTCY SERVICE Batavia, OH Relevant course work† Database Systems, Database Administration, Database Security & Auditing, Computer Security,Computer Networks, Programming & Software Development, IT, Information Security Concept & Admin,† IT System Acquisition & Integration, Advanced Web Development, and Ethical Hacking: Network Security & Pen Testing. Work Experience Developer TATA CONSULTANTCY SERVICE June 2016 to Present MRM (Government of ME, RI, MS) Developer†††† Working with various technologies such as Java, JSP, JSF, DB2(SQL), LDAP, BIRT report, Jazz version control, Squirrel SQL client, Hibernate, CSS, Linux, and Windows. Work as part of a team that provide support to enterprise applications. Perform miscellaneous support activities as requested by Management. Perform in-depth research and identify sources of production issues.†† SPLUNK Developer† Supporting the Splunk Operational environment for Business Solutions Unit aiming to support overall business infrastructure. Developing Splunk Queries to generate the report, monitoring, and analyzing machine generated big data for server that has been using for onsite and offshore team. Working with Splunk' premium apps such as ITSI, creating services, KPI, and glass tables. Developing app with custom dashboard with front- end ability and advanced XML to serve Business Solution unit' needs. Had in-house app presented at Splunk's .Conf Conference (2016). Help planning, prioritizing and executing development activities. Developer ( front end) intern TOMORROW PICTURES INC - Atlanta, GA April 2015 to January 2016 Assist web development team with multiple front end web technologies and involved in web technologies such as Node.js, express, json, gulp.js, jade, sass, html5, css3, bootstrap, WordPress.†Testing (manually), version control (GitHub), mock up design and ideas Education MASTER OF SCIENCE IN INFORMATION TECHNOLOGY in INFOTMATION TECHNOLOGY KENNESAW STATE UNIVERSITY - Kennesaw, GA August 2012 to May 2015 MASTER OF BUSINESS ADMINISTRATION in INTERNATIONAL BUSINESS AMERICAN INTER CONTINENTAL UNIVERSITY ATLANTA November 2003 to December 2005 BACHELOR OF ARTS in PUBLIC RELATIONS THE UNIVERSITY OF THAI CHAMBER OF COMMERCE - BANGKOK, TH June 1997 to May 2001 Skills Db2 (2 years), front end (2 years), Java (2 years), Linux (2 years), Splunk (2 years), SQL (3 years) Certifications/Licenses Splunk Certified Power User V6.3 August 2016 to Present CERT-112626 Splunk Certified Power User V6.x May 2017 to Present CERT-168138 Splunk Certified User V6.x May 2017 to Present CERT -181476 Driver's License Additional Information Skills† ∑††††SQL, PL/SQL, Knowledge of Data Modeling, Experience on Oracle database/RDBMS.† ∑††††††††Database experience on Oracle, DB2, SQL Sever, MongoDB, and MySQL.† ∑††††††††Knowledge of tools including Splunk, tableau, and wireshark.† ∑††††††††Knowledge of SCRUM/AGILE and WATERFALL methodologies.† ∑††††††††Web technology included: HTML5, CSS3, XML, JSON, JavaScript, node.js, NPM, GIT, express.js, jQuery, Angular, Bootstrap, and Restful API.† ∑††††††††Working Knowledge in JAVA, J2EE, and PHP.† Operating system Experience included: Windows, Mac OS, Linux (Ubuntu, Mint, Kali)"

PERSON_INFO_PROMPT = """From the Resume text for a job aspirant below, extract Entities strictly as instructed below
1. First, look for the Person Entity type in the text and extract the needed information defined below:
   `id` property of each entity must be alphanumeric and must be unique among the entities. You will be referring this property to define the relationship between entities.
    NEVER create new entity types that aren't mentioned below.
    Entity Types:
    Name:'string',ID:number,Email:string //Person Node
    
2. If you cannot find any information on the entities & relationships above, it is okay to return empty value. DO NOT create fictitious data
3. Do NOT create duplicate entities
4. Restrict yourself to extract only personal information. No Position, Company, Education or Skill information should be focussed.
5. NEVER Impute missing values
6. if any of the entities are missing, return an only empty value .
7. replace personal name with "NAME HERE" 

Example Output Format:
["label":"string","ID":"number","Email":"string"]

The resume is below:

"""

EDU_PROMPT = """

The instruction is to extract education-related entities from a resume, focusing specifically on degrees, universities, graduation dates, and scores. Each entity must have a unique alphanumeric id. The directive emphasizes avoiding fictitious data, duplicates, non-education entities, and missing value imputation. If no education information is present, an empty list should be returned.

Example Output Format:
["Edu1":{"degree":"Bachelor of Science","university":"string","graduationDate":"May 2022"},
"Edu2":{"degree":"Bachelor of Science","university":"string","graduationDate":"May 2022"}
]

The resume is below:

"""

SKILLS_PROMPT = """

The instruction is to extract skill entities from a resume, focusing exclusively on skills. Entities must be listed without duplicates, imputation of missing values, or inclusion of non-skill-related details like education. If no skill entities are identified, an empty list should be returned.
Separate skills with a comma

Example Output Format:
["Skills1" , "Skills2"]

The resume is below:

"""

WORK_EXP_PROMPT = """
The instruction is to extract work experience entities from a resume text based on specified criteria, focusing only on work experience and avoiding duplicates, education, or other unrelated details. The output should list these entities in a specified format, with examples provided for clarity. If no work experience is found, an empty list should be returned.

Example Output Format:
[{"name":"KFC"},{"name":"Teacher"}]

The resume is below:

"""

VOLUNTEER_PROMPT = """
The instruction is to extract volunteer work entities from a resume, focusing solely on volunteer experiences. The entities must be listed without duplication, imputation of missing values, or inclusion of irrelevant details like education. If no volunteer entities are found, an empty list should be returned.

Example Output Format:
[{"name":"KFC"},{"name":"Teacher"}]

The resume is below:

"""

PROJECTS_PROMPT = """
The instruction is to extract projects entities from a resume, focusing solely on projects experiences. The entities must be listed without duplication, imputation of missing values, or inclusion of irrelevant details like work experiance. If no projects entities are found, an empty list should be returned.

Example Output Format:
[{"name":"Machine Learning project", "description": "This project involves the implementation of a machine learning model, specifically fine-tuning a Language Model for a natural language processing task. Employed techniques such as transfer learning and hyperparameter optimization to enhance model performance."}]

The resume is below:

"""

WORDCOUNT_PROMPT = """
The instruction is to count the number of words in the resume.

Example Output Format:
"300"

The resume is below:

"""

SECRET_KEY_GEMINI = "AIzaSyB1-RLEHFheGAlC80C4WfGReFBRN6sccPc"