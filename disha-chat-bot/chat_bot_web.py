import json
import os
import base64
from flask import Flask, request, jsonify
from urllib import request as rqst, parse

app = Flask(__name__)

vosk_interface = os.environ.get('VOSK_SERVER_INTERFACE', '10.101.92.39')
vosk_port = int(os.environ.get('VOSK_SERVER_PORT', 5025))
vosk_model_path = os.environ.get('VOSK_MODEL_PATH', 'model')
vosk_cert_file = os.environ.get('VOSK_CERT_FILE', None)
vosk_key_file = os.environ.get('VOSK_KEY_FILE', None)
vosk_dump_file = os.environ.get('VOSK_DUMP_FILE', None)

dump_fd = None if vosk_dump_file is None else open(vosk_dump_file, "wb")
PREV_TEXT = ""

def getNumber(string):  # get number from words "জিরো ওয়ান সেভেন ফোর ফোর" = '01744'
    number = ["জিরো", "ওয়ান", "টু", "থ্রি", "ফোর", "ফাইভ", "সিক্স", "সেভেন", "এইট", "নাইন"]
    st = string.split(" ")
    wr = ""

    for i, w in enumerate(st):
        for j, n in enumerate(number):
            if w == n:
                if st[i - 1] == "ডাবল" or st[i - 1] == "ডবল":
                    wr = wr + str(j)
                if st[i - 1] == "ট্রিপল":
                    wr = wr + str(j) + str(j)
                wr = wr + str(j)

    if len(wr) > 1:
        return wr
    else:
        return string

@app.route('/')
def index():
    with open('index.html', 'r') as file:
        content = file.read()
    return content

@app.route('/message')
def message():
    output = request.args.get('output')
    sender = "01744125545"
    original_output = output
    global PREV_TEXT

    # sender_data = '{"sender":"'+sender+'","message":"'+output+'","cli": "01744125545","metadata":"bn","ivrStatus":"", "sender_id": "01744125545"}'
    sender_data = '{"sender":"'+sender+'","message":"'+output+'"}'
    # sender_data = {"sender": "default", "message": output}
    # # sender_data = '{"sender":"default","message":"'+output+'"}'
    post_data = sender_data.encode('utf-8')


    # sender_data = json.dumps({"sender": sender, "message": output})
    # post_data = sender_data.encode('utf-8')

    # print(post_data)
    ##############old code
    req = rqst.Request("http://192.168.10.78:5054/webhooks/rest/webhook", data=post_data)
    post_resp = rqst.urlopen(req)
    print(post_resp)
    ai_resp = json.loads(post_resp.read())
    print(ai_resp)
    bot_response = ai_resp[0]["text"] if len(ai_resp) > 0 else ''

    PREV_TEXT = bot_response
    dat = [{"bt": bot_response, "audio": ""}]
    return jsonify(dat)
    ##############old code

    
    # ehzawad
    # req = rqst.Request("http://192.168.10.78:5054/webhooks/rest/webhook", data=post_data)
    # post_resp = rqst.urlopen(req)
    # ai_resp = json.loads(post_resp.read())
    #
    # response_data = {
    #     "text": "",
    #     "buttons": [],
    #     "quick_replies": [],
    #     "carousel": []
    # }
    #
    # for resp in ai_resp:
    #     if "text" in resp:
    #         response_data["text"] = resp["text"]
    #     
    #     if "buttons" in resp:
    #         response_data["buttons"] = resp["buttons"]
    #     
    #     if "custom" in resp and resp["custom"]["payload"] == "quickReplies":
    #         response_data["quick_replies"] = resp["custom"]["data"]
    #
    #     if "custom" in resp and resp["custom"]["payload"] == "carousel":
    #         response_data["carousel"] = resp["custom"]["data"]
    #         
    # return jsonify(response_data)

if __name__ == '__main__':
    #context = (vosk_cert_file, vosk_key_file) if vosk_cert_file else None
    app.run(host="192.168.10.78", port=vosk_port)
