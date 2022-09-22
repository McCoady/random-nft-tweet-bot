import random
import requests
import tweepy
from dotenv import load_dotenv
import os
from web3 import Web3
from ens import ENS

# import api keys from .env file
load_dotenv()
ALCHEMY_API = os.environ.get("ALCHEMY_API")
CONSUMER_API = os.environ.get("CONSUMER_API")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")


w3 = Web3(Web3.HTTPProvider(f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API}"))
ns = ENS.fromWeb3(w3)

class Collection:
    def __init__(self, name: str, address: str, totalsup: int) -> None:
        self.name = name
        self.address = address
        self.totalsup = totalsup

# initiate your chosen collections & append them to a collections array
collections = []
# collection 1
collections.append( Collection("GenFrens","0x4b671ade2a853613e46c7c0a86d7df547d098b83", 256))
# collection 2
collections.append( Collection("SN0WCR4SH","0xb25e1fd137cff8ab3066079e4493d9403d8d7434", 243))
# collection 3
collections.append( Collection("Folded Faces","0xf01dfac37dd149cb686e05d06cd21930b011f10f", 300))

# choose random collection and random token id from the collection
collection_choice = random.choice(collections)
token_choice = random.randrange(collection_choice.totalsup)

print(f"Collection : {collection_choice.name} Token Id: {token_choice}")

# query alchemy api to find the NFT image and NFTs owner
image_url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{ALCHEMY_API}/getNFTMetadata?contractAddress={collection_choice.address}&tokenId={token_choice}&refreshCache=false"
owner_url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{ALCHEMY_API}/getOwnersForToken?contractAddress={collection_choice.address}&tokenId={token_choice}"
headers = {
    "accept": "application/json",
}
image_response = requests.get(url = image_url, headers = headers)
owner_response = requests.get(url = owner_url, headers = headers)

print(image_response.json())
image_link = image_response.json()["media"][0]["gateway"]
owner = owner_response.json()["owners"][0]

# convert owner address to checksum
owner_checksum = Web3.toChecksumAddress(owner)
print(owner_checksum)

# see if there is an ENS address attached to that address
owner_ens = ns.name(owner_checksum, strict=True)
owner_twitter = ""
if owner_ens != None:
    owner = owner_ens
    # if there is an ens name, check if they have set a twitter handle in their txt records
    twitter_res = ns.get_text(owner_ens, 'com.twitter')

    if  twitter_res != "":
        owner_twitter = f"(@{twitter_res})"

print(owner_ens)    
print(twitter_res)

# Build the content of the tweet you wish to post
tweet_text = f"🎉CIRCOLORS NFT of the day!🎉\n{collection_choice.name} #{token_choice} owned by {owner}{owner_twitter}.\n\nView on OpenSea: https://opensea.io/assets/ethereum/{collection_choice.address}/{token_choice}"

print(tweet_text)
print(image_link)

# grab the image from alchemy and download locally
path = "./img.png"
with open(path,"wb") as f:
    f.write(requests.get(image_link).content)

# connect to twitters API
auth = tweepy.OAuth1UserHandler(CONSUMER_API,CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# post tweet content and attach image file
api.update_status_with_media(status=tweet_text, filename=path)