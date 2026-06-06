class Time:

    __slots__ = ["__hours", "__minutes", "__seconds"]

    def __init__(self, hours=0, minutes=0, seconds=0):

        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def get_time(self):

        return '{}:{:02}:{:02}'.format(self.__hours, self.__minutes, self.__seconds)
    
class Song:
    
    

def main():

    time = Time(3, 12, 36)
    print(time.get_time())


if __name__ == "__main__":
    main()
        