#ResumeBuilder
#Evangellos Wiegers
#April 17, 2020

from Support import Skill, SkillSection, Award, Education, Experience, Reference, Other, AwardSection
from pathlib import Path
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import HRFlowable
from reportlab.lib.colors import gray, lightgrey, black
import shutil

def build(posting, name, address, phone, email, github_account, keywords, education_list, number_educations,
          skill_section, number_skills, experience_list, number_exp, references, number_ref, award_section,
          number_award, volunteering, number_vol, hobbies, number_hobbies):
    '''
    Function to build a resume and produce its pdf
    :param posting: string name of the posting
    :param name: string of persons full name
    :param address: string of persons address
    :param phone: string of persons phone
    :param email: string of persons email
    :param github_account: string of persons github
    :param keywords: string list of scraped keywords
    :param education_list: Education list of persons educational experience
    :param number_educations: number of Education experiences you want on the resume
    :param skill_section: SkillSection or Skill list object containing the a persons skills as Skill objects
    :param number_skills: number of skills you want on resume - is a list of size 4 if using SkillSection object
                            in skill_section or just an integer if using a list in skill_section
    :param experience_list: Experience list of persons non-educational experiences
    :param number_exp: number of non-educational experiences you want on the list
    :param references: References list of a persons references
    :param number_ref: number of references you want on your resume
    :param award_section: Award list of a persons awards
    :param number_award: number of awards you want on the resume
    :param volunteering: Volunteering list of a persons volunteering experience
    :param number_vol: number of volunteering experiences you want on the list
    :param hobbies: Other list of a persons hobbies
    :param number_hobbies: number of hobbies you want on the resume
    :post-condition: produces a PDF of the tailored resume in the same folder is Main.py
    :return: N/A
    '''


    ###################################################################################################################
    # first organizing skills
    # organize skills
    all_skills = None
    if keywords != None:
        if isinstance(skill_section, SkillSection):
            assert isinstance(number_skills, list) and len(number_skills) == 4, \
                'number_skills needs to be a list for skill_section of type SkillSection!'

            all_skills = SkillSection()
            # language skills
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

            # technical skills
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

            # interpersonal skills
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

            # other skills
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

    # organize education
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

    # organize experiences
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

    # organize referenves
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

    # organize awards
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

    # organize volunteering
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

    # organize hobbies
    all_hobbies = None
    count = 0
    if isinstance(hobbies, list):
        all_hobbies = []
        hobbies.sort(reverse=True, key=Other.get_year()[::-1])
        for hobby in hobbies:
            if count < number_hobbies:
                all_hobbies.append(hobby)
                count += 1
    elif isinstance(hobbies, str):
        all_hobbies = hobbies


    ###################################################################################################################
    # Now for actually build the PDF resume

    # creating filename
    file_name = posting + ".pdf"
    count = 0
    my_file = Path("../" + file_name)
    check = False
    # getting a new file name in case of repeats
    while check:
        if my_file.is_file():
            count += 1
            file_name = posting + "(" + str(count) + ").pdf"
            my_file = Path("./" + file_name)
        else:
            check = True

    #c reating PDF document
    doc = SimpleDocTemplate(file_name, pagesize=LETTER)
    elements = []

    #creating styles
    name_style = ParagraphStyle(name='Normal', fontname='Times-Bold', fontSize=22, alignment=1)
    info_style = ParagraphStyle(name='Normal', fontname='Times-Roman', fontSize=14, alignment=1)
    info_style2 = ParagraphStyle(name='Normal', fontname='Times-Roman', fontSize=14)
    section_style = ParagraphStyle(name='Normal', fontname='Times-Bold', fontSize=18, spaceBefore=6)
    title_style = ParagraphStyle(name='Normal', fontname='Times-Bold', fontSize=14)
    normal_style = ParagraphStyle(name='Normal', fontname='Times-Roman', fontSize=12)
    horizontal_line = HRFlowable(width="100%", thickness=2, lineCap='round', color=black, spaceBefore=3,
                               spaceAfter=6, hAlign='CENTER', vAlign='BOTTOM', dash=None)

    # add the contact info section to PDF
    elements.append(Paragraph(name, name_style))
    elements.append(Paragraph(address, info_style))
    elements.append(Paragraph(phone + " | " + email, info_style + " | " + github_account, info_style))
    elements.append(horizontal_line)

    # add education section to PDF
    if all_education != None:
        elements.append(Paragraph("EDUCATION", section_style))
        elements.append(horizontal_line)
        if isinstance(all_education, list):
            for educ in all_education:
                elements.append(Paragraph(educ.get_name() + " | " + educ.get_institution, title_style))
                descript = "      " + educ.get_degree_title + " | " + educ.get_grade + " | "+ educ.get_length()
                if not educ.get_is_finished():
                    descript += " (Expected)"
                elements.append(Paragraph(descript, info_style2))
        elif isinstance(all_education, str):
            elements.append(Paragraph(all_education, info_style2))

    # add skill section to PDF
    if all_skills != None:
        elements.append(Paragraph("RELEVENT SKILLS", section_style))
        elements.append(horizontal_line)
        if isinstance(all_skills, SkillSection):
            if all_skills.get_language() != None:
                elements.append(Paragraph("Languages and Proficiencies", title_style))
                for skill in all_skills.get_language():
                    elements.append(Paragraph("<bullet>" + skill.get_description() + "</bullet>", normal_style))
            if all_skills.get_technical() != None:
                elements.append(Paragraph("Technical and Design", title_style))
                for skill in all_skills.get_technical():
                    elements.append(Paragraph("<bullet>" + skill.get_description() + "</bullet>", normal_style))
            if all_skills.get_interpersonal() != None:
                elements.append(Paragraph("Interpersonal", title_style))
                for skill in all_skills.get_interpersonal():
                    elements.append(Paragraph("<bullet>" + skill.get_description() + "</bullet>", normal_style))
            if all_skills.get_other() != None:
                elements.append(Paragraph("Other", title_style))
                for skill in all_skills.get_other():
                    elements.append(Paragraph("<bullet>" + skill.get_description() + "</bullet>", normal_style))
        elif isinstance(all_skills, list):
            for skill in all_skills:
                elements.append(Paragraph("<bullet>" + skill.get_description() + "</bullet>", normal_style))
        elif isinstance(all_skills, str):
            elements.append(Paragraph(all_skills, normal_style))

    # new page
    elements.append(PageBreak())

    # add experience section
    if all_experiences != None:
        elements.append(Paragraph("RECENT EXPERIENCE", section_style))
        elements.append(horizontal_line)
        if isinstance(all_experiences, list):
            for exp in all_experiences:
                elements.append(Paragraph(exp.get_name() +
                                          "                            " + exp.get_length(), title_style))
                elements.append(Paragraph(exp.get_institution() + ", " + exp.get_location(), normal_style))
                elements.append(Paragraph("<bullet>" + exp.get_description() + "</bullet>", normal_style))
        elif isinstance(all_experiences, str):
            elements.append(Paragraph(all_experiences, normal_style))

    # add awards section
    if all_awards != None:
        elements.append(Paragraph("ACADEMIC HONOURS", section_style))
        elements.append(horizontal_line)
        if isinstance(all_awards, list):
            for award in all_awards:
                elements.append(Paragraph( "<bullet>" + award.get_name() + ", "
                                           + award.get_year() + "</bullet>", normal_style))
        elif isinstance(all_awards, str):
            elements.append(Paragraph(all_awards, normal_style))

    # add volunteering section
    if all_volunteering != None:
        elements.append(Paragraph("VOLUNTEERING", section_style))
        elements.append(horizontal_line)
        if isinstance(all_volunteering, list):
            for vol in all_volunteering:
                elements.append(Paragraph("<bullet>" + vol.get_name() + ", " + vol.get_year() + "</bullet>", normal_style))
        elif isinstance(all_volunteering, str):
            elements.append(Paragraph(all_volunteering, normal_style))

    # add hobby section
    if all_hobbies != None:
        elements.append(Paragraph("HOBBIES", section_style))
        elements.append(horizontal_line)
        if isinstance(all_hobbies, list):
            elements.append(Paragraph("<bullet>" + ', '.join(all_hobbies) + "</bullet>", normal_style))
        elif isinstance(all_hobbies, str):
            elements.append(Paragraph(all_hobbies, normal_style))

    # add reference section
    if all_references != None:
        elements.append(Paragraph("REFERENCES", section_style))
        elements.append(horizontal_line)
        if isinstance(all_references, list):
            for ref in all_references:
                elements.append(Paragraph(ref.get_name(), title_style))
                elements.append(Paragraph(ref.get_title() + ", " + ref.get_location(), normal_style))
                elements.append(Paragraph(ref.get_phone() + " or " + ref.get_email(), normal_style))
        elif isinstance(all_references, str):
            elements.append(Paragraph(all_references, normal_style))

    # building PDF and moving it to appropriate directory
    doc.build(elements)
    shutil.move(file_name, "..")

    return
