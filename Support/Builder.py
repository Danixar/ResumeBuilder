#ResumeBuilder
#Evangellos Wiegers
#April 17, 2020

from Support import Skill, SkillSection, Award, Education, Experience, Reference, Other, AwardSection

def build(name, address, phone, email, keywords, education_list, number_educations, skill_section,
          number_skills, experience_list, number_exp, references, number_ref, award_section,
          number_award, volunteering, number_vol, hobbies, number_hobbies):

    ###################################################################################################################
    #first organizing skills
    #organize skills
    all_skills = None
    if keywords != None:
        if isinstance(skill_section, SkillSection):
            assert isinstance(number_skills, list) and len(number_skills) == 4, \
                'number_skills needs to be a list for skill_section of type SkillSection!'

            all_skills = SkillSection()
            #language skills
            count = 0
            skill_section["Languages and Proficiencies"].sort(reverse=True, key= Skill.get_precedence())
            for skill in skill_section.get_language():
                if count >= number_skills[0]:
                    break
                elif len([i for i in skill.get_keywords() if i in keywords]) > 0:
                    all_skills.add_language(skill)
                    count += 1
            if count < number_skills[0]:
                for skill in skill_section.get_language():
                    if count >= number_skills[0]:
                        break
                    elif skill not in all_skills:
                        all_skills.add_language(skill)
                        count += 1

            #technical skills
            count = 0
            skill_section["Technical and Design"].sort(reverse=True, key= Skill.get_precedence())
            for skill in skill_section.get_technical():
                if count >= number_skills[1]:
                    break
                elif len([i for i in skill.get_keywords() if i in keywords]) > 0:
                    all_skills.add_technical(skill)
                    count += 1
            if count < number_skills[1]:
                for skill in skill_section.get_technical():
                    if count >= number_skills[1]:
                        break
                    elif skill not in all_skills:
                        all_skills.add_technical(skill)
                        count += 1

            #interpersonal skills
            count = 0
            skill_section["Interpersonal"].sort(reverse=True, key= Skill.get_precedence())
            for skill in skill_section.get_interpersonal():
                if count >= number_skills[2]:
                    break
                elif len([i for i in skill.get_keywords() if i in keywords]) > 0:
                    all_skills.add_interpersonal(skill)
                    count += 1
            if count < number_skills[2]:
                for skill in skill_section.get_interpersonal():
                    if count >= number_skills[2]:
                        break
                    elif skill not in all_skills:
                        all_skills.add_interpersonal(skill)
                        count += 1

            #other skills
            count = 0
            skill_section["Other"].sort(reverse=True, key= Skill.get_precedence())
            for skill in skill_section.get_other():
                if count >= number_skills[3]:
                    break
                elif len([i for i in skill.get_keywords() if i in keywords]) > 0:
                    all_skills.add_other(skill)
                    count += 1
            if count < number_skills[3]:
                for skill in skill_section.get_other():
                    if count >= number_skills[3]:
                        break
                    elif skill not in all_skills:
                        all_skills.add_other(skill)
                        count += 1

        elif isinstance(skill_section, list):
            assert isinstance(number_skills, int), 'number_skills must be int for skill_section type list'
            skill_section.sort(reverse=True, key= Skill.get_precedence())
            all_skills = []
            count = 0
            for skill in skill_section:
                if count >= number_skills:
                    break
                elif len([i for i in skill.get_keywords() if i in keywords]) > 0:
                    all_skills.append(skill)
                    count += 1
            if count < number_skills:
                for skill in skill_section:
                    if count >= number_skills:
                        break
                    elif skill not in all_skills:
                        all_skills.append(skill)
                        count += 1

    #organize education
    all_education = None
    count = 0
    if isinstance(education_list, list):
        all_education = []
        education_list.sort(reverse=True, key=Education.get_precedence())
        for educ in education_list:
            if count < number_educations:
                all_education.append(educ)
                count += 1
    elif isinstance(education_list, str):
        all_education = education_list

    #organize experiences
    all_experiences = None
    count = 0
    if isinstance(experience_list, list):
        all_experiences = []
        experience_list.sort(reverse=True, key=Experience.get_precedence())
        for exp in experience_list:
            if count < number_exp:
                all_experiences.append(exp)
                count += 1
    elif isinstance(experience_list, str):
        all_experiences = experience_list

    #organize referenves
    all_references = None
    count = 0
    if isinstance(references, list):
        all_references = []
        references.sort(reverse=True, key=Reference.get_precedence())
        for ref in references:
            if count < number_ref:
                all_references.append(ref)
                count += 1
    elif isinstance(references, str):
        all_references = references

    #organize awards
    all_awards = None
    count = 0
    if isinstance(award_section, list):
        all_awards = []
        award_section.sort(reverse=True, key=Award.get_year())
        for award in award_section:
            if count < number_award:
                all_awards.append(award)
                count += 1
    elif isinstance(award_section, str):
        all_awards = award_section

    #organize volunteering
    all_volunteering = None
    count = 0
    if isinstance(volunteering, list):
        all_volunteering = []
        volunteering.sort(reverse=True, key=Other.get_year())
        for vol in volunteering:
            if count < number_vol:
                all_volunteering.append(vol)
                count += 1
    elif isinstance(volunteering, str):
        all_volunteering = volunteering

    #organize hobbies
    all_hobbies = None
    count = 0
    if isinstance(hobbies, list):
        all_hobbies = []
        hobbies.sort(reverse=True, key=Other.get_year())
        for hobby in hobbies:
            if count < number_hobbies:
                all_hobbies.append(hobby)
                count += 1
    elif isinstance(hobbies, str):
        all_hobbies = hobbies

    ###################################################################################################################
    #Now for actually build the PDF resume



    return
