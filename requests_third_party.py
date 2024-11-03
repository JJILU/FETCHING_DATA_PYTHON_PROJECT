import requests
from rich import print_json

def get_comments(comment_id=1):
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {
        "id" : comment_id
    }

    response = requests.get(url, params=params)
    parsed_json = response.json()

    return  parsed_json

def save_comment(data):
    url = "https://jsonplaceholder.typicode.com/comments"

    response = requests.post(url, data=data)
    parsed_json= response.json()

    return  parsed_json

# testing how to handle request errors using the request package
def get_something():
    url = "https://jsonplaceholder.typicode.com/comments/xyz"

    try:
        response = requests.get(url)

        # loo
        response.raise_for_status()

        parsed_data = response.json()
        return parsed_data
    # handles status code errors
    except requests.exceptions.HTTPError as e:
        print(f"there was an HTTP error: {e}")
    # handles all request errors
    except requests.exceptions.RequestException as e:
        print(f"there was an error: {e}")



def main():
    user_comment = {
        "postId": 1,
        "email": "jamy@netninja.dev",
        "body": "I love the new flutter series by omi it's so clear she is the best"
    }

    # get requests
    # comments = get_comments(comment_id=100)
    # print_json(data=comments)

    # post request
    # post_response = save_comment(user_comment)
    # print_json(data=post_response)

    # handling request errors
    data = get_something()
    print_json(data=data)

if __name__ == "__main__":
    main()


'''
Query Paramters
--------------
- used to filter the results gotten back
- query parameters are variables inside the url
  itself after a question mark.
'''