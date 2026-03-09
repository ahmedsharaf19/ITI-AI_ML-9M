from django.shortcuts import render
from django.http import HttpResponse

# Marketplace Information
marketplace_info = {
    "name": "Marketplace",
    "description": "Your ultimate destination for quality products and exceptional shopping experience",
    "founded": "2020",
    "mission": "To revolutionize online shopping by connecting customers with quality products at competitive prices",
    "vision": "Becoming the most trusted and customer-centric online marketplace globally",
    "customers": "2.5M+",
    "products": "50K+",
    "satisfaction_rate": "98%",
}

# Developer Information
developer_info = {
    "name": "Ahmed Sharaf",
    "title": "AI Engineer Developer",
    "organization": "ITI AI - Cohort 46",
    "location": "Mansoura, Egypt",
    "email": "ahmed@example.com",
    "phone": "+20 1234567890",
    "bio": "Passionate full-stack developer with expertise in Django, Python, and modern web technologies. Dedicated to creating beautiful and functional web applications.",
    "github": "#",
    "linkedin": "#",
    "twitter": "#",
    "instagram": "#"
}

# Company Core Values
company_values = [
    {
        "title": "Customer First",
        "description": "Your satisfaction is our top priority. We go the extra mile to ensure your happiness.",
        "icon": "fas fa-heart"
    },
    {
        "title": "Integrity",
        "description": "We believe in honest business practices and building trust with every transaction.",
        "icon": "fas fa-shield-alt"
    },
    {
        "title": "Innovation",
        "description": "Constantly improving to bring you the best technology and shopping experience.",
        "icon": "fas fa-rocket"
    },
    {
        "title": "Global Vision",
        "description": "Connecting buyers and sellers from around the world in one unified platform.",
        "icon": "fas fa-globe"
    }
]

# Team Members
team_members = [
    {
        "name": "Sarah Johnson",
        "role": "CEO & Founder",
        "bio": "Visionary leader with 15+ years in e-commerce industry."
    },
    {
        "name": "Michael Chen",
        "role": "CTO",
        "bio": "Tech innovator passionate about scalable solutions."
    },
    {
        "name": "Emily Rodriguez",
        "role": "Head of Customer Service",
        "bio": "Dedicated to making every customer experience amazing."
    },
    {
        "name": "David Williams",
        "role": "Marketing Director",
        "bio": "Storyteller bringing brands and products to life."
    }
]

def about_us(request):
    context = {
        'marketplace': marketplace_info,
        'developer': developer_info,
        'values': company_values,
        'team': team_members
    }
    return render(request, 'about_us/about_us.html', context)