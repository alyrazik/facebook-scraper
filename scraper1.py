import scrapy


class Scraper1(scrapy.Spider):
    """
    A daughter spider class implements two functions at least.
    One is requests which generates URLs to follow (they are passed to the engine which passes them to the downloader
    after the scheduler find  a spot for it)
    Two is items which is the parsed content from requested web pages.
    """
    name = 'Scraper1'

    def start_requests(self):
        # this must return an iterable of requests,
        # iterable is like a list or string..anything you can iterate through
        """
        this must return an iterable of requests, iterable is like a list or string..anything you can iterate through
        Iterators or generators are a kind of iterables we can only iterate over once. It generates the values
        on the fly and doesn't store them in memory. so each value can only be used once.
        any functions that uses the keyword yield actually returns a generator. if you make a function call to it, it
        returns an object (an iterator or a generator). it doesn't not run.

        typically, one uses the generator in a for loop, in which, each time a generator is called, it yields a value
        by executing code from the last yield statement.
        this is done until the generator is exhausted (hits no yield and thus comes to an end).

        This function returns Request objects that are then scheduled by the scrapy scheduler.
        upon receiving a response from each Request, the scheduler/engine instantiates a Response object and call the
        callback method specified in the Request by the callback parameter passing the response as an argument
        """

        url = 'http://quotes.toscrape.com/page/1/'
        yield scrapy.Request(url, callback=self.parse)
        # this generator function yields Request objects; represent HTTP requests in Scrapy.

    def parse(self, response):
        # this is a function that's called by the scrapy engine to handle the downloaded content for each request.
        # the engine passes the 'response' parameter to this function.
        # the response parameter is of type TextResponse; it holds the content of the page and several helper methods
        # to handle it.

        # the tasks usually performed in the parse function is:
        # 1. parse the input and extracts useful info
        # 2. saves to json or whatever
        # 3. find new urls to follow and creating new requests.

        filename = 'scraper1.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
