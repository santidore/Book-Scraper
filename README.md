
# 📚🕷 Python Book Scraper using Scrapy 📚🕷

This is a web scraping project built with Scrapy, a Python framework for extracting data from websites. The purpose of this project is to scrape information about romance books from the website "http://books.toscrape.com" through XPath technology and retrieve details such as book titles, prices, availability, and cover images.

## Prerequisites

- Python 3.x
- Scrapy library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/santidore/Book-Scraper/
```
2. Install the required dependencies using pip:

```bash
pip install scrapy
```
3. Create a new Scrapy project using the command: 

```bash
scrapy startproject bookscraper
```
4. Navigate to the project directory:

```bash
cd bookscraper
```
5. Copy the file `books_scraper.py` into the "spiders" directory of your Scrapy project.

## Configuration

- The spider's starting URL is set to the romance books category page on "http://books.toscrape.com".
- The spider uses XPath selectors to extract relevant data from the website's HTML structure.
- Pagination is supported, and the spider will automatically navigate to the next page to scrape more data.
  
## Running the program
1. Run the spider to start scraping using the following command:

```bash
scrapy crawl romance_books_spider -o romance_books.json
```
2. You should now be able to find the obtained results in a .json file named romance_books.json located in the bookscraper directory!

## Example .json file
```json
[
{"title": "Chase Me (Paris Nights #2)", "price": 25.27, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/9c/2e/9c2e0eb8866b8e3f3b768994fd3d1c1a.jpg"},
{"title": "Black Dust", "price": 34.53, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/44/cc/44ccc99c8f82c33d4f9d2afa4ef25787.jpg"},
{"title": "Her Backup Boyfriend (The Sorensen Family #1)", "price": 33.97, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/1e/bb/1ebbbc3e2d3249b111033cfc40763b0b.jpg"},
{"title": "First and First (Five Boroughs #3)", "price": 15.97, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/c4/d1/c4d1517cc9370e292366b6132ca9ca36.jpg"},
{"title": "Fifty Shades Darker (Fifty Shades #2)", "price": 21.96, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/cc/bd/ccbdae9e29b3594301528fa2c876ec29.jpg"},
{"title": "The Wedding Dress", "price": 24.12, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/28/99/28992d89f4abf54fba183fc8d074adf3.jpg"},
{"title": "Suddenly in Love (Lake Haven #1)", "price": 55.99, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/e9/f4/e9f4bc8cf5ffaea1504623c936e90a48.jpg"},
{"title": "Something More Than This", "price": 16.24, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/59/10/5910fbd8a95e8e9de9c660b71e0694e2.jpg"},
{"title": "Doing It Over (Most Likely To #1)", "price": 35.61, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/e9/25/e9250495a525eb203652ad9da85ccb8e.jpg"},
{"title": "The Wedding Pact (The O'Malleys #2)", "price": 32.61, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/7e/67/7e67addd80caaf8a9f9e9daa9cf66bb2.jpg"},
{"title": "Hold Your Breath (Search and Rescue #1)", "price": 28.82, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/0b/89/0b89c3b317d0f89da48356a0b5959c1e.jpg"},
{"title": "Dirty (Dive Bar #1)", "price": 40.83, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/ae/90/ae903f6f6d059954be4e85497dd76bf5.jpg"},
{"title": "Take Me Home Tonight (Rock Star Romance #3)", "price": 53.98, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/a6/4b/a64b3c559f59748bfdbbe75be3e16075.jpg"},
{"title": "Off the Hook (Fishing for Trouble #1)", "price": 47.67, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/1d/78/1d78fe226e1adb9cb591fa21f8a9bf68.jpg"},
{"title": "A Gentleman's Position (Society of Gentlemen #3)", "price": 14.75, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/f0/e0/f0e0db3edcb14293a52b51929cc72979.jpg"},
{"title": "Sit, Stay, Love", "price": 20.9, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/8e/40/8e408552c2e7ee81cd60c03c79f604af.jpg"},
{"title": "A Girl's Guide to Moving On (New Beginnings #2)", "price": 31.3, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/f7/a9/f7a90a63f66ac92cc280def001970ed2.jpg"},
{"title": "The Perfect Play (Play by Play #1)", "price": 59.99, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/40/16/4016ffba678f309171d8130135f6eb8e.jpg"},
{"title": "Dark Lover (Black Dagger Brotherhood #1)", "price": 12.87, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/3c/a2/3ca2e61181fc1122658af8f85354bae8.jpg"},
{"title": "Changing the Game (Play by Play #2)", "price": 13.38, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/57/47/57472d9c6d483bee9c38c90bfa10b3ee.jpg"},
{"title": "A Walk to Remember", "price": 56.43, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/fa/1b/fa1b0fac146201645c740b02802e2211.jpg"},
{"title": "The Purest Hook (Second Circle Tattoos #3)", "price": 12.25, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/15/68/1568ef85fdb4e405b9f8bc62ef855c10.jpg"},
{"title": "The Obsession", "price": 45.43, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/24/93/2493c74c614afcc435cc00e33bd55f64.jpg"},
{"title": "Reservations for Two", "price": 11.1, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/39/a4/39a4d96a5bc75a34aae97676a4b854fa.jpg"},
{"title": "Best of My Love (Fool's Gold #20)", "price": 27.41, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/06/8c/068ccab8875670fccb8b72234370d16f.jpg"},
{"title": "Where Lightning Strikes (Bleeding Stars #3)", "price": 39.77, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/73/d9/73d948af3f2adb6dd693ff4bd43e7760.jpg"},
{"title": "This One Moment (Pushing Limits #1)", "price": 48.71, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/9b/06/9b061431c4fbb98cc18068a523a49988.jpg"},
{"title": "Rhythm, Chord & Malykhin", "price": 28.34, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/43/85/4385ee0304bc3546f2b6eaa75c46d4f8.jpg"},
{"title": "My Perfect Mistake (Over the Top #1)", "price": 38.92, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/0d/03/0d03eb55ed070a53b6c4b6eedd48b458.jpg"},
{"title": "Listen to Me (Fusion #1)", "price": 58.99, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/00/dd/00dd43f59d255cbc16e9d9c9ed20a997.jpg"},
{"title": "Imperfect Harmony", "price": 34.74, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/fb/29/fb299a516730a2f2602b10f945f7a8e5.jpg"},
{"title": "Fighting Fate (Fighting #6)", "price": 39.24, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/57/e2/57e255929f6e597c18cb3843904cd92b.jpg"},
{"title": "Deep Under (Walker Security #1)", "price": 47.09, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/74/e4/74e4ec43c40926c7b57fc0fe0f397183.jpg"},
{"title": "Charity's Cross (Charles Towne Belles #4)", "price": 41.24, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/39/e0/39e008f84bbd24b49a7532c2024b855e.jpg"},
{"title": "Bounty (Colorado Mountain #7)", "price": 37.26, "stock": true, "imageUrl": "http://books.toscrape.com/media/cache/80/ff/80ff924ed78cd7c5172410d0d92f8dfe.jpg"}
]
```
## Contributing

Contributions to this project are welcome. If you find any issues or improvements, feel free to open an issue or submit a pull request.
