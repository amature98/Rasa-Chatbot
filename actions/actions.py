# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions

# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet


# class ActionBookFlight(Action):

#     def name(self):
#             return "action_book_flight"

#     def run(self, dispatcher, tracker, domain):
#         # Get the slot values
#         destination = tracker.get_slot('destination')
#         date = tracker.get_slot('date')
#         number_of_people = tracker.get_slot('number_of_people')

#         # Here you would add the code to call your flight booking API.
#         # For this example, we'll just pretend we successfully booked a flight and return a message.

#         message = f"Successfully booked a flight for {number_of_people} person(s) to {destination} on {date}."
#         dispatcher.utter_message(text=message)

#         # You might want to set some slots to influence the conversation
#         return [SlotSet("booking_confirmation", "true")]

