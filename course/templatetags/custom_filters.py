from django import template

register = template.Library()

@register.filter
def is_enrolled(user_enrollments, course):
    if user_enrollments is None:
        return False
    return user_enrollments.filter(course=course).exists()