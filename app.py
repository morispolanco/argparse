import argparse
import requests

def get_api_response(api_key, session_id, question):
    api_url = "https://api.afforai.com/api/api_completion"
    
    # Prepare the payload
    payload = {
        "apiKey": api_key,
        "sessionID": session_id,
        "history": [{"role": "user", "content": question}],
        "powerful": False,
        "google": True
    }

    # Make the API request
    response = requests.post(api_url, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.json()
    else:
        # If the request was unsuccessful, print an error message
        print(f"Error: Failed to get API response. Status code: {response.status_code}")
        return None

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Guatemalan Laws Q&A App")

    # Define command line arguments
    parser.add_argument("--api_key", required=True, help="API key for authentication")
    parser.add_argument("--session_id", required=True, help="Session ID for the API")
    parser.add_argument("--question", required=True, help="Question to ask about Guatemalan laws")

    # Parse the command line arguments
    args = parser.parse_args()

    # Get the API response
    api_response = get_api_response(args.api_key, args.session_id, args.question)

    # Display the API response
    if api_response:
        print("API Response:")
        print(api_response)

if __name__ == "__main__":
    main()
