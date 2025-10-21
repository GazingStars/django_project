
# Django-приложение клинических рекомендаций

Веб‑приложение на **Django** для хранения и просмотра **клинических рекомендаций**.  
Поддерживает список рекомендаций, детальную страницу, главную и страницу «О проекте», регистрацию моделей в админ‑панели, а также аккуратные шаблоны и стили.

---

## Технологии

- **Python 3.11+**, **Django 5.x** (совместимо с 4.x)
- Django ORM (SQLite/PostgreSQL — на выбор)
- Шаблоны Django + **Static files** (CSS/изображения)
- Админ‑панель Django

---

## Структура приложения (фрагменты)

```

  /clinic_lab                
    admin.py
    models.py
    urls.py
    views.py
    /templates
      about.html
      clinical_recommendation_detail.html
      index.html
      recommendation_list.html
    /static/clinic_lab/css
      styleIndex.css
      stylerecommendation_list.css
      clinical_recommendation_detail.css
      style_About.css
  project_root/
    settings.py
    urls.py
manage.py
```

---

## Модели

### GeneralInformationOfClinicalRecommendation
Общая карточка клинической рекомендации:
- `title: CharField` — заголовок (отображается в списках/карточках)
- `MCB: TextField` — кодирование по МКБ
- `Age_category: TextField` — возрастная категория
- `Status: TextField` — статус

### ClinicalRecommendation
Детализированная часть, связана **1:1** с общей карточкой:
- `general_info: OneToOneField` → `GeneralInformationOfClinicalRecommendation`
- `title: CharField` — заголовок (дублируется/уточняется)
- `description: TextField` — свободное описание
- `list_of_abbreviations: TextField` — список сокращений
- `terms_and_definitions: TextField` — термины и определения
- `Brief_information: TextField` — краткая информация
- `Laboratory_diagnostic_tests: TextField` — лабораторные исследования

Обе модели имеют `__str__`, чтобы красиво отображаться в админке.

---

## Маршруты (URLs)

Определены в `clinic_lab/urls.py`:

- `/` — главная (`index`)
- `/recommendation/` — список рекомендаций (`recommendation_list`)
- `/recommendation/<int:pk>/` — детальная страница рекомендации (`clinical_recommendation_detail`)
- `/about/` — страница «О проекте» (`about`)

Подключите их в **корневом** `project_root/urls.py`:
```python
from django.urls import path, include

urlpatterns = [
    path('', include('clinic_lab.urls')),
    path('admin/', admin.site.urls),
]
```

---

## Views

- `index` — главная, передаёт контент о проекте.
- `recommendation_list` — выдаёт список рекомендаций + общие карточки.
- `clinical_recommendation_detail(pk)` — детальная страница по первичному ключу.
- `about` — статическая страница с описанием проекта и контактами.

---

## Шаблоны и стили

Шаблоны в `clinic_lab/templates` используют переданные из вью переменные.  
Основные CSS в `clinic_lab/static/clinic_lab/css`. Примеры:
- `index.html` — hero‑секция, меню навигации (с классами `navbar`, `hero-section` и пр.).
- `recommendation_list.html` — сетка карточек рекомендаций с адаптивными стилями.
- `clinical_recommendation_detail.html` — аккуратная карточка с секциями.
- `about.html` — блок с контактами.

> Не забудьте подключить **static** в шаблонах: `{% load static %}` и в `settings.py` указать `STATIC_URL` / `STATICFILES_DIRS`.

---

## Развёртывание локально

1) **Клонирование и окружение**
```bash
git clone https://github.com/yourusername/alea-kl.git
cd alea-kl
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

2) **Установка зависимостей**
```bash
pip install -U pip
pip install django
# опционально: pip install psycopg2-binary  # если используете PostgreSQL
```

3) **Настройки**
   В `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'clinic_lab',
]

STATIC_URL = 'static/'
# Если есть внешняя папка со статикой:
# STATICFILES_DIRS = [ BASE_DIR / 'static' ]
```

4) **Миграции и суперпользователь**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5) **Наполнить тестовыми данными (опционально)**
   Через админ‑панель (`/admin/`) создать:
- `GeneralInformationOfClinicalRecommendation` (общая карточка)
- `ClinicalRecommendation` и привязать 1:1 к общей карточке

6) **Запуск**
```bash
python manage.py runserver
```
Открой: http://127.0.0.1:8000/

---

## Админ‑панель

`clinic_lab/admin.py` регистрирует модели с удобными настройками:
- `GeneralInformationAdmin` → `list_display=('title','MCB','Age_category','Status')`, поиск по `title`, `MCB`.
- `ClinicalRecommendationAdmin` → `list_display=('title',)`, поиск по `title`, фильтр по `general_info`.

Админ доступен по `/admin/` после создания суперпользователя.

---

## Проверка страниц

- Главная: `/` — название проекта, слоган, особенности, ссылка на «О проекте».
- Список рекомендаций: `/recommendation/` — карточки на CSS‑сетке, переход на детальную.
- Детальная страница: `/recommendation/<id>/` — блок «Общая информация» и секции с контентом.
- О проекте: `/about/` — описание и контакты, стилизованные блоки.

---

## Полезные команды

```bash
python manage.py shell           # интерактивная оболочка
python manage.py collectstatic   # для продакшена со STATIC_ROOT
python manage.py dumpdata > fixtures.json  # экспорт данных
python manage.py loaddata fixtures.json    # импорт данных
```


---

## Дорожная карта

- [ ] Поиск/фильтры по списку рекомендаций
- [ ] Версионирование рекомендаций (история правок)
- [ ] Экспорт в PDF/Docx
- [ ] Контроль доступа (группы/роли: врач/редактор/админ)
- [ ] API (Django REST Framework) для внешних клиентов
- [ ] Тесты (pytest/Django TestCase)

---

