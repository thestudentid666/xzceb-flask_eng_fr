"""
assignment: translator service
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(APIKEY)
LANGUAGESVR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

LANGUAGESVR.set_service_url(URL)


def englishToFrench(txt):
    """
    this function translates English to French
    """
    result = LANGUAGESVR.translate(text=txt, model_id='en-fr').get_result()
    return result['translations'][0]['translation']


def frenchToEnglish(txt):
    """
    this function translates French to English
    """
    result = LANGUAGESVR.translate(text=txt, model_id='fr-en').get_result()
    return result['translations'][0]['translation']
