import requests
from bs4 import BeautifulSoup
import random
import time

class AnekdotParser:
    def __init__(self):
        self.base_url = "https://www.anekdot.ru"
        self.used_jokes = set()  
        self.max_attempts = 50   
        
    def get_random_page(self):
        """Получает случайную страницу с анекдотами"""
        random_id = random.randint(1, 5000)
        url = f"{self.base_url}/random/anekdot/{random_id}"
        return url
    
    def extract_jokes_from_page(self, html_content):
        """Извлекает анекдоты из HTML страницы"""
        jokes = []
        soup = BeautifulSoup(html_content, 'html.parser')
        
        joke_elements = soup.find_all('div', class_='text')
        
        for element in joke_elements:
            joke_text = element.get_text().strip()
            if joke_text and len(joke_text) > 20: 
                joke_hash = hash(joke_text[:100])  
                if joke_hash not in self.used_jokes:
                    jokes.append(joke_text)
                    self.used_jokes.add(joke_hash)
        
        return jokes
    
    def get_random_joke(self):
        """Получает случайный анекдот"""
        attempt = 0
        
        while attempt < self.max_attempts:
            try:
                page_url = self.get_random_page()
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                response = requests.get(page_url, headers=headers, timeout=10)
                response.encoding = 'utf-8'
                
                if response.status_code == 200:
                    jokes = self.extract_jokes_from_page(response.text)
                    
                    if jokes:
                        selected_joke = random.choice(jokes)
                        return selected_joke
                
                time.sleep(1)
                attempt += 1
                
            except Exception as e:
                print(f"Ошибка при получении анекдота: {e}")
                attempt += 1
                time.sleep(2)
        
        return "Извините, не удалось найти новый анекдот. Попробуйте позже."

    def get_unique_random_joke(self):
        """Получает уникальный случайный анекдот"""
        joke = self.get_random_joke()
        return joke
def main():
    parser = AnekdotParser()
    

    print("-" * 50)
    
    joke = parser.get_unique_random_joke()
    print(joke)
    


if __name__ == "__main__":
    main()