import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

from googletrans import Translator

class translate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def translate(self, ctx, *text):
        try:
            inputText = ""
            for i in range(0,len(text)):
                if(i==0):
                    inputText = text[i]
                else:
                    inputText = inputText + " " + text[i]

            translator = Translator()
            translation = translator.translate(inputText)
            inputLang = translation.src
            outputText = translation.text

            if(inputLang == "af"):
                inputLang = "Afrikaans"
            elif(inputLang == "sq"):
                inputLang = "Albanian"
            elif(inputLang == "ar"):
                inputLang = "Arabic"
            elif(inputLang == "eu"):
                inputLang = "Basque"
            elif(inputLang == "be"):
                inputLang = "Belarusian"
            elif(inputLang == "bg"):
                inputLang = "Bulgarian"
            elif(inputLang == "ca"):
                inputLang = "Catalan"
            elif(inputLang == "zh"):
                inputLang = "Chinese"
            elif(inputLang == "hr"):
                inputLang = "Croatian"
            elif(inputLang == "cs"):
                inputLang = "Czech"
            elif(inputLang == "da"):
                inputLang = "Danish"
            elif(inputLang == "nl"):
                inputLang = "Dutch"
            elif(inputLang == "en"):
                inputLang = "English"
            elif(inputLang == "et"):
                inputLang = "Estonian"
            elif(inputLang == "fo"):
                inputLang = "Faeroese"
            elif(inputLang == "fa"):
                inputLang = "Farsi"
            elif(inputLang == "fi"):
                inputLang = "Finnish"
            elif(inputLang == "fr"):
                inputLang = "French"
            elif(inputLang == "gd"):
                inputLang = "Gaelic"
            elif(inputLang == "de"):
                inputLang = "German"
            elif(inputLang == "el"):
                inputLang = "Greek"
            elif(inputLang == "he"):
                inputLang = "Hebrew"
            elif(inputLang == "hi"):
                inputLang = "Hindi"
            elif(inputLang == "hu"):
                inputLang = "Hungarian"
            elif(inputLang == "is"):
                inputLang = "Islandic"
            elif(inputLang == "id"):
                inputLang = "Indonesian"
            elif(inputLang == "ga"):
                inputLang = "Irish"
            elif(inputLang == "it"):
                inputLang = "Italian"
            elif(inputLang == "ja"):
                inputLang = "Japanese"
            elif(inputLang == "ko"):
                inputLang = "Korean"
            elif(inputLang == "ku"):
                inputLang = "Kurdish"
            elif(inputLang == "lv"):
                inputLang = "Latvian"
            elif(inputLang == "lt"):
                inputLang = "Lithuanian"
            elif(inputLang == "mk"):
                inputLang = "Macedonian"
            elif(inputLang == "ml"):
                inputLang = "Malayalam"
            elif(inputLang == "ms"):
                inputLang = "Malaysian"
            elif(inputLang == "mt"):
                inputLang = "Maltese"
            elif(inputLang == "no"):
                inputLang = "Norwegian"
            elif(inputLang == "pl"):
                inputLang = "Polish"
            elif(inputLang == "pt"):
                inputLang = "Portugese"
            elif(inputLang == "pa"):
                inputLang = "Punjabi"
            elif(inputLang == "rm"):
                inputLang = "Rhaeto-Romanic"
            elif(inputLang == "ro"):
                inputLang = "Romanian"
            elif(inputLang == "ru"):
                inputLang = "Russian"
            elif(inputLang == "sr"):
                inputLang = "Serbian"
            elif(inputLang == "sk"):
                inputLang = "Slovak"
            elif(inputLang == "sl"):
                inputLang = "Slovenian"
            elif(inputLang == "sb"):
                inputLang = "Sorbian"
            elif(inputLang == "es"):
                inputLang = "Spanish"
            elif(inputLang == "sv"):
                inputLang = "Swedish"
            elif(inputLang == "th"):
                inputLang = "Thai"
            elif(inputLang == "ts"):
                inputLang = "Tsonga"
            elif(inputLang == "tn"):
                inputLang = "Tswana"
            elif(inputLang == "tr"):
                inputLang = "Turkish"
            elif(inputLang == "uk"):
                inputLang = "Ukranian"
            elif(inputLang == "ur"):
                inputLang = "Urdu"
            elif(inputLang == "ve"):
                inputLang = "Venda"
            elif(inputLang == "vi"):
                inputLang = "Vietnamese"
            elif(inputLang == "cy"):
                inputLang = "Welsh"
            elif(inputLang == "xh"):
                inputLang = "Xhosa"
            elif(inputLang == "ji"):
                inputLang = "Yiddish"
            elif(inputLang == "zu"):
                inputLang = "Zulu"

            mes = "Input Language: %s\nTranslated Text: %s"%(inputLang,outputText)
            await ctx.message.channel.send(mes)
        except:
            await ctx.message.channel.send("Translate is temporarily unavailable.")

    @commands.command()
    async def translateTo(self, ctx, destination,*text):
        try:
            inputText = ""
            for i in range(0,len(text)):
                if(i==0):
                    inputText = text[i]
                else:
                    inputText = inputText + " " + text[i]

            translator = Translator()
            translation = translator.translate(inputText, dest = destination)
            inputLang = translation.src
            outputText = translation.text

            if(inputLang == "af"):
                inputLang = "Afrikaans"
            elif(inputLang == "sq"):
                inputLang = "Albanian"
            elif(inputLang == "ar"):
                inputLang = "Arabic"
            elif(inputLang == "eu"):
                inputLang = "Basque"
            elif(inputLang == "be"):
                inputLang = "Belarusian"
            elif(inputLang == "bg"):
                inputLang = "Bulgarian"
            elif(inputLang == "ca"):
                inputLang = "Catalan"
            elif(inputLang == "zh"):
                inputLang = "Chinese"
            elif(inputLang == "hr"):
                inputLang = "Croatian"
            elif(inputLang == "cs"):
                inputLang = "Czech"
            elif(inputLang == "da"):
                inputLang = "Danish"
            elif(inputLang == "nl"):
                inputLang = "Dutch"
            elif(inputLang == "en"):
                inputLang = "English"
            elif(inputLang == "et"):
                inputLang = "Estonian"
            elif(inputLang == "fo"):
                inputLang = "Faeroese"
            elif(inputLang == "fa"):
                inputLang = "Farsi"
            elif(inputLang == "fi"):
                inputLang = "Finnish"
            elif(inputLang == "fr"):
                inputLang = "French"
            elif(inputLang == "gd"):
                inputLang = "Gaelic"
            elif(inputLang == "de"):
                inputLang = "German"
            elif(inputLang == "el"):
                inputLang = "Greek"
            elif(inputLang == "he"):
                inputLang = "Hebrew"
            elif(inputLang == "hi"):
                inputLang = "Hindi"
            elif(inputLang == "hu"):
                inputLang = "Hungarian"
            elif(inputLang == "is"):
                inputLang = "Islandic"
            elif(inputLang == "id"):
                inputLang = "Indonesian"
            elif(inputLang == "ga"):
                inputLang = "Irish"
            elif(inputLang == "it"):
                inputLang = "Italian"
            elif(inputLang == "ja"):
                inputLang = "Japanese"
            elif(inputLang == "ko"):
                inputLang = "Korean"
            elif(inputLang == "ku"):
                inputLang = "Kurdish"
            elif(inputLang == "lv"):
                inputLang = "Latvian"
            elif(inputLang == "lt"):
                inputLang = "Lithuanian"
            elif(inputLang == "mk"):
                inputLang = "Macedonian"
            elif(inputLang == "ml"):
                inputLang = "Malayalam"
            elif(inputLang == "ms"):
                inputLang = "Malaysian"
            elif(inputLang == "mt"):
                inputLang = "Maltese"
            elif(inputLang == "no"):
                inputLang = "Norwegian"
            elif(inputLang == "pl"):
                inputLang = "Polish"
            elif(inputLang == "pt"):
                inputLang = "Portugese"
            elif(inputLang == "pa"):
                inputLang = "Punjabi"
            elif(inputLang == "rm"):
                inputLang = "Rhaeto-Romanic"
            elif(inputLang == "ro"):
                inputLang = "Romanian"
            elif(inputLang == "ru"):
                inputLang = "Russian"
            elif(inputLang == "sr"):
                inputLang = "Serbian"
            elif(inputLang == "sk"):
                inputLang = "Slovak"
            elif(inputLang == "sl"):
                inputLang = "Slovenian"
            elif(inputLang == "sb"):
                inputLang = "Sorbian"
            elif(inputLang == "es"):
                inputLang = "Spanish"
            elif(inputLang == "sv"):
                inputLang = "Swedish"
            elif(inputLang == "th"):
                inputLang = "Thai"
            elif(inputLang == "ts"):
                inputLang = "Tsonga"
            elif(inputLang == "tn"):
                inputLang = "Tswana"
            elif(inputLang == "tr"):
                inputLang = "Turkish"
            elif(inputLang == "uk"):
                inputLang = "Ukranian"
            elif(inputLang == "ur"):
                inputLang = "Urdu"
            elif(inputLang == "ve"):
                inputLang = "Venda"
            elif(inputLang == "vi"):
                inputLang = "Vietnamese"
            elif(inputLang == "cy"):
                inputLang = "Welsh"
            elif(inputLang == "xh"):
                inputLang = "Xhosa"
            elif(inputLang == "ji"):
                inputLang = "Yiddish"
            elif(inputLang == "zu"):
                inputLang = "Zulu"

            mes = "Input Language: %s\nTranslated Text: %s"%(inputLang,outputText)
            await ctx.message.channel.send(mes)
        except ValueError:
            await ctx.message.channel.send("Invalid ISO 639-1 code.")
        except:
            await ctx.message.channel.send("Translate is temporarily unavailable.")

def setup(client):
    client.add_cog(translate(client))
