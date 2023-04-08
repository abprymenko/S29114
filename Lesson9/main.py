# import urllib.request
# opener = urllib.request.build_opener()
# response = opener.open ("https://httpbin.org/get")
# print(response.read())

import requests
# response = requests.get("https://httpbin.org/get")
# print(response.content)
# print(response.text)
counter_key = 0
res_pars_list = {}
response = requests.get("https://coinmarketcap.com/")
if(response.status_code == 200):
    response_text = response.text
    response_parse = response_text.split("<span>")
    for parse_elem_1 in response_parse:
        if parse_elem_1.startswith("$"):
            sequence = parse_elem_1.split("</span>")
            for parse_elem_2 in sequence:
                if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                    res_pars_list[counter_key] = parse_elem_2
                    counter_key +=1
    print(res_pars_list)
    for key, value in res_pars_list.items():
        print(f"{key} - {value}")
    #print(f'Bitcoin BTC - {res_pars_list[0]}')
else:
    print("status code not 200")
