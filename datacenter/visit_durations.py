from django.utils.timezone import localtime
from django.utils import timezone

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

def is_visit_long(visit, minutes=60):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at or timezone.now())
    delta = leaved_at - entered_at
    total_minutes = int(delta.total_seconds() / SECONDS_IN_MINUTE)
    return total_minutes > minutes

def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at or timezone.now())
    delta = leaved_at - entered_at
    return delta

def format_duration(duration):
    total_seconds = duration.total_seconds()
    hours = int(total_seconds // SECONDS_IN_HOUR)
    minutes = int((total_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE)
    seconds = int(total_seconds % SECONDS_IN_MINUTE)
    return f'{hours:02}:{minutes:02}:{seconds:02}'