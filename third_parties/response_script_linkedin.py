import requests

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
api_key = os.environ.get('PROXYCURL_API_KEY')
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'url': 'https://www.linkedin.com/in/jonathan-a-saddler/',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

print(response.json())


#use jsonlint.com to validate the copied json file
