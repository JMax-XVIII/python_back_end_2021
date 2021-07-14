
class Entregable():

    def entregar(self):
        pass

    def devolver(self):
        pass

    def isEntregado(self):
        pass

    def compareTo(self, Objecta):
        pass

class Serie(Entregable):

    #atributos

    titulo = ""
    genero = ""
    creador = ""

    def __init__(self, titulo, genero, creador, numero_temporadas = 3):
        self.titulo = titulo
        self.numero_temporadas = numero_temporadas
        self.entregado = False
        self.genero = genero
        self.creador = creador

    # metodos

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_numero_temporadas(self, numero_temporadas):
        self.numero_temporadas = numero_temporadas

    def set_genero(self, genero):
        self.genero = genero

    def set_creador(self, creador):
        self.creador = creador

    def get_titulo(self):
        return self.titulo

    def get_numero_temporadas(self):
        return self.numero_temporadas

    def get_genero(self):
        return self.genero

    def get_creador(self):
        return self.creador

    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado

    def compareTo(self, Objecta):

        if self.numero_temporadas < Objecta.numero_temporadas:
            aux = False
        if self.numero_temporadas > Objecta.numero_temporadas:
            aux = True

        return aux

    def __str__(self):
        text = "Titulo: {0} - Genero: {1} - Numero de Temporadas: {2}" \
               " - Creador: {3}"
        return text.format(self.get_titulo(), self.get_genero(), self.get_numero_temporadas(), self.get_creador())

class VideoJuego(Entregable):

    titulo = ""
    genero = ""
    company = ""

    def __init__(self, titulo, genero, company, horas_estimadas=10):
        self.titulo = titulo
        self.genero = genero
        self.company = company
        self.horas_estimadas = horas_estimadas
        self.entregado = False

    def set_titulo(self, titulo):
        self.titulo = titulo
    def set_genero(self,genero):
        self.genero = genero
    def set_company(self,company):
        self.company = company
    def set_horas_estimadas(self, horas_estimadas):
        self.horas_estimadas = horas_estimadas

    def get_titulo(self):
        return self.titulo
    def get_genero(self):
        return self.genero
    def get_company(self):
        return self.company
    def get_horas_estimadas(self):
        return self.horas_estimadas

    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado

    def compareTo(self, Objecta):
        aux = False
        if self.horas_estimadas < Objecta.horas_estimadas:
            aux = False
        if self.horas_estimadas > Objecta.horas_estimadas:
            aux = True
        return aux

    def __str__(self):
        text = "Titulo: {0} - Genero: {1} - Company: {2}" \
               " - Horas Estimadas: {3}"
        return text.format(self.get_titulo(), self.get_genero(), self.get_company(), self.get_horas_estimadas())

class VideoClub():

    def status_stock(self):
        ### Series
        serie_1 = Serie("The 100", "Ficcion", "Jason Rothenberg",12)
        serie_2 = Serie("Buffy", "Ficcion", "Joss Whedon",8)
        serie_3 = Serie("House", "Drama Medico", "David Shore",7)
        serie_4 = Serie("The Walking Dead", "Survival Horror", "Frank Darabont",800)
        serie_5 = Serie("Lost", "Weird Stuf", "Some Guy",5)
        #Juegos
        juego1 = VideoJuego("Overwatch", "FPS", "Blizzard",1580)
        juego2 = VideoJuego("Fuga de caballos paraliticos", "LCD", "Camel Productions",2)
        juego3 = VideoJuego("Evading Taxes", "Mafia Administration", "Political Productions",80)
        juego4 = VideoJuego("Get Paid Without Working", "Fantasy", "Comfortable Marx", 1)
        juego5 = VideoJuego("Shoot all the clowns", "Graffic adventure", "Dickinson Shouts",80)

        array_series = [serie_1, serie_2, serie_3, serie_4, serie_5]
        array_videojuegos = [juego1, juego2, juego3, juego4, juego5]

        array_series[1].entregar()
        array_series[3].entregar()
        array_series[4].entregar()

        array_videojuegos[3].entregar()
        array_videojuegos[2].entregar()

        series_regresadas = 0
        juegos_regresados = 0

        for series in array_series:
            if series.isEntregado() == True:
                series_regresadas +=1

        for juegos in array_videojuegos:
            if juegos.isEntregado() == True:
                juegos_regresados +=1

        text = "Juegos Regresados: {0}"
        print(text.format(juegos_regresados))
        text = "Series Regresadas: {0}"

        print(text.format(series_regresadas))
        aux_list_video_juegos = []
        aux_list_series = []

        for pos in range(array_videojuegos.__len__()):
                aux_list_video_juegos.append(array_videojuegos[pos].get_horas_estimadas())
                aux_list_series.append(array_series[pos].get_numero_temporadas())
        text = "El Video Juego Con Mas Horas es: {0}"
        print(text.format(array_videojuegos[aux_list_video_juegos.index(max(aux_list_video_juegos))]))
        text = "La Serie Con Mas Temporadas es: {0}"
        print(text.format(array_series[aux_list_series.index(max(aux_list_series))]))

VideoClub = VideoClub()
VideoClub.status_stock()
