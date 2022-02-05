# Trello

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
