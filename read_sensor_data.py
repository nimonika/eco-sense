import requests
import json


def get_agrimetrics_data_for_field():
    facts_endpoint = "https://api.agrimetrics.co.uk/field-facts/gcpwz8b1b"
    trends_endpoint = "https://api.agrimetrics.co.uk/field-trends/gcpwz8b1b"
    res = requests.get(
        facts_endpoint, headers= {"Ocp-apim-subscription-key":"763da909b13044f8b4dbe0f334db2df9"})
    response = res.json()
    for item in  response["hasSoilLayer"]:
        print(item)

    res = requests.get(
        trends_endpoint, headers={"Ocp-apim-subscription-key": "763da909b13044f8b4dbe0f334db2df9"})
    response = res.json()
    print(response["hasSownCrop"])




get_agrimetrics_data_for_field()
