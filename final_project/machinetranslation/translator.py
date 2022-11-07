'''
Module to translate from english to french and from french to english.
Uses IBM Watson language translator.
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    '''Takes the string in english and translates it to french'''
    #write the code here
    try:
        french_text = language_translator.translate(text=english_text, model_id='en-fr')
        french_text = french_text.get_result()
        french_text = french_text['translations'][0]['translation']
    except Exception:
        french_text = "Error: Try again"
    return french_text

def french_to_english(french_text):
    '''Takes the string in french and translates it to english'''
    #write the code here
    try:
        english_text = language_translator.translate(text=french_text, model_id='fr-en')
        english_text = english_text.get_result()
        english_text = english_text['translations'][0]['translation']
    except Exception:
        english_text = "Erreur : réessayez"
    return english_text
