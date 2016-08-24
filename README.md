# OpenStax CNX API Client

This is a web api client for retrieving data from CNX textbooks. The api has been designed to be intuitive and easy to use.

> Note: This library is under heavy development. The api my undergo dramatic changes.

## Install

1. Clone the repository to your local computer. 
2. Create a virtual environment
3. Run `python setup.py install`

## Quick Start

```python
import cnx

book = cnx.book('Introduction to Sociology')
book.version

>> 6.20

chapter = book.chapter('What is Culture?')
chapter.text()

>> <html xmlns="http://www.w3.org/1999/xhtml">
<head xmlns:c="http://cnx.rice.edu/cnxml" xmlns:md="http://cnx.rice.edu/mdml"><title>What Is Culture?</title><meta name="created-time" content="2015/01/20 05:12:34 -0600"/><meta name="revised-time" content="2015/03/13 09:37:38.363 GMT-5"/><meta name="author" content="OpenStaxCollege"/><meta name="licensor" content="OSCRiceUniversity"/><meta name="license" content="http://creativecommons.org/licenses/by/4.0/"/><meta name="keywords" content="Cultural imperialism, Cultural relativism, Cultural universals, Culture shock, Ethnocentrism, Material culture, Nonmaterial culture, Society, Xenocentrism"/><meta name="subject" content="Social Sciences"/></head>

<body xmlns="http://www.w3.org/1999/xhtml" xmlns:c="http://cnx.rice.edu/cnxml" xmlns:md="http://cnx.rice.edu/mdml" xmlns:qml="http://cnx.rice.edu/qml/1.0" xmlns:mod="http://cnx.rice.edu/#moduleIds" xmlns:bib="http://bibtexml.sf.net/" xmlns:data="http://dev.w3.org/html5/spec/#custom"><div data-type="document-title">What Is Culture?</div><div data-type="abstract"><ul>
<li>Differentiate between culture and society</li>
<li>Explain material versus nonmaterial culture</li>
<li>Discuss the concept of cultural universalism as it relates to society</li>
<li>Compare and contrast ethnocentrism and xenocentrism</li>
</ul></div>

...
```


