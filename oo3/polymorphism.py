# use inheritance for polymorphism

class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")

        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print("Playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print("Playing {} as wav".format(self.filename))

class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        print("Playing {} as ogg".format(self.filename))


def main():
    ogg = OggFile("myfile.ogg")
    ogg.play()
    mp3 = MP3File("myfile.mp3")
    mp3.play()

    try:
        not_mp3 = MP3File("myfile.ogg")
        not_mp3.play()

    except Exception:
        print("Wrong Format!")


if __name__ == "__main__":
    main()


############### duck typing

class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"): # flac without . also works
            raise Exception("Invalid file format")

        self.filename = filename

    def play(self):
        print("playing {} as flac".format(self.filename))


# duck typing in python makes polymorphism less cool






























