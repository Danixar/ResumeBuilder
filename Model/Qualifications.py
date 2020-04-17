#ResumeBuilder
#Evangellos Wiegers
#April 17, 2020


class Skill:
    '''

    '''
    def __init__(self, keywords, description, precedence):
        self.keywords = keywords
        self.description = description
        self.precedence = precedence

    def set_keywords(self, keywords):
        for obj in keywords:
            assert isinstance(obj, str), 'object of wrong type!'
        self.keywords = [x for x in keywords if x]

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

    def __init__(self):
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

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year


class Qualification:

    def __init__(self, name, start, end, institution, location, precedence):
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
        return self.end - self.start

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

    def __init__(self, name, start, end, institution, location, precedence, is_finished, grade, degree_title):
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

    def __init__(self, name, start, end, institution, location, precedence, description):
        super(Experience, self).__init__(name, start, end, institution, location, precedence)
        self.description = description

    def set_description(self, description):
        assert isinstance(description, str), 'object of wrong type!'
        self.description = description

    def get_description(self):
        return self.description


class Reference(Qualification):

    def __init__(self, name, start, end, institution, location, precedence, email, phone):
        super(Reference, self).__init__(name, start, end, institution, location, precedence)
        self.email = email
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone


class Other:

    def __init__(self, description):
        self.description = description

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
