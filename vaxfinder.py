import googlemaps

def find(address):
    # Removed API for GitHub (Add in your own key here)
    API_KEY = "AIzaSyDVKqdtzC0GmyYJBcjLCpbea_BMZ58lo4k"

    # Call Maps API searching for COVID-19 Vaccines near {address}
    map_client = googlemaps.Client(API_KEY)

    location_name = "COVID-19 Vaccine"

    response = map_client.places(query=address)

    # Find the latitude and longitude of the user entered address using Google GeoCoding API
    for i in range(6):
        latitude = response['results'][0]['geometry']['location']['lat']
        longitude = response['results'][0]['geometry']['location']['lng']

    response = map_client.places(
        query=location_name, location=(latitude, longitude))

    # Create array to hold future location objects
    location_array = []

        # Define a location object that takes in a name, address, photoURL, phone-number and website
    class location():
        def __init__(self, name, address, photo, phone_number, website):
            self.name = name
            self.address = address
            self.photo = photo
            self.phone_number = phone_number
            self.website = website

    # Parse through the JSON response to find the name and address
    for i in range(6):
        name = (response["results"][i]["name"])
        address = (response["results"][i]["formatted_address"])

        # Parse through the JSON response to find the photoURL
        try:
            photo_ref = (
                (response["results"][i]["photos"][0]['photo_reference']))
            img_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_ref}&sensor=false&key=AIzaSyDVKqdtzC0GmyYJBcjLCpbea_BMZ58lo4k"
            photo = (img_url)
        except:
            # If a photoURL is not present, use a stock image
            photo = (
                "https://149362684.v2.pressablecdn.com/wp-content/uploads/COVID-Vaccine-Graphic.png")

        # Find Place_id, website and phone number from JSON
        my_place_id = response['results'][i]['place_id']
        my_fields = ['formatted_phone_number', 'website']

        phone_number = ((map_client.place(place_id=my_place_id, fields=my_fields))[
                            'result']['formatted_phone_number'])

        try:
            website = (map_client.place(place_id=my_place_id, fields=my_fields))[
                'result']['website']
        except:
            # If website is not present, use stock url
            website = "https://covvax.herokuapp.com/"

        # Create location type objects using the following paramers and add it to an array of location objects
        location_array.append(
            location(name, address, photo, phone_number, website))

    return location_array