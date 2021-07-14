# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
# 0519測試成功 青蛙綠色
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime
from rasa_sdk.events import EventType
from rasa_sdk.events import AllSlotsReset


class Actioncheck(Action):

    def name(self) -> Text:
        return "action_park_2"

    # def apply_to(self, tracker):
    #     tracker.setslot(key, value)

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = " "

        slot_frog = tracker.get_slot("duck_name")
        color_name = tracker.get_slot("color")
        frog_intent = tracker.get_intent_of_latest_message()
        print("slot_frog", slot_frog)
        print("frog_intent", frog_intent)
        print("color_name", color_name)

        # 青蛙顏色判斷式
        if color_name is None:
            color_name = "cream"
            print("7777")
        else:
            color_list = list(color_name)
        print

        if frog_intent == "color":
            color_list = list(color_name)
            if color_list != []:
                print("list", color_list)
                if color_list[0] == "Y" or color_list[0] == "y" or color_list[0] == "I" or color_list[0] == "i":
                    if color_name == "yellow" or color_name == "Yellow":
                        response = "Oh, no. \nIt’s raining. \nDo you have an umbrella? \n*Student: Yes, I do/No, I don't.*"
                        color_list.clear()
                    else:
                        response = "Do you mean yellow?\n*Student: Yes/No.*"
                        color_list.clear()

                else:
                    response = "%s is not a color! \nWhat color is the duck" % (
                        color_name)
            else:
                print("you")

        elif frog_intent == "student_frog":
            frog_list = list(slot_frog)
            if frog_list != []:
                print("list", frog_list)
                if frog_list[0] == "D" or frog_list[0] == "d" or frog_list[0] == "t" or frog_list[0] == "T":
                    if slot_frog == "duck":
                        response = "What color is it? \n*Student:It is yellow.*"
                        frog_list.clear()
                    else:
                        response = "Do you mean duck? \n*Student: Yes/No.*"
                        frog_list.clear()

                else:
                    response = "%s is not a animal! \nWhat’s that in the pond?" % (slot_frog)

        elif frog_intent == "affirm":
            response = "Oh, no. \nIt’s raining. \nDo you have an umbrella? \n*Student: Yes, I do/No, I don't.*"
            print("affirm")

        elif frog_intent == "deny":
            response = "Let’s go to other places so that we don’t get wet. \nWhere do you want to go next? \n*Student: I want to go to the library/supermarket/school/restaurant.*"
            print("deny")

        else:
            print("5555555555", frog_intent)
            response = "I didn't understand. \nCould you please say it again?"

        print("RES", response)
        print("意圖排名: ", tracker.latest_message)

        dispatcher.utter_message("{}".format(response))
        print("000 END 000")

        return [AllSlotsReset()]
