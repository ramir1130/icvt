# ICVT

Простое веб-приложение на Flask, которое позволяет загружать изображение и искать похожие в папке `db/` с помощью перцептивного хеша (`imagehash`). Нужен для проверки изображений которые могут быть защищены авторскими правами.

## Технологии

- Python (Flask)
- HTML, CSS, JavaScript
- Pillow + ImageHash

## Установка

```bash
git clone https://github.com/ramir1130/icvt.git
cd icvt
python server.py
