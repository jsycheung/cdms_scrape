import requests  # module to make API request to the CDMS URL

# Assume you have a list of molecule tags for cdms
tag_list = ['003501', '004501', '005501', '005502']

# This is a link of the API, which is the link (endpoint) where you click on the CDMS website and it automatically downloads the cat file.
# Here I only used the first item in the list as an example, but you can imagine using for loop to scrape through the list
api_url = f"https://cdms.astro.uni-koeln.de/classic/entries/c{tag_list[0]}.cat"

# Get the response from the CDMS endpoint
response = requests.get(api_url)

# It writes the response into a .cat file in your directory containing cdms_scrape.py, w+ makes it overwriting the file if a file of the same name exists
with open(f"c{tag_list[0]}.cat", "w+") as f:
    f.write(response.text)
