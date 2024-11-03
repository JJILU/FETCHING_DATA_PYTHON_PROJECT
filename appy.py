# later make network requests using 3rd-party library called requests

# fetching data - get request with urlib package built into the standard library
from urllib import  request
import json
from  rich import print_json

# fetching data
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        with request.urlopen(url) as response:
            data = response.read()

            parsed_json = json.loads(data)
            return parsed_json
    except:
        print("could not fetch the data.")
        return  None

def get_users():
        url = "https://dummyjson.com/users"

        try:
            with request.urlopen(url) as response:
                data = response.read()

                users = json.loads(data)
                return users
        except Exception as e:
            print(f"could not load users: {e}")
            return None



def main():
    # posts = get_posts()
    # print_json(data=posts)

    blog_users = get_users()
    print_json(data=blog_users)

if __name__ == "__main__":
    main()

