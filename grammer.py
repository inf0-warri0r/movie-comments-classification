"""
Author : tharindra galahena (inf0_warri0r)
Project: movie comments classification
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 12/01/2013
License:

     Copyright 2013 Tharindra Galahena

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
This program. If not, see http://www.gnu.org/licenses/.

"""


class grammer:
    def __init__(self):
        self.endings = {}
        self.stop = {}
        self.fun = ['.', ',', '"', ';', ':', '-', '_', '\'',
            '?', '(', ')', '[', ']', '/', '\\', '!',
            '0', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', '*', '&', '$', '@', '^', '+',
            '=']

    def replace_fun(self, word):

        for c in self.fun:
            word = word.replace(c, '')
        return word

    def process_stop(self):

        try:
            f3 = open("data/stop", 'r')
        except IOError:
            print "ERROR : ' data/stop ' is missing"
            exit(0)

        stop_words = f3.read().splitlines()
        for word in stop_words:
            word = self.replace_fun(word)
            self.stop[word] = 1

    def process_endings(self):

        try:
            f = open("data/endings", 'r')
        except IOError:
            print "ERROR : ' data/endings ' is missing"
            exit(0)
        en = f.read().splitlines()
        for i in range(1, 12):
            self.endings[i] = {}

        for e in en:
            es = e.split()
            if es[1] == '1':
                self.endings[len(es[0])][es[0]] = 1
            elif es[1] == '2':
                self.endings[len(es[0]) + 2][es[0]] = 1

    def stm(self, word):
        l = len(word)
        if l > 11:
            counter = 11
        else:
            counter = l - 1
        for i in range(0, counter):
            end = word[l - counter + i:]
            if self.endings[counter - i].get(end, 0) == 1:
                word = word[:l - counter + i]
                return word
            elif len(end) > 2 and end[0] == end[1]:
                end = end[2:]
                if self.endings[counter - i].get(end, 0) == 1:
                    word = word[:l - counter + i + 1]
                    return word
        return word
