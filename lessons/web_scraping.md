# Web Scraping
To scrape a web-page or a whole website means to first download the page or pages, then parse the HTML and using the structure 
of the document select the parts of the document which is of interest. 

We could e.g. want to analyze the recent news articles from [dr.dk](https://dr.dk) and therefore need to scrape the front-page
to get the title for each article.

locate the data ...

<img src="images/web_scraping/dr.dk-frontpage.png" width="300">

download html ...

```html
<html>
    <head></head>
    <body>
        <article>
            <h1>Silicon Valley-guru ...</h1>
        </article>
        ... more articles
    </body>
</html>
```

parse and extract relevant parts ...

```
Silicon Valley-guru og direktør for tænketank: Klimaforandringerne kan være løst i 2035
Bla, bla, bla: Greta Thunberg håner verdens ledere på klimakonference
Havets store spillere vil være CO2-neutrale i 2050 - nu skal politikerne bare med ombord
Kontakttallet stiger, og SSI varsler smittestigning
Jeg skulle have trukket mig lang tid før Tokyo
```
## Copyright - Important!!!

Even though public available many websites have copyright restrictions which should be followed:
- look at Terms of Service
- look at /robots.txt

If you are allowed to scrape data the following rules should still be followed:
- **Do not**  re-distribute collected data without a clear written statement saying you are allowed to
- **always** make clear where data comes from when used in papers etc. use quotation and references

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

The web-server responds with a `HTTP-response` like:

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

## Copyright and Ethics
Even though web-sites are public available they are still owned by a person / company. Often we are not allowed
to scrape and use their data without permission.

- check "terms of use" and similar
- check /robots.txt

## Exercises

### exercises questions
see kristoffers ...

### Assigments...
lav øvelse i browser hvor de skal bruge inspect and og documents.querySelectorAll() til at finde sti til fx overskrifter...
lav øvelse hvor de skal scrape xxx fra au's hjemmeside, eller måske publications fra pure ...

# TODO 
- finish this document
- make slides based on this (and slides from previous courses)
- create live-code examples and test them
- create exercises and assigments (see chapter about web-scraping)
