from django.shortcuts import render, redirect
from .models import Transaction
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def create_view(request):
    if request.method == "POST":
        Transaction.objects.create(
            name=request.POST.get("name", ""),
            email=request.POST.get("email", ""),
            description=request.POST.get("description", ""),
            amount=abs(int(request.POST.get("amount", 0))),
            type=request.POST.get("type", ""),
        )

        return redirect("/")

    return render(request, "create.html")

def edit_view(request: HttpRequest, transaction_id: int) -> HttpResponse:
    transaction = Transaction.objects.filter(id=transaction_id).first()
    users = User.objects.all()

    if request.method == "POST":
        transaction.description = request.POST.get("description", "")
        transaction.name = request.POST.get("name")
        transaction.amount = request.POST.get("amount", 0)
        transaction.status = request.POST.get("status")
        transaction.save()
        return redirect("/")

    context = {
        'transaction': transaction,
        'users': users,
    }

    return render(request, "edit.html", context)
