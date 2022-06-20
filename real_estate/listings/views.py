from django.shortcuts import render,get_object_or_404
from .models import Listings
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import ListingsForm
from django.urls import reverse_lazy

class ListingsListView(ListView):
    model = Listings
    context_object_name = 'Listings'
    template_name='listings/listing_list.html'


# def listings(request):
#     listings = get_object_or_404(Listings)
#     context = {'listings':listings}
#     return render(request,'listings/listings_list.html',context)



class ListingDetailView(DetailView):
    model = Listings
    context_object_name ='listing'
    template_name = "listings/listing_detail.html"


# def listing_detail(request,id):
#     listing = get_object_or_404(Listings, pk=Listing_id)
#     context ={'listing':listing}
#     return render(request,'listings/listing_detail.html',context)



class ListingsCreateView(CreateView):
    model = Listings
    form_class = ListingsForm
    template_name = "listings/listing_create.html"
    
# def listing_create(request):
#     form = ListingForm()
#     if request.method == 'POST':
#         form = ListingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return reverse('listings:listing_list')
   
#     context = {'form':form}
#     return render(request,'listings/listing_create.html',context)


class ListingUpdateView(UpdateView):
    model = Listings
    template_name = "listings/listing_update.html"
    form_class = ListingsForm

# def listing_create(request,pk):
#     listing = Listings.objects.get(id=pk)
#     form = ListingForm(instace=listing)
#     if request.method == 'POST':
#         form = ListingForm(request.POST,instace=listing)
#         if form.is_valid():
#             form.save()
#             return reverse('listings:listing_list')
   
#     context = {'form':form}
#     return render(request,'listings/listing_create.html',context)

class ListingDeleteView(DeleteView):
    model = Listings
    template_name = "listings/listing_delete.html"
    success_url = reverse_lazy('listings:listings_list')

# def list_delete(request,pk):
#     listing = Listings.objects.get(id=pk)
#     listing.delete()
#     return redirect("listings:listing_list")