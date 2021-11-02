import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
from flask import Flask

app=Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

DIALOGFLOW_PROJECT_ID = 'skilletscreatary-swwq'
DIALOGFLOW_LANGUAGE_CODE = 'th'
SESSION_ID = 'me'

text_to_be_analyzed = "นัดติวฟิสิกส์วันเสาร์นี้แปดโมงเช้า"

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
query_input = dialogflow.types.QueryInput(text=text_input)
try:
    response = session_client.detect_intent(session=session, query_input=query_input)
except InvalidArgument:
    raise

# print("Query text:", response.query_result.query_text)
# print("Detected intent:", response.query_result.intent.display_name)
# print("Detected intent confidence:", response.query_result.intent_detection_confidence)
# print("Fulfillment text:", response.query_result.fulfillment_text)


@app.route('/')
def Querytext():
    result1=response.query_result.query_text
    return result1
@app.route('/intent')
def Intent():
    result2=response.query_result.intent.display_name
    return result2
@app.route('/confidence')
def Confidence():
    result3=response.query_result.intent_detection_confidence
    return result3
@app.route('/fullfillment')
def Fullfillmant():   
    result4=response.query_result.fulfillment_text
    return result4

# @app.route('/')
# def trans():
#     result1=response.query_result.query_text
#     result2=response.query_result.intent.display_name
#     result3=response.query_result.intent_detection_confidence
#     result4=response.query_result.fulfillment_text
#     return result4
if __name__ == '__main__':
    app.run()
  