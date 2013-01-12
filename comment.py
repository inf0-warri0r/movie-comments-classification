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
import grammer


class comment:
    def __init__(self):
        self.positive = {}
        self.negative = {}
        self.g = grammer.grammer()
        self.g.process_endings()
        self.g.process_stop()

    def fill(self, a, b, comments):
        for comment in comments:
            no = True
            for word in comment.split():
                word = word.lower()
                word = self.g.replace_fun(word)
                if word == 'not' or word == 'isnt' or word == 'dont' or word == 'aint':
                    no = False
                    continue
                if self.g.stop.get(word, 0) == 0:
                    word = self.g.stm(word)
                    if word == "":
                        continue
                    if no:
                        a[word] = a.get(word, 0) + 1
                    else:
                        b[word] = b.get(word, 0) + 1
                        no = True
        return a, b

    def file_read(self, file_path):
        try:
            f = open(file_path, 'r')
        except IOError:
            print "ERROR : ", file_path, "file reading error "
            return list()
        lines = f.read().splitlines()
        return lines

    def positive_input(self, file_path):
        positive_comments = self.file_read(file_path)
        if len(positive_comments) <= 0:
            return 0
        self.positive, self.negative = self.fill(self.positive,
            self.negative, positive_comments)
        return 1

    def negative_input(self, file_path):
        negative_comments = self.file_read(file_path)
        if len(negative_comments) <= 0:
            return 0
        self.negative, self.positive = self.fill(self.negative,
            self.positive, negative_comments)
        return 1

    def check_comment(self, test_comment):
        words = test_comment.split()
        positive_c = 0.0
        negative_c = 0.0
        no = True
        for word in words:
            word = word.lower()
            p = 0
            n = 0
            word = self.g.replace_fun(word)
            if word == 'not' or word == 'isnt' or word == 'dont' or word == 'aint':
                no = False
                continue
            if self.g.stop.get(word, 0) == 0:
                word = self.g.stm(word)
                if word == "":
                    continue
                if no:
                    p = p + self.positive.get(word, 0)
                    n = n + self.negative.get(word, 0)
                else:
                    n = n + self.positive.get(word, 0)
                    p = p + self.negative.get(word, 0)
                    no = True
            if p + n > 0:
                positive_c = positive_c + float(p) / float(p + n)
                negative_c = negative_c + float(n) / float(p + n)
        if positive_c > negative_c:
            return 'g'
        elif negative_c > positive_c:
            return 'b'
        return 'f'

    def test(self, file_path):
        test_comments = self.file_read(file_path)
        if len(test_comments) <= 0:
            return 0, 0, 0
        total = len(test_comments)
        pc = 0
        nc = 0
        for test_comment in test_comments:
            c = self.check_comment(test_comment)
            if c == 'g':
                pc = pc + 1
            elif c == 'b':
                nc = nc + 1

        return pc, nc, total

    def test_all(self, positive_file_path, negative_file_path):

        positive_c1, negative_c1, total1 = self.test(positive_file_path)
        if total1 == 0:
            return 0, 0
        positive_c2, negative_c2, total2 = self.test(negative_file_path)
        total = total1 + total2
        error = total1 - positive_c1 + total2 - negative_c2
        return total, float(error) / float(total)

    def record(self):
        f = open("data/positive.data", 'w')
        for key in self.positive:
            f.write(str(key) + " " + str(self.positive[key]) + '\n')

        f = open("data/negative.data", 'w')
        for key in self.negative:
            f.write(str(key) + " " + str(self.negative[key]) + '\n')

    def load(self):
        self.positive = {}
        self.negative = {}

        lines = self.file_read("data/positive.data")
        if len(lines) <= 0:
            return 0
        for line in lines:
            data = line.split()
            self.positive[data[0]] = int(data[1])

        lines = self.file_read("data/negative.data")
        for line in lines:
            data = line.split()
            self.negative[data[0]] = int(data[1])
        return 1
