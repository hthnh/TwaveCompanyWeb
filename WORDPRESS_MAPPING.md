# WORDPRESS_MAPPING.md

Tai lieu nay mo ta cach chuyen du lieu tu `app/data/site.json` sang WordPress theo huong de ban giao cho team non-technical.

## 1) Muc tieu
- Giu nguyen logic hien tai cua website placeholder.
- Dua toan bo noi dung vao dashboard WordPress de nguoi dung sua khong can code.
- Co the import du lieu mau tu `site.json` nhanh.

## 2) Tong quan mapping

### 2.1 Brand + Header + Footer + Home
- Nen luu trong `Theme Options` (ACF Options Page) vi day la du lieu toan site.

### 2.2 Product categories
- Map vao taxonomy `product_category`.

### 2.3 Products
- Map vao Custom Post Type `product`.

### 2.4 Menu dieu huong
- `menus.primary` -> WP Menu: `Primary Menu`
- `menus.footer_intro` -> WP Menu: `Footer Intro Menu`
- `menus.footer_products` -> WP Menu: `Footer Products Menu` (chi dung fallback)

## 3) Cau hinh WordPress can tao

### 3.1 CPT: `product`
Field co ban cua post:
- `post_title` <- `products[].name`
- `post_name` <- `products[].slug`
- `post_status` = `publish`

Taxonomy:
- `product_category` <- `products[].category_slug`

ACF fields cho `product`:
- `product_sku` (text) <- `sku`
- `product_price` (number) <- `price`
- `short_description` (textarea) <- `short_description`
- `hero_image` (image) <- `hero_image`
- `thumbnail_image` (image) <- `thumbnail`
- `highlights` (repeater: `text`) <- `highlights[]`
- `specs` (repeater: `label`, `value`) <- `specs[]`
- `sections` (repeater: `title`, `content`) <- `sections[]`
- `gallery` (gallery/repeater image) <- `gallery[]`

### 3.2 Taxonomy: `product_category`
- `name` <- `product_categories[].name`
- `slug` <- `product_categories[].slug`
- `description` <- `product_categories[].description`

### 3.3 ACF Options Page (Global)
Group `Site Settings`:
- `brand_name` <- `brand.name`
- `brand_logo` <- `brand.logo`

Group `Header Settings`:
- `hotline_display` <- `header.hotline_display`
- `hotline_tel` <- `header.hotline_tel`
- `language_label` <- `header.language_label`

Group `Footer Settings`:
- `footer_description` <- `footer.description`
- `footer_address` <- `footer.contact.address`
- `footer_phone_display` <- `footer.contact.phone_display`
- `footer_phone_tel` <- `footer.contact.phone_tel`
- `footer_email` <- `footer.contact.email`
- `footer_social` (repeater: `label`, `href`, `icon`, `text`) <- `footer.social[]`
- `copyright_holder` <- `footer.copyright_holder`

Group `Homepage Settings`:
- Hero:
  - `hero_kicker`, `hero_title`, `hero_description`
  - `hero_primary_label`, `hero_primary_url`
  - `hero_secondary_label`, `hero_secondary_url`
  - `hero_stats` (repeater: `value`, `label`)
- Product section:
  - `home_products_title`, `home_products_subtitle`
  - `home_products_items` (repeater: `title`, `description`, `url`)
- Capability section:
  - `capability_title`, `capability_description`
  - `capability_bullets` (repeater: `text`)
  - `capability_panel_title`, `capability_panel_description`
  - `capability_panel_btn_label`, `capability_panel_btn_url`
- News section:
  - `home_news_title`
  - `home_news_items` (repeater: `tag`, `title`, `description`)
- CTA section:
  - `home_cta_title`, `home_cta_description`
  - `home_cta_btn_label`, `home_cta_btn_url`

## 4) Mapping menu logic hien tai

`menus.primary[]` hien co them field dac biet:
- `match_prefix`: dung cho active state (theme code xu ly)
- `children_source = product_categories`: tu dong sinh submenu tu taxonomy `product_category`

Trong WP:
- Co 2 cach:
  1. Hardcode logic trong theme: neu item la "San pham" thi auto render taxonomy children.
  2. Quan ly thu cong bang WP Menu (de user keo-tha). 

Khuyen nghi giai doan dau: cach (1) de giong behavior hien tai nhanh va on dinh.

## 5) Mapping route/template Flask -> template WP

- `partials/header.html` -> `header.php`
- `partials/footer.html` -> `footer.php`
- `index.html` -> `front-page.php`
- `product.html` -> `archive-product.php`
- `product_detail.html` -> `single-product.php`

## 6) Ke hoach import du lieu mau

### 6.1 Thu tu import
1. Import `product_categories` vao taxonomy.
2. Import `products` vao CPT + gan taxonomy.
3. Import `brand/header/footer/home` vao ACF Options.
4. Tao menu WordPress tu `menus.*` (neu chon dung WP Menu).

### 6.2 Luu y anh
- Duong dan trong JSON dang la `images/logo.png` theo static Flask.
- Khi import qua WP can map thanh attachment IDs.
- Cach nhanh: upload logo/anh truoc, tao bang map `path -> attachment_id` trong script import.

## 7) Quy tac schema de de quan tri
- `slug` la unique, lowercase, dung `-`, khong dau.
- Moi product bat buoc: `slug`, `name`, `category_slug`, `short_description`.
- Khuyen nghi bat buoc them: `sku`, `price`, `hero_image`.
- `category_slug` phai ton tai trong `product_categories`.

## 8) Kiem thu truoc khi chuyen full
- Test list products + filter category.
- Test single product voi du data va thieu data (fallback).
- Test header submenu products (desktop + mobile).
- Test footer contact/social.
- Test chinh sua noi dung tu dashboard khong vo layout.

## 9) Muc tiep theo (sau khi ban ok)
- Tao bo field ACF bang JSON export.
- Tao script import `site.json` vao WordPress (WP-CLI command).
- Dung skeleton theme theo mapping ben tren.
