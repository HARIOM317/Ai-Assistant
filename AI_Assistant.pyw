# Import useful packages
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import time
import random
from tkinter import *
from threading import *
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
import requests
from bs4 import BeautifulSoup
from tkinter import colorchooser, messagebox
from pywikihow import search_wikihow
import subprocess


from gui_automation import GuiAuto
# Make instance of class GuiAuto
Gcurser = GuiAuto()     # for more pixels in GUI

# Initialize engine of pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Predefined English Jokes
english_jokes = [
    "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why don't scientists trust atoms? Because they make up everything!",
    'How do you organize a space party? You "planet"!',
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why couldn't the bicycle stand up by itself? Because it was two-tired!",
    "I'm on a seafood diet. I see food, and I eat it.",
    "Did you hear about the claustrophobic astronaut? He just needed a little space.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
    "Why couldn't the bicycle stand up by itself? Because it was two-tired!",
    'What do you call a fake noodle? An "impasta"!',
    "I used to play piano by ear, but now I use my hands.",
    "How does a penguin build its house? Igloos it together!",
    "Did you hear about the claustrophobic astronaut? He just needed a little space.",
    "What's orange and sounds like a parrot? A carrot!",
    'What do you call a pile of cats? A "meowtain"!',
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Why don't some couples go to the gym? Because some relationships don't work out!",
    'What do you call a bear with no teeth? A "gummy" bear!',
    "Why don't eggs tell jokes? Because they might crack up!",
    "What's brown and sticky? A stick!",
    "Did you hear about the kidnapping at the park? They woke up!",
    "I have a joke about construction, but I'm still working on it.",
    "What's the best time to go to the dentist? Tooth-hurty!"
  ]

# Predefined Hindi Jokes
hindiJokes = [
    '''पप्पु: मुझे सोने का बहुत शौक है।
मुन्ना: क्या यार, अबी तो तू सुबह उठा है!''',
    '''टीचर: तुम्हारे पिताजी क्या काम करते हैं?
स्टूडेंट: जी, वो रोज़ रात को सोते हैं।''',
    '''एक आदमी अपने दोस्त से: क्या तुमने कभी तुम्हारी बीवी को सच्ची मोहब्बत करने के लिए खोल कर बात की है?
दोस्त: हां, लेकिन तब जब तक खाने की तबलेट की तबियत ख़राब न हो।''',
    '''स्कूल के दिनों में टीचर: तुम इतने दिनों से कहां थे?
छात्र: गुरुजी, नींद में।''',
    '''एक आदमी डॉक्टर से: मेरी आंख में दर्द हो रहा है, ज़रा देखिए।
डॉक्टर: बहुत दिन हो गए, मान लो बिना दर्द के रहो।''',
    '''बच्चा: आपकी शादी कैसे हुई, नानी?
नानी: लड़का पहली बार मुझसे मिला, तो बोला, "नमस्ते दादी!"''',
    '''टीचर: तुम्हारे पिताजी क्या काम करते हैं?
स्टूडेंट: वो रोज़ बिना काम करते हैं, फिर भी मना करते हैं कि वो आराम कर रहे हैं।''',
    '''लड़का: आप मुझसे शादी करोगी?
लड़की: क्या तुम रोमांटिक हो?
लड़का: हां, ज़रूर, जब मेरा मोबाइल बैटरी लो तो मैं इसे करने की कोशिश करता हूँ।''',
    '''पप्पु: मुझे सोने का बहुत शौक है।
मुन्ना: क्या यार, अबी तो तू सुबह उठा है!''',
    '''टीचर: तुम अपनी किताब क्यों नहीं खोलते?
छात्र: मैंने ज़रा से हिन्दी की किताब खोल ली थी, तो पूरी कक्षा की बंद आँखों की दीदी देख रही थी।''',
    '''टीचर: तुमने पेपर में सबसे अच्छा नाम लिखा है।
स्टूडेंट: आपका भी तो नहीं लिखा, मैम।''',
    '''पप्पु: यार, तू अपनी गर्लफ़्रेंड के साथ बाहर घूमने जा रहा है?
मुन्ना: हां यार, उसने मुझसे कहा है कि उसका ख़र्चा जो खर्च हो जाएगा, वो वापस नहीं मांगेगी।''',
    '''एक आदमी बर्ड संकेतक दुकान में गया और बोला, "जिसमें मिलते ही नहीं, उसे दिखा दो।"''',
    '''टीचर: बच्चों, हमने बहुत सारे चूहे मार डाले। तुम मुझे बताओगे, वे सब कहां गए?
छात्र: मैम, वो सब बिल्कुल ठिक हैं, बहुत सारे मिलकर पिज्जा खा रहे हैं।''',
    '''टीचर: तुम लोगों की प्रतिभा की वजह से ही हम सब यहाँ हैं।
स्टूडेंट: वक़्त थोड़ा और देने का, जी।''',
    '''टीचर: तुम ने वादा किया था कि आज कक्षा समय पर पहुँचोगे।
स्टूडेंट: मैम, मैंने तो बस ख़बरदारी की थी, आपने तो उस पर यक़ीन किया।''',
    '''एक आदमी डॉक्टर से: मुझे ख़राब होने की तय्यारी करने के लिए कितने पैसे चाहिए?
डॉक्टर: 1000 रुपये।
आदमी: ठीक है, मुझे 1000 की जगह ख़राब करने की तय्यारी कर दो।''',
    '''एक आदमी अपने दोस्त से: मैं रात को अपनी बीवी से लड़ता रहता हूँ।
दोस्त: वो कैसे?
आदमी: मैं सोते समय अपनी बीवी की तरफ़ मुँह ज़बरदस्ती फ़ेल देता हूँ।''',
    '''टीचर: अगर कोई घर पर तोड़ दे, तो उसका क्या करोगे?
छात्र: उसकी बिल दुगना कर देंगे।''',
    '''संता: क्या तुम मेरे लिए कुछ ख़ास बना सकती हो?
प्रियंका: हां, आज रात को बिना माँ के बिना सुलाऊंगी।''',
    '''ज़ख़्मी सांप अपनी माँ के पास गया और बोला, "माँ, मुझे डॉक्टर के पास ले जाने की बजाय, तुमने मुझे पंडित के पास क्यों ले जाया?"''',
    '''टीचर: तुमने अपने बच्चों के नाम क्यों इतने अजीब रखे हैं?
माँ: ताकि वो बिना बुलाए ही स्कूल आ सकें।''',
    '''संता: बेटा, तुम्हारे पिताजी क्या काम करते हैं?
बेटा: वो बस रोज़ दोपहर को रात के बराबर सोते हैं।''',
    '''संता: बेटा, तुम्हारी शादी कैसे हुई?
बेटा: जी, पहली बार मैं जब भी उसके पास जाता था, तो वो बोलती थी, "नमस्ते जी!"''',
    '''पप्पु: यार, तुझे अपनी गर्लफ़्रेंड के साथ बाहर घूमने जाने में कितनी पर्याप्त धनराशि लगेगी, बता?
मुन्ना: क्या यार, उसने कहा है कि जो ख़र्चा हो जाएगा, वो वापस नहीं मांगेगी।''',
    '''टीचर: तुम्हारे बच्चों का बहुत अच्छा नाम है।
माँ: हां, पर आपके लिए वक़्त नहीं बचा, बिलकुल ठिक है।''',
    '''संता: क्या तुम मेरे लिए कुछ ख़ास बना सकती हो?
प्रियंका: हां, आज रात को बिना माँ के बिना सुलाऊंगी।''',
    '''ज़हरीला सांप: मुझे डॉक्टर के पास ले जाने की बजाय तुमने मुझे पंडित के पास क्यों ले जाया?
ज़ख़्मी सांप: क्योंकि ज़हरीले सांप भी पंडित जी के यहाँ ही जाते हैं।''',
    '''टीचर: तुमने अपने बच्चों के नाम क्यों इतने अजीब रखे हैं?
माँ: ताकि वो बिना बुलाए ही स्कूल आ सकें।''',
    '''संता: बेटा, तुम्हारी शादी कैसे हुई?
बेटा: जी, पहली बार मैं जब भी उसके पास जाता था, तो वो बोलती थी, "नमस्ते जी!"''',
    '''पप्पु: यार, तुझे अपनी गर्लफ़्रेंड के साथ बाहर घूमने जाने में कितनी पर्याप्त धनराशि लगेगी, बता?
मुन्ना: क्या यार, उसने कहा है कि जो ख़र्चा हो जाएगा, वो वापस नहीं मांगेगी।''',
    '''पप्पू अपनी पत्नी से-
अच्छा ये बताओ 'बिदाई' के समय तुम 
लड़कियां इतनी रोती क्यों हो?
पत्नी- 'पागल' अगर तुझे पता चले...
अपने घर से दूर ले जाकर कोई तुमसे 
'बर्तन मंजवाएगा' तो तू क्या नाचेगा...''',
    '''बैंक की cashier ने खिड़की पर खड़े आदमी को कहा 'पैसे नहीं है'
ग्राहक: और दो मोदी माल्या को पैसा, सारे पैसे लेकर भाग गए विदेश में
कैशियर ने खिड़की में से हाथ निकाला और उसकी गर्दन दबोच कर कहा 'साले बैंक में तो है तेरे खाते में नहीं है' भिखारी''',
    '''जज : घर में मालिक होते हुए तूने चोरी कैसे की?
चोर : साहब, आपकी नौकरी अच्छी है, और सैलरी 
भी अच्छी है, फिर आप ये सब सीख कर क्या करोगे?''',
    '''पब्लिक टॉयलेट में लिखा था
'दुनिया चांद पर पहुंच गयी
और तू यहीं पर बैठा है'
पप्पू ने अपना दिमाग लगाया 
और नीचे लिखा
'चांद पर पानी नहीं था
इसलिए वापस आ गया''',
    '''पति- प्यास लगी है पानी लेके आओ..
पत्नी- क्यों ना आज तुम्हें मटर पनीर 
और शाही पुलाव बनाकर खिलाऊं...
पति- वाह वाह...! 
मुंह में पानी आ गया..
पत्नी- आ गया ना मुंह में पानी 
बस इसी से काम चला लो..''',
    '''टीचर- टिटू बताओ..
अकबर ने कब तक शासन किया था ?
टिटू- सर जी..
पेज नंबर 14 से लेकर पेज नंबर 22 तक..।''',
    '''गोलू- जानू, तुम दिन पर दिन 
खूबसूरत होती जा रही हो...
पत्नी (खुश होकर)- तुमने कैसे जाना ?
गोलू- तुम्हें देखकर...
रोटियां भी जलने लगी हैं''',
    '''टिल्लू (लड़की से)- मैं 18 साल का हूं और तुम ?
लड़की- मैं भी 18 साल की हूं...
टिल्लू- तो फिर चलो ना, इसमें शरमाना क्या..
लड़की- कहां ?
टिल्लू- अरे पगली..
वोट देने और कहां...''',
    '''मां- बेटा क्या कर रहे हो
पप्पू- पढ़ रहा हूं मां..
मां- शाबास! बेटा क्या पढ़ रहे हो..?
पप्पू- आपकी होने वाली बहु के SMS''',
    '''टीचर- बच्चों कोई ऐसा वाक्य सुनाओ 
जिसमें हिंदी, पंजाबी, उर्दू और अंग्रेजी का प्रयोग हो..
पप्पू- सर ..
'इश्क दी गली विच ल No entry''',
    '''पत्नी- पूजा किया कीजिए,
बड़ी बलांए टल जाती हैं...
टिटू- हां... तुम्हारे
पिताजी ने बहुत की होगी 
उनकी टल गई और मेरे पल्ले पड़ गई..।''',
    '''एक बार एक वैज्ञानिक ने 'शादी क्या होती है'
ये समझने के लिए शादी कर ली...
.
अब...
.
उसको ये समझ नहीं आ रहा कि विज्ञान क्या होता है...?''',
    '''कल एक साधू बाबा मिले,
मैंने पूछा - कैसे हैं बाबाजी...?
.
बाबाजी बोले - हम तो साधु हैं बेटा,
हमारा 'राम' हमें जैसे रखता है हम वैसे ही रहते हैं...!
तुम तो सुखी हो ना बच्चा...?
. 
मैं बोला - हम तो सांसारिक लोग हैं बाबाजी
हमारी 'सीता' हमें जैसे रखती है, हम वैसे ही रहते हैं...!''',
    '''लड़की - तुम किसी शादी-ब्याह में नाचते क्यों नहीं हो...?
.
.
लड़का - नाचती तो लड़कियां हैं,
हम तो भोले के भक्त हैं,
पी के तांडव करते हैं...!
.
लड़की बेहोश...''',
    '''पत्नी - शादी क्या है...?
.
.
पति - 'मान भी जाओ' से लेकर 'भाड़ में जाओ' तक का सफर ही शादी है...
बाकी सब तो मोह-माया है...!''',
    '''पत्नी - आपको मेरी सुंदरता ज्यादा अच्छी लगती है
या मेरे संस्कार...?
.
.
पति - मुझे तो तेरी ये मजाक करने की आदत
बहुत अच्छी लगती है...!''',
    '''एक बार एक वैज्ञानिक ने 'शादी क्या होती है'
ये समझने के लिए शादी कर ली...
.
अब...
.
उसको ये समझ नहीं आ रहा कि विज्ञान क्या होता है...?''',
    '''कल एक साधू बाबा मिले,
मैंने पूछा - कैसे हैं बाबाजी...?
.
बाबाजी बोले - हम तो साधु हैं बेटा,
हमारा 'राम' हमें जैसे रखता है हम वैसे ही रहते हैं...!
तुम तो सुखी हो ना बच्चा...?
. 
मैं बोला - हम तो सांसारिक लोग हैं बाबाजी
हमारी 'सीता' हमें जैसे रखती है, हम वैसे ही रहते हैं...!''',
    '''लड़की - तुम किसी शादी-ब्याह में नाचते क्यों नहीं हो...?
.
.
लड़का - नाचती तो लड़कियां हैं,
हम तो भोले के भक्त हैं,
पी के तांडव करते हैं...!
.
लड़की बेहोश...''',
    '''पत्नी - शादी क्या है...?
.
.
पति - 'मान भी जाओ' से लेकर 'भाड़ में जाओ' तक का सफर ही शादी है...
बाकी सब तो मोह-माया है...!''',
    '''पत्नी - आपको मेरी सुंदरता ज्यादा अच्छी लगती है
या मेरे संस्कार...?
.
.
पति - मुझे तो तेरी ये मजाक करने की आदत
बहुत अच्छी लगती है...!''',
    '''मास्टर - सबसे पवित्र वस्तु क्या है...?
.
पप्पू - सर मोबाइल...
.
मास्टर (गुस्से में) - वो कैसे...?
.
पप्पू - वह बाथरूम, अस्पताल, श्मशान से होकर आने के बाद भी
बिना धोये हुए घर, रसोई और मंदिर सब जगह जा सकता है...!''',
    '''पत्नी - तुमने कभी मुझे सोना, हिरा या मोती गिफ्ट नहीं दिया...!
.
पति ने एक मुठ्ठी मिट्टी उठा के पत्नी के हाथ में दिया।
.
पत्नी - ये क्या है...?
.
पति - मेरे देश की धरती सोना उगले,
उगले हिरा मोती, मेरे देश की धरती।
.
पत्नी - एक थप्पड़ जड़ते हुए कहा कि
ये देश है विर जवानों का अलबेलों का मस्तानो का...!''',
    '''पप्पू होटल में चेक इन करता है और बोलता है-
डबल बेड का रूम चाहिए...!
.
होटल मैनेजर - लेकिन सर आप तो अकेले हैं।
.
पप्पू - हां, लेकिन मैं एक शादीशुदा इंसान हूं, तो मेरी इच्छा है कि
बेड की दूसरी साइड खामोशी को एंजॉय करूं...!''',
    '''मरीज - डॉक्टर, मैं खाना न खाऊं तो मुझे भूख लग जाती है,
ज्यादा काम करता हूं, तो थक जाता हूं... देर तक जगा रहूं, तो
नींद आ जाती है, मैं क्या करूं...?
.
.
डॉक्टर - रात भर धूप में बैठे रहो, सही हो जाओगे।''',
    '''लड़की ने पप्पू से पूछा - मोहब्बत शादी से पहले करनी चाहिए
या शादी के बाद...?
.
.
पप्पू ने कहा - कभी भी करो, लेकिन बीवी को
पता नहीं चलना चाहिए...!''',
    '''पत्नी - तुमने कभी मुझे सोना, हिरा या मोती गिफ्ट नहीं दिया...!
.
पति ने एक मुठ्ठी मिट्टी उठा के पत्नी के हाथ में दिया।
.
पत्नी - ये क्या है...?
.
पति - मेरे देश की धरती सोना उगले,
उगले हिरा मोती, मेरे देश की धरती।
.
पत्नी - एक थप्पड़ जड़ते हुए कहा कि
ये देश है विर जवानों का अलबेलों का मस्तानो का...!''',
    '''पप्पू होटल में चेक इन करता है और बोलता है-
डबल बेड का रूम चाहिए...!
.
होटल मैनेजर - लेकिन सर आप तो अकेले हैं।
.
पप्पू - हां, लेकिन मैं एक शादीशुदा इंसान हूं, तो मेरी इच्छा है कि
बेड की दूसरी साइड खामोशी को एंजॉय करूं...!''',
    '''मरीज - डॉक्टर, मैं खाना न खाऊं तो मुझे भूख लग जाती है,
ज्यादा काम करता हूं, तो थक जाता हूं... देर तक जगा रहूं, तो
नींद आ जाती है, मैं क्या करूं...?
.
.
डॉक्टर - रात भर धूप में बैठे रहो, सही हो जाओगे।''',
    '''लड़की ने पप्पू से पूछा - मोहब्बत शादी से पहले करनी चाहिए
या शादी के बाद...?
.
.
पप्पू ने कहा - कभी भी करो, लेकिन बीवी को
पता नहीं चलना चाहिए...!''',
    '''मुकेश - डॉक्टर साहब, मुझे एक समस्या है।
.
डॉक्टर - क्या...?
.
मुकेश - बात करते वक्त मुझे आदमी दिखाई नहीं देता...!
.
डॉक्टर - और ऐसा कब होता है...?
.
मुकेश - फोन पर बात करते वक्त...!
.
डॉक्टर बेहोश''',
  ]


# create speake function
def speak(audio):
    # Get value of gender and speed combo boxes
    gender = gender_combo_box.get()
    speed = speed_combo_box.get()
    computer_voices = engine.getProperty('voices')

    # define set_voice function to set the gender voice using gender combo box
    def set_voice():
        if gender == 'Male':
            engine.setProperty('voice', computer_voices[0].id)
            engine.say(audio)
            engine.runAndWait()
        else:
            engine.setProperty('voice', computer_voices[1].id)
            engine.say(audio)
            engine.runAndWait()

    # Define the Conditions for voice rate (Slow, Normal, Fast) using speed combo box
    if audio:
        if speed == 'Fast':
            engine.setProperty('rate', 200)
            set_voice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            set_voice()
        else:
            engine.setProperty('rate', 100)
            set_voice()


# create a function to wish user according the time
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")


# function to say a joke in english
# noinspection PyBroadException
def say_english_joke():
    try:
        joke = random.choice(english_jokes)
        speak("Okay, here is a joke for you...")
        userText.set("Request to say a english joke")
        compText.set(f'Okay, here is a joke for you...\n😂😂😂\n\n{joke}')
        speak(joke)
        time.sleep(7)
    except:
        pass


# Handle threading of say_english_joke function
def threading_say_english_joke():
    t1 = Thread(target=say_english_joke)
    t1.start()


# function to say a joke in hindi
# noinspection PyBroadException
def say_hindi_joke():
    try:
        joke = random.choice(hindiJokes)
        speak("Okay, here is a funny joke for you...")
        userText.set("Request to say a hindi joke")
        compText.set(f'Okay, here is a funny joke for you...\n😂😂😂\n\n{joke}')
        speak(joke)
        time.sleep(7)
    except:
        pass


# Handle threading of say_joke function
def threading_say_hindi_joke():
    t1 = Thread(target=say_hindi_joke)
    t1.start()


# create the function TakeCommand() for taking any command which will give the user.
# noinspection PyBroadException
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        time.sleep(1)
        compText.set("Listening...")
        r.adjust_for_ambient_noise(source)  # Remove source noise
        r.pause_threshold = 1
        audio = r.listen(source)    # Listen user query

    try:
        compText.set("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

    except:
        compText.set("Sorry sir i didn't understand what you said. \n\nSomething went wrong or please check your internet connection is ok")
        return "None"
    return query


# Handle threading of activate function
def threading_activate():
    t1 = Thread(target=activate)
    t1.start()


# create activate function to activate the AI Assistant
# noinspection PyBroadException
def activate():
    try:
        import pywhatkit
        # Calling wishMe function to wish the user
        wish_me()
        while True:
            random_song = random.randint(1, 243)
            query = take_command().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                try:
                    speak('searching wikipedia...')
                    results = wikipedia.summary(query, sentences=1)
                    userText.set(f"{query}")
                    compText.set(results)
                    speak("According to wikipedia")
                    speak(results)
                except:
                    speak("No such wikipedia found!")

            elif query == 'hi' or query == 'hello' or query == 'hey':
                userText.set(query)
                compText.set("Hello, How may I help you?")
                speak("Hello, How may I help you?")

            elif 'temperature of' in query or "temperature in" in query or 'temperature with' in query or 'temperature by' in query or 'weather of' in query or 'weather in' in query:
                query = query.replace("search", "")
                url = "https://www.google.com/search?q=" + query
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                ans_ = data.find("div", class_="BNeawe").text
                userText.set(f"User asked - {query}")
                compText.set(f"Answer - {ans_}")
                speak(f"{ans_}")

            elif 'temperature' in query or 'weather' in query:
                query = "current temperature"
                url = "https://www.google.com/search?q=" + query
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                ans_ = data.find("div", class_="BNeawe").text
                userText.set(f"User asked - {query}")
                compText.set(f"Temperature - {ans_}")
                speak(f"{ans_}")

            elif 'time' in query or 'the time' in query:
                current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
                userText.set(query)
                compText.set(current_time)
                speak(f"The current time is: {current_time}")

            elif 'date' in query or 'the date' in query:
                current_date = datetime.datetime.now().strftime("%d %B %Y")
                userText.set(query)
                compText.set(current_date)
                speak(f"The current date is: {current_date}")

            elif 'day' in query:
                day = datetime.datetime.now().strftime("%A")
                userText.set(query)
                compText.set(day)
                speak(f"Today is: {day}")

            elif 'month' in query:
                month = datetime.datetime.now().strftime("%B")
                userText.set(query)
                compText.set(month)
                speak(f"The month is: {month}")

            elif 'year' in query:
                year = datetime.datetime.now().strftime("%Y")
                userText.set(query)
                compText.set(year)
                speak(f"The year is: {year}")

            elif 'how are you' in query or 'what about you' in query or 'what is going on' in query:
                userText.set(query)
                compText.set("I am always fine.")
                speak("I am always fine.")

            elif 'too good' in query or 'awesome' in query or 'well done' in query or 'nice' in query or 'good' in query or 'wow' in query:
                userText.set(query)
                compText.set("Thank You!\nIt's my pleasure.")
                speak("thank you, it's my pleasure.")

            elif 'what can you do' in query or 'what you can do' in query or 'how you can help me' in query or 'how can you help me' in query:
                userText.set(query)
                compText.set("I can automate your daily tasks and I can also help you to search anything.")
                speak("I can automate your daily tasks and I can also help you to search anything.")

            elif 'play music' in query or 'play songs' in query or 'play a song' in query or 'open music' in query:
                userText.set(query)
                compText.set("Enjoy the music")
                music_dir = 'C:\\Users\\hariom mewada\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[random_song]))

            elif 'close browser' in query or 'close the browser' in query or 'close my browser' in query:
                try:
                    userText.set("Close the browser.")
                    compText.set("Closed Browser Successfully!")
                    speak("Closing the browser...")
                    os.system("taskkill /im msedge.exe /f")     # it will close the browser
                except Exception as e:
                    speak("The edge Browser is not found in progress...")
                    compText.set(str(e))

            elif 'your name' in query or 'tell me about your self' in query or 'who are you' in query:
                userText.set(query)
                compText.set("I am an AI Assistant and i can help you to automate your daily tasks. please tell me How may i help you?")
                speak("I am an AI Assistant. How may i help you?")

            elif 'how old are you' in query or 'your age' in query:
                userText.set(query)
                compText.set("There is no age define for me but i created at 15 March 2022.")
                speak("There is no age define for me but i created at 15 March 2022.")

            elif 'english joke' in query or 'joke in english' in query or 'english jokes' in query or 'jokes in english' in query:
                threading_say_english_joke()

            elif 'joke' in query or 'jokes' in query or 'hindi joke' in query or 'joke in hindi' in query or 'hindi jokes' in query or 'jokes in hindi' in query:
                threading_say_hindi_joke()

            # Conditional statements to open web app
            elif 'open youtube' in query or 'open the youtube' in query or 'open my youtube' in query:
                open_youtube()

            elif 'open google' in query or 'open the google' in query or 'open my google' in query:
                open_google()

            elif 'open gmail' in query or 'open the gmail' in query or 'open my gmail' in query:
                open_gmail()

            elif 'open outlook' in query or 'open the outlook' in query or 'open my outlook' in query:
                open_outlook()

            elif 'open whatsapp' in query or 'launch whatsapp' in query or 'start whatsapp' in query:
                open_site("Request for opening whatsapp", "Whatsapp has been opened successfully!", "https://web.whatsapp.com")

            elif 'open facebook' in query or 'launch facebook' in query or 'start facebook' in query:
                open_site("Request for opening facebook", "Facebook has been opened successfully!", "https://www.facebook.com")

            elif 'open linkedin' in query or 'launch linkedin' in query or 'start linkedin' in query:
                open_site("Request for opening linkedin", "LinkedIn has been opened successfully!", "https://www.linkedin.com/feed/")

            elif 'open github' in query or 'launch github' in query or 'start github' in query:
                open_site("Request for opening github", "Github has been opened successfully!", "https://github.com")

            # Conditional statements to open installed software
            elif 'open code' in query or 'vs code' in query or 'visual studio code' in query:
                open_software(query, "VS Code has been opened successfully!", "C:\\Users\\hariom mewada\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

            elif 'open android studio' in query or 'start android studio' in query or 'launch android studio' in query:
                open_software(query, "Android Studio has been opened successfully!", "C:\\Users\\hariom mewada\\AppData\\Local\\Programs\\Microsoft VS Code\\Android Studio")
            
            elif 'open chrome' in query or 'start chrome' in query or 'launch chrome' in query:
                open_software(query, "Google Chrome has been opened successfully!", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome")

            elif 'open edge' in query or 'start edge' in query or 'launch edge' in query or 'ms edge' in query or 'microsoft edge' in query:
                open_software(query, "MicroSoft Edge has been opened successfully!", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge")

            elif 'open firefox' in query or 'start firefox' in query or 'launch firefox' in query:
                open_software(query, "Firefox has been opened successfully!", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox")

            elif 'open brave' in query or 'start brave' in query or 'launch brave' in query:
                open_software(query, "Brave has been opened successfully!", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave")

            elif 'open word' in query or 'start word' in query or 'launch word' in query or 'open ms word' in query or 'start ms word' in query or 'launch ms word' in query or 'open microsoft word' in query or 'start microsoft word' in query or 'launch microsoft word' in query:
                open_software(query, "Microsoft word has been opened successfully!", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word")

            elif 'open power point' in query or 'start power point' in query or 'launch power point' in query or 'open ms power point' in query or 'start ms power point' in query or 'launch ms power point' in query or 'open microsoft power point' in query or 'start microsoft power point' in query or 'launch microsoft power point' in query or 'open powerpoint' in query or 'start powerpoint' in query or 'launch powerpoint' in query or 'open ms powerpoint' in query or 'start ms powerpoint' in query or 'launch ms powerpoint' in query or 'open microsoft powerpoint' in query or 'start microsoft powerpoint' in query or 'launch microsoft powerpoint' in query:
                open_software(query, "Microsoft power point has been opened successfully!", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint")

            elif 'open excel' in query or 'start excel' in query or 'launch excel' in query or 'open ms excel' in query or 'start ms excel' in query or 'launch ms excel' in query or 'open microsoft excel' in query or 'start microsoft excel' in query or 'launch microsoft excel' in query:
                open_software(query, "Microsoft excel has been opened successfully!", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel")

            elif 'open one note' in query or 'start one note' in query or 'launch one note' in query or 'open ms one note' in query or 'start ms one note' in query or 'launch ms one note' in query or 'open microsoft one note' in query or 'start microsoft one note' in query or 'launch microsoft one note' in query or 'open onenote' in query or 'start onenote' in query or 'launch onenote' in query or 'open ms onenote' in query or 'start ms onenote' in query or 'launch ms onenote' in query or 'open microsoft onenote' in query or 'start microsoft onenote' in query or 'launch microsoft onenote' in query:
                open_software(query, "Microsoft onenote has been opened successfully!", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote")

            elif 'open camera' in query or 'start camera' in query or 'launch camera' in query:
                subprocess.run('start microsoft.windows.camera:', shell=True)

            elif 'open' in query or 'start' in query or 'launch' in query:
                userText.set(query)
                compText.set("Sorry, Unable to open right now!")
                speak("Sorry, Unable to open right now!")

            elif 'empty recycle bin' in query or 'empty my recycle bin' in query or 'clear recycle bin' in query:
                userText.set(query)
                compText.set("Are you sure to clear the recycle bin?")
                clear_recycle_bin()

            elif "what" in query or 'who' in query or 'search' in query:
                query = query.replace("search", "")
                url = "https://www.google.com/search?q=" + query
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                ans_ = data.find("div", class_="BNeawe").text
                userText.set(f"User asked - {query}")
                compText.set(f"Answer - {ans_}")
                speak(f"{ans_}")

            elif 'how to' in query:
                userText.set(query)
                compText.set("Getting things ready...")
                max_result = 1
                result = search_wikihow(query, max_result)
                assert len(result) == 1
                compText.set(result[0])
                speak(result[0].summary)

            elif 'how' in query or 'whose' in query or 'tell me' in query or 'define' in query or 'which' in query or 'when' in query or 'where' in query or 'why' in query or 'whom' in query or 'whichever' in query or 'whatever' in query or 'whenever' in query or 'wherever' in query or 'however' in query or 'if' in query or 'whether' in query or 'will' in query or 'would' in query or 'can' in query or 'could' in query or 'may' in query or 'might' in query or 'must' in query or 'do' in query or 'does' in query or 'did' in query or 'is' in query or 'are' in query or 'was' in query or 'were' in query or 'has' in query or 'have' in query or 'had' in query or 'am' in query or 'shall' in query or 'would' in query or 'should' in query or 'might' in query or 'ought' in query or 'is there' in query or 'are there' in query or 'was there' in query or 'were there' in query:
                pywhatkit.search(query)
                url = "https://www.google.com/search?q=" + query
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                ans_ = data.find("div", class_="BNeawe").text
                userText.set(f"User asked - {query}")
                compText.set(f"Answer - {ans_}")

            elif 'quit' in query or 'exit' in query or 'close' in query or 'stop' in query:
                speak("Thanks sir! Have a nice day.")
                root.destroy()

            elif query == 'none':
                userText.set("None")
                compText.set("Sorry, I am unable to understand!")

            else:
                pywhatkit.search(query)
                url = "https://www.google.com/search?q=" + query
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                ans_ = data.find("div", class_="BNeawe").text
                userText.set(f"User asked - {query}")
                compText.set(f"Answer - {ans_}")

            time.sleep(3)

    except:
        messagebox.showinfo("AI Assistant", "Please check your internet connection")


# create function to automatically send the email
def send_email():
    webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm#inbox?compose=CllgCJNqsdqhqxMMnLLFsGmtWGDfNJLSrZhZZxzJtTMdvSHklGBQnXbsDXghVVZztjtVLkCBvSB")


# noinspection PyBroadException
def clear_recycle_bin():
    try:
        import winshell
        winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)
        speak("done sir")
    except:
        messagebox.showinfo("Recycle bin", "Already clear the recycle bin")


# function to open website
def open_site(user_text, comp_text, url):
    # noinspection PyBroadException
    try:
        userText.set(user_text)
        compText.set(comp_text)
        webbrowser.open(url)
    except:
        compText.set("Sorry! I am not able to open right now!")


# create function for opening the Chrome
# noinspection PyBroadException
def open_software(user_text, comp_text, path):
    try:
        userText.set(user_text)
        compText.set(comp_text)
        os.startfile(path)
    except:
        speak("Something went wrong!")
        compText.set("Something went wrong!")


# create function for opening the YouTube
# noinspection PyBroadException
def open_youtube():
    try:
        userText.set("Request for opening YouTube")
        compText.set("YouTube has been opened Successfully")
        webbrowser.open("https://www.youtube.com")
    except:
        compText.set("Something went wrong!")


# create function for opening the Google
# noinspection PyBroadException
def open_google():
    try:
        userText.set("Request for opening Google")
        compText.set("Google has been opened successfully")
        webbrowser.open("https://www.google.co.in")
    except:
        compText.set("Something went wrong!")


# create function for opening the Chrome
# noinspection PyBroadException
def open_chrome():
    try:
        userText.set("Request for opening Google Chrome")
        compText.set("Google Chrome has been opened successfully")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome")
    except:
        compText.set("Something went wrong!")


# create function for opening the gmail
# noinspection PyBroadException
def open_gmail():
    try:
        userText.set("Request for opening Gmail")
        compText.set("Gmail has been opened successfully")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    except:
        compText.set("Something went wrong!")


# create function for opening the Google Photos
# noinspection PyBroadException
def open_photos():
    try:
        userText.set("Request for opening Google Photos")
        compText.set("Google Photos has been opened successfully")
        webbrowser.open("https://www.google.com/photos/about")
    except:
        compText.set("Something went wrong!")


# create function for opening the Outlook
# noinspection PyBroadException
def open_outlook():
    try:
        userText.set("Request for opening Microsoft Outlook")
        compText.set("Microsoft Outlook has been opened successfully")
        webbrowser.open("https://outlook.live.com/owa")
    except:
        compText.set("Something went wrong!")


# create function for opening the Google Drive
# noinspection PyBroadException
def open_drive():
    try:
        userText.set("Request for opening Google Drive")
        compText.set("Google Drive has been opened successfully")
        webbrowser.open("https://drive.google.com/drive/u/4/my-drive")
    except:
        compText.set("Something went wrong!")


# Creating theme 1
def theme1():
    root.config(bg="#2b2b2b")
    Panel.config(bg="#2b2b2b")
    activate_button.config(bg="#2b2b2b")
    close_button.config(bg="#2b2b2b")
    Iconbar_Left.config(bg="#2b2b2b")
    Iconbar_Right.config(bg="#2b2b2b")
    youtube_button.config(bg="#2b2b2b")
    chrome_button.config(bg="#2b2b2b")
    drive_button.config(bg="#2b2b2b")
    photos_button.config(bg="#2b2b2b")
    gmail_button.config(bg="#2b2b2b")
    outlook_button.config(bg="#2b2b2b")
    recycle_bin_button.config(bg="#2b2b2b")
    send_mail_button.config(bg="#2b2b2b")
    user_image.config(bg="#2b2b2b")
    assistant_image.config(bg="#2b2b2b")
    userFrame.config(bg="#2b2b2b")
    compFrame.config(bg="#2b2b2b")
    open_side_menu.config(bg="#2b2b2b")
    time_label.config(bg="#2b2b2b")
    date_label.config(bg="#2b2b2b")
    label1.config(bg="#202020")
    label2.config(bg="#202020")
    userText.set("Request for changing the current theme.")
    compText.set("The Theme has been updated.")


# Creating theme 2
def theme2():
    root.config(bg="#2c3942")
    Panel.config(bg="#2c3942")
    activate_button.config(bg="#2c3942")
    close_button.config(bg="#2c3942")
    Iconbar_Left.config(bg="#2c3942")
    Iconbar_Right.config(bg="#2c3942")
    youtube_button.config(bg="#2c3942")
    chrome_button.config(bg="#2c3942")
    drive_button.config(bg="#2c3942")
    photos_button.config(bg="#2c3942")
    gmail_button.config(bg="#2c3942")
    outlook_button.config(bg="#2c3942")
    recycle_bin_button.config(bg="#2c3942")
    send_mail_button.config(bg="#2c3942")
    user_image.config(bg="#2c3942")
    assistant_image.config(bg="#2c3942")
    userFrame.config(bg="#2c3942")
    compFrame.config(bg="#2c3942")
    open_side_menu.config(bg="#2c3942")
    time_label.config(bg="#2c3942")
    date_label.config(bg="#2c3942")
    label1.config(bg="#314859")
    label2.config(bg="#314859")
    userText.set("Request for changing the current theme.")
    compText.set("The Theme has been updated.")


# Creating theme 3
def theme3():
    root.config(bg="#051a2a")
    Panel.config(bg="#051a2a")
    activate_button.config(bg="#051a2a")
    close_button.config(bg="#051a2a")
    Iconbar_Left.config(bg="#051a2a")
    Iconbar_Right.config(bg="#051a2a")
    youtube_button.config(bg="#051a2a")
    chrome_button.config(bg="#051a2a")
    drive_button.config(bg="#051a2a")
    photos_button.config(bg="#051a2a")
    gmail_button.config(bg="#051a2a")
    outlook_button.config(bg="#051a2a")
    recycle_bin_button.config(bg="#051a2a")
    send_mail_button.config(bg="#051a2a")
    user_image.config(bg="#051a2a")
    assistant_image.config(bg="#051a2a")
    userFrame.config(bg="#051a2a")
    compFrame.config(bg="#051a2a")
    open_side_menu.config(bg="#051a2a")
    time_label.config(bg="#051a2a")
    date_label.config(bg="#051a2a")
    label1.config(bg="#011627")
    label2.config(bg="#011627")
    userText.set("Request for changing the current theme.")
    compText.set("The Theme has been updated.")


# Creating default theme
def default_theme():
    root.config(bg="#222634")
    Panel.config(bg="#222634")
    activate_button.config(bg="#222634")
    close_button.config(bg="#222634")
    Iconbar_Left.config(bg="#222634")
    Iconbar_Right.config(bg="#222634")
    youtube_button.config(bg="#222634")
    chrome_button.config(bg="#222634")
    drive_button.config(bg="#222634")
    photos_button.config(bg="#222634")
    gmail_button.config(bg="#222634")
    outlook_button.config(bg="#222634")
    recycle_bin_button.config(bg="#222634")
    send_mail_button.config(bg="#222634")
    user_image.config(bg="#222634")
    assistant_image.config(bg="#222634")
    userFrame.config(bg="#222634")
    compFrame.config(bg="#222634")
    open_side_menu.config(bg="#222634")
    time_label.config(bg="#222634")
    date_label.config(bg="#222634")
    label1.config(bg="#1b1e29")
    label2.config(bg="#1b1e29")
    userText.set("Request for changing the current theme.")
    compText.set("The Theme has been updated.")


# Handle threading of change_theme function
def threading_change_theme():
    t1 = Thread(target=change_theme)
    t1.start()


# Creating change_theme function to change the theme
def change_theme():
    new_window = Tk()
    new_window.geometry("150x250")
    new_window.config(bg="#1b1e29")
    new_window.resizable(False, False)
    default = Button(new_window, text="Default", font=("Monotype Corsiva", 15), padx=5, bd=0, relief=FLAT, bg="#1b1e29", fg="white", activebackground="#1b1e29", activeforeground="white", cursor='hand2', command=default_theme)
    default.pack(pady=(5, 0))
    button1 = Button(new_window, text="Theme1", font=("Monotype Corsiva", 15), padx=5, bd=0, relief=FLAT, bg="#1b1e29", fg="white", activebackground="#1b1e29", activeforeground="white", cursor='hand2', command=theme1)
    button1.pack()
    button2 = Button(new_window, text="Theme2", font=("Monotype Corsiva", 15), padx=5, bd=0, relief=FLAT, bg="#1b1e29", fg="white", activebackground="#1b1e29", activeforeground="white", cursor='hand2', command=theme2)
    button2.pack()
    button3 = Button(new_window, text="Theme3", font=("Monotype Corsiva", 15), padx=5, bd=0, relief=FLAT, bg="#1b1e29", fg="white", activebackground="#1b1e29", activeforeground="white", cursor='hand2', command=theme3)
    button3.pack()
    new_window.mainloop()


# Handle threading of change_font function
def threading_change_font():
    t1 = Thread(target=change_font)
    t1.start()


# Creating change_font function to change the font color
# noinspection PyTypeChecker
def change_font():
    add_color = colorchooser.askcolor(title="Select Color")
    color = add_color[1]
    label1.config(fg=color)
    label2.config(fg=color)


# Handle threading of about_my_self function
def threading_about_my_self():
    t1 = Thread(target=about_myself)
    t1.start()


# Create the about_my_self function
def about_myself():
    userText.set("Tell me about your self.")
    compText.set("I am an AI Assistant and i can help you to automate your daily tasks and can make your life easy.")
    speak("I am an AI Assistant and i can help you to automate your daily tasks and can make your life easy.")


# Handle threading of close_program function
def threading_close_program():
    t1 = Thread(target=close_program)
    t1.start()


# Create the close_program function to close the assistant
def close_program():
    speak("Thanks sir! Have a nice day. Exiting...")
    root.destroy()
    exit()


# Starting the code....
if __name__ == '__main__':
    root = Tk()
    root.geometry("1800x900+50+20")
    root.title("AI Assistant")
    root.resizable(False, False)
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\icon.ico")
    root.attributes('-alpha', 0.98)  # Transparent 2% or 0.02%
    root.config(background='#232734')

    img = ImageTk.PhotoImage(Image.open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\AI.png'))
    Panel = Label(root, image=img, bg='#232734')
    Panel.pack(side=TOP, fill=BOTH, expand=NO)

    # create activate and close button
    activate_button = Button(root, text='Activate', command=threading_activate, font=("Pristina", 25, 'italic'), bg="#232734", activebackground="#232734", fg="Orange", activeforeground="Red", bd=0, width=10, cursor='hand2')
    activate_button.pack()
    close_button = Button(root, text='Close', command=threading_close_program, font=("Pristina", 25, 'italic'), bg="#232734", activebackground="#232734", fg="Orange", activeforeground="Red", bd=0, width=10, cursor='hand2')
    close_button.pack()

    Iconbar_Left = Frame(root, width=100, bg='#232734')
    Iconbar_Left.place(x=360, y=30)

    Iconbar_Right = Frame(root, width=100, bg='#232734')
    Iconbar_Right.place(x=1240, y=30)

    youtube = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\youtube-icon.png")
    Google_Chrome = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\Google-Chrome-icon.png")
    google_photos = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\google-photos.png")
    drive = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\Google-Drive-icon.png")
    gmail = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\Gmail-icon.png")
    Outlook = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\Microsoft-Outlook.png")

    youtube_button = Button(Iconbar_Left, image=youtube, bg="#232734", bd=0, activebackground="#232734", command=open_youtube, cursor='hand2')
    youtube_button.pack(side=LEFT, padx=10)
    chrome_button = Button(Iconbar_Left, image=Google_Chrome, bg="#232734", bd=0, activebackground="#232734", command=open_chrome, cursor='hand2')
    chrome_button.pack(side=LEFT, padx=10)
    photos_button = Button(Iconbar_Left, image=google_photos, bg="#232734", bd=0, activebackground="#232734", command=open_photos, cursor='hand2')
    photos_button.pack(side=LEFT, padx=10)

    drive_button = Button(Iconbar_Right, image=drive, bg="#232734", bd=0, activebackground="#232734", command=open_drive, cursor='hand2')
    drive_button.pack(side=LEFT, padx=10)
    gmail_button = Button(Iconbar_Right, image=gmail, bg="#232734", bd=0, activebackground="#232734", command=open_gmail, cursor='hand2')
    gmail_button.pack(side=LEFT, padx=10)
    outlook_button = Button(Iconbar_Right, image=Outlook, bg="#232734", bd=0, activebackground="#232734", command=open_outlook, cursor='hand2')
    outlook_button.pack(side=LEFT, padx=10)

    empty_recycle_bin = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\recycle-bin-icon.png")
    send_mail = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\mail-icon.png")

    recycle_bin_button = Button(root, image=empty_recycle_bin, text="Empty Recycle Bin", bg="#232734", bd=0, activebackground="#3b415a", command=clear_recycle_bin, cursor='hand2', font=("Aparajita", 10), fg='white', compound=TOP, activeforeground='gold')
    recycle_bin_button.place(x=380, y=175)

    send_mail_button = Button(root, image=send_mail, text="Send Email", bg="#232734", bd=0, activebackground="#3b415a", command=send_email, cursor='hand2', font=("Aparajita", 10), fg='white', compound=TOP, activeforeground='gold')
    send_mail_button.place(x=1290, y=175)

    compText = StringVar()
    userText = StringVar()

    userText.set("Click on Activate Button to Activate Assistant")
    compText.set("I am an AI Assistant! Please Activate and tell me How can i help you...")

    userFrame = LabelFrame(root, text='_____________User____________', font=("Tempus Sans ITC", 20), bg='#232734', fg='#F0F8FF')
    userFrame.pack(side=LEFT, fill=Y, expand=YES, padx=100, pady=20)

    compFrame = LabelFrame(root, text='___________Assistant__________', font=("Tempus Sans ITC", 20), bg="#232734", fg='#F0F8FF')
    compFrame.pack(side=RIGHT, fill=Y, expand=YES, padx=100, pady=20)

    User = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\User.png")
    Assistant = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\AI_Assistant.png")

    user_image = Label(root, image=User, bg="#232734")
    user_image.place(x=430, y=320)
    assistant_image = Label(root, image=Assistant, bg="#232734")
    assistant_image.place(x=1315, y=320)

    label1 = Message(userFrame, padx=20, pady=30, textvariable=userText, font=('Monotype Corsiva', 15, 'italic'), bg='#1c1f29', fg='White', justify=CENTER)
    label1.pack(fill=BOTH, expand=YES)

    label2 = Message(compFrame, padx=20, pady=30, textvariable=compText, font=('Monotype Corsiva', 15, 'italic'), bg='#1c1f29', fg='White', justify=CENTER)
    label2.pack(fill=BOTH, expand=YES)

    # create gender combo box
    gender_combo_box = Combobox(root, values=['Male', 'Female'], font='Georgia 10', state='r', width=10)
    gender_combo_box.place(x=825, y=550)
    gender_combo_box.set('Female')

    # create speed combo box
    speed_combo_box = Combobox(root, values=['Fast', 'Normal', 'Slow'], font='Georgia 10', state='r', width=10)
    speed_combo_box.place(x=825, y=640)
    speed_combo_box.set('Normal')

    # Creating side menu
    def toggle_menu():
        f1 = Frame(root, width=145, height=1000, bg='#36454F')
        f1.place(x=0, y=0)

        def button(x, y, text, activbcolor, bcolor, cmd):
            # noinspection PyUnusedLocal
            def on_press(e):
                my_button1['background'] = activbcolor
                my_button1['foreground'] = 'black'

            # noinspection PyUnusedLocal
            def on_leave(e):
                my_button1['background'] = bcolor
                my_button1['foreground'] = '#FFFFF0'

            my_button1 = Button(f1, text=text, width=12, justify=CENTER, fg='#FFFFF0', bd=0, bg=bcolor, activeforeground='black', activebackground=activbcolor, command=cmd, font='Georgia 9', pady=5, padx=10, anchor='w', cursor='hand2')

            my_button1.bind('<Enter>', on_press)
            my_button1.bind('<Leave>', on_leave)

            my_button1.place(x=x, y=y)

        button(0, 60, "About me", 'sky blue', '#36454F', threading_about_my_self)
        button(0, 100, "Say hindi joke", 'sky blue', '#36454F', threading_say_hindi_joke)
        button(0, 140, "Say english joke", 'sky blue', '#36454F', threading_say_english_joke)
        button(0, 180, "Change Theme", 'sky blue', '#36454F', threading_change_theme)
        button(0, 220, "Font color", 'sky blue', '#36454F', threading_change_font)
        button(0, 260, "Exit", 'sky blue', '#36454F', threading_close_program)

        def delete():
            f1.destroy()

        Button(f1, image=bar_image, command=delete, activebackground='#36454F', bg='#36454F', fg='white', bd=0, activeforeground='white').place(x=10, y=10)

    bar_image = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\three_lines.png')
    open_side_menu = Button(root, command=toggle_menu, image=bar_image, bd=0, fg='white', bg='#232734', activebackground='#232734')
    open_side_menu.place(x=10, y=10)

    time_label = Label(root, text="", font="Calibri 16", fg='white', bg="#222634")
    time_label.place(x=1640, y=10)
    date_label = Label(root, text="", font="Calibri 10", fg='white', bg="#222634")
    date_label.place(x=1640, y=50)

    def my_time():
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        current_date = datetime.datetime.now().strftime("%d-%b-%y")
        date_label.config(text=current_date)
        time_label.config(text=current_time)
        time_label.after(200, my_time)

    my_time()

    root.mainloop()
