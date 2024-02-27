import logging
import difflib
from difflib import unified_diff

from django.shortcuts import render
from synopsis.models import Text

# Create your views here.

def colorize_diff(a, b):
    matcher = difflib.SequenceMatcher(None, a, b)
    diff = ''
    for opcode, a0, a1, b0, b1 in matcher.get_opcodes():
        if opcode == 'equal':
            diff += f'<span class="similar">{a[a0:a1]}</span>'
        elif opcode == 'replace':
            diff += f'<span class="different">{b[b0:b1]}</span>'
        elif opcode == 'insert':
            diff += f'<span class="different">{b[b0:b1]}</span>'
        elif opcode == 'delete':
            diff += '<span class="omission">[...]</span>'
    return diff


def index(request):
    """
    The index view for the synopsis app
    """
    error = None
    try:
        # get all the texts from the database
        texts = Text.objects.all().filter(enabled=True).order_by('created_at').reverse()
        base_text = Text.objects.all().filter(enabled=True).order_by('created_at').first().text
        base_text = texts.first().text
        diffs = []

        for text in texts:
            diff = colorize_diff(base_text, text.text)
            text.text = diff
            # text.save()
            diffs.append(diff)

        # replace d


        print("Diffs: ", diffs)

        # diff the texts and mark the differences with <span> tags
        """
        for text in texts[1:]:
            diff = list(unified_diff(base_text.splitlines(), text.text.splitlines(), lineterm=''))
            diff_html = []
    
            for line in diff:
                if line.startswith('+'):
                    diff_html.append(f'<span style="background-color: #ccffcc;">{line}</span>')
                elif line.startswith('-'):
                    diff_html.append(f'<span style="background-color: #ffcccc;">{line}</span>')
                else:
                    diff_html.append(line)
    
            diffs.append('\n'.join(diff_html))
            
        """
    except Exception as error:
        logging.error(f'Error: {error}')
        texts = []
        diffs = []

    context = {
        'error_message': error,
        'texts': texts,
        #'diffs': [text.text for text in texts],
        'diffs': diffs,
    }
    return render(request, 'synopsis/index.html', context)
