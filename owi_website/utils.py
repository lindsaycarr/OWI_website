
import feedparser
from bs4 import BeautifulSoup




def pull_full_feed(feed_url):
    """
    pull page data from a my.usgs.gov confluence wiki feed
    :param feed_url: the url of the feed, created in confluence feed builder
    :return: the html of the page itself, stripped of header and footer
    """
    feed = feedparser.parse(feed_url)

    # Process html to remove unwanted mark-up and fix links
    post = ''
    entries = feed['entries']

    posts = []
    if len(entries) > 0:
        for entry in entries:
            post = {}
            post['title'] = entry.title
            soup = BeautifulSoup(entry.summary, 'lxml')

            # Remove edited by paragraph
            soup.p.extract()

            # Remove final div in the feed
            feed_div = soup.find('div', class_='feed')
            children_divs = feed_div.findAll('div')
            children_divs[len(children_divs) - 1].extract()

            # Translate any in page links to use relative URL
            base = feed['entries'][0].summary_detail.base
            links = feed_div.select('a[href^="' + base + '"]')
            for link in links:
                link['href'] = link['href'].replace(base, '')
            #grab the div with the content
            post['content'] = soup.div.contents[2]
            posts.append(post)


    return posts

