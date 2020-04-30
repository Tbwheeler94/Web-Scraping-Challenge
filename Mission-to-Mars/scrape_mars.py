from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def init_browser():
    #Activate splinter
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", headless=False, **executable_path)

def scrape_info():
    browser = init_browser()

    ##############
    #First Scrape#
    ##############

    #Visit Mars news site
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    #Scrape page, save html as soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Retreive news title
    news_title = soup.find('div', class_='list_text').find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    ###############
    #Second Scrape#
    ###############

    #Visit Mars images site
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    #Scrape page, save html as soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Retreive image link
    featured_image = soup.find('img', class_="thumb")
    link = featured_image['src']
    featured_image_url = "https://www.jpl.nasa.gov" + str(link)

    ###############
    #Third Scrape##
    ###############

    #Connect to Twitter page
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    time.sleep(4)

    #Scrape page, save html as soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Find weather data
    mars_weather = soup.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0").text

    ################
    #Fourth Scrape##
    ################

    #Define and connect to Mars page html table
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)

    #Clean data
    df = tables[0]
    df.columns = ['Description', 'Value']
    df = df.to_html()

    ########################
    #Fifth Set of Scrapes###
    ########################

    #Cerberus Hemisphere
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Save image link
    cerberus_hemisphere = soup.find('li').find('a')['href']

    #Schiaparelli Hemisphere
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Save image link
    schiaparelli_hemisphere = soup.find('li').find('a')['href']

    #Syrtis Major Hemisphere
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Save image link
    syrtis_major_hemisphere = soup.find('li').find('a')['href']

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Search image
    valles_marineris_hemisphere = soup.find('li').find('a')['href']

    #Save array of image dictionaries
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": valles_marineris_hemisphere},
    {"title": "Cerberus Hemisphere", "img_url": cerberus_hemisphere},
    {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_hemisphere},
    {"title": "Syrtis Major Hemisphere", "img_url": syrtis_major_hemisphere},
    ]

    ################################
    #Store All Data in a Dictionary#
    ################################

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_df": df,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data