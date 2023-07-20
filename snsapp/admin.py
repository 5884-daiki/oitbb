from django.contrib import admin
from .models import Post,Connection,Category#,Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Connection)
admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tag_list')
    list_display_links = ('id', 'title')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION

# 変更履歴を取得したいモデルのIDを指定
model_id = 1  # ここではモデルのIDを1に仮定しています

# ログエントリをフィルタリング
#log_entries = LogEntry.objects.filter(object_id=model_id)

# 各ログエントリをループして表示
#for entry in log_entries:
#    # ログのタイプを取得して表示
#    if entry.action_flag == ADDITION:
#        action = "追加"
#    elif entry.action_flag == CHANGE:
#        action = "変更"
#    elif entry.action_flag == DELETION:
#        action = "削除"
#    else:
#        action = "不明"
#
#    print(f"ID: {entry.id}, ユーザー: {entry.user}, アクション: {action}, 時間: {entry.action_time}")
