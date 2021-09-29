# Web Scraping
To scrape a web-page or a whole website means to first download the page or pages, then parse the HTML and using the structure 
of the document select the parts of the document which is of interest. 

We could e.g. want to analyze the recent news articles from [dr.dk](https://dr.dk) and therefore need to scrape the front-page
to get the title for each article.

<img src="images/web_scraping/dr.dk-frontpage.png" width="300">

```
Silicon Valley-guru og direktør for tænketank: Klimaforandringerne kan være løst i 2035
Bla, bla, bla: Greta Thunberg håner verdens ledere på klimakonference
Havets store spillere vil være CO2-neutrale i 2050 - nu skal politikerne bare med ombord
Kontakttallet stiger, og SSI varsler smittestigning
Jeg skulle have trukket mig lang tid før Tokyo
```

## The Internet and Word Wide Web
60's -> 80's
Arpanet, FTP, SMTP, etc.

### Tim Berners-Lee and Cern
90's
problem ...
hypertext (Vanemar Bush, Ted Nelson) + internt
problem -> solution (http, html, browser, server)

### HTTP Protocol
A protocol is a set of rules for how to communicate within a certain domain.

An url is made of `PROTOCOL://DOMAIN/PATH?QUERY-STRING` eg. `https://dr.dk/sport?sort=latest`. The browser uses the domain name 
to resolve the ip-address of the server and send an `HTTP-request` like:

```http request
GET /sport?sort=latest
```

The web-server reponds with a `HTTP-response` like:

```http request
HTTP/1.1 200 OK

<html><head><title>My Web Page</title></head><body><h1>Welcome</h1></body></html>
```

## HTML
structure, tags -> elements, attributes


## CSS
...

### selectors
We need to know these to target the elements when scraping...

type-selector, class-selector, id-selector, combinators -> descendant selectors

## Browser Tools
inspect element
console -> document.querySelectorAll() for testing...

## Web Scraping
Request, BS4

Example: get all titles dr.dk
Example: get all title and article-content tv2.dk
Example: get all titles for a paginated result comicscontainer.dk

### exercises questions
see kristoffers ...
