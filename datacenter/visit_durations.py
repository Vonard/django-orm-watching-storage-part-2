from django.utils.timezone import localtime
from django.utils import timezone


def is_visit_long(visit, minutes=60):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at or timezone.now())
    delta = leaved_at - entered_at
    total_minutes = int(delta.total_seconds() / 60)
    if total_minutes < minutes:
        return False
    return True

def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at or timezone.now())
    delta = leaved_at - entered_at
    return delta

def format_duration(duration):
    total_seconds = duration.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int((total_seconds % 60))
    return f'{hours:02}:{minutes:02}:{seconds:02}'