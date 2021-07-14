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



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        global get_number
        get_number = tracker.get_slot("number")
        # print("number",get_number)
        goods = tracker.get_slot("goods")
        print("商品名稱: ",goods)
        dict2 = {'zero': 0,'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five':5, 'six': 6, 'seven': 7, 'eight': 8, 'night': 9}
        dict_goods = {'bagel': 30, 'donut': 30, 'muffin': 30, 'apple': 25, 'orange': 20, 'watermelon': 40, 'juice': 30, 'milk': 35, 'tea': 25,'bagels': 30, 'donuts': 30, 'muffins':30, 'apples':25, 'oranges':20, 'watermelon':40}
        con = 1
        price = 30
        
        # ipad英文轉數字
        if get_number is None:
            con = 1
            
        if get_number in dict2:
            
            for key in dict2:
                if get_number == key:
                    con = dict2[key]
                    print("商品數量: ",con)
        
        if get_number.isdigit():
            con = int(get_number)
            print("商品數量: ",con)
        
        #對應價格
        if goods is not None:

            for key in dict_goods:
                if goods == key:
                    price = dict_goods[key]
                    print("單價: ",price)
        #總金額
        if con != None and price != None: 
            total = price * con
        else:
            total = 60            
        print("總金額是: ",total)
       
        # print("最近插槽資訊: ",tracker.current_slot_values() )

        print("追蹤當前意圖: ",tracker.latest_message['intent'])
        print('追蹤意圖、實體資訊、',tracker.latest_message)
        dispatcher.utter_message("A {} is {} NTD, the total cost is {} NTD \n*Student: Okay Here you are.*".format(goods,price,total))
        
        


      

            
        return [SlotSet("goods", goods)]





