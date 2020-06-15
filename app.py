from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """Renders the Index Route with links to Fortune, Fortune Results and Weather."""
    return render_template('index.html')

@app.route('/fortune', methods=['GET', 'POST'])
def fortune_form():
    """Renders the Fortune Route."""
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    """Renders the Fortune Results Route."""
    name = request.args.get('name')
    age = request.args.get('age')
    animal = request.args.get('animal')
    city = request.args.get('city')
    beverage = request.args.get('beverage')
    

    if users_favorite_animal == 'Chimera':
        fortune = "Change can hurt, but it leads a path to something better."
    elif users_favorite_animal == 'Dragon':
        fortune = "People are naturally attracted to you." 
    elif users_favorite_animal == "Kraken":
        fortune = "What ever you're goal is in life, embrace it visualize it, and for it will be yours."
    elif users_favorite_animal == 'Griffin':
        fortune = "Be on the lookout for coming events; They cast their shadows beforehand."
    else:
        fortune = "good luck in life!"
    return render_template('fortune_results.html', fortune = fortune)


from flask import Flask, render_template, request
import requests

# Set up 'app' variable
app = Flask(__name__)

# The App ID for the OpenWeatherMap API. This is kind of like our login
# credentials.
APP_ID = '2608f679d4594364525f6c6cc2246c79'

# The base URL of the OpenWeatherMap API.
weather_url = "https://api.openweathermap.org/data/2.5/weather"

def kelvin_to_fahrenheit(temp_kelvin):
    """Converts a temperature in degrees Kelvin to degrees Fahrenheit,
    and returns the result."""
    return temp_kelvin * 9/5 - 459.67

@app.route('/')
def homepage():
    """Return HTML content of homepage."""

    return """
    Search for your city:
    <br>
    <form action="/results" method="GET">
      <input type="text" name="city">
      <button type="submit">Search</button>
    </form>
    """

@app.route('/results')
def results_page():
    """Return HTML content of results page showing a city's temperature."""

    # Get the user's city from the URL's query string (i.e. whatever was entered
    # in the previous page's form)
    users_city = request.args.get('city')

    # Make a dictionary to hold the parameters that we'll pass in our API call
    query_params = {
        'q': users_city,
        'appid': APP_ID
    }

    # Make an API call and store the response
    response = requests.get(BASE_URL, params=query_params)

    # Print some info to the console so that we can see what the API call sent
    # in its response
    print("Status code: " + str(response.status_code))
    print("URL: " + response.url)
    print("JSON Response: " + str(response.json()))

    response_json = response.json()

    # Extract the temperature from the API response (we can find out which field
    # this is by inspecting the JSON result)
    temp_kelvin = response_json['main']['temp']

    # Convert the temperature to Fahrenheit
    temp_fahrenheit = kelvin_to_fahrenheit(temp_kelvin)

    # Return some HTML including the temperature
    return """
    It is {0:.2f} degrees Fahrenheit today.
    """.format(temp_fahrenheit)


if __name__ == "__main__":
    app.run(debug=True)