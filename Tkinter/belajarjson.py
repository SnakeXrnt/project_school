
import json
logs = {}

with open('log_user.json','r') as f:
    logs = json.load(f)


user = 'kenzie'




with open('log_user.json' , "w") as f :
