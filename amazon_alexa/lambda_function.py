from __future__ import print_function
import json
from botocore.vendored import requests

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {'type': 'PlainText', 'text': output},
        'card': {
            'type': 'Simple',
            'title': f"SessionSpeechlet - {title}",
            'content': f"SessionSpeechlet - {output}",
        },
        'reprompt': {
            'outputSpeech': {'type': 'PlainText', 'text': reprompt_text}
        },
        'shouldEndSession': should_end_session,
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Pesix's Alexa Skill. Pesix helps you to track your carbon footprint and compete with your friends for rewards. Do you want to make a payment?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please make a payment."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Psix's Alexa skill. Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))



def who_is_the_receiver(intent, session):

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    name=intent['slots']['price']['value']
    speech_output = (
        f"When do you want me to schedule your payment of {str(name)} dollars?"
    )
    reprompt_text = (
        f"When do you want me to schedule your payment of {str(name)} dollars?"
    )
    url = "https://www.jsonstore.io/54298701bfa16f8c77653c87b9008c3f3a681c74ca82c59649efc9159f910e46"
    pay={'receiver': name}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Accept': 'text/plain'
    }
    response = requests.request("POST", url, data=json.dumps(pay), headers=headers)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def what_is_the_bet(intent,session):
    
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    name=intent['slots']['date']['value']
    speech_output = f"Your payment is successfully scheduled for {name} with your Capitol One credit card. Fetching your records from the Ethereum blockchain. You are on fourth position on the leaderboard. Would you like to know more?"
    reprompt_text = f"Your payment is successfully scheduled for {name} with your Capitol One credit card. Fetching your records from the Ethereum blockchain. You are on fourth position on the leaderboard. Would you like to know more?"
    url="https://www.jsonstore.io/f69f67573b1097131a3d0dd3238f05c01eb95d943adc8ec173d9b903f0989419"
    pay={'receiver': name}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Accept': 'text/plain'
    }
    response = requests.request("POST", url, data=json.dumps(pay), headers=headers)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        

def what_is_the_committDate(intent,session):
    
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    name=intent['slots']['ans']['value']
    speech_output = "You moved from position second to fourth this month. Maybe, you should be more considerate of your consumption. Remember to turn off the lights. Imagine, how will you feel if someone turns you on and then leaves?"
    reprompt_text = "You moved from position second to fourth this month. Maybe, you should be more considerate of your consumption. Remember to turn off the lights. Imagine, how will you feel if someone turns you on and then leaves?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "Payabill":
        return who_is_the_receiver(intent, session)
    elif intent_name == "CommittDate":
        return what_is_the_bet(intent, session)
    elif intent_name == "Answer":
        return what_is_the_committDate(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name in ["AMAZON.CancelIntent", "AMAZON.StopIntent"]:
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
