class ByUserMixin(object):

    def get_queryset(self):
        return self.model.objects.for_user(user=self.request.user)
