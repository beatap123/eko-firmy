import datetime
from django.db import models
from django.utils import timezone


class Firm(models.Model):
    firm_name = models.CharField(max_length=300)
    detail = models.TextField()
    add_date = models.DateTimeField(auto_now_add = True)
    searching_date = models.DateTimeField()  # na razie nie różni się od add_date

    def was_searching_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.searching_date <= now
    was_searching_recently.admin_order_field = 'searching_date'
    was_searching_recently.boolean = True
    was_searching_recently.short_description = 'Searching recently?'

    def __str__(self):
        return self.firm_name


# #def last_searching_firm(request, firm_id):  #to nie powinien być widok tylko funkcja
#     firm = get_object_or_404(Firm, pk=firm_id)
#     selected_choice = firm.firm_name.get(pk=request.POST['firm_name'])
#     selected_choice.last_searching_firm += 1
#     selected_choice.save()
#     # Always return an HttpResponseRedirect after successfully dealing
#     # with POST data. This prevents data from being posted twice if a
#     # user hits the Back button.
#     return HttpResponseRedirect(reverse('firma/results'))
