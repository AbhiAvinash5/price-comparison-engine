from flask import Flask, render_template, request
import urllib.parse

app = Flask(__name__)

# Placeholder function for scraping multiple sites
def get_prices(product):
    query = urllib.parse.quote_plus(product)

    # Example data for demonstration
    results = [
        {"site":"Flipkart","name":f"{product} Model A","price":45000,"link":"https://flipkart.com/productA"},
        {"site":"Amazon","name":f"{product} Model B","price":44000,"link":"https://amazon.in/productB"},
        {"site":"eBay","name":f"{product} Model C","price":46000,"link":"https://ebay.com/productC"}
    ]
    # Sort by price
    results = sorted(results, key=lambda x: x['price'])
    return results

@app.route("/", methods=["GET","POST"])
def index():
    results = []
    lowest = None
    if request.method == "POST":
        product = request.form.get("product")
        if product:
            results = get_prices(product)
            if results:
                lowest = results[0]  # Lowest price
    return render_template("index.html", results=results, lowest=lowest)

if __name__ == "__main__":
    app.run(debug=True)