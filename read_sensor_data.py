import requests
import json
import csv


def get_agrimetrics_data_for_field():
    facts_endpoint = "https://api.agrimetrics.co.uk/field-facts/u120f79yd"
    trends_endpoint = "https://api.agrimetrics.co.uk/field-trends/u120f79yd"
    locations_endpoint = "https://api-k8s-green-test.agrimetrics.co.uk/fields-v2?pageSize=1000"
    res = requests.get(
        facts_endpoint, headers= {"Ocp-apim-subscription-key":"763da909b13044f8b4dbe0f334db2df9"})
    response = res.json()
    print(response)
    for layer in response["hasSoilLayer"]:
        for soilLayer, value  in layer.items():
            print(soilLayer, value)



    res = requests.get(trends_endpoint, headers={"Ocp-apim-subscription-key": "763da909b13044f8b4dbe0f334db2df9"})
    response = res.json()
   # print(response["hasSownCrop"])

    # res = requests.get(locations_endpoint)
    # response = res.json()
    #
    # print(len(response["results"]))
    #
    # results=[]
    # for item in response["results"]:
    #     obj = {}
    #     obj["lat"] = item["centroid"]["lat"]
    #     obj["lon"] = item["centroid"]["lon"]
    #     obj["id"] = item["@id"].rsplit("/", 1)[1]
    #     results.append(obj)
    #
    # print(results)
    # csv_columns = ['id', 'lat', 'lon']
    # csv_file = "data.csv"
    # try:
    #     with open(csv_file, 'w') as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    #         writer.writeheader()
    #         for data in results:
    #             writer.writerow(data)
    # except IOError:
    #     print("I/O error")





get_agrimetrics_data_for_field()
