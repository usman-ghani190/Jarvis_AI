import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
import openai
import random


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.speak(text)


def extract_website_names(query):
    websites = []
    query = query.lower()
    open_index = query.find("open")
    if open_index != -1:
        website_string = query[open_index + len("open"):].strip()
        words = website_string.split()
        website_name = " ".join(words)
        websites.append(website_name)
    return websites


def write_to_file(content, filename):
    with open(filename, 'w') as f:
        f.write(content)


def stop_listening():
    global keep_listening
    say("stopping listening. Processing your request")
    keep_listening = False


chatStr = ""


def chat(query):
    openai.api_key = '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'
    global chatStr
    chatStr += f"Usman: {query}\nJarvis: "
    print(chatStr)
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        max_tokens=256
    )
    # print(response.choices[0].text)
    say(response.choices[0].text)
    chatStr += f"{response.choices[0].text}\n"
    return response.choices[0].text


def ai(prompt):
    openai.api_key = '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'
    text = f"OpenAI response for prompt: {prompt} \n *****************************\n\n"

    # prompt = query.lower().split("generate", 1)[-1].strip()
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=256
    )
    print(response.choices[0].text)
    text += response.choices[0].text
    if not os.path.exists("openai"):
        os.mkdir("openai")
    with open(f"openai\\prompt-{random.randint(1, 12312)}.txt", "w") as f:
        f.write(text)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 1500
        print("Recognizing...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-IN")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some error occurred!"


if __name__ == '__main__':
    say("Hello I am Jarvis AI, how can I assist you?")
    while True:
        print("Listening...")
        query = takecommand()

        if "open music" in query.lower():
            os.system(r"C:\Users\GHANI\Downloads\Music\2.mp3")

        elif "time" in query.lower():
            cur_time = datetime.datetime.now().strftime("%I:%M %p")
            say(f"the time is {cur_time}")

        elif "stop" in query.lower():
            stop_listening()

        elif "generate".lower() in query.lower():
            ai(prompt=query)

        elif "quit".lower() in query.lower():
            exit()

        elif "reset".lower() in query.lower():
            chatStr = ""
        else:
            sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                     ["facebook", "https://www.facebook.com"], ["google", "https://www.google.com"],
                     ["whatsapp", "https://www.whatsapp.com"]]
            found_sites = False
            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                    say(f"opening {site[0]} sir")
                    webbrowser.open(site[1])
                    found_sites = True
                    break

            if not found_sites:
                websites = extract_website_names(query)
                for website in websites:
                    formatted_url = f"https://{website}.com"
                    print(f"opening {formatted_url} sir")
                    try:
                        webbrowser.open(formatted_url)
                        found_sites = True
                        break
                    except Exception as e:
                        print(f"Error opening {formatted_url}: {e}")

            if not found_sites:
                print("entering chat mode...")
                chat(query)
