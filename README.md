# ringzer0bot
This repository uses the Scrapy framework to scrape the scoreboard of www.ringzer0ctf.com.  
The data scraped are saved to a MongoDB database for further analysis.

## Requirements
* MongoDB
* Scrapy

## Example usage
```
$ scrapy crawl ringzer0flag
```

## Example of analysis results
#### Top five country:

| Country | Users |
|---------|-------------|
| Canada  | 5666        |
|United States|4333|
|India|1556|
|France|1075|
|United Kingdom|898|

#### Top file country by totalized points

| Country | Points |
|---------|-------------|
| Canada  | 75682        |
|United States|19584|
|Russian Federation|12282|
|France|11903|
|Viet Nam|11182|

