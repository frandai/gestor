from .models import MainOrganization


def add_mainorganization_to_context(request):
    return {
        'mainorganization': MainOrganization.objects.all().first()
    }