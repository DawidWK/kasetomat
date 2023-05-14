from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from django.http import JsonResponse

from core.models import Kaseta, Order
from core.forms import CartForm, KasetaForm
import json
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['kasety'] = Kaseta.objects.all()
        
        # if request has get method with key title then filter kasety by title
        title = self.request.GET.get('title', None)
        if title:
            context['kasety'] = Kaseta.objects.filter(title__icontains=title)

        return context

        
class OrderListView(ListView):
    template_name = "order_list.html"
    model = Order
    
    
    
class KasetaFormView(FormView):
    template_name = "kaseta_form.html"
    form_class = KasetaForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CartFormView(FormView):
    template_name = "cart_form.html"
    form_class = CartForm
    success_url = "/"

    def form_valid(self, form):
        instance = form.save()
        
        kasety = self.request.POST.get('kasety', "[]")
        kasety = json.loads(kasety)
        
        for kaseta in kasety:
            kaseta_instance = Kaseta.objects.get(title=kaseta)
            instance.kasety.add(kaseta_instance)
            kaseta_instance.availability -= 1
            kaseta_instance.save()
        
        
        return super().form_valid(form)
    

def mark_order_as_returned(request, pk):
    order = Order.objects.get(pk=pk)
    order.is_returned = True
    order.save()
    
    # mark kasety as available
    for kaseta in order.kasety.all():
        kaseta.availability += 1
        kaseta.save()
    return JsonResponse({"status": "ok"})