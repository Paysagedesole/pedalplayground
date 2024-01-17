from json import load,dump
import webbrowser
def openInExplorer(Brand, Name):
    print(f"{Brand}  {Name}")
googleSearchLink = "https://www.google.com/search?q="
with open("C:/Users/avegh/Documents/GitHub/pedalplayground/public/data/pedals.json") as f:
    data = load(f)

for pedal in data:
    Brand = pedal["Brand"]
    Model = pedal["Name"]
    pedal["Type"] = ""
    pedal["Style"] = ""
    pedal["Price"] = ""
    print(pedal)
newFile = open("C:/Users/avegh/Documents/GitHub/pedalplayground/public/data/newPedals.json","w")
dump(pedal,newFile,indent=4)
newFile.close()
    #webbrowser.open(f"{googleSearchLink}{Brand}+{Model}")