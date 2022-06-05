from dataclasses import dataclass
import hydra
from omegaconf import DictConfig
from gtts import gTTS
from playsound import playsound
import datetime
import random
from src.listen_respond import listen

@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig):

    introduction = cfg.new_name, "is ready to use"
    intro = ''
    for items in introduction:
        
        intro = intro + items
        intro_obj=gTTS(text=intro,lang=cfg.language, slow=False)
        intro_obj.save("sounds/new_introduction.mp3")
    playsound("sounds/new_introduction.mp3")

if __name__ == "__main__":

    assistant  = main()

    while True:
        conversation_listen = listen()

        if "time" in conversation_listen:
            time = datetime.datetime.now().time().strftime('%H:%M')
            time_obj=gTTS(text=time,lang='en', slow=False).save("sounds/time.mp3")
            playsound("sounds/time.mp3")
            exit()
        elif "temperature" or "weather" in conversation_listen:
            choices = ['Hot', 'Rainy', 'Cold', 'Need a light jacket']
            random_choice = random.choice(choices)
            weather_obj = gTTS(text=random_choice, lang='en', slow=False).save("sounds/weather.mp3")
            playsound("sounds/weather.mp3")
            exit()
        elif "exit" in conversation_listen:
            exit()
        else:
            sentence = "Do not know how to respond yet"
            sentence_object = gTTS(text=sentence, lang='en', slow=False).save("sounds/unknown.mp3")
            playsound("sounds/unknown.mp3")
            exit()