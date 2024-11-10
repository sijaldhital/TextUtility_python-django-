from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounts = request.POST.get('charcount', 'off')

    # Initialize analyzed text with original text for cumulative transformations
    analyzed_text = djtext
    purposes = []  # To keep track of purposes

    # Apply transformations based on selected options
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_text = ''.join(char for char in analyzed_text if char not in punctuations)
        purposes.append('Remove Punctuations')

    if fullcaps == 'on':
        analyzed_text = analyzed_text.upper()
        purposes.append('Changed to Uppercase')

    if newlineremover == 'on':
        analyzed_text = ''.join(char for char in analyzed_text if char not in "\n\r")
        purposes.append('Removed New Lines')

    if extraspaceremover == 'on':
        analyzed_text = ' '.join(analyzed_text.split())
        purposes.append('Removed Extra Spaces')

    # Calculate character count without altering `analyzed_text`
    char_count = len(analyzed_text) if charcounts == 'on' else None
    if charcounts == 'on':
        purposes.append('Count Characters')

    # Prepare parameters for the template
    params = {
        'purpose': ', '.join(purposes),
        'analyzed_text': analyzed_text,
        'char_count': char_count
    }

    return render(request, 'analyze.html', params)
