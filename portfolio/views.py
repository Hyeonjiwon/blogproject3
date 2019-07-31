from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio

def portfolio(request):
    portfolios = Portfolio.objects #쿼리셋
    return render(request, 'portfolio.html', {'portfolios':portfolios})

def new_port(request):
    return render(request, 'new_port.html')


def detail_port(request, portfolio_id):
    details = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'detail_port.html', {'details':details})