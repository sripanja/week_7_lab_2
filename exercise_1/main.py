import requests

fhir_id = 3
# Define the URL for the GET request
url = f'http://137.184.71.65:8080/fhir/Patient/{fhir_id}'

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Access the response content (usually JSON data)
    data = response.json()  # Use response.text for non-JSON data
    print("Data retrieved successfully!")
    print(data)
    print(f"Gender: {data['gender']}")

    first_name = data['name'][0]['given'][0]
    family_name = data['name'][0]['family']
    print(f"Given Name: {first_name}")
    print(f"Family Name: {family_name}")
    birth_date = data['birthDate']
    print(f"Birth Date: {birth_date}")


    city = data['address'][0].get('city')
    print(f"City: {city}")

else:
    print(f"Request failed with status code: {response.status_code}")