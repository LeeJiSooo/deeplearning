import requests
from bs4 import BeautifulSoup

def scrape_naver_news():
    """
    네이버 뉴스 IT/과학 섹션에서 가장 많이 본 뉴스 상위 10개의 헤드라인과 링크를 스크래핑합니다.
    """
    URL = 'https://news.naver.com/main/ranking/popularDay.naver?rankingType=popular_day&sectionId=105'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(URL, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"오류: 웹 페이지를 가져오는 데 실패했습니다: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_list = soup.select('.rankingnews_list > li')
    
    headlines = []
    for item in news_list[:10]:
        anchor = item.select_one('.list_title')
        if anchor and anchor.has_attr('href'):
            title = anchor.get_text(strip=True)
            link = anchor['href']
            
            if link.startswith('/main/ranking/'):
                link = "https://news.naver.com" + link
            
            headlines.append({'title': title, 'link': link})
            
    return headlines
