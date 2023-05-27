from django.contrib import admin
from .models import Post, Comment, Blog, Tag, Category, Today

# Register your models here.


admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Today)
admin.site.register(Category)
admin.site.register(Blog)

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'author',)
    # list_editable = ('title', 'content') 관리자 페이지에서 바로 편집가능
    # list_filter = ['created_at',]
    # search_fields = ('id', 'author__username') # 두번째는 author 객체의 username 변수를 기준으로 검색하겠다~ 라는뜻임.
    # search_help_text = '게시판 번호 혹은 작성자 명으로 검색이 가능합니다.'

    
    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.body = '운영 규정 위반으로 인한 게시글 삭제 조치.'
            item.save()