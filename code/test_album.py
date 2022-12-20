import pytest
from album import Album
import csv
import os

class TestAlbum:

    def test_instance_declared(self):
        exemplo = Album()
        assert isinstance(exemplo, Album)

    def teste_atributos_padrao(self):
        exemplo = Album()
        assert isinstance(exemplo._figurinhas_all, list)
        assert len(exemplo._figurinhas_all) == 678
        assert exemplo._figurinhas_coladas_album == []
        assert len(exemplo._figurinhas_coladas_album) == 0
        assert isinstance(exemplo._figurinhas_faltantes, list)
        assert len(exemplo._figurinhas_faltantes) == 678
        assert exemplo._figurinhas_repetidas == []
        assert len(exemplo._figurinhas_repetidas) == 0    
        assert isinstance (exemplo._paises, list)
        assert len(exemplo._paises) == 32

    def teste_metodo_create_countries(self):
        exemplo = Album()
        lista_paises = exemplo.create_countries()
        assert isinstance(lista_paises, list)
        assert len(lista_paises) == 32
        assert lista_paises[0] == 'QAT' 
        assert 'KOR' in lista_paises[-1]
        assert 'BRA' in lista_paises
        assert 'XXX' not in lista_paises

    def teste_metodo_create_figures(self):
        exemplo = Album()
        lista_figurinhas = exemplo.create_figures()
        assert isinstance(lista_figurinhas, list)
        assert len(lista_figurinhas) == 678
        assert lista_figurinhas[0] == '00'
        assert lista_figurinhas[-1] == 'C8'
        assert 'BRA1' in lista_figurinhas
        assert 'BRA21' not in lista_figurinhas

    def teste_metodo_check_figure_add(self):
        exemplo = Album()
        figuras = exemplo._figurinhas_coladas_album
        assert len(figuras) == 0
        figuras.append('BRA1')
        assert not exemplo.check_figure_add('BRA1')
        assert exemplo.check_figure_add('BRA2')

    def teste_metodo_add_figure(self):
        exemplo = Album()
        figuras = exemplo._figurinhas_coladas_album
        assert len(figuras) == 0
        exemplo.add_figure('BRA1')
        assert not exemplo.add_figure('BRA1')

    def teste_metodo_open_package(self):
        exemplo = Album()
        exemplo.add_figure('BRA1')
        assert len(exemplo._figurinhas_coladas_album) == 1
        exemplo.add_figure('KOR4')
        exemplo.add_figure('URU10')
        exemplo.add_figure('POR6')
        exemplo.add_figure('SRV17')
        assert len(exemplo._figurinhas_coladas_album) == 5 
        assert len(exemplo._figurinhas_repetidas) == 0 # Verifica se todas as figurinhas estão em figurinhas coladas

    def teste_metodo_open_package_fail(self):
        exemplo = Album()
        exemplo.add_figure('BRA1')
        assert len(exemplo._figurinhas_coladas_album) == 1
        exemplo.add_figure('BRA1') # Repetida
        exemplo.add_figure('URU10')
        exemplo.add_figure('POR6')
        exemplo.add_figure('SRV21') # Não existe
        assert len(exemplo._figurinhas_coladas_album) < 5 
        assert len(exemplo._figurinhas_repetidas) == 1

    def teste_metodo_figurinhas_faltantes(self):
        exemplo = Album()
        lista_faltantes = exemplo.figurinhas_faltantes()
        assert len(lista_faltantes) == 678        
        exemplo.add_figure('BRA1') 
        exemplo.add_figure('URU10')
        exemplo.add_figure('POR6')
        lista_faltantes = exemplo.figurinhas_faltantes()
        assert len(lista_faltantes) == 675

    def teste_metodo_gravar_figurinhas_coladas(self):
        caminho = 'figurinhas_coladas.csv'
        assert os.path.exists(caminho) # Verifica se o caminho do arquivo existe
        with open(caminho) as file:
            reader = csv.reader(file)
            num_linhas = 0
            for row in reader:
                num_linhas += 1
                assert isinstance(row, list) # Verifica se a linha é uma lista
                assert isinstance(row[0], str) # Verifica se o arquivo na 1ª posição da lista é um str
        assert num_linhas > 0

    def teste_metodo_gravar_figurinhas_repetidas(self):
        caminho = 'figurinhas_repetidas.csv'
        assert os.path.exists(caminho)
        with open(caminho) as file:
            reader = csv.reader(file)
            num_linhas = 0 
            for row in reader:
                num_linhas += 1
                assert isinstance(row, list)
                assert isinstance(row[0], str)
        assert num_linhas >= 1

    def teste_metodo_gravar_figurinhas_faltantes(self):
        caminho = 'figurinhas_faltantes.csv'
        assert os.path.exists(caminho)
        with open(caminho) as file:
            reader = csv.reader(file)
            num_linhas = 0 
            for row in reader:
                num_linhas += 1
                assert isinstance(row, list)
                assert isinstance(row[0], str)
        assert num_linhas == 1

    def teste_metodo_remove_figure(self):
        exemplo = Album()
        exemplo._figurinhas_repetidas = ['BRA1', 'KOR12', 'ESP11', 'QAT8', 'CRO12']
        assert len(exemplo._figurinhas_repetidas) == 5
        exemplo.remove_figure('ESP11')
        assert len(exemplo._figurinhas_repetidas) == 4

