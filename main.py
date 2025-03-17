from flask import Flask, jsonify
import requests

app = Flask(__name__)

def discovery_data():
    """
    Returns a dictionary containing discovery information about the service.
    """
    return {
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    }

@app.route('/discovery', methods=['GET'])
def discovery():
    """
    Endpoint that returns discovery information about the service.
    """
    return jsonify(discovery_data())

def get_app_details(url='http://localhost:5000/discovery'):
    """Fetches app details from the /discovery endpoint of another service.

    Args:
        url (str): The URL of the discovery endpoint. Defaults to 'http://localhost:5000/discovery'.

    Returns:
        tuple: A tuple containing the app name and version, or "Unknown App", "Unknown Version" on error.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return data.get('name', 'Unknown App'), data.get('version', 'Unknown Version')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching app details: {e}")
        return "Unknown App", "Unknown Version"

if __name__ == '__main__':
    # Example usage:
    # You could start two instances of this code. 
    # one at port 5000 and other at 8000
    # to test the get_app_details() functionality
    # then in the second instance modify url parameter to get from 
    # the other instance.

    print("Running on port 5000. ")
    app.run(debug=True, port=5000) 
