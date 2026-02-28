import json
import os


DEFAULT_SITE_CONTENT = {
    "brand": {
        "name": "Twave",
        "logo": "images/logo.png"
    },
    "menus": {
        "primary": [],
        "footer_intro": [],
        "footer_products": []
    },
    "header": {
        "hotline_display": "",
        "hotline_tel": "",
        "language_label": "EN"
    },
    "home": {
        "hero": {
            "kicker": "",
            "title": "",
            "description": "",
            "primary_button": {"label": "", "href": "#"},
            "secondary_button": {"label": "", "href": "#"},
            "stats": []
        },
        "products": {
            "title": "",
            "subtitle": "",
            "items": []
        },
        "capability": {
            "title": "",
            "description": "",
            "bullets": [],
            "panel": {
                "title": "",
                "description": "",
                "button": {"label": "", "href": "#"}
            }
        },
        "news": {
            "title": "",
            "items": []
        },
        "cta": {
            "title": "",
            "description": "",
            "button": {"label": "", "href": "#"}
        }
    },
    "product_categories": [],
    "products": [],
    "footer": {
        "description": "",
        "contact": {
            "address": "",
            "phone_display": "",
            "phone_tel": "",
            "email": ""
        },
        "social": [],
        "copyright_holder": "Twave"
    }
}


def deep_merge(base, override):
    result = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def load_site_content(base_dir):
    data_path = os.path.join(base_dir, "data", "site.json")
    try:
        with open(data_path, "r", encoding="utf-8-sig") as f:
            loaded = json.load(f)
        if not isinstance(loaded, dict):
            return DEFAULT_SITE_CONTENT
        return deep_merge(DEFAULT_SITE_CONTENT, loaded)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_SITE_CONTENT


def get_catalog_data(base_dir):
    site = load_site_content(base_dir)
    categories = site.get("product_categories", [])
    products = site.get("products", [])

    category_by_slug = {
        category.get("slug"): category
        for category in categories
        if category.get("slug")
    }

    hydrated_products = []
    for product in products:
        item = dict(product)
        category = category_by_slug.get(item.get("category_slug"), {})
        item["category_name"] = category.get("name", "Chưa phân loại")
        hydrated_products.append(item)

    return hydrated_products, categories
