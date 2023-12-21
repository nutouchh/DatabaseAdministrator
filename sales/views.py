from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from sales.models import Sales
from django.shortcuts import render


def get_sum_rub_for_fo():
    sales_data = Sales.objects.values('region__federal_district').annotate(total_rub=Sum('rub'))

    labels = [entry['region__federal_district'] for entry in sales_data]
    data = [int(entry['total_rub']) for entry in sales_data]

    return labels, data

def get_manufacturer_proportion():
    sales_data = Sales.objects.values('product__manufacturer').annotate(total_unit=Sum('unit'))

    labels = [entry['product__manufacturer'] for entry in sales_data]
    data = [int(entry['total_unit']) for entry in sales_data]

    return labels, data

def get_product_bar():
    sales_data = Sales.objects.filter(
        region__region='Москва и область',
        product__manufacturer='Аванта'
    ).values('product__product').annotate(
        total_rub=Sum('rub'),
        total_units=Sum('unit')
    )

    labels = [entry['product__product'] for entry in sales_data]
    quantities_sold = [int(entry['total_units']) for entry in sales_data]
    sales_in_rubles = [int(int(entry['total_rub']) * 0.01) for entry in sales_data]

    labels = labels[:10]
    quantities_sold = quantities_sold[:10]
    sales_in_rubles = sales_in_rubles[:10]

    return labels, quantities_sold, sales_in_rubles

def get_bubble():
    sales_data = Sales.objects.filter(product__manufacturer='Аванта').values('product__brand').annotate(
        total_rub=Sum('rub'),
        total_units=Sum('unit')
    )

    labels = [entry['product__brand'] for entry in sales_data]
    x_values = [int(entry['total_rub']) for entry in sales_data]
    y_values = [int(entry['total_units']) for entry in sales_data]
    r_values = [int(int(entry['total_rub']) * 0.0000004) for entry in sales_data]

    labels = labels
    x_values = x_values
    y_values = y_values
    r_values = r_values

    data = [
        {'x': x_values[index], 'y': y_values[index], 'r': r_values[index]}
        for index in range(len(labels))
    ]

    return labels, data

@login_required
def chart(request):
    labels1, data1 = get_sum_rub_for_fo()
    labels2, data2 = get_manufacturer_proportion()
    labels3, quantities_sold, sales_in_rubles = get_product_bar()
    labels4, data4 = get_bubble()

    context = {
        'labels1': labels1,
        'data1': data1,
        'labels2': labels2,
        'data2': data2,
        'labels3': labels3,
        'quantities_sold': quantities_sold,
        'sales_in_rubles': sales_in_rubles,
        'labels4': labels4,
        'data4': data4,
    }

    return render(request, 'sales/dashboard.html', context)
