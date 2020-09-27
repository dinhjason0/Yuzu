import json

with open ('.\cogs\players..json') as f:
    data = json.load(f)

for item in data["Database"]["Player"]:
    print(item)
