class Time:

    __slots__ = ["__hours", "__minutes", "__seconds"]

    def __init__(self, hours=0, minutes=0, seconds=0):

        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def get_time(self):

        return '{}:{:02}:{:02}'.format(self.__hours, self.__minutes, self.__seconds)
    
    def get_hours(self):

        return self.__hours
    
    def get_minutes(self):

        return self.__minutes
    
    def get_seconds(self):

        return self.__seconds
    
    def set_hours(self, hours):

        self.__hours = hours

    def set_minutes(self, minutes):

        self.__minutes = minutes
    
    def set_seconds(self, seconds):

        self.__seconds = seconds


class Song:

    __slots__ = ["__title", "__artist", "__duration"]

    def __init__(self, title, artist, duration):

        self.__title = title
        self.__artist = artist
        self.__duration = duration
    
    def get_song(self):

        return "TITLE: " + self.__title + "\nArtist: " + self.__artist + "\nDuration: " + self.__duration.get_time()
    
    def get_title(self):
        
        return self.__title
    
    def get_artist(self):

        return self.__artist
    
    def get_duration(self):

        return self.__duration
    

class Album:

    __slots__ = ["__title", "__artist", "__num_track", "__total_duration"]

    def __init__(self, title):
        
        self.__title = title
        self.__artist = []
        self.__num_track = 0
        self.__total_duration = Time()

    def add_song(self, song):

        artist = song.get_artist()
        self.__artist.append(artist)

        if len(self.__artist) > 1:
            self.__artist = "Various"

        hours = song.get_duration().get_hours()
        minutes = song.get_duration().get_minutes()
        seconds = song.get_duration().get_seconds()

        self.__total_duration.set_hours(self.__total_duration.get_hours + hours)
        self.__total_duration.set_minutes(self.__total_duration.get_minutes + minutes)
        self.__total_duration.set_seconds(self.__total_duration.get_seconds + seconds)

        self.__num_track += 1

    def get_title(self):

        return self.__title
    
    def get_artist(self):

        return self.__artist


def print_album(album):
    a = ""
    print("TITLE: " + album.get_time())

    for artist in album.get_artist():
        a = " " + artist
    
    print("ARTISTS:" + a)



        
        
    

def main():

    time = Time(0, 4, 7)
    print(time.get_time())
    song = Song("Time to Say Goodbye", "Andrea Bocelli and Sarah Brightman", time)
    print(song.get_song())


if __name__ == "__main__":
    main()
        