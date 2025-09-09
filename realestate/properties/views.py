from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Property

def property_list(request):
    properties = Property.objects.filter(status__in=['for_sale', 'for_rent'])
    
    # Search functionality
    search = request.GET.get('search')
    if search:
        properties = properties.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(city__icontains=search) |
            Q(state__icontains=search)
        )
    
    # Filter by property type
    property_type = request.GET.get('property_type')
    if property_type:
        properties = properties.filter(property_type=property_type)
    
    # Filter by status
    status = request.GET.get('status')
    if status:
        properties = properties.filter(status=status)
    
    # Filter by price range
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    
    # Pagination
    paginator = Paginator(properties, 6)  # Show 6 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'property_types': Property.PROPERTY_TYPES,
        'status_choices': Property.STATUS_CHOICES,
        'current_search': search,
        'current_property_type': property_type,
        'current_status': status,
        'current_min_price': min_price,
        'current_max_price': max_price,
    }
    
    return render(request, 'properties/property_list.html', context)

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    context = {
        'property': property,
    }
    return render(request, 'properties/property_detail.html', context)

def home(request):
    # Get latest 6 properties
    recent_properties = Property.objects.filter(status__in=['for_sale', 'for_rent'])[:6]
    
    context = {
        'recent_properties': recent_properties,
    }
    return render(request, 'properties/home.html', context)
