from analyzer import Analyzer
from browser import Browser
from crawler import Crawler
from match import Match

from datetime import datetime
from scandir import walk
import json

def cache_season(season, matches, cache_path):
    cache_file_name = cache_path + season + '.json'
    matches_json = json.dumps([ob.__dict__ for ob in matches], default=serializeJson)

    with open(cache_file_name, 'w') as f:
        f.write(matches_json)
        f.close

def deserialize_matches(text):
    dictionary = json.loads(text)
    matches = []
    for element in dictionary:
        match = Match()
        match.from_dictionary(element)
        matches.append(match)
    return matches

def get_cached_data(cache_path):
    seasons = []
    for root, dirs, files in walk(cache_path):
        for filename in files:
            if not filename.endswith('.json'):
                print 'unknown file: ' + filename
                continue
            
            season = filename.split('.')[0]
            f = open(cache_path + filename, 'r')
            text = f.read()
            matches = deserialize_matches(text)
            seasons.append([season, matches])
    return seasons

def serializeJson(obj):
    if isinstance(obj, (datetime)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

current_season = 127
only_current_season = True
need_stats = False
cache_path = 'cache/seasons/'


if need_stats:
    browser = Browser()
    crawler = Crawler()
    try:
        for i in range(current_season, 1, -1):
            season, matches = crawler.parse(browser, i)
            print season + ' ' + str(len(matches)) + ' matches'
            cache_season(season, matches, cache_path)
            if only_current_season:
                break
    except Exception as ex:
        browser.close_browser()
        raise ex

    browser.close_browser()

seasons = get_cached_data(cache_path)
analyzer = Analyzer(seasons)

#analyzer.print_all_competitions()
#analyzer.find_seasons_with_most_n_goal_wins(5)
#analyzer.find_seasons_with_most_n_goal_games(5)

analyzer.find_seasons_with_least_conceded_over_n_games(10, False)
