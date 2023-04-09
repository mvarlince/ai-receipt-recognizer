import config

# import azure form recognizer libraries
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.exceptions import ResourceNotFoundError

# create the client and authenticates with the endpoint and key
endpoint = config.AZ_FORM_RECOGNIZER_ENDPOINT
key = config.AZ_FORM_RECOGNIZER_KEY

# create the client and authenticate with the endpoint and key
form_recognizer_client = FormRecognizerClient(endpoint, AzureKeyCredential(key))
myReceiptUrl = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/receipt/contoso-receipt.png"

# user from recognizer client to recognize the receipt from myReceiptUrl
poller = form_recognizer_client.begin_recognize_receipts_from_url(myReceiptUrl)
receipts = poller.result()

# loop through results and extract data from results
for receipt in receipts:
    for name, field in receipt.fields.items():
        if name == "Items":
            print("Receipt Items:")
            for idx, items in enumerate(field.value):
                print("...Item #{}".format(idx + 1))
                for item_name, item in items.value.items():
                    print("......{}: {} has confidence {}".format(
                        item_name, item.value, item.confidence))
        else:
            print("{}: {} has confidence {}".format(
                name, field.value, field.confidence))
