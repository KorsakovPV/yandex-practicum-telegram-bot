import typing

from speechkit import Session, ShortAudioRecognition, SpeechSynthesis

from config import settings
from logger import logger


def generate_voice(text: str) -> typing.BinaryIO:
    logger.info("generate_voice")
    session = Session.from_yandex_passport_oauth_token(
        settings.OAUTH_TOKEN, settings.CATALOG_ID
    )
    synthesizeAudio = SpeechSynthesis(session)
    return synthesizeAudio.synthesize_stream(text=text, voice="ermil")  # voice='oksana'


def recognize_command(data: typing.BinaryIO) -> str:
    logger.info("recognize_command")
    session = Session.from_yandex_passport_oauth_token(
        settings.OAUTH_TOKEN, settings.CATALOG_ID
    )
    recognizeShortAudio = ShortAudioRecognition(session)
    return recognizeShortAudio.recognize(data=data.read(), rawResults=True).lower()
