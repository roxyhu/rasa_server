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
        return "action_check_restaurant"

    # def apply_to(self, tracker):
    #     tracker.setslot(key, value)


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        meal1 = tracker.get_slot("meal1")  
        meal2 = tracker.get_slot("meal2")
        meal3 = tracker.get_slot("meal3") 

        dict_meal = {'spaghetti': 230, 'French fries': 80, 'soda': 30, 'Sauda': 30}
        # print("0000000000000000",tracker.slots)
        slotAll = tracker.current_slot_values()  
        meall_price = 0
        meal2_price = 0
        meal3_price = 0

        for key,value in slotAll.items():
            if value != None and (meal1 == value or meal2 == value or meal3 ==value):
                print("00",value)
                for key in dict_meal:
                    if key == meal1:
                        meall_price = dict_meal[key]
                        print("1",meall_price)
                    if key == meal2:
                        meal2_price = dict_meal[key]
                        print("2",meal2_price)
                    if key == meal3:
                        meal3_price = dict_meal[key]
                        print("3",meal3_price)
        print("a",meall_price)
        print("b",meal2_price)
        print("c",meal3_price)
        total = meall_price + meal2_price + meal3_price

        print("total",total)

        dispatcher.utter_message("Your total is {} NT dollars.\n*Student:Okay, here you are.* ".format(total))
        print("000 END 000")



      
        return [AllSlotsReset()]

