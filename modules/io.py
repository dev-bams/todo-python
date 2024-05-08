import json
f = open("tasks.json", "r")
users = json.load(f)
f.close()
for user in users:
    print(type(user))
