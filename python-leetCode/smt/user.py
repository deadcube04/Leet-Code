import re

class User:
    def __init__(self, name : str, email : str, password : str):
        
        self.name = name
        self.email = email
        self.password = password
    
    @classmethod
    def create(cls, name, email, password):

        if not User.validateName(name) or not User.validatePassword(password) or not User.validateEmail(email): 
            return None
        else:
            return cls(name, email, password)
        


    @staticmethod
    def validateName(name) -> bool:
        if (name.strip() and
            len(name) > 1):
            return True
        return False
    


    @staticmethod
    def validateEmail(email) -> bool:
        return True if email.strip() or (bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))) else False #valida se é um email

    
    @staticmethod
    def validatePassword(password : str) -> bool:
        if (len(password) >= 8 and                          # 8 ou mais carcteres
            re.search(r'[A-Z]', password) and       #uma letra maiuscula
            re.search(r'[a-z]', password) and       #uma minuscula
            re.search(r'\d', password) and          # um numero
            re.search(r'[@#$%&?-_*]', password)):    # um desses simbolos especiais
                return True
        return False
