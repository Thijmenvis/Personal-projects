#!/usr/bin/env python2

print "hoeveel op de bank nu?"
bank = raw_input("> ")
print "hoeveel dagen tot betaling?"
dagen = raw_input("> ")
budget = (float(bank) / float(dagen))
print "vanaf nu maar %r euro per dag!" % budget

def rekening():
    print """
        op de bank:             %r
        dagen tot betaling:     %r
        ----------------------------------------
        budget per dag:         %r
        """ % (float(bank), float(dagen), budget)

rekening()

prompt = raw_input("> ")
