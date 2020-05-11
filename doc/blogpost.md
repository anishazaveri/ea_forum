Data Analysis and Deep Learning on posts from the EA Forum

This post describes the results from the following:
1)	Scrape all posts from the EA Forum
2)	Explore overall trends in the data: posts with the greatest number of comments, authors with the greatest number of posts etc.
3)	Build a wordcloud to visualize the most used words
4)	Fine-tune GPT2 on the EA Forum text corpus and generate text.

Code and data can be found [here](https://github.com/anishazaveri/ea_forum).


1. __Scraping__

The `robots.txt` [file](https://forum.effectivealtruism.org/robots.txt) of EA Forum , disallows crawling/scraping data from `/allPosts`. To get around this, I used a [link extractor](https://chrome.google.com/webstore/detail/link-klipper-extract-all/fahollcgofmpnehocdgofnhkkchiekoo?hl=en) in Chrome and extracted yearly links from the `/allPosts` page (this required manually clicking “Load more” but it wasn’t too cumbersome). 

Next, I used [Scrapy](https://scrapy.org/) to scrape the following fields from each link: 'date', 'author', 'title', 'number of comments' and 'content'. I extracted data for posts published between 01-01-2013 and 05-04-2020.  

I cleaned the data and restricted subsequent analysis on posts published between 01-01-2013 to 04-15-2020, since  recent posts were unlikely to have accumulated comments.

2)	__Exploratory Data Analysis__

Here are the number of posts published on the EA Forum each year:


![](https://raw.githubusercontent.com/anishazaveri/ea_forum/master/out/images/posts_year.png)






**date**|**title**|**author**|**num\_comments**
:-----:|:-----:|:-----:|:-----:
4/23/2019|[Long-Term Future Fund: April 2019 grant recommendations](https://forum.effectivealtruism.org/posts/CJJDwgyqT4gXktq6g/long-term-future-fund-april-2019-grant-recommendations)|[Habryka](https://forum.effectivealtruism.org/users/habryka)|240
10/26/2017|[Why & How to Make Progress on Diversity & Inclusion in EA](https://forum.effectivealtruism.org/posts/YCPc4qTSoyuj54ZZK/why-and-how-to-make-progress-on-diversity-and-inclusion-in)|[Kelly\_Witwicki](https://forum.effectivealtruism.org/users/kelly_witwicki)|235
11/15/2019|[I'm Buck Shlegeris, I do research and outreach at MIRI, AMA](https://forum.effectivealtruism.org/posts/tDk57GhrdK54TWzPY/i-m-buck-shlegeris-i-do-research-and-outreach-at-miri-ama)|[Buck](https://forum.effectivealtruism.org/users/buck)|230
10/24/2016|Concerns with Intentional Insights|Jeff\_Kaufman|186
2/26/2019|After one year of applying for EA jobs: It is really, really hard to get hired by an EA organisation|EA applicant|182
1/16/2020|Growth and the case against randomista development|HaukeHillebrandt|168
9/15/2014|Open Thread|RyanCarey|163
11/11/2017|An Exploration of Sexual Violence Reduction for Effective Altruism Potential|Kathy\_Forth|156
10/22/2014|Should Giving What We Can change its Pledge? |Michelle\_Hutchinson|144
9/3/2019|Are we living at the most influential time in history?|William\_MacAskill|140ving at the most influential time in history?|140




