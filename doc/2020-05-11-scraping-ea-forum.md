---
layout: post
title: Data Analysis and Deep Learning on posts from the EA Forum
---

This post describes the results from the following:

1)	Scrape all posts from the EA Forum

2)	Explore overall trends in the data: posts with the greatest number of comments, authors with the greatest number of posts etc.

3)	Build a wordcloud to visualize the most used words

4)	Fine-tune GPT2 on the EA Forum text corpus and generate text.

Code and data can be found [here](https://github.com/anishazaveri/ea_forum).


# Scraping
---
The `robots.txt` [file](https://forum.effectivealtruism.org/robots.txt) of EA Forum , disallows crawling/scraping data from `/allPosts`. To get around this, I did the following:
- Manually loaded yearly links from `/allPosts` (this required manually clicking each year followed by "Load More")
- Used a [link extractor](https://chrome.google.com/webstore/detail/link-klipper-extract-all/fahollcgofmpnehocdgofnhkkchiekoo?hl=en) in Chrome to extract links from the page into a .csv file
- Used [Scrapy](https://scrapy.org/) to scrape the following fields from each link: 'date', 'author', 'title', 'number of comments' and 'content'. I extracted data for posts published between 01-01-2013 and 05-10-2020.  

I cleaned the data and restricted subsequent analysis on posts published between 01-01-2013 to 04-15-2020, since  recent posts were unlikely to have accumulated comments.

# Exploratory Data Analysis

### *Number of yearly posts*

<img src="https://raw.githubusercontent.com/anishazaveri/ea_forum/master/out/images/posts_year.png" width="300"/>

### *Posts with the most comments*


**date**|**title**|**author**|**num\_comments**
:-----:|:-----:|:-----:|:-----:
4/23/2019|[Long-Term Future Fund: April 2019 grant recommendations](https://forum.effectivealtruism.org/posts/CJJDwgyqT4gXktq6g/long-term-future-fund-april-2019-grant-recommendations)|[Habryka](https://forum.effectivealtruism.org/users/habryka)|240
10/26/2017|[Why & How to Make Progress on Diversity & Inclusion in EA](https://forum.effectivealtruism.org/posts/YCPc4qTSoyuj54ZZK/why-and-how-to-make-progress-on-diversity-and-inclusion-in)|[Kelly\_Witwicki](https://forum.effectivealtruism.org/users/kelly_witwicki)|235
11/15/2019|[I'm Buck Shlegeris, I do research and outreach at MIRI, AMA](https://forum.effectivealtruism.org/posts/tDk57GhrdK54TWzPY/i-m-buck-shlegeris-i-do-research-and-outreach-at-miri-ama)|[Buck](https://forum.effectivealtruism.org/users/buck)|231
10/24/2016|[Concerns with Intentional Insights](https://forum.effectivealtruism.org/posts/fn7bo8sYEHS3RPKQG/concerns-with-intentional-insights)|[Jeff\_Kaufman](https://forum.effectivealtruism.org/users/jeff_kaufman)|186
2/26/2019|[After one year of applying for EA jobs: It is really, really hard to get hired by an EA organisation](https://forum.effectivealtruism.org/posts/jmbP9rwXncfa32seH/after-one-year-of-applying-for-ea-jobs-it-is-really-really)|[EA applicant](https://forum.effectivealtruism.org/users/ea-applicant)|182
1/16/2020|[Growth and the case against randomista development](https://forum.effectivealtruism.org/posts/bsE5t6qhGC65fEpzN/growth-and-the-case-against-randomista-development)|[HaukeHillebrandt](https://forum.effectivealtruism.org/users/haukehillebrandt)|168
9/15/2014|[Open Thread](https://forum.effectivealtruism.org/posts/4Pek6aKbEoXSZvNFT/open-thread)|[RyanCarey](https://forum.effectivealtruism.org/posts/4Pek6aKbEoXSZvNFT/open-thread)|163
11/11/2017|[An Exploration of Sexual Violence Reduction for Effective Altruism Potential](https://forum.effectivealtruism.org/posts/gFpaHk2aKq2jGijnd/an-exploration-of-sexual-violence-reduction-for-effective)|[Kathy\_Forth](https://forum.effectivealtruism.org/users/kathy_forth)|156
10/22/2014|[Should Giving What We Can change its Pledge? ](https://forum.effectivealtruism.org/posts/9Xp7BGoKnbSiP3Ng8/should-giving-what-we-can-change-its-pledge)|[Michelle\_Hutchinson](https://forum.effectivealtruism.org/users/michelle_hutchinson)|144
9/3/2019|[Are we living at the most influential time in history?](https://forum.effectivealtruism.org/posts/XXLf6FmWujkxna3E6/are-we-living-at-the-most-influential-time-in-history-1)|[William\_MacAskill](https://forum.effectivealtruism.org/users/william_macaskill)|140

### *Posts with the most karma*


**date**|**title**|**author**|**num\_karma**
:-----:|:-----:|:-----:|:-----:
2/26/2019|[After one year of applying for EA jobs: It is really, really hard to get hired by an EA organisation](https://forum.effectivealtruism.org/posts/jmbP9rwXncfa32seH/after-one-year-of-applying-for-ea-jobs-it-is-really-really)|[EA applicant](https://forum.effectivealtruism.org/users/ea-applicant)|285
1/16/2020|[Growth and the case against randomista development](https://forum.effectivealtruism.org/posts/bsE5t6qhGC65fEpzN/growth-and-the-case-against-randomista-development)|[HaukeHillebrandt](https://forum.effectivealtruism.org/users/haukehillebrandt)|269
1/13/2020|[EAF's ballot initiative doubled Zurich's development aid](https://forum.effectivealtruism.org/posts/dTdSnbBB2g65b2Fb9/eaf-s-ballot-initiative-doubled-zurich-s-development-aid)|[Jonas Vollmer](https://forum.effectivealtruism.org/users/jonas-vollmer)|254
9/26/2019|[Some personal thoughts on EA and systemic change](https://forum.effectivealtruism.org/posts/QYH9yJ4WfHRs3ftJD/some-personal-thoughts-on-ea-and-systemic-change)|[Carl\_Shulman](https://forum.effectivealtruism.org/users/carl_shulman)|183
9/3/2019|[Are we living at the most influential time in history?](https://forum.effectivealtruism.org/posts/XXLf6FmWujkxna3E6/are-we-living-at-the-most-influential-time-in-history-1)|[William\_MacAskill](https://forum.effectivealtruism.org/users/william_macaskill)|174
6/2/2019|[Is EA Growing? EA Growth Metrics for 2018](https://forum.effectivealtruism.org/posts/f6WnAe3qDQqmmz38x/is-ea-growing-some-ea-growth-metrics-for-2017)|[Peter\_Hurford](https://forum.effectivealtruism.org/users/peter_hurford)|168
3/7/2019|[SHIC Will Suspend Outreach Operations](https://forum.effectivealtruism.org/posts/3HaXa7dtu86NQNEZJ/shic-will-suspend-outreach-operations) |[cafelow](https://forum.effectivealtruism.org/users/cafelow)|165
8/20/2019|[List of ways in which cost-effectiveness estimates can be misleading](https://forum.effectivealtruism.org/posts/zdAst6ezi45cChRi6/list-of-ways-in-which-cost-effectiveness-estimates-can-be)|[saulius](https://forum.effectivealtruism.org/users/saulius)|155
6/20/2019|[Information security careers for GCR reduction](https://forum.effectivealtruism.org/posts/ZJiCfwTy5dC4CoxqA/information-security-careers-for-gcr-reduction)|[ClaireZabel](https://forum.effectivealtruism.org/users/clairezabel)|153
8/14/2019|[Ask Me Anything!](https://forum.effectivealtruism.org/posts/oPGJrqohDqT8GZieA/ask-me-anything)|[William\_MacAskill](https://forum.effectivealtruism.org/users/william_macaskill)|150


### *Authors with the most posts*


**author**|**num\_posts**
:-----:|:-----:
[Aaron Gertler](https://forum.effectivealtruism.org/users/aarongertler)|87
[Milan\_Griffes](https://forum.effectivealtruism.org/users/milan_griffes)|83
[Peter\_Hurford](https://forum.effectivealtruism.org/users/peter_hurford)|74
[RyanCarey](https://forum.effectivealtruism.org/users/ryancarey)|66
[Tom\_Ash](https://forum.effectivealtruism.org/users/tom_ash)|58


### *Authors with highest mean post karma (author must have >1 post)*


**author**|**mean\_post\_karma**
:-----:|:-----:
[Buck](https://forum.effectivealtruism.org/users/buck)|92.2
[Jonas Vollmer](https://forum.effectivealtruism.org/users/jonas-vollmer)|77.0
[Luisa_Rodriguez](https://forum.effectivealtruism.org/users/luisa_rodriguez)|74.7
[saulius](https://forum.effectivealtruism.org/users/saulius)|73.5
[sbehmer](https://forum.effectivealtruism.org/users/sbehmer)|73.0

# Word Clouds

My next goal was to make a word cloud representing the most commonly used words in the EA Forum. I preprocessed the post content as follows:

- Tokenized words
- Expanded word contractions e.g. 'don't' -> 'do not'
- Converted all words to lowercase
- Removed tokens that were only punctuation
- Filtered out stop words using [nltk](https://www.nltk.org/)
- Removed any tokens containing numbers
- Removed any tokens containing 'http' or 'www'

Here's the resulting word cloud (built using https://github.com/amueller/word_cloud on x tokens):



The most common word appeared to be 'people' and 'work'. I thought it would be instructive to see if these were over-represented in the EA Forum specifically, or are generally over-represented in most online documents. So, to generate a control, I scraped all posts from [Slate Star Codex](https://slatestarcodex.com/) (SSC) and performed text preprocessing to generate x tokens. 

Using R's [wordcloud](https://cran.r-project.org/web/packages/wordcloud/index.html) package I built a "comparative" word cloud showing words over-represented in text corpus from the EA Forum over SSC and vice-versa. 

What about words that were common between the EA Forum and SSC?


# __GPT2__
Finally, I used the text corpus from the EA Forum to fine-tune GPT2, from OpenAI, a language model trained on a dataset of 8 million web pages. I used a [Colab notebook](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce) made using [gpt2-simple](https://minimaxir.com/2019/09/howto-gpt2/) as a template and fine-tuned either the "small" (124 M parameters) or "medium" (355 M parameters). 



> What is Rationality in AI?
Background Rationality is an ideology of AI, a belief system based on the belief that humans are naturally sentient. It argues that all human actions are responsible for the wellbeing of all sentient beings. This view is based on a large body of evidence. It is not a new, classicist theory of AI. Instead it is a mixture of old and new philosophy.

>TL;DR's for the EA Forum/Welcome: ”Effective altruists are trying to figure out how to build a more effective AI, using paperclips, but we're not really sure how it's possible to do so.

>GITC's Vaccination Prevention Research Project
This is the first post of a three part series on the development of effective vaccines. This series will start with a list of possible vaccines that can be developed by the GPI team, ending with a brief overview of the science behind vaccine development. We will then address a variety of questions in the areas of biosecurity, biosecurity technologies and improved vaccine safety.This is a work in progress and we hope to get back to you soon. 

prompts

>Introduction to effective altruism [ edit ] The most basic assumption about effective altruism is that we must act rationally. It follows from this that you should maximize the benefit of the action you’re taking. The absolute value of a given intervention is the number of lives saved or improved. If the total benefit of the intervention is too small, you should not take it.

>Introduction to effective altruism as a means to furthering one's life, many people I have spoken with who are currently living on less than $10,000 per year have completed some EA-related training. The basic idea of effective altruism is that one should donate your money to the most effective charities. In practice, many people who are involved with EA don't do this, and they will only use other methods to do it.






