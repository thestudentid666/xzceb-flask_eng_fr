import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/f16b98ed-9c9a-4eac-b85d-436f7ba1d501')

translation = language_translator.translate( text='Hello', model_id='en-fr').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))


def englishToFrench(englishText):
    #write the code here
    translation = language_translator.translate( text = englishText , model_id='en-fr').get_result()
#print(json.dumps(translation, indent=2, ensure_ascii=False))
    print(translation['translations'][0])
#   return frenchText
    return 1
englishToFrench('''nice to meet you todayage Translator uses standard HTTP response codes to indicate whether a method completed successfully. HTTP response codes in the 2xx range indicate success. A response in the 4xx range is some sort of failure, and a response in the 5xx range usually indicates an internal system error that cannot be resolved by the user. Response codes are listed with the method.

The Python SDK generates an exception for any unsuccessful method invocation. When the Python SDK receives an error response from the Language Translator service, it generates an ApiException with the following fields.''')
def frenchToEnglish(frenchText):
    #write the code here
    translation = language_translator.translate( text = englishText , model_id='fr-en').get_result()
#print(json.dumps(translation, indent=2, ensure_ascii=False))
    print(translation['translations'][0])
    return englishText
