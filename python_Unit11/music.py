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

        return "TITLE: " + self.__title + ", Artist: " + self.__artist + ", Duration: " + self.__duration.get_time()
    
    def get_title(self):
        
        return self.__title
    
    def get_artist(self):

        return self.__artist
    
    def get_duration(self):

        return self.__duration
    

class Album:

    __slots__ = ["__title", "__artist", "__track", "__total_duration"]

    def __init__(self, title):
        
        self.__title = title
        self.__artist = []
        self.__track = []
        self.__total_duration = Time()

    def add_song(self, song):


        if len(self.__artist) > 1:
            self.__artist = "Various"

        else:
            artist = song.get_artist()
            self.__artist.append(artist)

        hours = song.get_duration().get_hours()
        minutes = song.get_duration().get_minutes()
        seconds = song.get_duration().get_seconds()

        self.__total_duration.set_hours(self.__total_duration.get_hours() + hours)
        self.__total_duration.set_minutes(self.__total_duration.get_minutes() + minutes)
        self.__total_duration.set_seconds(self.__total_duration.get_seconds() + seconds)

        self.__track.append(song)

        if self.__total_duration.get_minutes() >= 60:
            self.__total_duration.set_hours(self.__total_duration.get_hours() + self.__total_duration.get_minutes() // 60) 
            self.__total_duration.set_minutes(self.__total_duration.get_minutes() % 60)

        if self.__total_duration.get_seconds() >= 60:
            self.__total_duration.set_minutes(self.__total_duration.get_minutes() + self.__total_duration.get_seconds() // 60) 
            self.__total_duration.set_seconds(self.__total_duration.get_seconds() % 60)


    def get_title(self):

        return self.__title
    
    def get_artist(self):

        return self.__artist
    
    def get_tracks(self):

        return self.__track
    
    def get_duration(self):
        
        return self.__total_duration


def print_album(album):
    a = ""
    print("ALBUM TITLE: " + album.get_title())

    if album.get_artist() == "Various":
        a = "Various"
    
    else: 
        for artist in album.get_artist():
            a = " " + artist
    
    print("ARTISTS:" + a)
    print("Duraion: " + album.get_duration().get_time())

    for song in album.get_tracks():
        print(song.get_song())

        
    

def main():

    # Time 테스트
    print("=== TIME TEST ===")
    t1 = Time(0, 4, 7)
    t2 = Time(0, 3, 25)
    t3 = Time(0, 5, 10)

    print(t1.get_time())
    print(t2.get_time())
    print(t3.get_time())


    # Song 테스트
    print("\n=== SONG TEST ===")
    s1 = Song(
    "Time to Say Goodbye",
    "Andrea Bocelli and Sarah Brightman",
    t1
    )

    s2 = Song(
    "Bohemian Rhapsody",
    "Queen",
    t2
    )

    s3 = Song(
    "Yellow",
    "Coldplay",
    t3
    )

    s4 = Song(
    "Shape of You",
    "Ed Sheeran",
    Time(0, 3, 53)
    )

    s5 = Song(
    "Someone Like You",
    "Adele",
    Time(0, 4, 45)
    )

    s6 = Song(
    "Blinding Lights",
    "The Weeknd",
    Time(0, 3, 20)
    )

    s7 = Song(
    "Viva La Vida",
    "Coldplay",
    Time(0, 4, 2)
    )

    s8 = Song(
    "Hotel California",
    "Eagles",
    Time(0, 6, 30)
    )

    

    print(s1.get_song())
    print()

    print(s2.get_song())
    print()

    print(s3.get_song())


    # Album 테스트
    print("\n=== ALBUM TEST ===")

    album = Album("My Favorite Album")

    album.add_song(s1)
    album.add_song(s2)
    album.add_song(s3)
    album.add_song(s4)
    album.add_song(s5)
    album.add_song(s6)
    album.add_song(s7)
    album.add_song(s8)


    print("\n=== PRINT ALBUM ===")
    print_album(album)


if __name__ == "__main__":
    main()

        