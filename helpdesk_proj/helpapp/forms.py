from django.forms import ModelForm
from helpapp.models import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        # fields = ('title', 'submitter_email', 'assigned_to', 'status', 'description', 'priority')
        fields = '__all__'