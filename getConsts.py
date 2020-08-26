from array import array
import sys

def getInjTarPos(pos):
    if pos==0: # Old top light injector (location of SK deployment)
        injPos = array('d',[-35.3, 777.7, 1802.7])
        tarPos = array('d',[-35.3, 777.7, -1810.0]) # SK is 14.81, 915.6, -1810.0
    elif pos==1: # New top (default for vertical laser analysis)
        injPos = array('d',[-70.7, -777.7, 1802.7])
        tarPos = array('d',[-25.00, -694.5, -1810.0])
    elif pos==2: # B1 injector
        injPos = array('d',[1490.73, 768.14, 1232.25])
        tarPos = array('d',[-1474.44, -825.362, 1243.0])
    elif pos==3: # B2 injector
        injPos = array('d',[1490.73, 768.14, 595.95])
        tarPos = array('d',[-1453.88, -860.984, 600.0])
    elif pos==4: # B3 injector
        injPos = array('d',[1490.73, 768.14, -40.35])
        tarPos = array('d',[-1494.65, -788.019, -99.00])
    elif pos==5: # B4 injector
        injPos = array('d',[1490.73, 768.14, -605.95])
        tarPos = array('d',[-1459.59, -851.269, -565.00])
    elif pos==6: # B5 injector
        injPos = array('d',[1490.73, 768.14, -1242.25])
        tarPos = array('d',[-1427.93, -903.300, -1232.00])
    elif pos==7: # bottom injector
        injPos = array('d',[-70.7, 777.7, -1802.7])
        tarPos = array('d',[-103.00, 768.8, 1810.0])
    else:
        print "ERROR: Invalid position definition. Should be integer from 0-7."
        print "Exiting..."
        sys.exit(1)
    return injPos, tarPos

def getSpeedOfLight(wav):
    '''Takes wavelength in nm, returns specific speed of light in water in cm/ns.'''
    if wav==337:
        c = 21.3070107
    elif wav==375:
        c = 21.5782452
    elif wav==405:
        c = 21.7289524 #note that SK script seems buggy so in MC wav=337nm is used
        #c = 21.3070107
    elif wav==420:
        c = 21.7899000
    elif wav==473:
        c = 21.9527283
    else:
        print "ERROR: Incorrect value submitted for wavelength. Should be in nm."
        print "Exiting..."
        sys.exit(1)
    print "INFO: Wavelength is "+str(wav)+"nm. Speed of light in water = "+str(c)+"cm/ns"
    return c
