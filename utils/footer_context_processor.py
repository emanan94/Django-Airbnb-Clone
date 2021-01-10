from settings.models import Info


def get_footer(request):
    my_footer=Info.objects.last()
    return {'my_footer':my_footer}