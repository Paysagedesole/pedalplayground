from json import load,dump
import webbrowser
from script_testMistralAi import FindPedalTypeAndPrice

        

def openInExplorer(Brand, Name):
    print(f"{Brand}  {Name}")
googleSearchLink = "https://www.google.com/search?q="
with open("C:/Users/avegh/Documents/GitHub/pedalplayground/public/data/pedals.json") as f:
    data = load(f)
 
index = 0;
newData = data

for pedal in newData:
    Brand = pedal["Brand"]
    Model = pedal["Name"]
    #pedal["PARAMETER"] = "" 
    pedalInfos = FindPedalTypeAndPrice(f"{Brand} {Model}")
    pedal["Type"] = pedalInfos[0]
    pedal["Price"] = pedalInfos [1]
    print(f"{Brand},{Model},type : {pedalInfos[0]}; price : {pedalInfos [1]}")
    newData[index-1]=pedal
    
    newFile = open("C:/Users/avegh/Documents/GitHub/pedalplayground/public/data/newPedals.json","w")
    dump(newData,newFile,indent=4)
    newFile.close()