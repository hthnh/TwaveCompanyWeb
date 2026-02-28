# DATA_SCHEMA.md

Huong dan nay mo ta schema cua `site.json` dang duoc app su dung.

## 1) Muc tieu
- Toan bo noi dung website duoc quan ly trong `app/data/site.json`.
- Header, footer, homepage, danh muc san pham va trang chi tiet san pham deu doc tu file nay.
- Them/bot noi dung chi can sua JSON, khong can sua template.

## 2) Cau truc tong quan

```json
{
  "brand": {},
  "menus": {},
  "header": {},
  "home": {},
  "product_categories": [],
  "products": [],
  "footer": {}
}
```

## 3) Chi tiet tung block

### 3.1 `brand`
```json
"brand": {
  "name": "Twave",
  "logo": "images/logo.png"
}
```
- `name`: Ten thuong hieu.
- `logo`: Duong dan anh trong `app/static/`.

### 3.2 `menus`
```json
"menus": {
  "primary": [
    { "label": "Gioi thieu", "href": "/gioi-thieu" },
    {
      "label": "San pham",
      "href": "/san-pham",
      "match_prefix": true,
      "children_source": "product_categories"
    }
  ],
  "footer_intro": [
    { "label": "Ve cong ty", "href": "/gioi-thieu" }
  ],
  "footer_products": []
}
```
- `primary`: Menu chinh tren header.
- `match_prefix`: Danh dau active cho nhom route (vd `/san-pham/...`).
- `children_source = product_categories`: Tu dong sinh submenu tu danh muc san pham.
- `footer_intro`: Cot link gioi thieu o footer.
- `footer_products`: Fallback cho cot san pham footer neu khong dung danh muc dong.

### 3.3 `header`
```json
"header": {
  "hotline_display": "028 3969 0973",
  "hotline_tel": "02839690973",
  "language_label": "EN"
}
```

### 3.4 `home`
```json
"home": {
  "hero": {
    "kicker": "...",
    "title": "...",
    "description": "...",
    "primary_button": { "label": "...", "href": "/san-pham" },
    "secondary_button": { "label": "...", "href": "/lien-he" },
    "stats": [
      { "value": "20+", "label": "..." }
    ]
  },
  "products": {
    "title": "...",
    "subtitle": "...",
    "items": [
      { "title": "...", "description": "...", "href": "/san-pham" }
    ]
  },
  "capability": {
    "title": "...",
    "description": "...",
    "bullets": ["..."],
    "panel": {
      "title": "...",
      "description": "...",
      "button": { "label": "...", "href": "/lien-he" }
    }
  },
  "news": {
    "title": "...",
    "items": [
      { "tag": "...", "title": "...", "description": "..." }
    ]
  },
  "cta": {
    "title": "...",
    "description": "...",
    "button": { "label": "...", "href": "/lien-he" }
  }
}
```

### 3.5 `product_categories`
```json
"product_categories": [
  {
    "slug": "dan-dung",
    "name": "Dan dung",
    "description": "..."
  }
]
```
- `slug`: Dinh danh duy nhat (khong dau, khong khoang trang).
- Duoc dung cho:
  - Filter trang `/san-pham?danh-muc=<slug>`
  - Submenu header
  - Cot san pham o footer

### 3.6 `products`
```json
"products": [
  {
    "slug": "ong-pvc-cao-cap",
    "name": "Ong PVC cao cap",
    "category_slug": "dan-dung",
    "short_description": "...",
    "thumbnail": "images/logo.png",
    "hero_image": "images/logo.png",
    "price": 980000,
    "sku": "TW-PVC-001",
    "highlights": ["..."],
    "specs": [
      { "label": "Dai duong kinh", "value": "21 - 114 mm" }
    ],
    "sections": [
      { "title": "Ung dung", "content": "..." }
    ],
    "gallery": ["images/logo.png"]
  }
]
```
- Tat ca san pham dung chung 1 cau truc trang detail.
- `category_slug` phai khop voi 1 `product_categories.slug`.
- `hero_image`, `gallery[]`: anh trong `app/static/`.

### 3.7 `footer`
```json
"footer": {
  "description": "...",
  "contact": {
    "address": "...",
    "phone_display": "...",
    "phone_tel": "...",
    "email": "..."
  },
  "social": [
    { "label": "Facebook", "href": "#", "icon": "fa-brands fa-facebook-f" }
  ],
  "copyright_holder": "Tan Hung Company"
}
```

## 4) Quy trinh nhanh

### Them danh muc moi
1. Them object moi vao `product_categories`.
2. Refresh trang, menu/bo loc se cap nhat.

### Them san pham moi
1. Them object vao `products` theo dung schema.
2. Dat `category_slug` trung voi slug danh muc.
3. Refresh `/san-pham` va `/san-pham/<slug>` de kiem tra.

### Them muc menu thu cong
1. Them item vao `menus.primary` hoac `menus.footer_intro`.
2. Neu muon submenu tu dong theo danh muc, dat:
```json
"children_source": "product_categories"
```

## 5) Luu y quan trong
- File duoc doc moi request, sua JSON xong chi can refresh trang.
- JSON phai hop le (dung dau phay, dong ngoac).
- Neu bo trong field, app co default de tranh vo giao dien, nhung nen nhap day du de UI dep.
- Dung UTF-8 khi luu file de hien thi tieng Viet dung.
