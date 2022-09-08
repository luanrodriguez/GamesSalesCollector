import requests
from bs4 import BeautifulSoup


def _collect_steam_games():
    JSON_TO_SEND = []

    GAMES_URL = 'https://store.steampowered.com/search/?filter=topsellers&specials=1'

    response = requests.get(GAMES_URL)            
    soup = BeautifulSoup(response.content, 'html.parser')
    top_sellers_rows = soup.find(id='search_resultsRows')
    anchor_tags = top_sellers_rows.find_all('a')

    for game in anchor_tags:
        game_url = game.attrs['href']
        img = game.find('div', {'class': 'col search_capsule'}).img.attrs['src']
        name = game.find('span', {'class': 'title'}).get_text()
        discount_percentage = game.find('div', {'class': 'col search_discount responsive_secondrow'}).span.getText()
        discount_div = game.find('div', {'class': 'col search_price discounted responsive_secondrow'})
        original_price = discount_div.span.get_text()
        discount_price = discount_div.get_text().replace(f'\n{original_price}','').strip()
            

        JSON_TO_SEND.append({
            "name":name,
            "img":img,
            "discount_percentage":discount_percentage,
            "original_price": original_price,
            "discount_price": discount_price,
            "game_url": game_url
        })
    return JSON_TO_SEND


games_websites_names_options = {
    'steam': _collect_steam_games
}


def collect_games(game_website_name):
    games_informations = games_websites_names_options.get(game_website_name)()
    return games_informations