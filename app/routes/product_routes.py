from flask import Blueprint, abort, current_app, render_template, request

from app.content_store import get_catalog_data

product_bp = Blueprint("product", __name__)


@product_bp.route("/san-pham")
def products():
    product_list, categories = get_catalog_data(current_app.root_path)
    active_category = request.args.get("danh-muc", "").strip()

    if active_category:
        product_list = [
            product
            for product in product_list
            if product.get("category_slug") == active_category
        ]

    return render_template(
        "product.html",
        products=product_list,
        categories=categories,
        active_category=active_category,
    )


@product_bp.route("/san-pham/<slug>")
def product_detail(slug):
    product_list, categories = get_catalog_data(current_app.root_path)
    product = next((p for p in product_list if p.get("slug") == slug), None)
    if product is None:
        abort(404)

    related_products = [
        p
        for p in product_list
        if p.get("slug") != slug and p.get("category_slug") == product.get("category_slug")
    ][:3]

    return render_template(
        "product_detail.html",
        product=product,
        categories=categories,
        related_products=related_products,
    )
