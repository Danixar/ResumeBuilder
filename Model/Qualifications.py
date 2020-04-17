


class Skill:

    def __init__(self, keywords, description, precedence):
        self.keywords = self.setKeywords(keywords)
        self.description = self.setDescription(description)
        self.precedence = self.setPrecedence(precedence)

    def setKeywords(self, keywords):
        for obj in keywords:
            assert isinstance(obj, str), 'object of wrong type!'
        self.keywords = [x for x in keywords if x]

    def getKeywords(self):
        return self.keywords

    def setDescription(self, description):
        assert isinstance(description, str), 'object of wrong type!'
        self.description = description

    def getDescription(self):
        return self.description

    def setPrecedence(self, precedence):
        assert isinstance(precedence, int), 'object of wrong type!'
        assert (precedence >= 1 and precedence <= 10), 'precedence out of range!'
        self.precedence = precedence

    def getPrecedence(self):
        return self.precedence



class Award:

    def __init__(self, name, year):
        self.name = self.setName(name)
        self.year = self.setYear(year)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setYear(self, year):
        self.year = year

    def getYear(self):
        return self.year



class Qualification:

    def __init__(self, name, start, end, institution, location, precedence):
        self.name = self.setName(name)
        self.start = self.setStart(start)
        self.end = self.setEnd(end)
        self.institution = self.setInstitution(institution)
        self.location = self.setLocation(location)
        self.precedence = self.setPrecedenc(precedence)

    def setName(self, name):
        assert isinstance(name, str), 'object of wrong type!'
        self.name = name

    def getName(self):
        return self.name

    def setStart(self, start):
        assert isinstance(start, int), 'object of wrong type!'
        self.start = start

    def getStart(self):
        return self.start

    def setEnd(self, end):
        assert isinstance(end, int), 'object of wrong type!'
        self.end = end

    def getEnd(self):
        return self.end

    def getLength(self):
        return self.end - self.start

    def setInstitution(self, institution):
        assert isinstance(institution, str), 'object of wrong type!'
        self.institution = institution

    def getInstitution(self):
        return self.institution

    def setLocation(self, location):
        assert isinstance(location, str), 'object of wrong type!'
        self.location = location

    def getLocation(self):
        return self.location

    def setPrecedence(self, precedence):
        assert isinstance(precedence, int), 'object of wrong type!'
        assert (precedence >= 1 and precedence <= 10), 'precedence out of range!'
        self.precedence = precedence

    def getPrecedence(self):
        return self.precedence


class Education(Qualification):

    def __init__(self, name, start, end, institution, location, precedence, isFinished, grade, degreeTitle):
        super(Education, self).__init__(name, start, end, institution, location, precedence)
        self.isFinished = self.setIsFinished(isFinished)
        self.grade = self.setGrade(grade)
        self.degreeTitle = self.setdegreeTitle(degreeTitle)

    def setIsFinished(self, isFinished):
        assert isinstance(isFinished, bool), 'object of wrong type!'
        self.isFinished = isFinished

    def getIsFinished(self):
        return self.isFinished

    def setGrade(self, grade):
        assert isinstance(grade, int or float), 'object of wrong type!'
        floatGrade = grade
        if isinstance(floatGrade, int):
            floatGrade = float(floatGrade)
        self.grade = floatGrade

    def getGrade(self):
        return self.grade

    def setdegreeTitle(self, degreeTitle):
        assert isinstance(degreeTitle, str), 'object of wrong type!'
        self.degreeTitle = degreeTitle

    def getDegreeTitle(self):
        return self.degreeTitle



class Experience(Qualification):

    def __init__(self, name, start, end, institution, location, precedence, description):
        super(Experience, self).__init__(name, start, end, institution, location, precedence)
        self.description = self.setDescription(description)

    def setDescription(self, description):
        assert isinstance(description, str), 'object of wrong type!'
        self.description = description

    def getDescription(self):
        return self.description



class Reference(Qualification):

    def __init__(self, name, start, end, institution, location, precedence, email, phone):
        super(Reference, self).__init__(name, start, end, institution, location, precedence)
        self.email = self.setEmail(email)
        self.phone = self.setPhone(phone)

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setPhone(self, phone):
        self.phone = phone

    def getPhone(self):
        return self.phone










