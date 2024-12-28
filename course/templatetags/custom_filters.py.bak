from django import template

register = template.Library()

@register.filter
def is_enrolled(user_enrollments, course):
    """
    Check if the given course is in the user's enrollments.
    """
    return user_enrollments.filter(course=course).exists()
