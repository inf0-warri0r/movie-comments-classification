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

import comment


def header():
    print "--------------------------------------------------"
    print "       -- MOVIE COMMENTS CLASSIFICATION --        "
    print "                                                  "
    print "   Author : tharindra galahena (inf0_warri0r)     "
    print "   Blog   : http://www.inf0warri0r.blogspot.com   "
    print "--------------------------------------------------"
    print ""


def menu():
    print " MENU"
    print ""
    print " 1. Train"
    print " 2. Test"
    print " 3. Load Data"
    print " 4. Record Data"
    print " 5. Check Comment"
    print " 6. Exit"
    print ""

if __name__ == '__main__':

    com = comment.comment()
    header()

    while 1:
        menu()
        number = int(raw_input('Enter your input Number : '))
        if number == 1:
            print ""
            print "TRAINING"
            print ""
            plst = raw_input('Enter the file name of positive comments list:')
            nlst = raw_input('Enter the file name of negative comments list:')
            print ""
            print "Training is started ... "
            print ""
            if com.positive_input(plst) == 1:
                if com.negative_input(nlst) == 1:
                    print " - TRAINING COMPLETED -"
            print ""
        elif number == 2:
            print ""
            if len(com.positive) > 0 and len(com.negative) > 0:
                print "TESTING"
                print ""
                plst = raw_input('Enter the name of positive test list:')
                nlst = raw_input('Enter the name of negative test list:')

                print ""
                print "Testing is started ..."
                print ""
                total, error = com.test_all(plst, nlst)
                if total != 0:
                    print " - TESTING COMPLETED -"
                    print ""
                    print "Total comments checked : ", total
                    print "The error rate : ", error
            else:
                print "The program have not been trained / loaded"
                print "Train the program or Load data before testing"
            print ""
        elif number == 3:
            print ""
            print "LOADING DATA"
            print ""
            print "Recording is started ..."
            print ""
            if com.load() != 0:
                print "- LOADING COMPLETED -"
            print ""
        elif number == 4:
            print ""
            if len(com.positive) > 0 and len(com.negative) > 0:
                print "RECORDING DATA"
                print ""
                print "Recording is started ..."
                com.record()
                print ""
                print "- RECORDING COMPLETED -"
            else:
                print "The program have not been trained"
                print "Train the program or Load data before testing"
            print ""
        elif number == 5:
            print ""
            if len(com.positive) > 0 and len(com.negative) > 0:
                print "CHECK COMMENT"
                loop = True
                while loop:
                    print ""
                    msg = "Enter your Comment to Check "
                    msg = msg + "(enter 'quit' to go back to MENU):"
                    comment = raw_input(msg)
                    if comment == 'quit':
                        loop = False
                        continue
                    c = com.check_comment(comment)
                    print ""
                    if c == 'g':
                        print "The comment is a positive comment"
                    elif c == 'b':
                        print "The comment is a negative comment"
                    else:
                        print "Unable to classfy the comment"
            else:
                print "The program have not been trained"
                print "Train the program or Load data before testing"
            print ""
        elif number == 6:
            break
