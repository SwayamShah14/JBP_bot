import json
import tweepy

class TweetProcessor(tweepy.Stream):
    def on_data(self, data):
        decoded = json.loads(data)
        print(data)

def load_keys():
    """Load keys file"""
    # Find the file and open it
    file = open("../.secrets/keys.json")
    # Parse JSON
    keys = json.load(file)
    # Return results
    return keys

def main():
    keys = load_keys()
    stream = TweetProcessor(
      keys["API"],
      keys["API_SECRET"],
      keys["ACCESS"],
      keys["ACCESS_SECRET"]
    )
    keyword = input("What would you like to track? ")
    stream.filter(track=[keyword])

if __name__ == "__main__":
    main()
