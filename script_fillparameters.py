from json import load,dump
import webbrowser
import keyboard


        

def openInExplorer(Brand, Name):
    print(f"{Brand}  {Name}")
googleSearchLink = "https://www.google.com/search?q="
with open("D:/PedalPlayground/pedalplayground/public/data/pedals.json") as f:
    data = load(f)
 
index = 0;
newData = data


        
previousBrand = ""
nextBrandToCheck ="Aguilar"
shouldOpenSearch = False
for pedal in newData:
    Brand = pedal["Brand"]
    Model = pedal["Name"]
    print(f"{Brand},{Model}")
    newData[index-1]=pedal
    ++index

    if nextBrandToCheck == Brand:
        shouldOpenSearch = True;
    if shouldOpenSearch:
        if previousBrand != Brand:
            print ("NEXT BRAND ")
            previousBrand = Brand
            while True:
                print(keyboard.read_event())
                if keyboard.read_key() == "²":
                    break

        webbrowser.open(f"{googleSearchLink}{Brand}+{Model}")
