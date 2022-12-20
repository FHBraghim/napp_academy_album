import random
import csv
import os

class Album():

    def __init__(self):
        self._paises = self.create_countries()
        self._figurinhas_all = self.create_figures()
        self._figurinhas_coladas_album = []
        self._figurinhas_repetidas = []
        self._figurinhas_faltantes = self.figurinhas_faltantes()
    
    def create_countries(self):
        paises =  ['QAT', 'ECU', 'SEN', 'NED']
        paises += ['ENG', 'IRN', 'USA', 'WAL']
        paises += ['ARG', 'KSA', 'MEX', 'POL']
        paises += ['FRA', 'AUS', 'DEN', 'TUN']
        paises += ['ESP', 'CRC', 'GER', 'JPN']
        paises += ['BEL', 'CAN', 'MAR', 'CRO']
        paises += ['BRA', 'SRB', 'SUI', 'CMR']
        paises += ['POR', 'GHA', 'URU', 'KOR']
        return paises

    def create_figures(self):
        figurinhas =  ['00']
        figurinhas += ['FWC' + str(numero) for numero in range(1, 19)]
        figurinhas += [pais + str(numero) for pais in self._paises for numero in range(1, 21)]
        figurinhas += ['FWC' + str(numero) for numero in range(19, 30)]
        figurinhas += ['C' + str(numero) for numero in range(1, 9)]
        return figurinhas

    def add_figure(self, figure):
        if self.check_figure_add(figure):
            self._figurinhas_coladas_album.append(figure)
            return True
        else:
            self._figurinhas_repetidas.append(figure)
            print(f"Essa figurinha: '{figure}' já está colada no álbum")
            return False

    def check_figure_add(self, figure):
        if figure not in self._figurinhas_coladas_album:
            return True
        else:
            return False

    def open_package(self):
        pacote = []
        for i in range(5):
            figura = random.choice(list(self._figurinhas_all))
            self.add_figure(figura)
            pacote.append(figura)
        return pacote

    def figurinhas_faltantes(self):
        figurinhas_faltantes = list(set(self._figurinhas_all) - set(self._figurinhas_coladas_album))
        figurinhas_faltantes.sort()
        return figurinhas_faltantes

    def remove_figure(self, figure):
        if self.check_figure_repeated(figure):
            self._figurinhas_repetidas.remove(figure)
            print(f"Uma cópia de '{figure}' foi removida do monte de figurinhas repetidas")
            return True
        else:
            print(f"No monte de figurinhas repetidas, não há uma cópia de '{figure}'")
            return False

    def check_figure_repeated(self, figure):
        if figure in self._figurinhas_repetidas:
            return True
        else:
            return False

    def gravar_figurinhas_coladas(self, filename='./code/figurinhas_coladas.csv'):
        stickers = self._figurinhas_coladas_album
        stickers.sort()
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(stickers)

    def ler_figurinhas_coladas(self, filename='./code/figurinhas_coladas.csv'):
        with open(filename) as csvfile:
            sreader = csv.reader(csvfile)
            lista = [] 
            for row in sreader:
                lista += row
            return lista

    def gravar_figurinhas_repetidas(self, filename='./code/figurinhas_repetidas.csv'):
        stickers = self._figurinhas_repetidas
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(stickers)

    def ler_figurinhas_repetidas(self, filename='./code/figurinhas_repetidas.csv'):
        with open(filename) as csvfile:
            sreader = csv.reader(csvfile)
            lista = [] 
            for row in sreader:
                lista += row
            return lista

    def gravar_figurinhas_faltantes(self, filename='./code/figurinhas_faltantes.csv'):
        stickers = self.figurinhas_faltantes()
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(stickers)

    def ler_figurinhas_faltantes(self, filename='./code/figurinhas_faltantes.csv'):
        with open(filename) as csvfile:
            sreader = csv.reader(csvfile)
            lista = [] 
            for row in sreader:
                lista += row
            return lista

    def show_figures_added(self):
        os.system("clear")
        coladas = self._figurinhas_coladas_album
        for fig in coladas:
            if fig == '00':
                print(f"{fig}, ", end='')
                print()
            if fig in ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']:
                print(f"{fig}, ", end='')
                print()
            if 'FWC' in fig:
                print(f"{fig}, ", end='')
        print()
        for pais in self._paises:
            for fig in coladas:
                if pais in fig:
                    print(f"{fig}, ", end='')                    
            print()

    def show_figures_repeated(self):
        os.system("clear")
        repetidas = self._figurinhas_repetidas
        for fig in repetidas:
            if fig == '00':
                print(f"{fig}, ", end='')
                print()
            if fig in ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']:
                print(f"{fig}, ", end='')
                print()
            if 'FWC' in fig:
                print(f"{fig}, ", end='')
        print()
        for pais in self._paises:
            for fig in repetidas:
                if pais in fig:
                    print(f"{fig}, ", end='')                    
            print()
    
    def show_figures_missing(self):
        os.system("clear")
        faltantes = self.figurinhas_faltantes()
        for fig in faltantes:
            if fig == '00':
                print(f"{fig}, ", end='')
                print()
            if fig in ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']:
                print(f"{fig}, ", end='')
                print()
            if 'FWC' in fig:
                print(f"{fig}, ", end='')
        print()
        for pais in self._paises:
            for fig in faltantes:
                if pais in fig:
                    print(f"{fig}, ", end='')                    
            print()