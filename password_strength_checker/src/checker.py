import re

def check_password_strength(password):
    digit_conditions = [
        bool(re.search(r"[a-z]", password)),
        bool(re.search(r"[A-Z]", password)),
        bool(re.search(r"[0-9]", password)),    
        bool(re.search(r"[!@#$%^&*()\-_=+{};:,.<>?/[\]]", password))]

    digit_condition_names = [
        'LOWERCASE CHARACTER',
        'UPPERCASE CHARACTER',
        'NUMVER',
        'SPECIAL DIGIT']

    base_score = sum(digit_conditions)
    
    needed_conditions = ''
    for i in range(0, 4):
        if(digit_conditions[i] == False):
            needed_conditions += ', ' + digit_condition_names[i]

    
    if(len(password) >= 16 and base_score == 4):
        return 'VERY STRONG'
    
    if(len(password) >= 12 and base_score == 4):
        return 'STRONG, need MORE CHARACTERS.'
    
    if(len(password) >= 8 and base_score >= 3):
        return 'MEDIUM, need MORE CHARACTERS' + needed_conditions
    
    if(len(password) >= 8 and base_score >= 2):
        return 'WEAK, need MORE CHARACTERS' + needed_conditions
    
    return 'VERY WEEK, need MORE CHARACTERS' + needed_conditions