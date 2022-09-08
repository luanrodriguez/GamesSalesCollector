import json


def turn_into_file(games_informations):
    filename = 'games.json'
    with open(filename, 'w') as f:
        f.write(json.dumps(games_informations))
        f.close()
    
    return filename
