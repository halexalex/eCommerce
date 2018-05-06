import os
from mimetypes import guess_type
from wsgiref.util import FileWrapper

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, View

from analytics.mixins import ObjectViewedMixin
from carts.models import Cart

from .models import Product, ProductFile


class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(ObjectViewedMixin, DetailView):
    queryset = Product.objects.all().featured()
    template_name = 'products/featured-detail.html'


class UserProductHistoryView(LoginRequiredMixin, ListView):
    template_name = 'products/user-history.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserProductHistoryView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        views = request.user.objectviewed_set.all().by_model(Product, model_queryset=True)
        return views


class ProductListView(ListView):
    template_name = 'products/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context)


class ProductDetailSlugView(ObjectViewedMixin, DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404('Not found...')
        except Product.MultipleObjectsReturned:
            queryset = Product.objects.filter(slug=slug, active=True)
            instance = queryset.first()
        except:
            raise Http404('Uhhhmmm')

        return instance


class ProductDownloadView(View):
    def get(self, *args, **kwargs):
        slug = kwargs.get('slug')
        pk = kwargs.get('pk')
        downloads_qs = ProductFile.objects.filter(pk=pk, product__slug=slug)
        if downloads_qs.count() != 1:
            raise Http404('Download not found!')
        download_obj = downloads_qs.first()
        # permission checks
        file_root = settings.PROTECTED_ROOT
        filepath = download_obj.file.path
        final_filepath = os.path.join(file_root, filepath)  # where the file is stored
        with open(final_filepath, 'rb') as f:
            wrapper = FileWrapper(f)
            mimetype = 'application/force-download'
            guessed_mimetype = guess_type(filepath)[0]
            if guessed_mimetype:
                mimetype = guessed_mimetype

            response = HttpResponse(wrapper, content_type=mimetype)
            response['Content-Disposition'] = f'attachment;filename={download_obj.name}'
            response['X-SendFile'] = str(download_obj.name)
            return response


class ProductDetailView(ObjectViewedMixin, DetailView):
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404
    print(instance)
    context = {
        'object': instance
    }
    return render(request, 'products/detail.html', context)
