'''
    Autor: Kacper Kułak
'''

import os
import argparse

def stworz_parser():

    parser = argparse.ArgumentParser()
    
    parser.add_argument("miesiace", help = "lista miesiecy do wybrania")
    
    parser.add_argument("dzien", help = "lista dni do wybrania")
    
    parser.add_argument("pory_dnia", help = "lista póra dnia: r (rano) lub w (wieczorem) np. [r, w]. Domyślnie rano", nargs = "?", default = "rano")

    parser_trybu = parser.add_mutually_exclusive_group()

    parser_trybu.add_argument("-t", action = "store_ture", help = "tworzy pliki", defualt = 'o')
    parser_trybu.add_argument("-o", action = "store_ture", help = "odczytuje pliki", defualt = 'o')

    parser.add_argument("-c", action = "store_true", help = "tworzenie / odczyt plikow w formacie csv.")
    parser.add_argument("-j", action = "store_true", help = "tworzenie / odczyt plikow w formacie json.")
    
    return parser

def main():
    parser = stworz_parser()
    
    args = parser.parse_args()




if __name__ == "__main__":
    main()