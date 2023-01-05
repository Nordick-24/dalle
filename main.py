import os
import openai
from loguru import logger


prompt = input("Explain Your Pictuar:\n")
openai.api_key = os.getenv("api_token")


response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="256x256",
)

logger.info("Processing, Please Wait....")

print(response["data"][0]["url"])

downloadIt = input("Do ypu want download it?: (y/n)")

if downloadIt == "y":
    import requests
    response = requests.get(response["data"][0]["url"]).content
    with open("result.png", "wb") as result:
        result.write(response)

    logger.success("")

else:
    print("ABorted!")
