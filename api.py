import requests
import json

class API:
    def __init__(self, url):
        self.url=url

    def get_request(self):
        response = requests.get(url=self.url)
        print(response.status_code)
        return response.json()
    def post_request(self, data):
        response = requests.post(url=self.url, json=data)
        print(response.status_code)
        return response.json()
    def put_request(self, data):
        response=requests.put(url=self.url, json=data)
        print(response.status_code)
        return response.json()
    def delete_request(self):
        response=requests.delete(url=self.url)
        print(response.status_code)
        return response.json()

obj_api = API(url="https://jsonplaceholder.typicode.com/posts/1")

print("GET request")
response = obj_api.get_request()
print(json.dumps(response, indent=2))

data={
    "userId": 2,
    "id": 3
}
print("POST request")
response = obj_api.post_request(data=data)
print(response)

data={
    "body": "How are you"
}
print("PUT request")
response = obj_api.put_request(data=data)
print(response)

print("DELETE request")
response = obj_api.delete_request()
print(response)