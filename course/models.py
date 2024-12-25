from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    written_date = models.DateField(auto_now=True)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    video_url = models.URLField(blank=True)
    instructor = models.ForeignKey(User, related_name="courses", on_delete=models.CASCADE)

    CATEGORY_CHOICES = [
        ('frontend', 'Frontend Development'),
        ('backend', 'Backend Development'),
        ('data_science', 'Data Science'),
        ('machine', 'Machine Learning'),
        ('artificial', 'Artificial Intelligence'),
        ('ui', 'DUI/UX Design'),
    ]

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='backend',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Courses'
        ordering = ('created_date', 'id')



class Playlist(models.Model):
    course = models.ForeignKey(Course, related_name='playlists', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.title

    def get_video_id(self):
        from urllib.parse import urlparse, parse_qs
        query = urlparse(self.video_url).query
        video_id = parse_qs(query).get('v')
        return video_id[0] if video_id else None

    def get_embed_url(self):
        if "watch?v=" in self.video_url:
            return self.video_url.replace("watch?v=", "embed/")
        return self.video_url


class Enrollment(models.Model):
    user = models.ForeignKey(User, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enrolled_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # Prevents multiple enrollments in the same course

    def __str__(self):
        return f'{self.user.username} enrolled in {self.course.name}'


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class CourseReview(models.Model):
#     course = models.ForeignKey(Course, related_name="reviews", on_delete=models.CASCADE)
#     student = models.ForeignKey(CustomUser, related_name="reviews", on_delete=models.CASCADE)
#     rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
#     review = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Review of {self.course.title} by {self.student.username}"