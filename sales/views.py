from django.shortcuts import render
from django.db.models import Count,F,Sum,Avg
from django.db.models.functions import ExtractYear,ExtractMonth
from django.http import JsonResponse
from .models import Sales, Purchase
from .utils import (
    months,colorDanger,
    colorPrimary,colorSuccess,
    generate_color_palette,get_year_dict)
# Create your views here.

def display_charts(request):
    return render(request, 'charts.html', {})

def filter_options(request):
    merged_purchases=Purchase.objects.annotate(
        year=ExtractYear(
            'time_created'
        )).values(
            'year'
            ).order_by(
                '-year'
                ).distinct()
    options= [purchase['year'] for purchase in merged_purchases]

    return JsonResponse(data={
        'options':options
    })



def get_annual_sales(request, year):
    purchases=Purchase.objects.filter(time_created__year=year)
    merged_purchases=purchases.annotate(
        price=F('book__price')
    ).annotate(month=ExtractMonth('time_created')).values(
        'month'
    ).annotate(
        average=Sum(
            'book__price'
        )
    ).values(
        'month',
        'average'
    ).order_by('month')
    sales_dict=get_year_dict()
    for merge in merged_purchases:
        sales_dict[months[merge['month']-1]]=round(merge['average'], 2)

    return JsonResponse({
        'title':f'Sales in {year}',
        'data':{
            'labels':list(sales_dict.keys()),
            'datasets':[{
                'label':'Amount (KSHS)',
                'backgroundColor':generate_color_palette(7),
                'borderColor':generate_color_palette(5),
                'data':list(sales_dict.values())
            }]
        }
    })