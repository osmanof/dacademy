from django.db import models


class Group(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    tutor = models.ForeignKey('users.Teacher', on_delete=models.PROTECT)
    code = models.IntegerField('Код', unique=True)
    teacher_name = models.CharField('ФИО Учителя', max_length=150, blank=True)

    students = models.ManyToManyField('users.Student', through='classes.GroupStudent', related_name='student_groups')
    course = models.ForeignKey('courses.Course', related_name='groups', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.code}'

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class GroupStudent(models.Model):
    group = models.ForeignKey('classes.Group', on_delete=models.CASCADE)
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    main = models.BooleanField("Основной", default=False)

    def __str__(self):
        return f'{self.student} {self.group}'

    class Meta:
        verbose_name = 'Ученик класса'
        verbose_name_plural = 'Ученики классов'
        unique_together = ('group', 'student')


class GroupCourse(models.Model):
    group = models.ForeignKey('classes.Group', on_delete=models.CASCADE, related_name='group_courses')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='group_courses')
    active = models.BooleanField('Активен')

    def __str__(self):
        return f'{self.group} {self.course}'

    class Meta:
        verbose_name = 'Курс класса'
        verbose_name_plural = 'Курсы классов'
