from django import template

register = template.Library()


@register.filter()
def list_attributes(model):
    filter_fields = ['pk', 'id', 'user', 'car']
    for field in model._meta.fields:
        if field.name not in filter_fields:
            if field.choices:
                yield field.name.replace('_', ' ') , getattr(model, 'get_{}_display'.format(field.name))
            else:
                yield field.name.replace('_', ' '), getattr(model, field.name)
