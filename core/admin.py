from django.contrib import admin 

from .models import Category , Technology , Project , SkillCategory , Skill , LearningJourney , Certificate



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

@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = (
            "title",
            "skill",
            "route_title",
            "provider",
            "status",
            "display_order"
        )
    

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
    "title",
    "provider",
    "issue_date",
    "display_order",
)


