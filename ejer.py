class developer:
    
    def __init__(self):
        self.__seniority = 'junior'
        self.skills = ''
        
    def display(self):
        print ('welcome to turing with {seniority} developer with skill {skills}'.format(seniority=self.__seniority, skills=self.skills))
        
class nodejs(developer):
    
    def __init__(self):
        super().__init__()
        self.__seniority= 'senior'