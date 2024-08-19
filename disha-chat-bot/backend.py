import json
from urllib import request as rqst
import uuid
import socket
from urllib.error import URLError, HTTPError

def send_message_to_rasa(session_id, message):
    sender_data = json.dumps({"sender": session_id, "message": message})
    post_data = sender_data.encode('utf-8')
    req = rqst.Request("http://192.168.214.12:5054/webhooks/rest/webhook", data=post_data)
    try:
        with rqst.urlopen(req, timeout=10) as post_resp:
            return json.loads(post_resp.read())
    except HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
    except URLError as e:
        if isinstance(e.reason, socket.timeout):
            print("Connection timed out. The server is taking too long to respond.")
        elif isinstance(e.reason, ConnectionRefusedError):
            print("Connection refused. The Rasa server might be down or not running.")
        else:
            print(f"Failed to reach the server. Reason: {e.reason}")
    except json.JSONDecodeError:
        print("Received an invalid response from the server.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def chat_session(session_id):
    print(f"Starting chat session {session_id}")
    while True:
        inputdata = input(f"You ({session_id}): ")
        if inputdata.lower() in ['exit', 'new']:
            return inputdata.lower()
        
        ai_resp = send_message_to_rasa(session_id, inputdata)
        if ai_resp is not None:
            print(f"AI ({session_id}): ", ai_resp)
        else:
            print("Failed to get a response from the AI. Please try again.")

def main():
    current_session = None
    while True:
        if not current_session:
            command = input("Enter 'new' for a new session, 'exit' to quit: ")
        else:
            command = current_session
        
        if command.lower() == 'new':
            current_session = str(uuid.uuid4())
            result = chat_session(current_session)
            if result == 'exit':
                break
            current_session = None
        elif command.lower() == 'exit':
            break
        else:
            print("Invalid command. Please enter 'new' or 'exit'.")

if __name__ == "__main__":
    main()
