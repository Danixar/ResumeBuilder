#ResumeBuilder
#Evangellos Wiegers
#April 17, 2020

from .Support import Skill, SkillSection, Award, AwardSection, Education, \
    Experience, Reference, Other, scrape, build

########################################################################################################################
# This is the main file which contains the script for the Resume Builder
# How to use:
    # edit the below info sections to tailor the content of the resume to your person
    # After, run this file to produce a PDF resume
    # On the command line, when prompted enter the URL of the job posting of "None" for a general resume
    # This should result in a new resume PDF appearing in your downloads folder which is tailored to the job posting
# Last Edited April 17, 2020

# Edit, at your discretion, this file to alter resume info and builder.py in the Support module to alter the
# style of the resume

# The below info is the resume info of the creator of this script and serves as a template
# NOTE: contact info and references have been altered for privacy - all other fields are truthful
# See the Support package for information on the classes used and their required parameters
# Edit the below info accordingly to fit yourself
name = "Evan Wiegers"
address = "3208 Thames Crescent, Regina, SK"
phone = "(306) 540 - 7573"
email = "evan.wiegers@usask.ca"

# Adding the info for the Education section
second_degree = Education("Computer Science", 2019, 2021, "University of Saskatchewan",
                  "Saskatoon, SK", 10, False, 93, "B.Sc.")
first_degree = Education("Chemical Engineering", 2014, 2018, "University of Saskatchewan",
                  "Saskatoon, SK", 9, True, 90, "B.E.")
education_list = [second_degree, first_degree]

# Adding the info for the Skill Section
language_skills = Skill(["python", "java", "c", "bash", "unix", "microsoft"], "Python, Java, C, Bash & Unix, "
                        "Visual Basic for Applications, Microsoft Office Suite", 10)
python_skill = Skill(["python", "recursion", "recursive"],
                     "Utilized Python, recursive programming principles, and "
                     "computational logic to program a logic proof solver", 9)
java_skill = Skill(["java", "uml", "mvc", "gui"], "Designed programs for a hospital system and a space invaders game "
                    "using Java, UML diagrams, graphical user interfaces, and the "
                    "model-view-controller design pattern", 10)
c_skill = Skill(["C", "source", "shell", "makefile", "git", "bash", "linux"], "Applied C, source code modularization, "
                    "makefile, shell scripts, and git version control in Bash to create a program to produce chaos game "
                    "representations of genomic sequences", 7)
microsoft_skill = Skill(["Microsoft", "Excel", "VBA", "Office"], "Employed Microsoft Excel and VBA to determine the "
                    "optimal operations of a hydrogen production plant for hydrotreating in "
                    "the Western Canadian oil sands", 8)
written_skill = Skill(["written", "communication"], "Improved written communication by creating project "
                "reports, memoranda, and charters to easily convey results and recommendations to "
                "engineering supervisors in industry", 9)
verbal_skill = Skill(["verbal", "communication", "powerpoint"], "Developed verbal communication and "
                "received input while delivering PowerPoint presentations on the hydrotreating of oil sands bitumen", 9)
team_skill = Skill(["team", "group", "project"], "Promoted teambuilding and collaboration as project manager of "
                "both software development (Comp. Sci.) and project design teams (Chem. Eng.)", 8)

skill_section = SkillSection()
skill_section.add_language(language_skills)
skill_section.add_technical(python_skill)
skill_section.add_technical(java_skill)
skill_section.add_technical(c_skill)
skill_section.add_technical(microsoft_skill)
skill_section.add_interpersonal(written_skill)
skill_section.add_interpersonal(verbal_skill)
skill_section.add_interpersonal(team_skill)
# NOTE: can choose to use a general list for the skills, for example
    # skill_sections = [python_skill, java_skill, c_skill, microsoft_skill]

# Adding the info for the Experience section
colliers_work = Experience("Business Analyst Intern", 2019, 2019, "Colliers International", 7,
                           "Regina and Saskatoon, SK", "Organized and streamlined property data pertinent to "
                            "the company’s nationwide database")
holdings_work = Experience("Business Analyst Intern", 2017, 2017, "Kouros Holdings Ltd", 6,
                           "Regina, SK", "Created spreadsheets to report and assess current financial balances "
                            "and forecast revenues and expenditures")
experience_list = [colliers_work, holdings_work]

# Adding the info for the Awards sections
award10 = Award("Society of Chemical Industry, Canadian Section Merit Award", 2018)
award9 = Award("Dean’s Honour Roll", "2014-2018")
award8 = Award("Canadian Society for Chemical Engineering Award (Silver Medal)", 2018)
award7 = Award("APEGS Prize", "2017-2018")
award6 = Award("Engineering Class of 1960 Scholarship", "2017-2018")
award5 = Award("Douglas Durie Memorial Fund", "2017-2018")
award4 = Award("Class of 1961 Chemical Engineers (CEGUS’61)", "2017-2018")
award3 = Award("Golden Key International Honour Society", 2016)
award2 = Award("R.L Eager Book Prize in Physical Chemistry", "2015-2016")
award1 = Award("Teruo Natori Scholarship Fund", 2016)

award_section = [award10, award1, award2, award3, award4, award5, award6, award7, award8, award9]

# Adding the info for the References section
references = "Available upon request"
    # NOTE: if you wanted to add references to the resume you would, for example, do the following:
    # first_ref = Reference("Musab Hamid", 2014, 2020, "Univeristy of Houston", "Houston, TX",
                          # 10, "musab.hamid@htown.com", "(632) 4495 - 381")

# Adding info for the volunteer section - add in descending order of importance
volunteer2 = Other("Computer Science Volunteer Tutor", "2019-present")
volunteer1 = Other("Engineering Volunteer Tutor", "2016-2018")
volunteering = [volunteer2, volunteer1]

# Adding info for Hobbies
hobbies = [] # I dont use these for resumes
            # NOTE: if you want to use hobbies just add to this list hobbies
            # of type Other class found in the Support package
            # as demonstrated in the volunteering section

# Add the number of objects of a given section
# you desire - i.e. 5 skills
number_educations = 2
number_skills = [1, 4, 3, 0] # list if using SkillSection class i.e. 1 Language skill, 4 technical skills, etc
number_exp = 2
number_ref = 2
number_award = 8
number_vol = 2
number_hobbies = 0

# Here ends the information
########################################################################################################################

if __name__ == '__main___':
    #entering the URL of the job posting or none elsewise
    myURL = input("Enter the URL of the job posting: ")
    if myURL.lower().strip() == "none":
        keywords = None
    else:
        keywords = scrape(myURL)

    # see builder.py to better understand this function
    # this function organizes and builds your resume info based on the scraped keywords
    build(name, address, phone, email, keywords, education_list, number_educations, skill_section, number_skills,
          experience_list, number_exp, references, number_ref, award_section, number_award, volunteering, number_vol,
          hobbies, number_hobbies)

########################################################################################################################
