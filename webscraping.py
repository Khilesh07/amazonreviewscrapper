import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

reviewlist = []
def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup
def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = {
            'product': soup.title.text.replace('Amazon.in:Customer reviews:', '').strip(), #'
            'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
            'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass
for x in range(1,999):
    soup = get_soup(f'https://www.amazon.in/Lenovo-inch-27-94-Wi-Fi-Platinum/product-reviews/B099ML77P9/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviewspageNumber={x}')
    print(f'Getting page: {x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df.to_csv('lp48.csv', index=False)
print('Done')
