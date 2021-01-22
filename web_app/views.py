from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from django.utils import timezone


logger = logging.getLogger(__file__)

logging.basicConfig(
    format='%(levelname)s:%(filename)s:%(message)s',
    level=logging.DEBUG,
)


class IndexView(View):
    def get(self, request):
        data = {
            'time': timezone.now().strftime("%d/%m/%Y, %H:%M:%S"),
            'url': request.build_absolute_uri(),
            'method': 'GET',
            'status': '404',
        }
        logger.info(data)
        form = ContactForm()
        return render(
            request,
            'web_app/index.html',
            {'form': form},
        )

    def post(self, request):
        form = ContactForm(request.POST)
        data = {
            'time': timezone.now().strftime("%d/%m/%Y, %H:%M:%S"),
            'url': request.build_absolute_uri(),
            'method': 'GET',
            'status': '200',
            'email': request.POST.get('email')
        }
        logger.info(data)
        if form.is_valid():
            return HttpResponse("Ok.")
        return render(
            request,
            'web_app/index.html',
            {'form': form},
        )


class APIView(View):
    def get(self, request):
        data = {
            'time': timezone.now().strftime("%d/%m/%Y, %H:%M:%S"),
            'url': request.build_absolute_uri(),
            'method': 'GET',
            'status': '404',
            'params': dict(request.GET)
        }
        logger.info(data)
        return HttpResponse('Not found')

    @csrf_exempt
    def post(self, request):
        method = request.GET.get('method')
        if method == 'ping':
            status = 200
        else:
            status = 400

        data = {
            'time': timezone.now().strftime("%d/%m/%Y, %H:%M:%S"),
            'url': request.build_absolute_uri(),
            'method': 'POST',
            'status': status,
            'params': dict(request.GET)
        }
        logger.info(data)

        return HttpResponse({}, status=status)
