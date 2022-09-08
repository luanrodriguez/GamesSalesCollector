from dotenv import load_dotenv
from src.send_to_s3 import send_to_s3
from src.collect_games import collect_games
from src.turn_into_file import turn_into_file

load_dotenv()

try:
    games_informations = collect_games('steam')
    filename = turn_into_file(games_informations)
    send_to_s3(filename)
    print('Success!')

except Exception as err:
    print(f'Error: {err}')