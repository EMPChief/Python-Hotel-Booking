from fpdf import FPDF
import pandas as pd
import random

class ArticleReceiptGenerator:
    def __init__(self, articles_path):
        self.articles_path = articles_path

    def read_articles(self):
        articles_df = pd.read_csv(
            self.articles_path, dtype={"id": int, 
                                       "name": str, 
                                       "price": float, 
                                       "in_stock": int})
        return articles_df

    def find_article_by_id(self, article_id):
        articles_df = self.read_articles()
        article = articles_df.loc[articles_df['id'] == article_id]
        if not article.empty:
            article = article.iloc[0]
            if article['in_stock'] > 0:
                articles_df.loc[articles_df['id'] == article_id, 'in_stock'] -= 1
                articles_df.to_csv(self.articles_path, index=False)
                print(f"Article {article['name']} has been sold.")
                return {
                    'id': article['id'],
                    'name': article['name'],
                    'price': article['price'],
                    'in_stock': article['in_stock']}
            else:
                print(f"Article {article['name']} is out of stock.")
                return None
                
    
    @staticmethod
    def generate_article_receipt(article):
        random_receipt_number = random.randint(1, 9999)
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, f"Receipt Nr. {random_receipt_number}", 0, 1, "C")
        pdf.ln(10)
        
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Article: {article['name']}", 0, 1)
        pdf.cell(0, 10, f"ID: {article['id']}", 0, 1)
        pdf.cell(0, 10, f"Price: ${article['price']:.2f}", 0, 1)
        
        pdf.output(f"data/article_receipt_{random_receipt_number}.pdf")

if __name__ == "__main__":
    receipt_generator = ArticleReceiptGenerator("articles.csv")
    article = receipt_generator.find_article_by_id(106)
    if article:
        receipt_generator.generate_article_receipt(article)
    else:
        print("Article not found.")
