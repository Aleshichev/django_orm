from inventory.models import Brand, Category, Tag, Stock
from django.db import connection, reset_queries

Brand.objects.create(brand_id=1, name="adidas", category_id=1)
Category.objects.create(name="T-shirts")

x = Brand(brand_id=3, name="adidas2").save()  # create and update

x = Brand.objects.all()  # return query

x = Brand.objects.all().values()  # return [dict]
x = Brand.objects.all().values("name")

x = Brand.objects.all().query  # SQL запрос

Brand.objects.all().delete()

connection.queries  # все SQL запросы  [-1] индекс запроса
reset_queries()  # очистить все запросы

x = Brand.objects.filter(brand_id=1)
x = Brand.objects.all().count()

# ------------------- SQL ------------------------------------

cursor = connection.cursor()
cursor.execute(
    "INSERT INTO inventory_brand (brand_id, name) VALUES (%s,%s)", ("1", "trpuma")
)


# ----------------many-to-many --------------------------------
x = Brand.objects.get(brand_id=234)
x.tag.add(Tag.objects.get(id=2))
x.tag.remove(Tag.objects.get(id=2))
x.tag.add(Tag.objects.create(name="new"))

Stock.objects.update(quantity=11, product_brand_id=234)

Brand.objects.bulk_create(
    [
        Brand(brand_id=233, name="aduidas", category_id=1),
        Brand(brand_id=235, name="nikpe", category_id=2),
    ]
)


# ------------------ get -----------------------
from django.shortcuts import get_object_or_404
from django.db.models import Q

Tag.objects.get(id=1)
Tag.objects.get_or_create(name="egfgf-ytr")

get_object_or_404(Tag, name="egfgf-ytr")

# ------------filter exclude ----------------------------

Tag.objects.all().filter(id=5)
Tag.objects.filter(id=5)
Tag.objects.exclude(id=5)

Tag.objects.filter(id=5) | Tag.objects.filter(id=4)  # AND   OR
Tag.objects.filter(Q(id=5) | Q(id=4))  # AND   OR
Tag.objects.filter(id__gt=5)  # greater than
Tag.objects.filter(name__startswith="e")  # startswith

# --------------- foreign key ----------------------------

Brand.objects.filter(category_id__name="new")  # через category в Brand
Brand.objects.filter(category_id__name__contains="n")   # содержит

first_brand = Category.objects.first()
first_brand.brand_set.all()     # обратная доступность


#----------- one to one -------------------
Brand.objects.filter(stocks__quantity=11)
Brand.objects.filter(stocks__quantity_lte=11)  # less than or equal
Brand.objects.filter(stocks__quantity_qte=1)   # greater than or equal

Stock.objects.filter(product_brand__name__contains='adi')

#-----------many to many ------------------------

Brand.objects.filter(tag__id=1)
Brand.objects.filter(tag__name__contains='eg')

Brand.tag.through.objects.all()
Tag.objects.filter(brand_tags__brand_id=1)


