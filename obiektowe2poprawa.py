import random
from termcolor import colored

class BaseItem:
    def __init__(self, title: str, publishment_year: int, genere: str, play_count: int):
        self.title = title
        self.publishment_year = publishment_year
        self.genere = genere
        self.play_count = play_count

    def __str__(self):
        return f"{self.title} ({self.publishment_year})"

    def play(self):
        self.play_count += 1
        print(f"Play count: {self.play_count}")


class Film(BaseItem):
    pass


class Series(BaseItem):
    def __init__(self, title: str, publishment_year: int, genere: str, play_count: int, no_episode: int,
                 no_season: int):
        super().__init__(title, publishment_year, genere, play_count)
        self.no_episode = no_episode
        self.no_season = no_season

    def __str__(self):
        return f"{self.title} S{self.no_season:02d}E{self.no_episode:02d}"


class MovieLibrary(list):


    def get_all_of_type(self, movie_type):
        movie_list = []
        for item in self:
            if isinstance(item, movie_type):
                movie_list.append(item)

        sorted_movie_list = sorted(movie_list, key=lambda item: item.title)
        return sorted_movie_list

    def get_film(self):
        return self.get_all_of_type(Film)

    def get_series(self):
        return self.get_all_of_type(Series)

    def search(self, title: str):
        for item in self:
            if item.title == title:
                return item

    def top_titles(self, quantity: int, movie_type):
        result = []
        if movie_type == Film:
            sort_title = self.get_film()
            sort_views = sorted(sort_title, key=lambda movie: movie.play_count)
        elif movie_type == Series:
            sort_title = self.get_series()
            sort_views = sorted(sort_title, key=lambda series: series.play_count)
        else:
            raise Exception

        for item in range(quantity):
            result.append(sort_views[item])

        return result


def generate_views(library: list):
    chosen_item = random.choice(library)
    chosen_item.play_count = random.randrange(1_000_000, 50_000_000)


def generate_views_10_times(library: list):
    for _ in range(10):
        generate_views(library)

def main():

    storage = [Film('Titanic', 1997, 'drama', 15_928_283),
                     Series('Greys Anatomy', 2005, 'medical drama', 8_547_273,14,3),
                     Film('Notting Hill', 1999, 'romantic comedy', 10_627_829),
                     Film('Love Actually', 2004, 'romantic comedy', 12_647_029),
                     Series('New Girl', 2011, 'comedy', 3_938_823,5,6),
                     Series('Friends', 1994, 'comedy', 28_938_192,10,5),
                     Series('Reign', 2013, 'historical drama', 1_938_931,8,3)]

    #generate views
    generate_views(storage)
    generate_views_10_times(storage)

    movie_library = MovieLibrary(storage)


    #get films:
    print(colored("ONLY FILMS:", 'red'))
    only_films = movie_library.get_film()
    for film in only_films:
        print(film)

    #get series
    print(colored("ONLY SERIES:",'red'))
    only_series = movie_library.get_series()
    for series in only_series:
        print(series)
    #search title
    chosen = movie_library.search('New Girl')
    print(colored(f"I found: {chosen}",'cyan'))

    #top series
    print(colored("TOP SERIES",'yellow'))
    top_series = movie_library.top_titles(3,Series)

    for series in top_series:
        print(series)

    #top films
    print(colored("TOP FILMS", 'yellow'))
    top_films = movie_library.top_titles(2, Film)

    for film in top_films:
        print(film)


if __name__ == '__main__':
    main()

