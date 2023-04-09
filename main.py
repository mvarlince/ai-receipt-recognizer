import json

# import azure form recognizer libraries
from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormContentType
from azure.ai.formrecognizer import FormRecognizerApiVersion
from azure.ai.formrecognizer import FormField

# create the client and authenticates wuth the endpoint and key