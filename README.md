# daily-nft-tweet-bot 🎨🤖
 A python script that tweets a random NFT from a collection(or collections) each day. The script can get the owner of the NFT, then check if they have an ENS tied to that address & if they've set a twitter handle in their ENS txt records.

## Requirements 👮‍♂️

- [Twitter Developer Account](https://developer.twitter.com/en/apply-for-access) with [Elevated Access](https://developer.twitter.com/en/portal/products/elevated). 
- [An Alchemy API Key](https://www.alchemy.com/)
- A cloud service set up to run your code remotely (such as [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) or [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler)) 

## Setup 🔬

- Fork the project locally
- Sign up for Alchemy, create an app and copy the API key you're given.
- Create a Twitter Developer app, with read and write access.
- Request 'Elevated Access' for your twitter app, allowing you to use the API v1.1 endpoints.
- In the root of your repository create a .env file and input the apis in the following format:
```
ALCHEMY_API = {alchemy api here}
CONSUMER_API = {twitter developer app consumer api key here}
CONSUMER_SECRET = {twitter developer app consumer secret here}
ACCESS_TOKEN = {twitter developer app access token here}
ACCESS_SECRET = {twitter developer app access secret here}
```
- In main.py edit the instances of `Collection` (ln29-34) to match the details of your project(s)
- In main.py edit `tweet_text` to however you'd wish to format the text content of your tweet.
- You then should be ready to either run your script locally or push it the cloud hosting service of your choosing!

## Donations 🤑
If this script is useful for you/your project and you want to throw a few wei a Toads way that would be wonderful.

Eth address: mctoady.eth 🐸