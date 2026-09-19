from django.contrib import admin 

from .models import Category , Technology , Project , SkillCategory , Skill



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "featured",
        "created_at",
    )
    
    
admin.site.register(Category)
admin.site.register(Technology)
admin.site.register(SkillCategory)
admin.site.register(Skill)


