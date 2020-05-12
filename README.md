# ea_forum
Project to scrape the [EA Forum](https://forum.effectivealtruism.org/) and [Slate Star Codex](https://slatestarcodex.com/).

## Goals
1) Overall statistics - look at the most commented posts etc.
2) Wordclouds
3) Fine-tune GPT2 and generate text

## Data and files
- Spiders used for scraping are 
  - `src/scrapy/ea_forum/ea_forum/spiders/forum_scraper.py` and
  - `src/scrapy/ssc/ssc/spiders/ssc_scraper.py` 
- Scraped and cleaned data are in 
  - `data/ea_forum/cleaned_data_eaforum.csv` and 
  - `data/ssc/cleaned_data_ssc.csv`.
- Code used for cleaning data, exploratory_data_analysis and wordcloud generation is under `/src/eda`

