#ResumeBuilder
#Evangellos Wiegers
#April 17, 2020


class Skill:
    '''
    Class for a person's skills (i.e. python, java, linux, etc)
    '''
    def __init__(self, keywords, description, precedence):
        '''
        Constructor
        :param keywords: a list of strings (words) found on a resume that would relate to the given skill
        :param description: string describing the skill (i.e. utilized python to build a ResumeBuilder script)
        :param precedence: int precedence from 1-10 of how important this skill is relative to the others
        '''
        assert isinstance(keywords, list), 'keywords not a list!'
        assert isinstance(description, str), 'description of wrong type!'
        assert isinstance(precedence, int), 'precedence of wrong type!'
        assert (10 >= precedence >= 1), 'precedence out of range!'

        self.keywords = keywords
        self.description = description
        self.precedence = precedence

    def set_keywords(self, keywords):
        for obj in keywords:
            assert isinstance(obj, str), 'object of wrong type!'
        self.keywords = [x for x in keywords if x]

    def add_keyword(self, word):
        assert isinstance(word, str), 'object of wrong type!'
        self.keywords.append(word)

    def get_keywords(self):
        return self.keywords

    def set_description(self, description):
        assert isinstance(description, str), 'object of wrong type!'
        self.description = description

    def get_description(self):
        return self.description

    def set_precedence(self, precedence):
        assert isinstance(precedence, int), 'object of wrong type!'
        assert (10 >= precedence >= 1), 'precedence out of range!'
        self.precedence = precedence

    def get_precedence(self):
        return self.precedence


class SkillSection:
    '''
    Class to contain the various sections of skills
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.dict = {"Languages and Proficiencies": [], "Technical and Design": [],
                     "Interpersonal": [], "Other": []}

    def get_skills(self):
        return self.dict

    def get_language(self):
        return self.dict.get("Languages and Proficiencies")

    def add_language(self, language):
        self.dict.get("Languages and Proficiencies").append(language)

    def remove_language(self, language):
        self.dict.get("Languages and Proficiencies").remove(language)

    def get_technical(self):
        return self.dict.get("Technical and Design")

    def add_technical(self, technical_skill):
        self.dict.get("Technical and Design").append(technical_skill)

    def remove_technical(self, technical_skill):
        self.dict.get("Technical and Design").remove(technical_skill)

    def get_interpersonal(self):
        return self.dict.get("Interpersonal")

    def add_interpersonal(self, interpersonal_skill):
        self.dict.get("Interpersonal").append(interpersonal_skill)

    def remove_interpersonal(self, interpersonal_skill):
        self.dict.get("Interpersonal").remove(interpersonal_skill)

    def get_other(self):
        return self.dict.get("Other")

    def add_other(self, other_skill):
        self.dict.get("Other").append(other_skill)

    def remove_other(self, other_skill):
        self.dict.get("Other").remove(other_skill)


class Award:
    '''
    Class for awards won by the user
    '''
    def __init__(self, name, year):
        '''
        Constructor
        :param name: string name of the award
        :param year: string or int year awarded
        '''
        assert isinstance(name, str), 'name of wrong type!'
        assert isinstance(year, str or int), 'year of wrong type!'

        self.name = name
        self.year = str(year)

    def set_name(self, name):
        assert isinstance(name, str), 'name of wrong type!'
        self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        assert isinstance(year, str or int), 'year of wrong type!'
        self.year = str(year)

    def get_year(self):
        return self.year


class AwardSection:

    def __init__(self):
        self.dict = {}

    def add_section(self, name):
        assert isinstance(name, str), 'name must be a unique string!'
        assert name not in self.dict.keys(), 'section created already!'
        self.dict[name] = []

    def get_section(self):
        return self.dict.keys()

    def add_award(self, section, award):
        assert section in self.dict.keys(), 'section not created yet!'
        self.dict[section].append(award)


class Qualification:
    '''
    Parent class for several different qualifications
    '''
    def __init__(self, name, start, end, institution, location, precedence):
        '''
        Constructor
        :param name: string name of qualification
        :param start: int start year
        :param end:  int end year
        :param institution: string institution qualification is derived from
        :param location: string city/town qualification came from
        :param precedence: int precedence from 1-10 of how important this qualification is relative to the others
        '''
        assert isinstance(name, str), 'name of wrong type!'
        assert isinstance(start, int), 'start of wrong type!'
        assert isinstance(end, int), 'end of wrong type!'
        assert end >= start, 'start date needs to be previous to end date'
        assert isinstance(institution, str), 'institution of wrong type!'
        assert isinstance(precedence, int), 'precedence of wrong type!'
        assert (10 >= precedence >= 1), 'precedence out of range!'

        self.name = name
        self.start = start
        self.end = end
        self.institution = institution
        self.location = location
        self.precedence = precedence

    def set_name(self, name):
        assert isinstance(name, str), 'object of wrong type!'
        self.name = name

    def get_name(self):
        return self.name

    def set_start(self, start):
        assert isinstance(start, int), 'object of wrong type!'
        self.start = start

    def get_start(self):
        return self.start

    def set_end(self, end):
        assert isinstance(end, int), 'object of wrong type!'
        self.end = end

    def get_end(self):
        return self.end

    def get_length(self):
        assert self.end >= self.start, 'start date needs to be previous to end date'
        if self.start == self.end:
            return self.end
        else:
            return self.end + "-" + self.start

    def set_institution(self, institution):
        assert isinstance(institution, str), 'object of wrong type!'
        self.institution = institution

    def get_institution(self):
        return self.institution

    def set_location(self, location):
        assert isinstance(location, str), 'object of wrong type!'
        self.location = location

    def get_location(self):
        return self.location

    def set_precedence(self, precedence):
        assert isinstance(precedence, int), 'object of wrong type!'
        assert (10 >= precedence >= 1), 'precedence out of range!'
        self.precedence = precedence

    def get_precedence(self):
        return self.precedence


class Education(Qualification):
    '''
    Class for an educational experience
    '''
    def __init__(self, name, start, end, institution, location, precedence, is_finished, grade, degree_title):
        '''
        Constructor
        :param name: string name of qualification
        :param start: int start year
        :param end:  int end year
        :param institution: string institution qualification is derived from
        :param location: string city/town qualification came from
        :param precedence: int precedence from 1-10 of how important this qualification is relative to the others
        :param is_finished: boolean if education is completed or not
        :param grade: up-to date grade
        :param degree_title: official title (i.e. B.Sc. )
        '''
        assert isinstance(name, str), 'name of wrong type!'
        assert isinstance(start, int), 'start of wrong type!'
        assert isinstance(end, int), 'end of wrong type!'
        assert isinstance(institution, str), 'institution of wrong type!'
        assert isinstance(precedence, int), 'precedence of wrong type!'
        assert (10 >= precedence >= 1), 'precedence out of range!'
        assert isinstance(is_finished, bool), 'is_finished of wrong type!'
        assert isinstance(grade, int or float), 'grade of wrong type!'
        assert isinstance(degree_title, str), 'degree_title of wrong type!'

        super(Education, self).__init__(name, start, end, institution, location, precedence)
        self.isFinished = is_finished
        self.grade = grade
        self.degreeTitle = degree_title

    def set_is_finished(self, is_finished):
        assert isinstance(is_finished, bool), 'object of wrong type!'
        self.isFinished = is_finished

    def get_us_finished(self):
        return self.isFinished

    def set_grade(self, grade):
        assert isinstance(grade, int or float), 'object of wrong type!'
        float_grade = grade
        if isinstance(float_grade, int):
            float_grade = float(float_grade)
        self.grade = float_grade

    def get_grade(self):
        return self.grade

    def set_degree_title(self, degree_title):
        assert isinstance(degree_title, str), 'object of wrong type!'
        self.degreeTitle = degree_title

    def get_degree_title(self):
        return self.degreeTitle


class Experience(Qualification):
    '''
    Class for non-educational experience (i.e. work)
    '''
    def __init__(self, name, start, end, institution, location, precedence, description):
        '''
        Constructor
        :param name: string name of qualification
        :param start: int start year
        :param end:  int end year
        :param institution: string institution qualification is derived from
        :param location: string city/town qualification came from
        :param precedence: int precedence from 1-10 of how important this qualification is relative to the others
        :param description: brief description of what the user did in this experience
        '''
        assert isinstance(name, str), 'name of wrong type!'
        assert isinstance(start, int), 'start of wrong type!'
        assert isinstance(end, int), 'end of wrong type!'
        assert isinstance(institution, str), 'institution of wrong type!'
        assert isinstance(precedence, int), 'precedence of wrong type!'
        assert (10 >= precedence >= 1), 'precedence out of range!'
        assert isinstance(description, str), 'description of wrong type!'

        super(Experience, self).__init__(name, start, end, institution, location, precedence)
        self.description = description

    def set_description(self, description):
        assert isinstance(description, str), 'object of wrong type!'
        self.description = description

    def get_description(self):
        return self.description


class Reference(Qualification):
    '''
    Class for resume reference
    '''
    def __init__(self, name, start, end, institution, location, precedence, email, phone):
        '''
        Constructor
        :param name: string name of qualification
        :param start: int start year
        :param end:  int end year
        :param institution: string institution qualification is derived from
        :param location: string city/town qualification came from
        :param precedence: int precedence from 1-10 of how important this qualification is relative to the others
        :param email: string reference email
        :param phone: string phone number
        '''
        assert isinstance(name, str), 'name of wrong type!'
        assert isinstance(start, int), 'start of wrong type!'
        assert isinstance(end, int), 'end of wrong type!'
        assert isinstance(institution, str), 'institution of wrong type!'
        assert isinstance(precedence, int), 'precedence of wrong type!'
        assert (10 >= precedence >= 1), 'precedence out of range!'
        assert isinstance(email, str), 'email of wrong type!'
        assert isinstance(phone, str), 'phone of wrong type!'

        super(Reference, self).__init__(name, start, end, institution, location, precedence)
        self.email = email
        self.phone = phone

    def set_email(self, email):
        assert isinstance(email, str), 'email of wrong type!'
        self.email = email

    def get_email(self):
        return self.email

    def set_phone(self, phone):
        assert isinstance(phone, str), 'phone of wrong type!'
        self.phone = phone

    def get_phone(self):
        return self.phone


class Other:
    '''
    Class for any other experience (i.e. volunteering)
    '''
    def __init__(self, description, year=None):
        '''
        Constructor
        :param description: description of whatever this is
        '''
        assert isinstance(description, str), 'description of wrong type!'
        assert isinstance(year, str or int or None), 'year of wrong type!'

        self.description = description
        self.year = year

    def set_description(self, description):
        assert isinstance(description, str), 'description of wrong type!'
        self.description = description

    def get_description(self):
        return self.description

    def set_year(self, year):
        assert isinstance(year, str or int or None), 'year of wrong type!'
        self.year = year

    def get_year(self):
        return str(self.year)
