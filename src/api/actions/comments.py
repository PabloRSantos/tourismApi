def disapprove_comment(modeladmin, request, queryset):
    queryset.update(approved=False)


def approve_comment(modeladmin, request, queryset):
    queryset.update(approved=True)


disapprove_comment.short_description = "Reprovar comentários"
approve_comment.short_description = "Aprovar comentários"
