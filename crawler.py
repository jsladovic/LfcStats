from datetime import datetime
from match import Match

class Crawler:
    def __init__(self):
        self.url = 'http://www.lfchistory.net/SeasonArchive/Games/'
        self.matches_xpath = '//*[@id="DataTables_Table_0"]/tbody'
        self.season_xpath = '//*[@id="content"]/div/h3'
        
    def parse(self, browser, season):
        browser.get_page(self.url + str(season))

        nodes = browser.find_by_xpath(self.season_xpath)[0]
        season = nodes.text.split(' ')[3]

        nodes = browser.find_by_xpath(self.matches_xpath)[0].find_elements_by_tag_name('tr')
        matches = []
        for node in nodes:
            matches.append(self.parse_match(node))
            print(matches[-1].to_string())
            
        return season, matches

    def parse_match(self, node):
        nodes = node.find_elements_by_tag_name('td')
        if len(nodes) != 6:
            raise 'incorrect number of match nodes: ' + len(nodes)

        match_number = nodes[0].text
        date = datetime.strptime(nodes[1].text, '%d.%m.%Y')
        result = nodes[2].text.split('-')
        url = nodes[2].find_elements_by_tag_name('a')[0].get_attribute('href')
        opponent = nodes[3].text
        stadium = nodes[4].text
        competition = nodes[5].text
        match = Match()
        match.add_match_data(match_number, date, int(result[0]), int(result[1]), url, opponent, stadium, competition)
        return match
