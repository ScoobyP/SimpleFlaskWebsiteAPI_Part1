import json

class Database:
    def insert_info(self, name, email, password):
        with open('users.json', 'r') as rf:
            user_info = json.load(rf)
            if email in user_info:
                return 0
            else:
                user_info[email] = [name, password]
                with open('users.json', 'w') as wf:
                    json.dump(user_info, wf)
                    return 1
    def check_info( self, email, password):
        with open('users.json', 'r') as rf:
            user_info = json.load(rf)
            if email in user_info:
                if user_info[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
