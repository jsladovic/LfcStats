from datetime import datetime

class Match:
    def add_match_data(self, number, date, goals_for, goals_against, url, opponent, stadium, competition):
        self.match_in_season = number
        self.match_date = date
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.url = url
        self.opponent = opponent
        self.stadium = stadium
        self.competition = competition

    def to_string(self):
        return 'match ' + self.match_in_season + ' against ' + self.opponent + '(' + str(self.goals_for) + ':' + str(self.goals_against) + ')'

    def home(self):
        return self.stadium == 'Anfield'

    def won(self):
        return self.goals_for > self.goals_against

    def lost(self):
        return self.goals_for < self.goals_against

    def drew(self):
        return self.goals_for == self.goals_against

    def has_total_goals(self, n, exactly_n):
        if exactly_n:
            return (self.goals_for + self.goals_against) == n
        return (self.goals_for + self.goals_against) >= n

    def by_n(self, n, exactly_n):
        if self.drew():
            return False
        if self.won():
            if exactly_n:
                return (self.goals_for - self.goals_against) == n
            else:
                return (self.goals_for - self.goals_against) >= n
        if exactly_n:
            return (self.goals_against - self.goals_for) == n
        else:
            return (self.goals_against - self.goals_for) >= n

    def from_dictionary(self, dictionary):
        self.match_in_season = dictionary['match_in_season']
        self.match_date = datetime.strptime(dictionary['match_date'], '%Y-%m-%dT%H:%M:%S')
        self.goals_for = dictionary['goals_for']
        self.goals_against = dictionary['goals_against']
        self.url = dictionary['url']
        self.opponent = dictionary['opponent']
        self.stadium = dictionary['stadium']
        self.competition = dictionary['competition']
