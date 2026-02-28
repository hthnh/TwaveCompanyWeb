from flask import Blueprint, render_template
import json
import os

product_bp = Blueprint("product", __name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")

def load_products():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@product_bp.route("/san-pham")
def products():
    products = load_products()
    return render_template("products.html", products=products)

@product_bp.route("/san-pham/<slug>")
def product_detail(slug):
    products = load_products()
    product = next((p for p in products if p["slug"] == slug), None)
    return render_template("product_detail.html", product=product)