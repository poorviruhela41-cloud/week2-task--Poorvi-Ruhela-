import requests

API_KEY = "dbd4df4af05545ba979afe925dbc0dd8"   # <-- Yahan apni NewsAPI key dalen
BASE_URL = "https://newsapi.org/v2/top-headlines"

def get_headlines(category="general", country="us"):
    params = {
        "apiKey": API_KEY,
        "category": category,
        "country": country,
        "pageSize": 5  # sirf 5 news headlines
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        
        print(f"\n📰 Latest {category.capitalize()} Headlines:\n")
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
    else:
        print("❌ Error fetching news:", response.status_code)

def main():
    print("News Categories: general, business, entertainment, health, science, sports, technology")
    category = input("Enter category (default: general): ").strip().lower()
    
    if category == "":
        category = "general"
    
    get_headlines(category)

if __name__ == "__main__":
    main()