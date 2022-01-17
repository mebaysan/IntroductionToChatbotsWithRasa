# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
BASE_URL = "http://worldtimeapi.org/api/timezone/"

class ActionShowTimeZone(Action):
    """
    every class has just 2 methods: name & run
    """
    def name(self) -> Text:
        """Returns the name of action

        Returns:
            Text: the text we will register in `domain.py`
        """
        return "action_find_timezone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # we can get values from slots by `tracker` object
        target_timezone = tracker.get_slot('target_timezone')
        try:
            res = requests.get(BASE_URL+target_timezone)
            res = res.json()
        
            if res['utc_offset']:
                output = f"Time zone is {res['utc_offset']}"
            else:
                output = "Please type in this structure: Area/Region"
        except:
            output = 'Ops! There are too many requests on the time zone API. Please try a few moments later...'
        dispatcher.utter_message(text=output)       
        return []
