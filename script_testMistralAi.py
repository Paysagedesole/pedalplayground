from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os
import requests
from currency_converter import CurrencyConverter
from rapidfuzz import process,fuzz





def FindPedalTypeAndPrice(pedal):

    #region Google Search Engine
    CUSTOM_SEARCH_API_KEY = "AIzaSyAeSXhKpLYcExgiD3Mk2FY_OVOe2OvinFg"
    SEARCH_ENGINE_ID = "714738adff197437a"
    currencyConverter = CurrencyConverter()
    query = pedal
    page = 1
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={CUSTOM_SEARCH_API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
    data = requests.get(url).json()
    allPedalDescriptions = ""
    allPedalPrices = []
    search_items = data.get("items")
    # iterate over 10 results found
    if search_items != None:
        print("--------------------------------------------------new search result")
        for i, search_item in enumerate(search_items, start=1):
            try:
                long_description = search_item["pagemap"]["metatags"][0]["og:description"]
            except KeyError:
                long_description = "N/A"
            try:
                price = search_item["pagemap"]["offer"][0]["price"]
            except KeyError:
                price = "N/A"
            try:
                currency = search_item["pagemap"]["offer"][0]["pricecurrency"]
            except:
                currency = "N/A"

            allPedalDescriptions = allPedalDescriptions+long_description
            if price!="N/A" and currency!="N/A":
                price = currencyConverter.convert(price, currency,'USD')
                allPedalPrices.append(price)


        #endregion
        #region Mistral Ai API
        MISTRAL_AI_API_KEY = "AAjqaRK1gz6mJ0CYW2EQhh0fbkzJHjSI"
        model = "mistral-tiny"

        client = MistralClient(api_key=MISTRAL_AI_API_KEY)
        types = ["distortion","overdrive","fuzz","bitcrusher","preamp","D.I.","envelope filter","wah","reverb","delay","looper","sequencer","equalizer","compressor","chorus","flanger","phaser","synth","multi-effect","unknown"]
        pedalToCheck="KMA Machines Queequeg"
        try:
            chat_response = client.chat(
                    model=model,
                    temperature=0.1,
                    #messages=[ChatMessage(role="user", content=f"""Tell me what type of pedal is the {pedalToCheck}? You can choose between these type of effects : {types}. 
                    #                     It is very important that your answer is only one word long. You do not have the right to answer me with more than one word.
                    #                    WRITE ONLY ONE WORD!!!!!!
                    #                   You can select "unknown" if you do not have a better answer.""")],
                    messages=[ChatMessage(role="user", content=f"""Read the following content : {allPedalDescriptions}. 
                                        It speaks about a pedal. I need to know what type of pedal it is. 
                                        You can pick between these types : {types}
                                        You can only answer with one word.
                                        It is very important that your answer contains only one word.""")]
                )
        except:
            return "N/A","N/A"
        #endregion
        #region return

        type = chat_response.choices[0].message.content
        type = process.extractOne(type, types, scorer=fuzz.WRatio)[0]
        if price!="N/A" and currency!="N/A": 
            pedalPrice = round(sum(allPedalPrices)/len(allPedalPrices),0)
        else:
            pedalPrice ="N/A"

        return type,pedalPrice
    return "N/A","N/A"
    #endregion
