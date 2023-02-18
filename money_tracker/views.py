from django.shortcuts import render
from money_tracker.models import TransactionRecord

def show_tracker(request):
    transaction_data = TransactionRecord.objects.all()
    context = {
        'list_of_transactions': transaction_data,
        'name': 'Wahyu Sahrijal'
    }
    return render(request, "tracker.html", context)
