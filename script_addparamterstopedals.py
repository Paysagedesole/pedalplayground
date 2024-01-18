from json import load,dump
import webbrowser
import keyboard


        

def openInExplorer(Brand, Name):
    print(f"{Brand}  {Name}")
googleSearchLink = "https://www.google.com/search?q="
with open("D:/PedalPlayground/pedalplayground/public/data/newPedals.json") as f:
    data = load(f)
 
index = 0;
newData = data

for pedal in newData:
    Brand = pedal["Brand"]
    Model = pedal["Name"]
    #pedal["PARAETER"] = "" 
    pedal["Instrument"] = "Any" 
    print(f"{Brand},{Model}")
    newData[index-1]=pedal
    index = index + 1

newFile = open("D:/PedalPlayground/pedalplayground/public/data/newPedals.json","w")
#dump(newData,newFile,indent=4)
newFile.close()