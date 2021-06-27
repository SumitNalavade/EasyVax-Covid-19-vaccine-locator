from flask import Flask, render_template, request
import googlemaps

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home_page():
    return render_template("index.html")


@app.route('/send', methods=['POST'])
def send():
    if(request.method == 'POST'):
        streetaddress = request.form['streetaddress']
        city = request.form['city']
        state = request.form['state']

        home_location = f'{streetaddress}, {city}, {state}'

        #Removed API for GitHub (Add in your own key here)
        API_KEY = ""

        map_client = googlemaps.Client(API_KEY)

        location_name = "COVID-19 Vaccine"

        response = map_client.places(query=home_location)

        for i in range(6):
            latitude = response['results'][0]['geometry']['location']['lat']
            longitude = response['results'][0]['geometry']['location']['lng']

        response = map_client.places(
            query=location_name, location=(latitude, longitude))

        location_array = []

        class location():
            def __init__(self, name, address, photo, phone_number, website):
                self.name = name
                self.address = address
                self.photo = photo
                self.phone_number = phone_number
                self.website = website

        for i in range(6):
            name = (response["results"][i]["name"])
            address = (response["results"][i]["formatted_address"])

            try:
                photo_ref = (
                    (response["results"][i]["photos"][0]['photo_reference']))
                img_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_ref}&sensor=false&key=AIzaSyDVKqdtzC0GmyYJBcjLCpbea_BMZ58lo4k"
                photo = (img_url)
            except:
                photo = (
                    "https://149362684.v2.pressablecdn.com/wp-content/uploads/COVID-Vaccine-Graphic.png")

            my_place_id = response['results'][i]['place_id']
            my_fields = ['formatted_phone_number', 'website']

            phone_number = ((map_client.place(place_id=my_place_id, fields=my_fields))[
                            'result']['formatted_phone_number'])

            try:
                website = (map_client.place(place_id=my_place_id, fields=my_fields))[
                    'result']['website']
            except:
                website = "https://covvax.herokuapp.com/"

            location_array.append(
                location(name, address, photo, phone_number, website))

        return(render_template('index.html', location_array=location_array))
