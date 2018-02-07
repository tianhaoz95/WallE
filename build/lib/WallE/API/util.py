from .Manage.Plan import Interactive, Schedule

def get_plan(interface_type):
    if interface_type == 'interactive':
        return Interactive
    if interface_type == 'schedule':
        return Schedule
    return None
