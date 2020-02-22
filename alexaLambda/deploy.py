import logging
import gettext
import json
import requests
import urllib3

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractRequestInterceptor, AbstractExceptionHandler)
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response
from alexa import data

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _(data.WELCOME_MESSAGE)

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class ProdDeployIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ProdDeployIntent")(handler_input)

    def deployApplicationToProd(self):
        params = (
            ('token', 'deploytoprod'),
        )
        response = requests.get('http://user:password@1.1.1.1:8080/job/Devcon/job/prod/build', params=params)

    def handle(self, handler_input):
        _ = handler_input.attributes_manager.request_attributes["_"]
        self.deployApplicationToProd()
        speak_output = _(data.HELLO_MSG)

        return (
            handler_input.response_builder
            .speak(speak_output)
            .response
        )

class StageMyAppIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("StageMyAppIntent")(handler_input)

    def stageApplicationToProd(self):
        params = (
            ('token', 'stageapptoprod'),
        )
        response = requests.get('http://user:pass@1.1.1.1:8080/job/Devcon/job/prod/build', params=params)

    def getApprovalStatus(self):
        ApprovalFileUrl = "https://xxx.blob.core.windows.net/content/approval.json"
        
        http = urllib3.PoolManager()
        approvalData = json.loads((http.request('GET', ApprovalFileUrl)).data.decode('utf-8'))
        
        return approvalData['Approved']

    def handle(self, handler_input):
        _ = handler_input.attributes_manager.request_attributes["_"]
        stageStatus =  self.getApprovalStatus()
        if stageStatus == "true":
            print("True True")
            self.stageApplicationToProd()
            speak_output = _(data.APPROVAL_SUCCESS)
        else:
            speak_output = _(data.APPROVAL_FAIL)
         
        return (
            handler_input.response_builder
            .speak(speak_output)
            .response
        )

class HelpIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _(data.HELP_MSG)

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _(data.GOODBYE_MSG)

        return (
            handler_input.response_builder
            .speak(speak_output)
            .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        _ = handler_input.attributes_manager.request_attributes["_"]
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = _(data.REFLECTOR_MSG).format(intent_name)

        return (
            handler_input.response_builder
            .speak(speak_output)
            .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):

    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _(data.ERROR)

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class LocalizationInterceptor(AbstractRequestInterceptor):

    def process(self, handler_input):
        locale = handler_input.request_envelope.request.locale
        i18n = gettext.translation(
            'data', localedir='locales', languages=[locale], fallback=True)
        handler_input.attributes_manager.request_attributes["_"] = i18n.gettext



sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(StageMyAppIntentHandler())
sb.add_request_handler(ProdDeployIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler())

sb.add_global_request_interceptor(LocalizationInterceptor())

sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()

