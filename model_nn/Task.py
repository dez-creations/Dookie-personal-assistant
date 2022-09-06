from datetime import datetime
import webbrowser
from Speak import Say

def Time():
    time = datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

def google(query):
    webbrowser.open("https://www.google.com/search?q=" + "query")

def InputExecution(query):
    query = str(query)

    if "google" in query:
        query = query.removeprefix("google")
        google(query=query)