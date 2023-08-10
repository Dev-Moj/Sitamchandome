# Google Search Index Checker

This Python script allows you to check how Google will index a website for a specific search phrase. By providing a search term and a website, the script will use the Google Custom Search JSON API to determine how many times that phrase has been suggested by Google for that website.

## Getting Started

To use this script, you will need an API Key and a Custom Search Engine ID from Google. Please note that if you are in a country sanctioned by the US, you will need to use a VPN to avoid any issues with Google.

### Prerequisites

This script requires the following Python libraries:

- google-api-python-client
- halo

You can install these libraries using pip:

```
pip install google-api-python-client halo
```

### Setting up the Custom Search Engine

To use the Custom Search JSON API, you need to create a custom search engine. Follow these steps:

1. Visit the [Custom Search Engine page](https://cse.google.com/cse/all).
2. Click on "Add" to create a new search engine.
3. In the "Sites to Search" box, enter "tester.test".
4. Enter a descriptive name for the search engine.
5. Click on "Create" to create the custom search engine.
6. Click on "Control Panel" to confirm the successful creation.
7. In the "Search Engine ID" section, make note of the value below. This will be needed later in the script. The search engine ID must be kept private.
8. If you want to get organized results from your entire web search, click on "Settings" from the left menu, then click the "Basics" tab. Go to the "Web Search" section and turn on this feature.

### Generating an API Key

To use the API, you need to generate an API key. Follow these steps:

1. Visit the [Google Custom Search API page](https://code.google.com/apis/customsearch/v1/overview.html).
2. Click on "Get Key" and create a new project with a descriptive name.
3. Clicking "Next" will generate the API key.
4. On the next page, you can configure various setup options, but they are not necessary for this script. Click on "Save" to complete the setup.

## Usage

1. Open a terminal and navigate to the directory where the script is saved.
2. Run the script using the following command:

```
python google_search_index_checker.py
```

3. Enter the search term when prompted.
4. Enter the website when prompted.
5. The script will display a loading spinner while it performs the search.
6. The script will output the website and the number of times the search phrase has been suggested by Google for that website.

## Example

```
name: Python tutorial
site: example.com
Loading...
('example.com', 5)
```

In the above example, the search phrase "Python tutorial" has been suggested by Google 5 times for the website "example.com".

## Notes

- This script is a basic implementation and may require further customization based on your specific needs.
- Make sure to keep your API key and search engine ID secure.
- The "halo" library is used to display a loading spinner in the terminal, but it is not necessary for the script to function. You can remove it if desired.