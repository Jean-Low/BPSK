import npyscreen as ns

def testFunc( *args):
    form = ns.Form(name = 'npyscreen Form!')
    form.edit()

if ( __name__ == "__main__"):
    #print("I Curse You!!!!")
    ns.wrapper_basic ( testFunc)
    #print("I take the Curse away!!!!")
