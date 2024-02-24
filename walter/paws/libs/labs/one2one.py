
def saint2year(saint_name):
    ''' Given a Saint, returns the year it was born

    Args:
        saint_name (str)

    Returns:
        saint_year (int)
    '''
    import random
    random.seed()
    saint_year = random.randint(999, 1900)
    return saint_year

#saint = "peter"
#y = saint2year(saint)
#print(y)


def year2city(games_year):
    ''' Given a year, returns what city held sporting games

    Args:
        games_year (int)

    Returns:
        games_city (str)
    '''
    import random
    random.seed()
    cities = [ 'Barcelona', 'Berlin', 'Chamonix', 'Helsinki', 'Lake Placid', 'Lilyhammer', 'Munich', 'Sapporo', 'Sydney', 'Tokio' ]
    games_city = random.choice(cities)
    return games_city

#my_year = 1977
#c = year2city(my_year)
#print(c)
