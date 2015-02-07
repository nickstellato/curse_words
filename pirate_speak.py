#!/usr/bin/env python2

import urllib

def read_text():
    quotes = open("C:\projects\curse_words\movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    convert_to_pirate(contents_of_file)

def convert_to_pirate(text_to_convert):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_convert)
    output = connection.read()
    print(output)
    connection.close()
    
read_text()