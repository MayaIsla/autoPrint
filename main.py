import os
import re
import subprocess

directoryLine = 'clean.txt'

defaultPrinter = subprocess.check_output("wmic printer get name,default", stderr=subprocess.STDOUT, shell=True)

strDefaultPrinter = (str(defaultPrinter))

partExt = strDefaultPrinter.partition('TRUE')
extDefaultPrinter = partExt[2]
printerDefault = extDefaultPrinter.partition('         ')

actualExtractedPrinter = printerDefault[0]
noWhiteSpace = actualExtractedPrinter.partition('     ')

extractedPrinter = noWhiteSpace[2]
actualPrinterWork = extractedPrinter.replace(" ", "")
#print(actualPrinterWork)

# printPrinter = subprocess.call('notepad.exe /p' + directoryLine)

printDir = subprocess.call('print ' + directoryLine + '/D:' + actualPrinterWork, stderr=subprocess.STDOUT, shell=False)
