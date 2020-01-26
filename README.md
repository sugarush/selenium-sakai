# Selenium Sakai Testing

## Installation

Make sure you have Google Chrome installed.

Then, install Selenium:

`pip install selenium`

Selenium requires a driver to work with a browser, so install the Google Chrome driver with the following command:

`brew cask install chromedriver`

## Pre-Testing

First, clone this repository:

`git clone https://github.com/sugarush/selenium-sakai.git`

Change directories to the cloned repository:

`cd selenium-sakai`

Then install any dependencies:

`pip install -r .requirements`

## Testing

To run all tests, from inside the repository directory, run the following:

`python -m unittest discover --verbose selenium_sakai`
