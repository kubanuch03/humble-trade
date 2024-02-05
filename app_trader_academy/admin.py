from django.contrib import admin
from .models import Unit, Lesson, StrategyCourse, StrategyLesson, Question, Answer

admin.site.register(Lesson)
admin.site.register(Unit)
admin.site.register(StrategyCourse)
admin.site.register(StrategyLesson)
admin.site.register(Question)
admin.site.register(Answer)
