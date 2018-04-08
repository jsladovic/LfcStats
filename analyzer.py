

class Analyzer:
    def __init__(self, seasons):
        self.seasons = []
        for season in seasons:
            self.seasons.append(Season(season))

    def print_all_competitions(self, print_per_season = False):
        competitions = set()
        for season in self.seasons:
            season_competitions = set()
            for match in season.matches:
                competitions.add(match.competition)
                season_competitions.add(match.competition)

            if print_per_season:
                print season.name
                for competition in sorted(season_competitions):
                    print '\t' + competition

        if not print_per_season:
            for competition in sorted(competitions):
                print competition
        

    def find_seasons_with_least_conceded_over_n_games(self, n, league_only = False):
        seasons = []
        for season in self.seasons:
            if league_only:
                matches = [match for match in season.matches if match.is_league()]
            else:
                matches = season.matches
                
            if len(matches) < n:
                #print 'Only played ' + str(len(matches)) + ' matches in the ' + season.name + ' season'
                continue

            min_conceded, min_conceded_start = self.find_lowest_conceded_over_n_games(matches, n)
            seasons.append([season.name, min_conceded, min_conceded_start])

        for season in seasons:
            print season[0] + ' conceded\t' + str(season[1]) + '\tstarting from match number ' + str(season[2] + 1)

    def find_lowest_conceded_over_n_games(self, matches, n):
        min_conceded = None
        min_conceded_start = None
        for i in range(0, len(matches) - n + 1):
            conceded = self.sum_of_conceded_since_match(matches, i, n)
            if min_conceded == None or min_conceded > conceded:
                min_conceded = conceded
                min_conceded_start = i

        return min_conceded, min_conceded_start

    def sum_of_conceded_since_match(self, matches, match, n):
        sum = 0
        for i in range(match, match + n):
            sum += matches[i].goals_against

        return sum

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
        seasons = self.sort(seasons, True)
        print '\nSeasons with most ' + str(n) + ' goal games:'
        for i in range(0, 10):
            print seasons[i]

    def sort(self, array, reverse_sort):
        array = sorted(array, key = lambda x: x[2])
        array = sorted(array, key = lambda x: x[1], reverse = reverse_sort)
        return array

class Season:
    def __init__(self, season):
        self.name = season[0]
        self.matches = season[1]
