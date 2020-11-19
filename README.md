# Trello

Welcome to my finished Plentific task repository 👋🙇

In order to run it, if you have Python configured, please navigate to cloned repository's source directory from a terminal window and use:


*<pre><code>behave features/trello.feature</code></pre>*

The default browser being used is Chrome.

In case you will run into issues regarding Chrome version, please modify CHROME_VERSION value in common/strings/browser.py on line 11
*(for example: 2.42, 2.43, 2.45 etc.)*.



### This small test suite covers these steps:

Actions/steps to be covered:

* API
    * Create a board
    * Create 3 cards on that board
    * Edit one of the cards
    * Delete one of the cards
    * Add a comment to one of the cards

* Selenium/UI

    * Verify that there are 2 cards on the board
    * Verify that there is a card with a comment
    * Add a new comment to that card
    * Set the card as DONE

### A few things worth noting:

Please delve into this section, after you ran the tests and have read the code.


1. Since I haven't done much in Python, any other ideas for setting up and improvement of Python projects are more then welcome welcome.

2. In a real world scenario, I would encrypt config file to hide api-keys/passwords. (For example git-crypt)

3. I would prefer to use some form of mapping to parametrize steps such as card creation.
I know perfectly how to get it done in Java, but since in this example I wouldn't be able to use pre-defined 
key-value pairs but instead get card id values from responses, it would be a little bit more tricky to set them properly.

4. Normally, multi-browser support would be implemented.

5. I would store element xpaths in variables.

6. I wanted to add Page Objects, but it would take additional time and I wanted to submit the project already.


I honestly had a lot of fun while working on this :)


In Java, I would be able to create such a test suite in around 2-3 hours.

I believe that after just a few weeks of work and code reviews, I would be able to have a really good pace and could put in use more programmatically efficient solutions. 

What I mean by that, is that I am aware of plenty better programming solutions, just not yet in Python.  
 