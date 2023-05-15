import config

# import azure form recognizer libraries
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.exceptions import ResourceNotFoundError

# create the client and authenticates with the endpoint and key
endpoint = config.AZ_FORM_RECOGNIZER_ENDPOINT
key = config.AZ_FORM_RECOGNIZER_KEY
form_recognizer_client = FormRecognizerClient(endpoint, AzureKeyCredential(key))

myReceiptUrl = config.RECEIPT_URL 

# use form recognizer client to recognize the receipt from myReceiptUrl
poller = form_recognizer_client.begin_recognize_receipts_from_url(myReceiptUrl)
receiptItems = poller.result()

# loop through results and extract data from results
for item in receiptItems:
    for name, field in item.fields.items():
        if name == "Items":
            print("Receipt Items:")
            for idx, items in enumerate(field.value):
                print("\n...Item #{} ".format(idx + 1))
                for item_name, item in items.value.items():
                    print("..... {}: {}  - confidence {}".format(
                        item_name, item.value, item.confidence))
        else:
            print("{}: {} has confidence {}\n".format(
                name, field.value, field.confidence))