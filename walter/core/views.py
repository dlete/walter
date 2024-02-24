# Python imports
import logging

# Core Django imports
from django.shortcuts import render

logger = logging.getLogger(__name__)
#logging.basicConfig(level=logging.DEBUG)
## https://docs.python.org/3/howto/logging-cookbook.html
#logger.setLevel(logging.INFO)

def about(request):
    context = {'bodymessage': "About this project"}
    return render(request, 'core/about.html', context)
