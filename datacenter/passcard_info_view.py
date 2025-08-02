from datacenter.models import Passcard, Visit
from datacenter.models import is_visit_long, get_duration, format_duration
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        entered_at = localtime(visit.entered_at)

        duration_seconds = get_duration(visit)
        duration = format_duration(duration_seconds)

        visit_item = {
            'entered_at': entered_at,
            'duration': duration,
            'is_strange': is_visit_long(visit)
        }
        this_passcard_visits.append(visit_item)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
