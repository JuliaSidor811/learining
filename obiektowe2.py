import random
class Film:
    def __init__(self,title:str,publishment_year:int,genere:str,play_count:int):
        self.title = title
        self.publishment_year = publishment_year
        self.genere = genere
        self.play_count = play_count

    def __str__(self):
        return f"{self.title} ({self.publishment_year})"

    def play(self):
        self.play_count+=1
        return f"Play count: {self.play_count}"



class Series(Film):
    def __init__(self,no_episode:int,no_season:int,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.no_episode = no_episode
        self.no_season = no_season
    def __str__(self):
        return f"{self.title} S{self.no_season:02d}E{self.no_episode:02d}"


def get_movies(library:list):
    movie_list = []
    for item in library:
        if not isinstance(item, Series):
            movie_list.append(item)
    sorted_movie_list = sorted(movie_list,key=lambda movie: movie.title )
    return sorted_movie_list

def get_series(library:list):
    series_list = []
    for item in library:
        if isinstance(item, Series):
            series_list.append(item)
    sorted_series_list = sorted(series_list,key=lambda series: series.title )
    return sorted_series_list

def search(library:list, title:str):
    for item in library:
        if item.title == title:
            return item

def generate_views(library:list):
    chosen_item = random.choice(library)
    chosen_item.play_count = random.randrange(1_000_000, 50_000_000)


def generate_views_10_times(library:list):
    i = 0
    while i < 10:
        generate_views(library)
        i+=1

def top_titles(library:list,quantity:int,content_type):
    result =[]
    if content_type == "Film":
        sort_title = get_movies(library)
        sort_views = sorted(sort_title,key=lambda movie: movie.play_count)
    elif content_type =="Series":
        sort_title = get_series(library)
        sort_views = sorted(sort_title,key=lambda series: series.play_count)
    else:
        sort_views = None

    if sort_views is not None:
        for item in range(quantity):
            result.append(sort_views[item])

    return result








def main():
    movie_library =[Film('Titanic',1997,'drama',15_928_283),
                    Series(14,3,'Greys Anatomy',2005, 'medical drama',8_547_273),
                    Film('Notting Hill',1999,'romantic comedy', 10_627_829),
                    Film('Love Actually',2004,'romantic comedy',12_647_029),
                    Series(5,6,'New Girl',2011,'comedy',3_938_823),
                    Series(10,5,'Friends',1994,'comedy',28_938_192),
                    Series(8,2,'Reign',2013,'historical drama',1_938_931)]

    #SAME FILMY
    only_movies = get_movies(movie_library)
    print("FILMS:\n")
    for movie in only_movies:
        print(movie)

    #SAME SERIALE
    only_series = get_series(movie_library)
    print("\nSERIES:\n")
    for series in only_series:
        print(series)

    #SZUKANIE PO TYTULE
    szukana = search(movie_library,"New Girl")

    #DODAWANIE WYSWIETLEN
    print(szukana.play())

    #GENEROWANIE WYSWIETLEN
    generate_views(movie_library)
    generate_views_10_times(movie_library)

    #TOP
    print("\nTOP FILMS\n")
    top_movies = top_titles(movie_library,2,"Film")
    for item in top_movies:
        print(item)

    print("\nTOP SERIES\n")
    top_series = top_titles(movie_library,3,"Series")
    for item in top_series:
        print(item)





if __name__ == '__main__':
    main()