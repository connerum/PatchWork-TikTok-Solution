import pyttsx3
engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 185)


"""VOLUME"""
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume',1.0)

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
print(voices)
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male



"""Running"""
text = "This is a Text-to-Speech test String!"
engine.say(text)
engine.runAndWait()
engine.stop()

