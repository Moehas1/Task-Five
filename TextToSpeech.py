url = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/1b4b7b8e-f7ff-4878-af00-d8de9144d717'
apikey = 'KL50w1CmdKXZD0IkgABl3b-smGMyOcuMVcEfQ4Tj6bBb'

from ibm_cloud_sdk_core import authenticators
from ibm_watson import TextToSpeechV1

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1 (authenticator=authenticator)
tts.set_service_url(url)
with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('My Name Is Mohammed', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)

with open('m.txt', 'r') as f:
    text = f.readlines()

text = [line.replace('\n', '') for line in text]
text = ''.join(str(line) for line in text)

with open('./Mohammed.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)

