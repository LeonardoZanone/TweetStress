import twitter

api = twitter.Api(consumer_key="VWLMmdDXB5KAgpxSiBnXXexBa",
                  consumer_secret="smLoh7HuBYJjtxW7vt8wxxMaEodYbTyphdSTbRmVVqFGPb8icg",
                  access_token_key="2885891602-inETHnY8ZbnyZMyiPjQGUTyXdCMo4MGeODHY6MW",
                  access_token_secret="v55RL9bM1s6DEySHvzKCPMoZCbbuA7D6f7nLevzTDrCdf")

result = api.GetSearch(raw_query="q=place%3A3c42576594e748ff&since_id=1259633531598356482&count=100")

print(result)