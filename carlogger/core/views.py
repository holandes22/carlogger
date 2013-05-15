from django.views.generic import DetailView
from django.contrib.auth.models import User


class ByUserMixin(object):

    def get_queryset(self):
        return self.model.objects.for_user(user=self.request.user)


class UserDetailView(DetailView):

    model = User
    template_name = 'registration/user_detail.html'

    def get_object(self):
        return self.request.user
