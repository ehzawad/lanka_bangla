from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
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

class Action_Otions1(Action):

    def name(self) -> Text:
        return "action_options1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_intent_of_latest_message() == "main_node":
            dispatcher.utter_message(response="utter_main_node")
            # dispatcher.utter_message(response="utter_one_button")
            # dispatcher.utter_message(response="utter_two_button")
            # dispatcher.utter_message(response="utter_three_button")


        elif tracker.get_intent_of_latest_message() == "loan_products":
            # dispatcher.utter_message(response="utter_loan_products")
            dispatcher.utter_message(response="utter_loan_products_button_one")
            # dispatcher.utter_message(response="utter_loan_products_button_two")
            dispatcher.utter_message(response="utter_loan_products_button_three")


        elif tracker.get_intent_of_latest_message() == "credit_card_offers":
            dispatcher.utter_message(response="utter_credit_card_offers")
            dispatcher.utter_message(response="utter_credit_card_offers_button_one")
            dispatcher.utter_message(response="utter_credit_card_offers_button_two")
            dispatcher.utter_message(response="utter_credit_card_offers_quick_replies")

        elif tracker.get_intent_of_latest_message() == "demo":
            return [FollowupAction("detail_form")]
        
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



        return []
    

class Action_Otions2(Action):

    def name(self) -> Text:
        return "action_options2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_intent_of_latest_message() == "banking":
            dispatcher.utter_message(response="utter_banking")
        
        elif tracker.get_intent_of_latest_message() == "insurance":
            msg="gPlex gives service in the field of insurance using ai which \
automates tasks like claims processing, customer inquiries, and risk \
assessment. It enhances efficiency, improves customer experience, and helps \
detect fraud by analyzing data and identifying patterns."
            dispatcher.utter_message(text=msg)  

        elif tracker.get_intent_of_latest_message() == "contact_centre_ai":
            msg="gPlex automates tasks such as managing customer queries, \
directing calls, and offering support in a contact center. \
It boosts efficiency, improves the customer experience, and provides insights \
from interactions to help refine services and strategies."
            dispatcher.utter_message(text=msg)     

        elif tracker.get_intent_of_latest_message() == "other":
            msg="For futher information call at +1 (972) 318-2900 or mail at sales@gplex.com"
            dispatcher.utter_message(text=msg)     

        elif tracker.get_intent_of_latest_message() == "voice":
            dispatcher.utter_message(response="utter_voice")

        elif tracker.get_intent_of_latest_message() == "messaging":
            dispatcher.utter_message(response="utter_messaging")

        elif tracker.get_intent_of_latest_message() == "contact_center":
            dispatcher.utter_message(response="utter_contact_center")


        elif tracker.get_intent_of_latest_message() == "exit":
            dispatcher.utter_message(text="Thank you have a good day!")
  
        return []
    
    
class Action_Otions3(Action):

    def name(self) -> Text:
        return "action_options3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_intent_of_latest_message() == "chatbot":
            dispatcher.utter_message(response="utter_chatbot")

        elif tracker.get_intent_of_latest_message() == "voicebot_disha":
            msg= "gPlex voicebot is a software powered by artificial intelligence (AI) \
that allow a caller to navigate an interactive voice response (IVR) system with their \
voice, generally using natural language."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "inbound":
            dispatcher.utter_message(response="utter_inbound")

        elif tracker.get_intent_of_latest_message() == "outbound":
            dispatcher.utter_message(response="utter_outbound")

        elif tracker.get_intent_of_latest_message() == "reporting":
            dispatcher.utter_message(response="utter_reporting")

        elif tracker.get_intent_of_latest_message() == "exit":
            dispatcher.utter_message(text="Thank you have a good day!")

        elif tracker.get_intent_of_latest_message() == "speech_to_text":
            msg="A speech recognition software that enables\
the recognition and translation of spoken language into text\
through computational linguistics."
            dispatcher.utter_message(text=msg)
        elif tracker.get_intent_of_latest_message() == "text_to_speech":
            msg= "Text-to-speech (TTS) is a type of assistive technology\
that reads digital text aloud. It's sometimes called “read aloud” technology.\
TTS can take words on a computer or other digital device and convert them into audio."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "voice_assistant":
            msg= "It is a software that carries out everyday tasks via voice command.\
 It's brings AI and machine learning together to recognize our voice and do what\
we ask it. "
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "ai_chatbot":
            dispatcher.utter_message(response="utter_ai_chatbot")

        return []



class Action_Otions4(Action):

    def name(self) -> Text:
        return "action_options4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_intent_of_latest_message() == "fintech":
            msg="Finance AI chatbot is a virtual assistant powered by \
artificial intelligence, designed to answer customer questions in a \
natural, conversational way, complete routine tasks like checking account \
balances, transfers, and bill payments, and interact with customers 24/7, \
delivering personalized and immediate support."
            dispatcher.utter_message(text=msg)
        
        if tracker.get_intent_of_latest_message() == "telecom":
            msg="AI chatbots for the telecom industry are trained to \
solve specific problems and queries from customers in that industry and \
specific companies. So, AI telecommunication chatbots can provide \
information about products, phone plans, or any other information about \
your business."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "software":
            msg="An AI chatbot in the software industry is a virtual \
assistant that talks to users through text or voice. It uses natural \
language processing (NLP) and machine learning to understand what users \
say and respond appropriately. These chatbots help with customer support, \
troubleshooting, and making software tasks easier."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "acd":
            msg="ACD (Automatic Call Distributor) call routing is a technology \
used in contact centers to distribute incoming calls to the most appropriate \
agent based on various criteria such as skill level, availability, and previous \
interactions."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "ivr":
            msg="Inbound IVR refers to the IVR type used to address customers' \
needs and queries when they call. Using this system, one can anticipate a \
caller's needs and give them access to the necessary information or support."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "sivr":
            msg="Speech Interactive Voice Response (SIVR) in inbound calls lets \
callers talk to an automated system. It understands requests and responds or \
directs the call. SIVR helps customer service lines provide information and \
solve problems without human agents."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "cti":
            msg="Computer Telephony Integration (CTI) in inbound calls links \
phone systems with computers to improve call handling. CTI is most commonly used \
by call centers handling a large number of incoming calls. CTI helps call \
centers work more efficiently and provide better customer service."
            dispatcher.utter_message(text=msg)


        elif tracker.get_intent_of_latest_message() == "predictive_dialer":
            msg="A predictive dialer in outbound calls automatically dials \
numbers from a list and connects answered calls to agents. It predicts agent \
availability and adjusts dialing to maximize productivity, commonly used in \
sales to increase call efficiency and reach more prospects."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "progressive_dialer":
            msg="Progressive dialer is a popular dialer system for outbound call \
centers that waits for agents to complete current calls before dialing the next \
number to improve connect rates and reduce call abandonment. It can increase \
agent efficiency and goal conversion rates."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "auto_dialer":
            msg="An auto dialer in outbound calls automatically dials phone \
numbers from a list and connects answered calls to agents. It speeds up the \
dialing process, saving time and ensuring agents are consistently engaged \
with potential customers. Auto dialers are commonly used in sales and marketing \
to increase call efficiency and reach a larger audience."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "call_blaster":
            msg="Call Blaster is a web-based automatic outbound dialing solution \
that enable companies to trigger automated calls to one or more people at a \
scheduled time. These messages can be customized as per your requirements, like \
marketing promotions, customer feedback, surveys, appointment reminders, etc."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "dashboard":
            msg="Dashboard reporting is a visual representation of a company's \
key performance indicators (KPIs). Using data from other reports, dashboard \
visuals provide charts and graphs to give an at-a-glance vision of your \
company's performance."
            dispatcher.utter_message(text=msg)

        elif tracker.get_intent_of_latest_message() == "wallboard":
            msg="Wallboards allow contact centers to have a visual overview of \
real-time performance. This display tool creates accountability for the \
employees and a quick summary of the status of the contact center."
            dispatcher.utter_message(text=msg)        

        elif tracker.get_intent_of_latest_message() == "unified_reporting":
            msg="Unified reporting in a contact center integrates data from \
multiple sources into one report, providing managers with a comprehensive view \
of agent performance, customer satisfaction, and operational efficiency to \
drive informed decisions and improvements."
            dispatcher.utter_message(text=msg)     

        elif tracker.get_intent_of_latest_message() == "other_report":
            msg="For futher information call at +1 (972) 318-2900 or mail at sales@gplex.com"
            dispatcher.utter_message(text=msg)     


        elif tracker.get_intent_of_latest_message() == "exit":
            dispatcher.utter_message(text="Thank you have a good day!")
  
        return []



class ValidateDetail_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_detail_form"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        print("validate_name")

        last_text = tracker.latest_message["text"]
        if len(last_text) < 5:
            return {"name": None}
        else:
            return {"name": last_text}


class Action_EndDetailForm(Action):

    def name(self) -> Text:
        return "action_end_detail_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name= tracker.get_slot("name")
        number= tracker.get_slot("number")
        company_name= tracker.get_slot("company_name")
        
        msg="Here are the info you provided:\
\nName:{name}\nNumber:{number}\nCompany Name:{company_name}. \
\nWe will contact you as soon as possible"

        dispatcher.utter_message(text=msg.format(name=name,
                                                 number=number,
                                                 company_name=company_name))

        return []







class ActionUtterTalkLLm(Action):

    def name(self) -> Text:
        return "action_utter_talkllm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last_text = tracker.latest_message.get("text")
        
        last_text = last_text.split("123_")[1]
        print(last_text)
        url = f'http://58.65.231.164:5000/llama3?text={last_text}'
        
        response = requests.post(url)
        genText = response.json()["genText"]
        bot_response = genText
        print(bot_response)

        dispatcher.utter_message(text = bot_response)
        
        # dispatcher.utter_message(text="Hi there, this is Disha with LLM power. How can I help you?")

        return []

class ActionValidateTalkToLLm(FormValidationAction):
    """validate_end_llm"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "validate_talk_to_llm_form"

    
    async def validate_end_llm(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        print("validate_end_llm")
    
        endLLm = tracker.get_slot('end_llm')
        last_text = tracker.latest_message.get("text")
        
        # print("********** ", endLLm)
        
        if last_text == "end_llm":
            #dispatcher.utter_message(text = "Thank you for using out LLM")
            dispatcher.utter_message(text = "LLM not available")
            return {"end_llm": endLLm, "requested_slot": None}
        else:
            url = f'http://58.65.231.164:5000/llama3?text={last_text}'
            ### LLM ##########
            # url = f'http://192.168.10.97:5000/llama3?text={last_text}'
            response = requests.post(url)
            genText = response.json()["genText"]
            bot_response = genText
            print(bot_response)
        
            dispatcher.utter_message(text = bot_response)
            return {"end_llm": None, "requested_slot": "end_llm"}
        

class ActionUtterLocation(Action):

    def name(self) -> Text:
        return "action_utter_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message="Our office is located in Mirpur.\
You can find us at House 8, Road 4, Section 11,Mirpur, Dhaka, Bangladesh"
        dispatcher.utter_message(text = message)
        
        return []
    


class ActionUtterCeo(Action):

    def name(self) -> Text:
        return "action_utter_ceo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message="Khondaker Shahadat Hossain is the CEO of Genuity Systems Ltd.\
He is one of the co-founders of Genuity Systems Ltd.\
He has 25 years of experienced in the IT industry.\
Started professional career in 1998 with Proshika Computer Systems\
- PCS (ProshikaNet), a renowned ISP in Bangladesh."
        dispatcher.utter_message(text = message)
        
        return []


class ActionUtterServicesOrProducts(Action):

    def name(self) -> Text:
        return "action_utter_services_or_products"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        link_AI_contact_center="https://gplex.ai/aivoice_bot"
        link_AI_voiceBot= "https://gplex.ai/aivoice_bot"
        link_AI_chatbot="https://gplex.ai/aichat_bot"
        #link_voice_banking=""
        #link_Voice_Analytics=""

        message="Hey...glad to know that you are interested in our products. Here is a list of our provided servicves:\
\n1. AI contact center: gPlex AI CCT, an AI-based contact center solution. To know more follow the link {link_AI_contact_center} .\
\n2. AI VoiceBot - DISHA: VoiceBot are AI powered software that enable callers to navigate with their voice.\
To know more follow the link {link_AI_voiceBot} .\
\n3. AI ChatBot : A computer program designed to have conversations with human. To delve deeper follow the link {link_AI_chatbot} ."
        dispatcher.utter_message(text = message.format(link_AI_contact_center = link_AI_contact_center,
                                                       link_AI_voiceBot = link_AI_voiceBot,
                                                       link_AI_chatbot=link_AI_chatbot))
        
        return []
    

# class ActionUtterUseCases(Action):

#     def name(self) -> Text:
#         return "action_utter_use_cases"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         link_financial_services="https://gplex.ai/financial"
#         link_Healthcare_Services="https://gplex.ai/health"
#         link_retail_and_ecommerce="https://gplex.ai/retail"
#         link_govt_services="https://gplex.ai/govt"
#         link_telecom_industry="https://gplex.ai/telecom"                         
                                                 

#         message = "Hey..glad to know that you want to explore more. Here are some use cases of our provided products:\
# \n1. Financial Services: AI-driven Voicebots can handle repetitive customer questions,\
# reducing the workload on human employees. To explore\
# further follow the link {link_financial_services}.\
# \n2. Healthcare Services: Our suite of AI solutions, including AI VoiceBoT, AI ChatBoT, and AI Contact\
# Center Technology, is designed to streamline operations, improve patient\
# engagement, and support healthcare professionals. For further exploration follow the link {link_Healthcare_Services}.\
# \n3. Retail & E-Commerce: gPlex AI revolutionizes customer service with the help of AI VoiceBots,\ AI ChatBots,\
# AI Contact Center Technology and AI Voice Analytics To explore more follow {link_retail_and_ecommerce}.\
# \n4. Governmental Services:  provide innovative solutions that streamline communications,\
# enhance public service delivery, and optimize operational efficiency for the Government. \
# For further exploration follow {link_govt_services}\
# \n5. Telecom Industry :  Telecom businesses take up artificial intelligence (AI) technology to try\
# to reduce operational costs, increase efficiency. For exploring further follow {link_telecom_industry}."

#         dispatcher.utter_message(text = message.format(link_financial_services=link_financial_services,
#                                                        link_Healthcare_Services=link_Healthcare_Services,
#                                                        link_retail_and_ecommerce=link_retail_and_ecommerce,
#                                                        link_govt_services=link_govt_services,
#                                                        link_telecom_industry=link_telecom_industry))
        
#         return []

# class ActionUtterWhyChooseGplex(Action):

#     def name(self) -> Text:
#         return "action_utter_why_choose_gplex"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         message="Here are some reasons for you to choose us:\
# \n1. gplex ai helps you to empower your business\
# \n2. gplex ai can help to boost your sales conversion rates by 25%\
# \n3. We provide you with automated quality assurance\
# \n4. Our services helps to provide your customers exceptional experience.\
# \n5. gles ai helps to amplify the performance of yout team \
# \n6. gPlex AI dynamically adjusts agent displays in response to customer inquiries, streamlining complex processes for better engagement."
#         dispatcher.utter_message(text = message)
        
#         return []

# class ActionUtterAboutClients(Action):

#     def name(self) -> Text:
#         return "action_utter_about_clients"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         message="Some of our valued customers:\
# \n1. ROBI AXIATA: gPlex implemented CIVR for Robi Axiata to improve customer experience.\
# \n2. BDJOBS : Bdjobs selected gPlex AI to improve their customer experience.\
# \n3. MINISTRY OF LAND: Govt. of Bangladesh (Land) selects gPlex AI voicebot & voice notify solution."
#         dispatcher.utter_message(text = message)
        
#         return []

# class ActionUtterClientFeedback(Action):

#     def name(self) -> Text:
#         return "action_utter_client_feedback"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         message = 'We place a high value on our clients\' feedback and take it seriously. Providing you some client responses:\
# \n1. "Great Service..easy to use, quick help and response if needed, lots of interesting user friendly features." -\
# feedback given by MD, LangkaBangla Finance PLC\
# \n2. "Very stable and robust service..We are using gPlex Contact Center with satisfaction since 2018 to conduct \
# business operations with smart features." - said by CIO, Robi Axiata Ltd.\
# \n3. "Outstanding experience" - feedback from MD, Mutual Trust Bank PLC'

#         dispatcher.utter_message(text = message)
        
#         return []
  
# class ActionUtterContactInfo(Action):

#     def name(self) -> Text:
#         return "action_utter_contact_info"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         message="To contact us dial at +1 (972) 318-2900 or mail at sales@gplex.com"
#         dispatcher.utter_message(text = message)
        
#         return []
  
# class ActionUtterUsedTechnology(Action):

#     def name(self) -> Text:
#         return "actio_utter_used_technology"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         link_speech_recognition= "https://gplex.ai/gplex_asr"
#         link_speech_to_text= "https://gplex.ai/gplex_stt"
#         link_text_to_speech= "https://gplex.ai/gplex_tts"
#         link_nlu= "https://gplex.ai/gplex_nlu"
        
#         message='Hey..glad to see your enthusiasm. Here is a list of the technologies we use:\
# \n1. Speech Recognition : Speech recognition technology is capable of converting spoken language (an audio signal) into written text.\
# For further information {link_speech_recognition} .\
# \n2. Speech-to-Text : Speech to text is essentially speech recognition software, often based on Artificial Intelligence.\
# To explore more follow the link {link_speech_to_text} .\
# \n3. Text-to-Speech : An assistive technology that reads digital text using AI algorithms. For further exploration follow\
# the link {link_text_to_speech} .\
# \n4. NLU : Natural language understanding uses computer software to understand input in the form of sentences using text or speech.\
# To explore more follow the link {link_nlu} '
#         dispatcher.utter_message(text = message.format(link_speech_recognition=link_speech_recognition,
#                                                        link_speech_to_text=link_speech_to_text,
#                                                        link_text_to_speech=link_text_to_speech,
#                                                        link_nlu=link_nlu))
        
#         return []
    



