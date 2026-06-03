from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Import your Tenant model (assuming django-tenants or similar)
# from customers.models import Client, Domain 

def signup_view(request):
    if request.method == 'POST':
        # 1. Get data from form
        company_name = request.POST.get('company_name')
        schema_name = request.POST.get('schema_name').lower() # lowercase for DB schema
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # 2. Logic to create Tenant (Specific to srinu005 project structure)
            # tenant = Client.objects.create(schema_name=schema_name, name=company_name)
            # Domain.objects.create(domain=f'{schema_name}.localhost', tenant=tenant, is_primary=True)

            # 3. Create the User inside the schema or globally
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                messages.success(request, "Account created successfully! Please login.")
                return redirect('login')
            else:
                messages.error(request, "Username already exists.")

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            
    return render(request, 'signup.html')


class HomeView(TemplateView):
    template_name = "index.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"
    login_url = "/login/"


class ProductsView(LoginRequiredMixin, TemplateView):
    template_name = "products.html"
    login_url = "/login/"
