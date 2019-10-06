#!/usr/bin/env python3
#
# ------------------------------------------------------------------------------
#
# Antenna Analysis
#
#
# This program uses the Real/Imaginary *.s1p output of a vector network analyzer
# to calculate VSWR over the LF, MF, HF, and 6m bands. It's helpful to feed it
# a many-point input from ~0.1 MHz to ~60 MHz, though you can of course focus
# on just the band you care about.
#
# For testing the tuning bands, I used an MFJ-945E with both the Tramsitter and
# Antenna to '5' (center for each) and recorded the S11 spectra on Bypass, then
# each of the inductances A-L and put them in the same folder as this code.
#
# The *.s1p files should be saved as "antennaName Tuner Bypass.s1p" and
# "antennaName Tuner A 5-5.s1p" where A is changed from A-L and antennaName is
# defined below.
#
# To record S11 spectra, I used a NanoVNA and the NanoVNA Saver software. Links
# for both are included below.
#
# NanoVNA: https://www.amazon.com/gp/product/B07T6LXNTV/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1
# NanoVNA Saver: https://github.com/mihtjel/nanovna-saver
# Software Walkthrough: https://www.rtl-sdr.com/nanovnasaver-software-walkthrough-nanovna-firmware-updates-bring-1-5-ghz-max-range/
#
# Good luck, and happy tuning!
#
# Elena Long, KC1KNI
# Oct. 6th, 2019
#
# ------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt

antennaName = "G5RV"

filenameBy = antennaName + ' Tuner Bypass.s1p'
dataBy = open(filenameBy,'r')
linesBy = dataBy.readlines()
dataBy.close()
freqBy = []
vswrBy = []
for line in linesBy:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqBy.append(freqVal)
        vswrBy.append(vswrVal)

filenameA = antennaName + ' Tuner A 5-5.s1p'
dataA = open(filenameA,'r')
linesA = dataA.readlines()
dataA.close()
freqA = []
vswrA = []
for line in linesA:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqA.append(freqVal)
        vswrA.append(vswrVal)

filenameB = antennaName + ' Tuner B 5-5.s1p'
dataB = open(filenameB,'r')
linesB = dataB.readlines()
dataB.close()
freqB = []
vswrB = []
for line in linesB:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqB.append(freqVal)
        vswrB.append(vswrVal)

filenameC = antennaName + ' Tuner C 5-5.s1p'
dataC = open(filenameC,'r')
linesC = dataC.readlines()
dataC.close()
freqC = []
vswrC = []
for line in linesC:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqC.append(freqVal)
        vswrC.append(vswrVal)

filenameD = antennaName + ' Tuner D 5-5.s1p'
dataD = open(filenameD,'r')
linesD = dataD.readlines()
dataD.close()
freqD = []
vswrD = []
for line in linesD:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqD.append(freqVal)
        vswrD.append(vswrVal)

filenameE = antennaName + ' Tuner E 5-5.s1p'
dataE = open(filenameE,'r')
linesE = dataE.readlines()
dataE.close()
freqE = []
vswrE = []
for line in linesE:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqE.append(freqVal)
        vswrE.append(vswrVal)

filenameF = antennaName + ' Tuner F 5-5.s1p'
dataF = open(filenameF,'r')
linesF = dataF.readlines()
dataF.close()
freqF = []
vswrF = []
for line in linesF:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqF.append(freqVal)
        vswrF.append(vswrVal)

filenameG = antennaName + ' Tuner G 5-5.s1p'
dataG = open(filenameG,'r')
linesG = dataG.readlines()
dataG.close()
freqG = []
vswrG = []
for line in linesG:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqG.append(freqVal)
        vswrG.append(vswrVal)

filenameH = antennaName + ' Tuner H 5-5.s1p'
dataH = open(filenameH,'r')
linesH = dataH.readlines()
dataH.close()
freqH = []
vswrH = []
for line in linesH:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqH.append(freqVal)
        vswrH.append(vswrVal)

filenameI = antennaName + ' Tuner I 5-5.s1p'
dataI = open(filenameI,'r')
linesI = dataI.readlines()
dataI.close()
freqI = []
vswrI = []
for line in linesI:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqI.append(freqVal)
        vswrI.append(vswrVal)

filenameJ = antennaName + ' Tuner J 5-5.s1p'
dataJ = open(filenameJ,'r')
linesJ = dataJ.readlines()
dataJ.close()
freqJ = []
vswrJ = []
for line in linesJ:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqJ.append(freqVal)
        vswrJ.append(vswrVal)

filenameK = antennaName + ' Tuner K 5-5.s1p'
dataK = open(filenameK,'r')
linesK = dataK.readlines()
dataK.close()
freqK = []
vswrK = []
for line in linesK:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqK.append(freqVal)
        vswrK.append(vswrVal)

filenameL = antennaName + ' Tuner L 5-5.s1p'
dataL = open(filenameL,'r')
linesL = dataL.readlines()
dataL.close()
freqL = []
vswrL = []
for line in linesL:
    p = line.split()
    if ("!" not in line) and ("#" not in line):
        freqVal = float(p[0])/1E6
        ReS11Val = float(p[1])
        ImS11Val = float(p[2])
        magS11Val = np.sqrt(ReS11Val**2 + ImS11Val**2)
        vswrVal = (1+np.sqrt(magS11Val**2))/(1-np.sqrt(magS11Val**2))
        freqL.append(freqVal)
        vswrL.append(vswrVal)



title = antennaName + " - All Bands"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(1,5)
plt.xlim(0,60)
# plt.legend()
plt.show()


title = antennaName + " - 2,200m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(0,5)
plt.xlim(135.7,137.8)
plt.legend()
plt.show()

title = antennaName + " - 630m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(0,5)
plt.xlim(472,479)
plt.legend()
plt.show()

title = antennaName + " - 160m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(1,5)
plt.xlim(1.8,2.0)
plt.legend()
plt.show()

title = antennaName + " - 80m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(1,5)
plt.xlim(3.5,4.0)
plt.legend()
plt.show()

title = antennaName + " - 40m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(1,5)
plt.xlim(7.0,7.3)
plt.legend()
plt.show()

title = antennaName + " - 30m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(1,5)
plt.xlim(10.1,10.15)
plt.legend()
plt.show()

title = antennaName + " - 20m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(1,5)
plt.xlim(14.0,14.35)
plt.legend()
plt.show()

title = antennaName + " - 17m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(1,5)
plt.xlim(18.068,18.168)
plt.legend()
plt.show()

title = antennaName + " - 15m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(1,5)
plt.xlim(21.0,21.45)
plt.legend()
plt.show()

title = antennaName + " - 12m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(1,5)
plt.xlim(24.89,24.99)
plt.legend()
plt.show()


title = antennaName + " - 10m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(1,5)
plt.xlim(28.0,29.7)
plt.legend()
plt.show()

title = antennaName + " - 6m"
plt.title(title)
plt.plot(np.array(freqBy),np.array(vswrBy), label="Bypass")
plt.plot(np.array(freqA),np.array(vswrA), label="A 5-5")
plt.plot(np.array(freqB),np.array(vswrB), label="B 5-5")
plt.plot(np.array(freqC),np.array(vswrC), label="C 5-5")
plt.plot(np.array(freqD),np.array(vswrD), label="D 5-5")
plt.plot(np.array(freqE),np.array(vswrE), label="E 5-5")
plt.plot(np.array(freqF),np.array(vswrF), label="F 5-5")
plt.plot(np.array(freqG),np.array(vswrG), label="G 5-5")
plt.plot(np.array(freqH),np.array(vswrH), label="H 5-5")
plt.plot(np.array(freqI),np.array(vswrI), label="I 5-5")
plt.plot(np.array(freqJ),np.array(vswrJ), label="J 5-5")
plt.plot(np.array(freqK),np.array(vswrK), label="K 5-5")
plt.plot(np.array(freqL),np.array(vswrL), label="L 5-5")
plt.xlabel("Frequency (MHz)")
plt.ylabel("VSWR")
plt.ylim(1,5)
plt.xlim(50.0,54.0)
plt.legend()
plt.show()
