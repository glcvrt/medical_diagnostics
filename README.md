Сайт компании медицинской диагностики

Установка зависимостей:
Для работы приложения необходимо установить зависимости. Для этого в консоли пишем команду:

pip install -r requirements.txt

Создание суперпользователя
Для автоматического создания администратора с полным набором прав необходимо прописать в консоли команду:

python manage.py csu
Затем можно будет осуществлять как авторизацию на сайте, так и вход в админку.

Заполнение сайта контентом
Перед началом работы необходимо зайти в административную панель и создать там, экземпляры специализаций, врачей, услуг
