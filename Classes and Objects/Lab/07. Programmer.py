class Programmer:

    def __init__(self, name, language, skills):

        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):

        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"
        
    
    def change_language(self, new_language, skills_needed):

        if self.skills >= skills_needed and new_language != self.language:
            temp  = self.language
            self.language = new_language

            return f"{self.name} switched from {temp} to {new_language}"


        if self.skills >= skills_needed and new_language == self.language:
            return f"{self.name} already knows {self.language}"


        if self.skills < skills_needed:
            return f"{self.name} needs {skills_needed - self.skills} more skills"
