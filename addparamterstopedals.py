from json import load,dump
import webbrowser
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
    pedal["Type"] = ""
    pedal["Style"] = ""
    pedal["Price"] = ""
    print(f"{Brand},{Model}")
    newData[index-1]=pedal
    ++index

newFile = open("C:/Users/avegh/Documents/GitHub/pedalplayground/public/data/newPedals.json","w")
dump(newData,newFile,indent=4)
newFile.close()
    #webbrowser.open(f"{googleSearchLink}{Brand}+{Model}")