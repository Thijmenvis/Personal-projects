import sys

argv = []
script, bank, dagen = argv

def rekening():
    print """
        op de bank:             %r
        dagen tot betaling:     %r
        ----------------------------------------
        budget per dag:         %r
        """ % (float(bank), float(dagen), budget)

if len(sys.argv) == 3:
    rekening()
else:
    print "didn't work"
