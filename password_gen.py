import collections
import json
import random
import re
import string


class PasswordGenerator:

    def __init__(self, config: str):
        pass

    def new(self) -> str:
        password = []
        with open('config.json') as p:
            data = json.load(p)
            g1 = data['allowed_characters']['groups'].values()
            for g in g1:
                for i in range(random.randint(2,8)):
                    password.append(random.choice(g))

            doubleDigits = str(random.randint(0,9)) + str(random.randint(0,9))
            password.append(doubleDigits)
            password.append(random.choice(string.ascii_uppercase))
            
            random.shuffle(password)

            password = ''.join(password)
            regex = r'(.)\1+' 
            password = re.sub(regex, r'\1', password)

        counts = collections.Counter(password)
        for k, v in counts.items():
            if v >= 3:
                password = password.replace(k, '')

        for bad_password in data['violations']['verboten']:
            if password in bad_password:
                 password = random.shuffle(password)
        return password
            

    def allowed(self, password: str) -> bool:
        with open('config.json') as p:
            data = json.load(p)
            for bad_password in data['violations']['verboten']:
                if bad_password in password:
                   print(password, 'False due to including the following phrase:', bad_password)
                   return False
                else:
                    pass
            counts = collections.Counter(password)
            for k, v in counts.items():
                   if v >= 3:
                        print(password, 'False due to 3 or more repeated characters: ', v)
                        return False
                   else:
                        pass
            if re.search(r'(.)\1+', password):
                print(password, 'False due to being two consecutive matches')
                return False
            else:
                pass
            if len(password) <= 3:
                print(password, 'False due to being too short')
                return False
            else:
                pass
            for char in password:
                if not char.isalnum():
                    print(password, 'False due to being invalid character')
                    return False
                else:
                    pass
        print('*****', password, '*****')
        return True

    def password_from_config_file(filepath: str) -> str:
        pass
