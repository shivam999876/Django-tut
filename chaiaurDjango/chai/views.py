from django.shortcuts import render
from django.apps import apps
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data['chai_varity']
            # import Store dynamically to avoid unresolved import symbol
            try:
                Store = apps.get_model('chai', 'Store')
            except LookupError:
                Store = None
            if Store is not None:
                stores = Store.objects.filter(chai_varieties=chai_varity)
    else:
        form = ChaiVarityForm()
    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form})