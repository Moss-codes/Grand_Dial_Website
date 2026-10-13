from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/index.html')

def draft(request):
    return render(request,'core/draft.html')

def collection(request):
    watches = [
        {
            "name": "Chronos Noir",
            "price": "$1,299",
            "description": "Matte black ceramic case with a sapphire crystal display.",
            "available": True,
        },
        {
            "name": "Aether Gold",
            "price": "$2,499",
            "description": "18k gold-plated chassis paired with a premium leather strap.",
            "available": False,
        },
        {
            "name": "Vortex Sport",
            "price": "$899",
            "description": "Aerospace-grade titanium built for extreme athletic endurance.",
            "available": True,
        },
        {
            "name": "Eclipse Steel",
            "price": "$1,150",
            "description": "Brushed stainless steel offering a timeless traditional look.",
            "available": True,
        },
        {
            "name": "Horizon Titanium",
            "price": "$1,799",
            "description": "Ultra-lightweight minimalist design with advanced health sensors.",
            "available": False,
        },
    ]
    return render(request,'core/collection.html', context={'watches':watches})