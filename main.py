from pytest import *

def bixtil_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return print('C\'est une année bissextile')
            else:
                return print('Revenez dans 4 ans')
        else:
            return print('C\'est une année bissextile')
    else:
        return print('Revenez dans 4 ans')

def test_bixtil_year(capsys):
    bixtil_year(2000)
    captured = capsys.readouterr()
    assert captured.out == "C'est une année bissextile\n"

    bixtil_year(1900)
    captured = capsys.readouterr()
    assert captured.out == "Revenez dans 4 ans\n"

    bixtil_year(2020)
    captured = capsys.readouterr()
    assert captured.out == "C'est une année bissextile\n"

    bixtil_year(2021)
    captured = capsys.readouterr()
    assert captured.out == "Revenez dans 4 ans\n"

    