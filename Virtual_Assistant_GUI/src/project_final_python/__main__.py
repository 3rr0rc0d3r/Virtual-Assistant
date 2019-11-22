import speech_recognition as sr
import time
import os

r = sr.Recognizer()
m = sr.Microphone()

#try:
    
with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))
while True:
    print("Say something, user.")
	
    with m as source: audio = r.listen(source)
    #print("Audio captured... ")
    #time.sleep(1)
    #print("Matching with dictionaries...")
    #time.sleep(1)
    #print("Recognizing..")
    #time.sleep(1)
    try:
        # recognize speech using Google Speech Recognition
        value = r.recognize_google(audio)

        # we need some special handling here to correctly print unicode characters to standard output
        if str is bytes:  # this version of Python uses bytes for strings (Python 2)
            print(u"You said {}".format(value).encode("utf-8"))
        else:  # this version of Python uses unicode for strings (Python 3+)
            print("You said {}".format(value))
    except sr.UnknownValueError:
        print("Oops! Didn't catch that. Say again!")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
	  
    #except KeyboardInterrupt:
	#break
        #pass

    if value=='open browser' or value=='open search':
	os.system('espeak "opening browser"')
        os.system('nohup chromium google.co.in')
	value=0
	
    

    if value=='open Facebook':
	os.system('espeak "opening facebook"')
        os.system('nohup chromium facebook.com')
	value=0

    if value=='open YouTube':
	os.system('espeak "opening youtube"')
        os.system('nohup chromium youtube.com')
	value=0

   


    if value=='hello assistant':
	os.system('echo "Hello, User!"')
        os.system('espeak "hello user" -p 25 -s 150')
	value=0
	
    
    if value=='tell me about you' or value=="okay tell me about you" or value=="ok tell me about you":
	os.system('espeak "I am a Virtual Assistant. I can do tasks for you"')
        os.system('espeak " I am a virtual assistant. I can do tasks for you" -p 25 -s 150')
	value=0

    if value=='thank you assistant' or value=='thank you':
	os.system('echo "You are welcome!"')
        os.system('espeak "you are welcome user" -p 25 -s 150')
	value=0

    
    if value=='goodbye' or value=="turn off" or value=="goodbye" or value=="goodbye assistant":
	os.system('clear')
	os.system('echo "Good bye. Have a great day!"')
        os.system('espeak "Good bye have a great day" -p 25 -s 150')
	value=0
	time.sleep(1)
	os.system('pkill gnome-terminal')

  

    if value=='open file manager':
	os.system('espeak "opening file manager"')
        os.system('dolphin')
	value=0
	
    if value=='open skype':
        os.system('skype')

    if value=='close browser':
        os.system('pkill chromium')

    if value=="show today's date" or value=="show date" or value=="display date":
	os.system('clear')
        os.system('date')
	value=0

    if value=="show calendar" or value=='display calendar':
        os.system('cal')
	value=0

   

    if value=='present location' or value=='show present location' or value=='display present location':
        os.system('pwd')
	value=0

    
    if value=='show processes' or value=='display processes':
	os.system('espeak "Okay"')
        os.system('top')
	value=0
