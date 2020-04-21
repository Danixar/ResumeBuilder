#ResumeBuilder
#Evangellos Wiegers
#April 17, 2020

from Support import Skill, SkillSection, Award, Education, Experience, Reference, Other, Qualification
from pathlib import Path
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import HRFlowable
from reportlab.lib.colors import gray, lightgrey, black
from datetime import datetime
from sys import platform
import shutil

def object_precedence(obj):
    '''
    Function to use precedence for the sort() key
     :param obj: object we want to get the precedence of
    :return: precedence of object
    '''
    assert isinstance(obj, Skill) or isinstance(obj, Qualification), 'Object of wrong type!'
    return obj.get_precedence()


def object_year(obj):
    '''
    Function to use year for the sort() key
    :param obj: object we want to get the year of
    :return: the object's year as a string in reverse (easier to use sort() in this case)
    '''
    assert isinstance(obj, Award) or isinstance(obj, Other), 'Object of wrong type!'
    return obj.get_year()[-4:]


def build(posting_name, company, company_address, name, address, phone, email, github_account, keywords, education_list, number_educations,
          skill_section, number_skills, experience_list, number_exp, references, number_ref, award_section,
          number_award, volunteering, number_vol, hobbies, number_hobbies, cover):
    '''
    Function to build a resume and produce its pdf
    :param posting_name: string name of the posting
    :param company: string name of company or None
    :param company_address: string address of company or none
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
    :param cover: boolean on whether you want a cover_letter or not
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
            section = skill_section.get_language()
            section.sort(key=object_precedence, reverse=True)
            for skill in section:
                if count >= number_skills[0]:
                    break
                elif len([i for i in skill.get_keywords() if i in keywords]) > 0:
                    all_skills.add_language(skill)
                    count += 1
            if count < number_skills[0]:
                for skill in section:
                    if count >= number_skills[0]:
                        break
                    elif skill not in all_skills.get_language():
                        all_skills.add_language(skill)
                        count += 1

            # technical skills
            count = 0
            section = skill_section.get_technical()
            section.sort(key=object_precedence, reverse=True)
            for skill in section:
                if count >= number_skills[1]:
                    break
                elif len([i for i in skill.get_keywords() if i in keywords]) > 0:
                    all_skills.add_technical(skill)
                    count += 1
            if count < number_skills[1]:
                for skill in section:
                    if count >= number_skills[1]:
                        break
                    elif skill not in all_skills.get_technical():
                        all_skills.add_technical(skill)
                        count += 1

            # interpersonal skills
            count = 0
            section = skill_section.get_interpersonal()
            section.sort(key=object_precedence, reverse=True)
            for skill in section:
                if count >= number_skills[2]:
                    break
                elif len([i for i in skill.get_keywords() if i in keywords]) > 0:
                    all_skills.add_interpersonal(skill)
                    count += 1
            if count < number_skills[2]:
                for skill in section:
                    if count >= number_skills[2]:
                        break
                    elif skill not in all_skills.get_interpersonal():
                        all_skills.add_interpersonal(skill)
                        count += 1

            # other skills
            count = 0
            section = skill_section.get_other()
            section.sort(key=object_precedence, reverse=True)
            for skill in section:
                if count >= number_skills[3]:
                    break
                elif len([i for i in skill.get_keywords() if i in keywords]) > 0:
                    all_skills.add_other(skill)
                    count += 1
            if count < number_skills[3]:
                for skill in section:
                    if count >= number_skills[3]:
                        break
                    elif skill not in all_skills.get_other():
                        all_skills.add_other(skill)
                        count += 1

        elif isinstance(skill_section, list):
            assert isinstance(number_skills, int), 'number_skills must be int for skill_section type list'
            skill_section.sort(reverse=True, key=object_precedence())
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
        education_list.sort(key=object_precedence, reverse=True)
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
        experience_list.sort(key=object_precedence, reverse=True)
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
        references.sort(key=object_precedence, reverse=True)
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
        award_section.sort(key=object_year, reverse=True)
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
        volunteering.sort(key=object_year, reverse=True)
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
        hobbies.sort(key=object_year, reverse=True)
        for hobby in hobbies:
            if count < number_hobbies:
                all_hobbies.append(hobby)
                count += 1
    elif isinstance(hobbies, str):
        all_hobbies = hobbies


    ###################################################################################################################
    # creating the PDF doc and formatting

    # creating filename
    file_name = posting_name + ".pdf"
    count = 0
    resume_path = "./Resumes/"
    if platform.lower() == "windows":
        resume_path = '.\\Resumes\\'
    my_file = Path(resume_path + file_name)
    check = False
    # getting a new file name in case of repeats
    while not check:
        if my_file.is_file():
            count += 1
            file_name = posting_name + "(" + str(count) + ").pdf"
            my_file = Path(resume_path + file_name)
        else:
            check = True

    #c reating PDF document
    doc = SimpleDocTemplate(file_name, pagesize=LETTER, bottomMargin=66.0,
                            topMargin=66.0, leftMargin=66.0, rightMargin=66.0, title="Evan Wiegers Resume",
                            subject="Evan Wiegers' Resume Builder Script", author="Evan Wiegers",
                            keywords=["Resume", "Builder", "Evan", "Wiegers"])
    elements = []

    # creating paragraph styles
    # top info styles
    name_style = ParagraphStyle(name='Normal', fontName='Times-Bold', fontSize=22, spaceAfter=6, alignment=1,
                                leading=24)
    info_style = ParagraphStyle(name='Normal', fontName='Times-Roman', fontSize=14, spaceAfter=6, alignment=1)


    # Cover styles
    cover_style = ParagraphStyle(name='Normal', fontName='Times-Roman', fontSize=12, leading=16)
    re_style = ParagraphStyle(name='Normal', fontName='Times-Bold', fontSize=12, leading=16)

    # resume section styles
    indent_style = ParagraphStyle(name='Normal', fontName='Times-Roman', fontSize=14, leftIndent=36)
    section_style = ParagraphStyle(name='Normal', fontName='Times-Bold', fontSize=18, spaceBefore=6, leading=24)
    title_style = ParagraphStyle(name='Normal', fontName='Times-Bold', fontSize=14, leading=18, spaceBefore=6)
    title_style2 = ParagraphStyle(name='Normal', fontName='Times-Bold', fontSize=14, leading=18, spaceBefore=6,
                                  spaceAfter=6)
    normal_style = ParagraphStyle(name='Normal', fontName='Times-Roman', fontSize=12, leading=18)
    bullet_style = ParagraphStyle(name='Normal', fontName='Times-Roman', fontSize=12, leading=18,
                                  bulletFontName="Times-Bold", bulletFontSize=14, leftIndent=35, bulletIndent=25)

    # extra styles
    whitespace_style = ParagraphStyle(name='Normal', fontName='Times-Bold', fontSize=12, spaceBefore=12)
    endnote_style = ParagraphStyle(name='Normal', fontName='Times-Italic', fontSize=10, leading=18, color=lightgrey)
    horizontal_line = HRFlowable(width="100%", thickness=2, lineCap='square', color=black, spaceBefore=3,
                               spaceAfter=18, hAlign='CENTER', vAlign='BOTTOM', dash=None)

    ###################################################################################################################
    # creating a cover
    if cover:
        elements.append(Paragraph(name, name_style))
        elements.append(Paragraph(email + " | " + phone + " | " + address, info_style))
        elements.append(horizontal_line)

        elements.append(Paragraph(datetime.now().strftime("%b %d, %Y"), cover_style))

        elements.append((Paragraph("", whitespace_style)))
        elements.append(Paragraph(company, cover_style))
        elements.append(Paragraph(company_address, cover_style))

        elements.append((Paragraph("", whitespace_style)))
        elements.append(Paragraph("Re: " + posting_name, re_style))
        elements.append((Paragraph("", whitespace_style)))

        elements.append(Paragraph("Dear Sir or Madame: ", cover_style))
        elements.append((Paragraph("", whitespace_style)))

        # elements.append(Paragraph("I am keenly interested in summer employment with {0}. Please consider this as my "
        #                           "application for any position available in systems operations.".format(company),
        #                           cover_style))
        # elements.append((Paragraph("", whitespace_style)))

        elements.append(Paragraph("I am a student at the University of Saskatchewan scheduled to graduate with a B.Sc. "
                                  "degree in Computer Science in spring, 2021. In 2018, I received a B.E. degree with "
                                  "great distinction in Chemical Engineering while finishing first in my class. In "
                                  "Computer Science my average to date is about 93%.", cover_style))
        elements.append((Paragraph("", whitespace_style)))

        elements.append(Paragraph("I think employment with {0} would provide me with an excellent opportunity to improve "
                                  "my skills through challenging assignments in a demanding, professional and positive "
                                  "work environment. I would appreciate an opportunity to contribute to the "
                                  "success of {0}. I am convinced working in {0}’s challenging, innovative and "
                                  "professional environment would greatly enhance my skills and set me on the road "
                                  "to realizing my full potential.".format(company), cover_style))
        elements.append((Paragraph("", whitespace_style)))

        elements.append(Paragraph("I believe I possess the required work ethic and communication skills that are "
                                  "necessary to contribute positively to a productive, positive and safe work "
                                  "environment. Further, I am highly motivated to accumulate full knowledge of my tasks "
                                  "to achieve the best possible performance. Over the course of my studies, I have "
                                  "worked with and communicated effectively in teams of people with diverse skillsets "
                                  "and backgrounds. I have served as project manager in my software development team "
                                  "and chemical engineering design projects. In that capacity, I have been exposed to "
                                  "many software programs while coordinating our teams’ action plans and the production "
                                  "of reports, memoranda, and presentations. At a previous internship, I systematically "
                                  "studied the company database beyond the requirements of my role to better understand "
                                  "how my work could improve business operations.", cover_style))
        elements.append((Paragraph("", whitespace_style)))

        elements.append(Paragraph("Attached is my resume. I hope to have an opportunity to discuss my application in "
                                  "greater detail with you. I may be contacted by phone at {0} or by email at "
                                  "{1}".format(phone, email), cover_style))
        elements.append((Paragraph("", whitespace_style)))

        elements.append(Paragraph("I greatly appreciate your consideration.", cover_style))
        elements.append((Paragraph("", whitespace_style)))
        #elements.append((Paragraph("", whitespace_style)))
        elements.append(Paragraph("Evan Wiegers", cover_style))

        #now on to the resume
        elements.append(PageBreak())


    ###################################################################################################################
    # Now for actually building the resume

    # add the contact info section to PDF
    elements.append(Paragraph(name, name_style))
    elements.append(Paragraph(email + " | " + github_account, info_style))
    elements.append(Paragraph(phone + " | " + address, info_style))
    elements.append(horizontal_line)

    # add education section to PDF
    if all_education != (None or []):
        elements.append(Paragraph("EDUCATION", section_style))
        elements.append(horizontal_line)
        if isinstance(all_education, list):
            for educ in all_education:
                elements.append(Paragraph(educ.get_name() + " | " + educ.get_institution(), title_style))
                descript = educ.get_degree_title() + " | " + educ.get_grade() + " | "+ educ.get_length()
                if not educ.get_is_finished():
                    descript += " (Expected)"
                elements.append(Paragraph(descript, indent_style))
        elif isinstance(all_education, str):
            elements.append(Paragraph(all_education, indent_style))

    # add skill section to PDF
    if all_skills != (None or []):
        elements.append(Paragraph("", whitespace_style))
        elements.append(Paragraph("RELEVENT SKILLS", section_style))
        elements.append(horizontal_line)
        if isinstance(all_skills, SkillSection):
            if all_skills.get_language() != (None or []):
                elements.append(Paragraph("Languages and Proficiencies", title_style2))
                for skill in all_skills.get_language():
                    elements.append(Paragraph("<bullet>&bull</bullet>" + skill.get_description(), bullet_style))
            if all_skills.get_technical() != (None or []):
                elements.append(Paragraph("Technical and Design", title_style2))
                for skill in all_skills.get_technical():
                    elements.append(Paragraph("<bullet>&bull</bullet>" + skill.get_description(), bullet_style))
            if all_skills.get_interpersonal() != (None or []):
                elements.append(Paragraph("Interpersonal", title_style2))
                for skill in all_skills.get_interpersonal():
                    elements.append(Paragraph("<bullet>&bull</bullet>" + skill.get_description(), bullet_style))
            if all_skills.get_other() != (None or []):
                elements.append(Paragraph("Other", title_style2))
                for skill in all_skills.get_other():
                    elements.append(Paragraph("<bullet>&bull</bullet>" + skill.get_description(), bullet_style))
        elif isinstance(all_skills, list):
            for skill in all_skills:
                elements.append(Paragraph("<bullet>&bull</bullet>" + skill.get_description(), bullet_style))
        elif isinstance(all_skills, str):
            elements.append(Paragraph(all_skills, normal_style))

    # new page
    elements.append(PageBreak())
    header = "Evan Wiegers (306) 540-7573 /2"

    # add experience section
    if all_experiences != (None or []):
        elements.append(Paragraph("RECENT EXPERIENCE", section_style))
        elements.append(horizontal_line)
        if isinstance(all_experiences, list):
            for exp in all_experiences:
                elements.append(Paragraph(exp.get_name() +
                                          "                            " + exp.get_length(), title_style))
                elements.append(Paragraph(exp.get_institution() + ", " + exp.get_location(), normal_style))
                elements.append(Paragraph("<bullet>&bull</bullet>" + exp.get_description(), bullet_style))
        elif isinstance(all_experiences, str):
            elements.append(Paragraph(all_experiences, normal_style))

    # add awards section
    if all_awards != (None or []):
        elements.append(Paragraph("", whitespace_style))
        elements.append(Paragraph("ACADEMIC HONOURS", section_style))
        elements.append(horizontal_line)
        if isinstance(all_awards, list):
            for award in all_awards:
                elements.append(Paragraph("<bullet>&bull</bullet>" + award.get_name() + ",  " + award.get_year(), bullet_style))
        elif isinstance(all_awards, str):
            elements.append(Paragraph(all_awards, normal_style))

    # add volunteering section
    if all_volunteering != (None or []):
        elements.append(Paragraph("", whitespace_style))
        elements.append(Paragraph("VOLUNTEERING", section_style))
        elements.append(horizontal_line)
        if isinstance(all_volunteering, list):
            for vol in all_volunteering:
                elements.append(Paragraph("<bullet>&bull</bullet>" + vol.get_description() + ",  " +
                                          vol.get_year(), bullet_style))
        elif isinstance(all_volunteering, str):
            elements.append(Paragraph(all_volunteering, normal_style))

    # add hobby section
    if all_hobbies != (None or []):
        elements.append(Paragraph("", whitespace_style))
        elements.append(Paragraph("HOBBIES", section_style))
        elements.append(horizontal_line)
        if isinstance(all_hobbies, list):
            elements.append(Paragraph("<bullet>&bull</bullet>" + ', '.join(all_hobbies), bullet_style))
        elif isinstance(all_hobbies, str):
            elements.append(Paragraph(all_hobbies, normal_style))

    # add reference section
    if all_references != (None or []):
        elements.append(Paragraph("", whitespace_style))
        elements.append(Paragraph("REFERENCES", section_style))
        elements.append(horizontal_line)
        if isinstance(all_references, list):
            for ref in all_references:
                elements.append(Paragraph(ref.get_name(), title_style))
                elements.append(Paragraph(ref.get_title() + ", " + ref.get_location(), normal_style))
                elements.append(Paragraph(ref.get_phone() + " or " + ref.get_email(), normal_style))
        elif isinstance(all_references, str):
            elements.append(Paragraph(all_references, normal_style))

    #add endnote
    elements.append(Paragraph("", whitespace_style))
    elements.append(Paragraph("This resume was created entirely with a Python script made by Evan Wiegers", endnote_style))

    # building PDF and moving it to appropriate directory
    doc.build(elements)
    shutil.move(file_name, "./Resumes")

    return
