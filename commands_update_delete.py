from inventory.models import Brand, Category, Tag, Stock


Brand.objects.filter(brand_id=1).update(name='new name')
Brand.objects.update_or_create(name="new name")
Tag.objects.update_or_create(name="new name2")
Tag.objects.update_or_create(name="new name2", defaults={"name": "old name3"})

objs = [ Tag.objects.get(id=4), Tag.objects.get(id=3),]
objs[0].name = 'old old name'
objs[1].name = 'new new name2'

Tag.objects.bulk_update(objs, 'name')

#------------------- delete -----------------------------
Brand.objects.filter(brand_id=4).delete()
