from django.contrib import admin
from django.db.models import Count, Sum
from .models import Assortment, Geography, Sales

# Register models

@admin.register(Assortment)
class AssortmentAdmin(admin.ModelAdmin):
    list_display = ('product', 'brand', 'info_brand', 'manufacturer', 'info_manufacturer')
    list_display_links = ['product']
    ordering = ('manufacturer', 'brand', 'product')
    list_per_page = 15
    search_fields = ['product', 'brand', 'manufacturer']
    list_filter = ['manufacturer']

    def info_manufacturer(self, assortment: Assortment):
        a = Assortment.objects.filter(manufacturer=assortment.manufacturer).values('brand').aggregate(
            res=Count('brand', distinct=True))
        return f"Производитель {assortment.manufacturer} выпускает " \
               f"{a['res'] } бренд(-ов)."

    def info_brand(self, assortment: Assortment):
        a = Assortment.objects.filter(brand=assortment.brand).values('product').aggregate(
            res=Count('product', distinct=True))
        return f"Бренд {assortment.brand} включает " \
               f"{a['res'] } продукт(-ов)."


@admin.register(Geography)
class GeographyAdmin(admin.ModelAdmin):
    list_display = ('id', 'region', 'federal_district', 'info')
    list_display_links = ('id', 'region')
    list_per_page = 15
    search_fields = ['region', 'federal_district']
    list_filter = ['federal_district']

    def info(self, geography: Geography):
        return f"{geography.federal_district} включает " \
               f"{len(Geography.objects.filter(federal_district=geography.federal_district))} регионов."


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('region', 'product', 'unit', 'total_units', 'rub', 'total_rubs')
    list_display_links = ('region', 'product')
    ordering = ('region', 'product')
    list_per_page = 30
    search_fields = ['region__region', 'product__product']
    list_filter = ['region__region']

    def total_units(self, sales: Sales):
        a = Sales.objects.filter(region=sales.region).aggregate(
            res=Sum('unit'))
        return f"ТОТАЛ по региону ({sales.region}): {a['res'] } шт."

    def total_rubs(self, sales: Sales):
        a = Sales.objects.filter(region=sales.region).aggregate(
            res=Sum('rub'))
        return f"ТОТАЛ по региону ({sales.region}): {round(a['res'])} руб."
