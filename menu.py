import requests

while(True):
    print("-------------TO CONTINUE PRESS: A-------------\n-------------TO QUIT PRESS: ANY OTHER KEY-------------")
    choice = input().lower().rstrip()
    if choice == "a":
        print("-------------Enter required fields in order-------------")
        location_info = str(input("Location: ").rstrip())
        maxresult_info = int(input("Maximum nuber of results: ").rstrip())
        url = "https://developers.zomato.com/api/v2.1/search?entity_type=city&q=" + location_info + "&count=" + str(maxresult_info) + "&order=asc"
        headers = {"user-key": "8d239e786498ac4aa890cbe688628e4d"}
        html = requests.get(url, headers=headers)
        html_json = html.json()
        resturant_details = html_json['restaurants']
        for x in html_json['restaurants']:
            print(x['restaurant']['name'] + " :" + x['restaurant']['phone_numbers'])
    else:
        break