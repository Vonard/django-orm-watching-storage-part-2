from datacenter.models import Visit, Passcard
from datacenter.visit_durations import is_visit_long, get_duration, format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)
        owner = visit.passcard.owner_name
        entered_at = localtime(visit.entered_at)

        non_closed_visits.append(
            {
                'who_entered': owner,
                'entered_at': entered_at,
                'duration': formatted_duration,
                'is_strange': is_visit_long(visit)
            })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

