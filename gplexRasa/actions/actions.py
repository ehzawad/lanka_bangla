from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import SlotSet
from typing import Dict, Text, List

from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
from rasa_sdk.types import DomainDict
import requests


#   - main_node
#   - product_information
#   - read_privacy_policy
#   - existing_customer
#   - new_customer
#   - credit_card
#   - deposit
#   - loan
#   - apply_now

class ActionCustomFallback(Action):
    def name(self) -> Text:
        return "action_custom_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the fallback message
        fallback_message = "I'm sorry, I didn't understand that. Can you please rephrase?"

        # Send the fallback message to the user
        dispatcher.utter_message(text=fallback_message)

        return []



def clean_name(name):
    return name

class ValidateOTPSmsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_otp_sms_form"
    def validate_otp_sender_sms(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `otp_sender_sms` value."""

        # If the name is super short, it might be wrong.
        name = clean_name(slot_value)
        if len(name) == 0:
            dispatcher.utter_message(text="That must've been a typo.")
            return {"otp_sender_sms": None}
        return {"otp_sender_sms": name}

    def validate_otp(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `otp` value."""

        # If the name is super short, it might be wrong.
        name = clean_name(slot_value)
        if len(name) == 0:
            dispatcher.utter_message(text="That must've been a typo.")
            return {"otp": None}
        
        otp_sender_sms = tracker.get_slot("otp_sender_sms")
        if len(otp_sender_sms) + len(name) < 3:
            dispatcher.utter_message(text="That's a very short name. We fear a typo. Restarting!")
            return {"otp_sender_sms": None, "otp": None}
        return {"otp": name}



class Action_Otions1(Action):

    def name(self) -> Text:
        return "action_options1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_intent_of_latest_message() == "main_node":
            dispatcher.utter_message(response="utter_main_node_text")
            dispatcher.utter_message(response="utter_main_node")
            # dispatcher.utter_message(response="utter_one_button")
            # dispatcher.utter_message(response="utter_two_button")
            # dispatcher.utter_message(response="utter_three_button")

        elif tracker.get_intent_of_latest_message() == "credit_card_status":
            dispatcher.utter_message(response="utter_credit_card_status_text")
            dispatcher.utter_message(response="utter_credit_card_status_quick_replies")

        # elif tracker.get_intent_of_latest_message() == "credit_card_sms":
        #     # dispatcher.utter_message(text="credit card sms")
        #     # FollowupAction for credit_card_status_form
        #     return [FollowupAction("action_reset_credit_card_status_form")]

        elif tracker.get_intent_of_latest_message() == "credit_card_email":
            dispatcher.utter_message(text="credit card email")

        elif tracker.get_intent_of_latest_message() == "loan_products":
            # dispatcher.utter_message(response="utter_loan_products")
            dispatcher.utter_message(response="utter_loan_products_button_one")
            # dispatcher.utter_message(response="utter_loan_products_button_two")
            dispatcher.utter_message(response="utter_loan_products_button_three")


        elif tracker.get_intent_of_latest_message() == "credit_card_offers":

            dispatcher.utter_message(response="utter_credit_card_offers_button_one")
            dispatcher.utter_message(response="utter_credit_card_offers_button_two")
            dispatcher.utter_message(response="utter_credit_card_offers_quick_replies")

        elif tracker.get_intent_of_latest_message() == "deposit_products":

            dispatcher.utter_message(response="utter_deposit_products_buttons")
            dispatcher.utter_message(response="utter_deposit_products_quick_replies")

        # elif tracker.get_intent_of_latest_message() == "credit_card_sms":
        #     return [FollowupAction("action_reset_credit_card_status_form")]
        
        elif tracker.get_intent_of_latest_message() == "product_information":
            dispatcher.utter_message(response="utter_product_information")

        elif tracker.get_intent_of_latest_message() == "about_us":
            dispatcher.utter_message(response="utter_about_us")

        elif tracker.get_intent_of_latest_message() == "exit":
            dispatcher.utter_message(text="Thank you have a good day!")

        # apply_for_deposit
        elif tracker.get_intent_of_latest_message() == "apply_for_deposit":
            dispatcher.utter_message(response="utter_apply_for_deposit")

        # apply_for_loan
        elif tracker.get_intent_of_latest_message() == "apply_for_loan":
            dispatcher.utter_message(response="utter_apply_for_loan")

        # apply_for_credit_card
        elif tracker.get_intent_of_latest_message() == "apply_for_credit_card":
            dispatcher.utter_message(response="utter_apply_for_credit_card")


        # elif tracker.get_intent_of_latest_message() == "read_privacy_policy":
        #     dispatcher.utter_message(text="test 1 2 3")

        elif tracker.get_intent_of_latest_message() == "existing_customer":
            print("existing_customer intent actions")
            dispatcher.utter_message(response="utter_existing_customer")

        elif tracker.get_intent_of_latest_message() == "new_customer":
            dispatcher.utter_message(response="utter_new_customer")

        # elif tracker.get_intent_of_latest_message() == "credit_card":
        #     dispatcher.utter_message(response="utter_credit_card")

        elif tracker.get_intent_of_latest_message() == "deposit":
            dispatcher.utter_message(response="utter_deposit")

        elif tracker.get_intent_of_latest_message() == "loan":
            dispatcher.utter_message(response="utter_loan")

        elif tracker.get_intent_of_latest_message() == "apply_now":
            dispatcher.utter_message(response="utter_apply_now")
        
        elif tracker.get_intent_of_latest_message() == "rateofinterest":
            dispatcher.utter_message(response="utter_rateofinterest")

        elif tracker.get_intent_of_latest_message() == "fee_charges":
            dispatcher.utter_message(response="utter_fee_charges")

        elif tracker.get_intent_of_latest_message() == "credit_card_products":
            dispatcher.utter_message(response="utter_credit_card_products")

        elif tracker.get_intent_of_latest_message() == "deposit_products":
            dispatcher.utter_message(response="utter_deposit_products")
        
        elif tracker.get_intent_of_latest_message() == "loan_products":
            dispatcher.utter_message(response="utter_loan_products")

        elif tracker.get_intent_of_latest_message() == "payment_solutions":
            dispatcher.utter_message(response="utter_payment_solutions")

        elif tracker.get_intent_of_latest_message() == "branches":
            dispatcher.utter_message(response="utter_branches")

        elif tracker.get_intent_of_latest_message() == "contact_center":
            dispatcher.utter_message(response="utter_contact_center")

        elif tracker.get_intent_of_latest_message() == "offers":
            dispatcher.utter_message(response="utter_offers")

        elif tracker.get_intent_of_latest_message() == "statement":
            dispatcher.utter_message(response="utter_statement")

        elif tracker.get_intent_of_latest_message() == "service_feedback":
            dispatcher.utter_message(response="utter_service_feedback")

        elif tracker.get_intent_of_latest_message() == "about_lankabangla":
            dispatcher.utter_message(response="utter_about_lankabangla")


        elif tracker.get_intent_of_latest_message() == "visacard_chequebook":
            dispatcher.utter_message(response="utter_visacard_chequebook")
            dispatcher.utter_message(response="utter_visacard_chequebook_quick_replies")

        # utter_mastercard_BEFTN
        elif tracker.get_intent_of_latest_message() == "mastercard_BEFTN":
            dispatcher.utter_message(response="utter_mastercard_BEFTN")
            dispatcher.utter_message(response="utter_mastercard_BEFTN_buttons")
            dispatcher.utter_message(response="utter_mastercard_BEFTN_quick_replies")


        # chequebook
        elif tracker.get_intent_of_latest_message() == "chequebook":
            dispatcher.utter_message(response="utter_chequebook")
            dispatcher.utter_message(response="utter_chequebook_quick_replies")

        # pin_change
        elif tracker.get_intent_of_latest_message() == "pin_change":
            dispatcher.utter_message(response="utter_pin_change")
            dispatcher.utter_message(response="utter_pin_change_text")
            dispatcher.utter_message(response="utter_pin_change_quick_replies")


        # deposit_offers
        elif tracker.get_intent_of_latest_message() == "deposit_offers":
            dispatcher.utter_message(response="utter_deposit_offers_text")
            dispatcher.utter_message(response="utter_deposit_offers_buttons")
            dispatcher.utter_message(response="utter_deposit_offers_quick_replies")

            
        # lankabangla_management
        elif tracker.get_intent_of_latest_message() == "lankabangla_management":
            print("lankabangla_management intent actions")
            dispatcher.utter_message(response="utter_lankabangla_management")

        # utter_LBFL_offers
        elif tracker.get_intent_of_latest_message() == "LBFL_offers":
            dispatcher.utter_message(response="utter_LBFL_offers")
            dispatcher.utter_message(response="utter_LBFL_offers_quick_replies")

        # no_data_found
        elif tracker.get_intent_of_latest_message() == "no_data_found":
            dispatcher.utter_message(response="utter_no_data_found")

    
        return []
