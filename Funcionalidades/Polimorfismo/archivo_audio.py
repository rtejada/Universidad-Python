class ArchivoAudio:
    def __init__(self, nombrearchivo):
        self.ext = ''
        if not nombrearchivo.endswith(self.ext):
            raise Exception('Formato archivo inválido')
        self.nombrearchivo = nombrearchivo


class ArchivoMP3(ArchivoAudio):

    ext = 'mp3'

    def play(self):
        print('Ejecutándose {} como mp3'. format(self.nombrearchivo))


class ArchivoWAv(ArchivoAudio):

    ext = 'wav'

    def play(self):
        print('Ejecutándose {} como mp3'. format(self.nombrearchivo))


class ArchivoOgg(ArchivoAudio):

    ext = 'ogg'

    def play(self):
        print('Ejecutándose {} como mp3'. format(self.nombrearchivo))


mp3 = ArchivoMP3('mi archivo.mp3')
print(mp3.play())
