#!/usr/bin/python3.8
print("bitte datei eingeben wo '\\r' entfernt werden soll!")
fileName=input("Dateiname: ")

print("öffne datei... und lese...")
readFile=open(fileName,"rb")
fileData=readFile.read()
readFile.close()

print("ersetze lösche windows müll!")
fileLengthBefore=len(fileData)
fileData=fileData.replace(b"\r",b"")
fileLengthAfter=len(fileData)

print("schliesse datei und speichere...")
writeFile=open(fileName,"wb")
writeFile.write(fileData)
writeFile.close()

print("\nalte datei: "+str(fileLengthBefore)+" bytes")
print("neue datei: "+str(fileLengthAfter)+" bytes")
print("aus datei gelöscht: "+str(fileLengthBefore-fileLengthAfter)+" Bytes")