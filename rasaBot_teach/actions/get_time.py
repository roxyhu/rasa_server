# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime



class ActionTest(Action):
    

    def name(self) -> Text:
        return "action_get_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:



        global get_time
        get_time = datetime.now().strftime('%H %M')
        print("time",get_time)
        print(type(get_time))



        dispatcher.utter_message("Reservation for one at {} right? \n*Student:Yes* ".format(get_time))
        
        

      

            
        return [SlotSet("", get_time)]