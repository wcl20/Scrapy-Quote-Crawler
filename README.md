# Scrapy Quote Crawler
Scrapy tutorial to extract Alber Einstein's quotes from [http://quotes.toscrape.com/](http://quotes.toscrape.com/).

## Setup
Generate Virtual environment
```bash
python3 -m venv ./venv
```
Enter environment
```bash
source venv/bin/activate
```
Install required libraries
```bash
pip install -r requirements.txt
```
Run program
```bash
cd tutorial
scrapy crawl quotes
```
Run program (with arguments)
```bash
cd tutorial
scrapy crawl quotes -a tag=wisdom
```
The quotes are stored in a JSON Lines file.


