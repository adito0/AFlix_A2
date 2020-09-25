from AditiFlix_App.domainmodel.movie import Movie


class WatchList:
    def __init__(self):
        self.__watchlist = list()

    @property
    def watchlist(self):
        return self.__watchlist

    def add_movie(self, movie):
        if isinstance(movie, Movie):
            if movie.title is not None:
                if movie not in self.__watchlist:
                    self.__watchlist.append(movie)

    def remove_movie(self, movie):
        if not isinstance(movie, Movie):
            return
        for i in range(len(self.__watchlist)-1, -1, -1):
            if movie == self.__watchlist[i]:
                self.__watchlist.pop(i)

    def select_movie_to_watch(self, index):
        if type(index) != int:
            return
        elif (index < len(self.__watchlist)) and (index >= 0):
            return self.__watchlist[index]
        else:
            return

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if self.size() < 1:
            return
        return self.__watchlist[0]

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        self.__index += 1
        if self.__index < self.size():
            return self.__watchlist[self.__index]
        else:
            raise StopIteration
            self.__index = -1

