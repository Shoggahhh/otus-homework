from django.shortcuts import render
from django.utils import timezone
from helpapp.models import Ticket
from django.views.generic import ListView, CreateView, DetailView
from helpapp.forms import TicketForm


class Ticketlist(ListView):
    model = Ticket
    template_name = 'helpapp/ticket_list.html'


class TicketCreate(CreateView):
    model = Ticket
    template_name = 'helpapp/create.html'
    success_url = '/ticket_list/'
    form_class = TicketForm

    # def get_form(self, form_class=TicketForm):
    #     form = super(TicketCreate, self).get_form(form_class)
    #     form.fields['created'].widget.attrs.update({'class': 'datepicker'})
    #     return form


class TicketDetail(DetailView):
    model = Ticket
    template_name = 'helpapp/detail.html'
