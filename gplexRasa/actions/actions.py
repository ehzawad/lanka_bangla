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
import random
import time


#   - main_node
#   - product_information
#   - read_privacy_policy
#   - existing_customer
#   - new_customer
#   - credit_card
#   - deposit
#   - loan
#   - apply_now


class ActionPrintInfo(Action):
    def name(self) -> Text:
        return "action_print_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Print the information
        print(f"Next Action: {tracker.get_intent_of_latest_message()}")
        print(f"Sender ID: {tracker.sender_id}")
        print(f"Tracker: {tracker.current_state()}")
        print(f"Domain: {domain}")

        # check if it inside an active loop
        if tracker.active_loop:
            print(f"Active Loop: {tracker.active_loop}")
            

        # You can also send a message to the user if needed
        dispatcher.utter_message(text="Information printed to console")

        return []

# action_service_type_credit_card
class ActionServiceType(Action):
    def name(self) -> Text:
        return "action_service_type_credit_card"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # if service_type is None, then set it to credit_card
        print("action_service_type_credit_card")
        service_type = tracker.get_slot("service_type")
        if service_type is None:
            service_type = "credit_card"
            return [SlotSet("service_type", service_type)]
        else:
            return []
        
# action_service_type_deposit
class ActionServiceTypeDeposit(Action):
    def name(self) -> Text:
        return "action_service_type_deposit"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # if service_type is None, then set it to credit_card
        print("action_service_type_deposit")
        service_type = tracker.get_slot("service_type")
        if service_type is None:
            service_type = "deposit"
            return [SlotSet("service_type", service_type)]
        else:
            return []
        
# action_service_type_loan
class ActionServiceTypeLoan(Action):
    def name(self) -> Text:
        return "action_service_type_loan"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # if service_type is None, then set it to credit_card
        print("action_service_type_loan")
        service_type = tracker.get_slot("service_type")
        if service_type is None:
            service_type = "loan"
            return [SlotSet("service_type", service_type)]
        else:
            return []


class BankAPI:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.base_url = 'http://192.168.214.6/ccmw'
        self.secret = 'PVFzWnlWQmJsdkNxQUszcWJrbFlUNjJVREpVMXR6R09kTHN5QXNHYSt1ZWM='
        self.otp_store = {}
        self.otp_validity = 300  # 5 minutes

    def generate_otp(self) -> str:
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])

    def store_otp(self, phone_number: str, otp: str):
        expiration_time = time.time() + self.otp_validity
        self.otp_store[phone_number] = {'otp': otp, 'expiration': expiration_time}

    def verify_otp(self, phone_number: str, user_input: str) -> bool:
        if phone_number not in self.otp_store:
            return False
        stored_data = self.otp_store[phone_number]
        if time.time() > stored_data['expiration']:
            del self.otp_store[phone_number]
            return False
        if user_input == stored_data['otp']:
            del self.otp_store[phone_number]
            return True
        return False

    def send_otp(self, phone_number: str) -> Dict[str, Any]:
        otp = self.generate_otp()
        print(f"Generated OTP: {otp}")
        self.store_otp(phone_number, otp)
        url = f'{self.base_url}/notification/common-api-sms-function'
        params = {
            'sercret': self.secret,
            'rm': 'I',
            'callid': '124534654',
            'connname': 'MWGCLSMS',
            'cli': phone_number,
            'sid': 'LBFPLC',
            'ncode': 'SNDOTP', # SNDOTP
            'sivrlnk': otp,
            'csms_id': f'4473433434pZ{otp}'
        }
        try:
            response = requests.get(url, params=params)
            data = response.json()
            if data and isinstance(data, list) and len(data) > 0:
                result = data[0]
                if result.get('status') == 'SUCCESS':
                    return {'success': True, 'message': 'OTP sent successfully'}
                else:
                    return {'success': False, 'message': 'Failed to send OTP'}
            else:
                return {'success': False, 'message': 'Invalid response from SMS API'}
        except requests.exceptions.RequestException as e:
            return {'success': False, 'message': f"Error sending OTP: {str(e)}"}
        

    def fetch_api_data(self, cli: str, terid: str) -> Dict[str, Any]:
        url = f'{self.base_url}/card/common-api-function'
        params = {
            'sercret': self.secret,
            'rm': 'I',
            'callid': '12324243433',
            'connname': 'MWGCAAMB',
            'cli': cli,
            'terid': terid
        }
        try:
            response = requests.get(url, params=params)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching API data: {str(e)}")
            return None

    def process_api_data(self, data: List[Dict[str, Any]], category: str) -> List[Dict[str, Any]]:
        if not data or not isinstance(data[0], dict):
            print(f"Invalid data format for {category}")
            return []
        
        response_data = data[0].get('responseData', [])
        
        if not response_data:
            print(f"No response data available for {category}")
            return []

        processed_data = [
            {
                'Account': account.get('Account', ''),
                'Name': account.get('Name', ''),
                'Date': account.get('Date', ''),
                'MinimumAmount': account.get('MinimumAmount', ''),
                'Amount': account.get('Amount', ''),
                'ClientId': account.get('ClientId', ''),
                'AccountNumber': account.get('AccountNumber', '')
            } for account in response_data
        ]
        
        return processed_data

    def get_account_data(self, cli: str, categories: List[str]) -> Dict[str, List[Dict[str, Any]]]:
        result = {}
        for category in categories:
            data = self.fetch_api_data(cli, category)
            if data:
                processed_data = self.process_api_data(data, category)
                result[category] = processed_data
            else:
                print(f"Failed to fetch data for {category}")
        return result

    def get_master_data(self, cli: str) -> List[Dict[str, Any]]:
        data = self.fetch_api_data(cli, 'Master')
        return self.process_api_data(data, 'Master')

    def get_visa_data(self, cli: str) -> List[Dict[str, Any]]:
        data = self.fetch_api_data(cli, 'VISA')
        return self.process_api_data(data, 'VISA')

    def get_debit_data(self, cli: str) -> List[Dict[str, Any]]:
        data = self.fetch_api_data(cli, 'Debit')
        return self.process_api_data(data, 'Debit')

    def get_loan_data(self, cli: str) -> List[Dict[str, Any]]:
        data = self.fetch_api_data(cli, 'Loan')
        return self.process_api_data(data, 'Loan')




# Initialize BankAPI
bank_api = BankAPI()




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
        """Validate `otp_sender_sms` value and send OTP."""
        name = clean_name(slot_value)
        print("Validating otp_sender_sms")
        print(name)
        print("intent name", end=" ")
        print(tracker.get_intent_of_latest_message())
        # print(tracker.latest_message['intent']['name'])

        if len(name) != 11:
            dispatcher.utter_message(text="The number should be a valid BD number, and it has to be 11 digits long.")
            return {"otp_sender_sms": None}



        # Send OTP
        result = bank_api.send_otp(name)
        if result['success']:
            dispatcher.utter_message(text="OTP sent successfully. Please check your phone and enter the OTP.")
            return {"otp_sender_sms": name}
        else:
            dispatcher.utter_message(text=f"Failed to send OTP: {result['message']}")
            return {"otp_sender_sms": None}

    def validate_otp(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `otp` value, verify OTP, and fetch credit card data."""
        name = clean_name(slot_value)
        print("Validating otp")
        print(name)

        if len(name) != 6:
            dispatcher.utter_message(text="The OTP should be 6 digits long.")
            return {"otp": None}

        otp_sender_sms = tracker.get_slot("otp_sender_sms")

        # check if it is inside an active loop
        if tracker.active_loop:
            print(f"Active Loop in validate_otp: {tracker.active_loop}")
        
        # Verify OTP
        if bank_api.verify_otp(otp_sender_sms, name):


            service_type = tracker.get_slot("service_type") or "requested"
            text2 = f"OTP verified successfully. Fetching your {service_type} information..."
            dispatcher.utter_message(text=text2)
            
            # Fetch account data
            account_data = bank_api.get_account_data(otp_sender_sms, ['Master', 'VISA', 'Deposit', 'Loan'])

            # print intent name
            print("intent name", end=" ")
            print(tracker.latest_message['intent']['name'])
            # Process and display the fetched account data
            
            # if service_type is credit_card
            if tracker.get_slot("service_type") == "credit_card":

                self.display_credit_card_data(dispatcher, account_data.get('Master', []), account_data.get('VISA', []))
            elif tracker.get_slot("service_type") == "deposit":
                self.display_deposit_data(dispatcher, account_data.get('Deposit', []))
            elif tracker.get_slot("service_type") == "loan":
                self.display_loan_data(dispatcher, account_data.get('Loan', []))
            else:
                dispatcher.utter_message(text="No data found for the selected service type.")

            return {"otp": name, "otp_verified": True}
        else:
            dispatcher.utter_message(text="Invalid OTP. Please try again.")
            return {"otp": None}
        

    def display_deposit_data(self, dispatcher: CollectingDispatcher, deposit_data):
        if deposit_data:
            dispatcher.utter_message(text="Deposit Account Information:")
            for account in deposit_data:
                dispatcher.utter_message(text=f"Account Number: {account['AccountNumber']}")
                dispatcher.utter_message(text=f"Account Name: {account['Name']}")
                dispatcher.utter_message(text=f"Balance: {account['Amount']}")
                if account.get('Date'):
                    dispatcher.utter_message(text=f"Last Transaction Date: {account['Date']}")
                dispatcher.utter_message(text="------------------------")
        else:
            dispatcher.utter_message(text="No deposit account information found for your account.")

    def display_loan_data(self, dispatcher: CollectingDispatcher, loan_data):
        if loan_data:
            dispatcher.utter_message(text="Loan Account Information:")
            for account in loan_data:
                dispatcher.utter_message(text=f"Loan Account Number: {account['AccountNumber']}")
                dispatcher.utter_message(text=f"Loan Type: {account['Name']}")
                dispatcher.utter_message(text=f"Outstanding Amount: {account['Amount']}")
                dispatcher.utter_message(text=f"Minimum Due: {account['MinimumAmount']}")
                if account.get('Date'):
                    dispatcher.utter_message(text=f"Due Date: {account['Date']}")
                dispatcher.utter_message(text="------------------------")
        else:
            dispatcher.utter_message(text="No loan account information found for your account.")    

    def display_credit_card_data(self, dispatcher: CollectingDispatcher, master_data, visa_data):
        has_credit_card = False

        # Display Master card data
        if master_data:
            has_credit_card = True
            dispatcher.utter_message(text="Master Card Information:")
            for account in master_data:
                dispatcher.utter_message(text=f"Account: {account['Account']}")
                dispatcher.utter_message(text=f"Balance: {account['Amount']}")
                dispatcher.utter_message(text=f"Minimum Amount Due: {account['MinimumAmount']}")
                if account.get('Date'):
                    dispatcher.utter_message(text=f"Due Date: {account['Date']}")
                dispatcher.utter_message(text="------------------------")
        
        # Display Visa card data
        if visa_data:
            has_credit_card = True
            dispatcher.utter_message(text="Visa Card Information:")
            for account in visa_data:
                dispatcher.utter_message(text=f"Account: {account['Account']}")
                dispatcher.utter_message(text=f"Balance: {account['Amount']}")
                dispatcher.utter_message(text=f"Minimum Amount Due: {account['MinimumAmount']}")
                if account.get('Date'):
                    dispatcher.utter_message(text=f"Due Date: {account['Date']}")
                dispatcher.utter_message(text="------------------------")
        
        if not has_credit_card:
            dispatcher.utter_message(text="No credit card information found for your account.")

        dispatcher.utter_message(text="Is there anything else you would like to know about your credit card?")
    

class ActionResetOtpFormSlots(Action):
    def name(self) -> Text:
        return "action_reset_otp_form_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("action_reset_otp_form_slots")
        print(tracker.slots)
        return [SlotSet(slot_name, None) for slot_name in ["otp_sender_sms", "otp", "otp_verified", "service_type"]]


class Action_Otions1(Action):

    def name(self) -> Text:
        return "action_options1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_intent_of_latest_message() == "main_node":
            dispatcher.utter_message(response="utter_main_node_text")
            dispatcher.utter_message(response="utter_main_node")


        elif tracker.get_intent_of_latest_message() == "credit_card_status":
            # print all the slots
            print(tracker.slots)
            dispatcher.utter_message(response="utter_credit_card_status_text")
            dispatcher.utter_message(response="utter_credit_card_status_quick_replies")

        # deposit_status
        elif tracker.get_intent_of_latest_message() == "deposit_status":
            dispatcher.utter_message(response="utter_deposit_status_text")
            dispatcher.utter_message(response="utter_deposit_status_quick_replies")

        # loan_status
        elif tracker.get_intent_of_latest_message() == "loan_status":
            dispatcher.utter_message(response="utter_loan_status_text")
            dispatcher.utter_message(response="utter_loan_status_quick_replies")

        elif tracker.get_intent_of_latest_message() == "credit_card_email":
            dispatcher.utter_message(text="credit card email")

        elif tracker.get_intent_of_latest_message() == "loan_products":

            dispatcher.utter_message(response="utter_loan_products_button_one")
            dispatcher.utter_message(response="utter_loan_products_button_two")
            dispatcher.utter_message(response="utter_loan_products_button_three")
            dispatcher.utter_message(response="utter_loan_products_button_four")
            dispatcher.utter_message(response="utter_loan_products_button_five")
            dispatcher.utter_message(response="utter_loan_products_button_six")



        elif tracker.get_intent_of_latest_message() == "credit_card_offers":

            dispatcher.utter_message(response="utter_credit_card_offers_button_one")
            dispatcher.utter_message(response="utter_credit_card_offers_button_two")
            dispatcher.utter_message(response="utter_credit_card_offers_quick_replies")

        elif tracker.get_intent_of_latest_message() == "deposit_products":

            dispatcher.utter_message(response="utter_deposit_products_buttons")
            dispatcher.utter_message(response="utter_deposit_products_quick_replies")


        
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


        elif tracker.get_intent_of_latest_message() == "existing_customer":
            print("existing_customer intent actions")
            dispatcher.utter_message(response="utter_existing_customer")

        elif tracker.get_intent_of_latest_message() == "new_customer":
            # dispatcher.utter_message(response="utter_new_customer_buttons")
            dispatcher.utter_message(response="utter_new_customer_quick_replies")

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
