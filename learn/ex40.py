class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

def line():
    print "-" * 10

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

here_is_another_song = Song(["hey how are you", "this is not a song but",
                            "just some weird thing i wrote"])

happy_bday.sing_me_a_song()
line()
bulls_on_parade.sing_me_a_song()
line()
here_is_another_song.sing_me_a_song()
