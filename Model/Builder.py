#ResumeBuilder
#Evangellos Wiegers
#April 17, 2020

from .Qualifications import Skill, SkillSection, Award, Education, Experience, Reference, Other

def build(name, address, phone, email, educationList, skillSections, experience,  references=None, awards=None, volunteering=None, hobbies=None):

    return