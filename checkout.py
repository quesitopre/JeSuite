import requests

url = 'https://api.makcorps.com/free/london'
headers = {
    'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MTc2NzczNjAsImlkZW50aXR5IjozLCJuYmYiOjE1MTc2NzczNjAsImV4cCI6MTUxNzY3OTE2MH0.ytSqQj3VDymEaJz9EIdskWELwDQZRD1Dbo6TuHaPz9U'
}

response = requests.get(url, headers=headers)

# Print the response
print(response.json())

# class for checkout Process 
#class CheckoutClick(self):
print("Checkout Clicked")
    