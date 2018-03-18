

class Analyzer:
    def __init__(self, seasons):
        self.seasons = []
        for season in seasons:
            self.seasons.append(Season(season))

    def find_seasons_with_most_n_goal_wins(self, n, exactly_n = False):
        seasons = []
        for season in self.seasons:
            seasons.append([season.name,
            len([m for m in season.matches if m.won() and m.by_n(n, exactly_n)]), len(season.matches)])
        seasons = self.sort(seasons)
        print '\nSeasons with most ' + str(n) + ' goal wins:'
        for i in range(0, 10):
            print seasons[i]

    def find_seasons_with_most_n_goal_games(self, n, exactly_n = False):
        seasons = []
        for season in self.seasons:
            seasons.append([season.name,
            len([m for m in season.matches if m.has_total_goals(n, exactly_n)]), len(season.matches)])
        seasons = self.sort(seasons)
        print '\nSeasons with most ' + str(n) + ' goal games:'
        for i in range(0, 10):
            print seasons[i]

    def sort(self, array):
        array = sorted(array, key = lambda x: x[2])
        array = sorted(array, key = lambda x: x[1], reverse = True)
        return array

class Season:
    def __init__(self, season):
        self.name = season[0]
        self.matches = season[1]
