# Web-Scraping-Challenge

## Overview: This challenge consisted of 2 parts

  1. Scraping several websites for data about Mars. Website scraped include:
      - [NASA Mars News](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)
      - [Nasa Jet Propulsion Laboratory](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
      - [Twitter @Mars Weather](https://twitter.com/marswxreport?lang=en)
      - [Space Facts - Mars](https://space-facts.com/mars/)
      - [Mars Hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
      
  2. Loading the collected data into a MongoDB collection and displaying the result on an web page using Flask. Screenshots of the site can be found in this repository.

### Step 1 Detailed Description - Scraping

  1. Initial scraping was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter to confirm data was being pulled correctly.
  2. Scraped the NASA Mars News Site for the latest News Title and Paragraph Text.
  3. Scraped the JPL Mars Space Images for the image url of the current Featured Mars Image.
  4. Scraped the Mars Weather twitter account for the latest weather report.
  5. Scraped Mars Facts using Pandas for facts about Mars, converted table to html.
  6. Converted USGS Astrogeology site for high res images of each of Mars's hemispheres.

### Step 2 Detailed Description - Loading Results into MongoDB and Building Flask Application

  1. I converted my Jupyter notebook into a single python script that executes all of my scraping results and return one Python dictionary containing all of the scraped data.
  2. I created a route called /scrape that imports my scrape_mars.py script and calls my scrape function.
  3. Stored the return value in Mongo as a Python dictionary.
  4. Created a root route that queries my Mongo database and passes the mars data into an HTML template to display the data.
  5. I created a template HTML file called index.html that take the mars data dictionary and display all of the data in the appropriate HTML elements. See screenshots in repository for final layout
