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

        home_location = streetaddress + ", " + city + ", " + state

        #Removed API for GitHub (Add in your own key here)
        API_KEY = ""

        map_client = googlemaps.Client(API_KEY)

        location_name = "COVID-19 Vaccine"

        response = map_client.places(query=home_location)

        for i in range(6):
            latitude = response['results'][0]['geometry']['location']['lat']
            longitude = response['results'][0]['geometry']['location']['lng']

        response = map_client.places(query=location_name, location=(latitude,longitude))

        name_array = []
        address_array = []
        photo_ref_array = []  
        phone_numbers_array = []
        website_array = []

        for i in range(6):
            name_array.append((response["results"][i]["name"]))
            address_array.append((response["results"][i]["formatted_address"]))

            try:
                photo_ref = ((response["results"][i]["photos"][0]['photo_reference']))
                img_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_ref}&sensor=false&key=AIzaSyDVKqdtzC0GmyYJBcjLCpbea_BMZ58lo4k"
                photo_ref_array.append(img_url)
            except:
                photo_ref_array.append("https://149362684.v2.pressablecdn.com/wp-content/uploads/COVID-Vaccine-Graphic.png")


        for i in range(6):
            my_place_id = response['results'][i]['place_id']
            my_fields = ['formatted_phone_number', 'website']

            phone_numbers_array.append((map_client.place(place_id=my_place_id, fields=my_fields))['result']['formatted_phone_number'])

            try:
                website_array.append((map_client.place(place_id=my_place_id, fields=my_fields))['result']['website'])
            except:
                "https://covvax.herokuapp.com/"

    
        return(render_template('index.html', address_array=address_array, name_array=name_array, photo_ref_array=photo_ref_array, phone_numbers_array=phone_numbers_array, website_array=website_array))


