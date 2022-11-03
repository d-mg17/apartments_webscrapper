# WebScraper using BeautifulSoup4
This is a Web Scrapper made using Python and the libraries BeautifulSoup4 & requests with the goal of finding apartments for rent in Puerto Rico depending of your area of choice {Metro, Centro}, with details about them like address, size and monthly rent. The result given are only the ones found on the first page of the search.

## How it works??
This project uses the library BeautifulSoup to parset the html document of a website and stores it an object. From this object it's form where we will scrappe the information we need. 

The goal of this project is to help us get information of apartments found on the web site <clasificadosonline.com> (www.clasificadosonline.com) and store it on a csv file. 

## How to run it:
1. Download the source code.
2. Activate the virtual enviroment.
3. Check that you have internet connection.
4. Run the following command on your terminal/cmd: `python scrapper.py AreaOfChoice file.csv` where `file.csv` is the name of the file where you want to store the results. You can add multiple areas of choices using `,`
5. Check the csv file that was created.
