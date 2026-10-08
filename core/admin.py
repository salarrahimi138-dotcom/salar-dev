from django.contrib import admin 

from .models import Category , Technology , Project , SkillCategory , Skill , LearningJourney , Certificate , Post , BlogCategory , Tag , About



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
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "status",
        "created_at",
    )
    search_fields = (
    "title",
    "content",
    )
    list_filter = (
    "status",
    "category",
    )
    prepopulated_fields = {
    "slug": ("title",)
}
admin.site.register(Tag)
admin.site.register(BlogCategory)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")
