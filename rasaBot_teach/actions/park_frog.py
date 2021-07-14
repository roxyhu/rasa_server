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
from rasa_sdk.events import EventType
from rasa_sdk.events import AllSlotsReset

class Actioncheck(Action):
    

    def name(self) -> Text:
        return "action_park_frog"

    # def apply_to(self, tracker):
    #     tracker.setslot(key, value)


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = " "
           
        slot_frog = tracker.get_slot("duck_name")
        color_name = tracker.get_slot("color")
        frog_intent = tracker.get_intent_of_latest_message()
        print("slot_frog",slot_frog)
        print("frog_intent",frog_intent)
        print("color_name",color_name)
        print()


        if slot_frog is None:
            slot_frog = "talk" 
            print("123")
        else:
            frog_list = list(slot_frog)

        if frog_intent == "student_frog":
            frog_list = list(slot_frog)
            if frog_list != []:
                print("list", frog_list)
                if frog_list[0] == "D" or frog_list[0] == "d" or frog_list[0] == "t" or frog_list[0] == "T":
                    if slot_frog == "duck":
                        response = "What color is it?\n*Student:It is yellow.*"
                        frog_list.clear()
                    else:
                        response = "Do you mean duck?\n*Student: Yes/No.*"
                        frog_list.clear()

                else:
                    response = "%s is not a animal! \nWhat’s that in the pond?" % (slot_frog)
                   
        elif frog_intent =="affirm":
            response = "What color is it?\n*Student:It is yellow.*"
            print("affirm")

        elif frog_intent == "deny":
            response = "What animal is it? \nCould you please say it again?"
            print("deny")
        
        else:
            response = "I didn't understand. \nCould you please say it again?"

        print("RES",response)





        

        dispatcher.utter_message("{}".format(response))
        print("000 END 000")
        print("意圖排名: ",tracker.latest_message)



      
        return [AllSlotsReset()]

