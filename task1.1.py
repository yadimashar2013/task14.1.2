from datetime import datetime


class SuperDate(datetime):
    season_ = {(12, 1, 2): 'Winter', range(3, 6): 'Spring', range(6, 10): 'Summer', range(10, 12): 'Autumn'}
    time_ = {range(6, 12): 'Morning', range(12, 18): 'Day', range(18, 24): 'Evening', range(0, 6): 'Night'}

    def __init__(self, year, month, day, hour):
        self.date = datetime(year, month, day, hour)

    def get_season(self):
        for i in self.season_:
            if self.date.month in i:
                return self.season_[i]

    def get_time_of_day(self):
        for i in self.time_:
            if self.date.hour in i:
                return self.time_[i]


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())
