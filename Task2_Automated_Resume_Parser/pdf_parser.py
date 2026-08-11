import pdfplumber           
import re       


def parse_resume(pdf_path):
    
    with pdfplumber.open(pdf_path) as resume_file:
        all_text = ""                     
        for page in resume_file.pages:          
            text = page.extract_text()
            all_text += text
   
        emails = re.findall("\w+@\w+\.\w+", all_text)               
    
        phones = re.findall(r"(?:\+91[-\s]?)?[6-9]\d{4}[-\s]?\d{5}", all_text)              
    
        lines = all_text.split('\n')                   
        name = lines[0]
    
        skills_list = ['Python','C++','Java','SQL','Flask','Django','HTML','CSS','JavaScript']
        found_skills = []
        for skill in skills_list:
            if skill in all_text:
                found_skills.append(skill)
    
        education_keyword = ['Education','B.Tech','B.E.','M.Tech','MCA','BCA','Bachelor','Master']
        education = []
        for keyword in education_keyword:
            if keyword in all_text:
                education.append(keyword)
    
    resume_data = {"Name" : name,"E-mail" : emails,"Phone" : phones,"Skills" : found_skills,"Education" : education}
    return resume_data
  
