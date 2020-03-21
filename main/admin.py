
import re
import requests
import github
import markdown

from django.contrib import admin

# Register your models here.
from .models import Topic, Repo, GithubToken
from .models import Game, Score, JavaScriptFile


def fetch_repos(modeladmin, request, queryset):

    def prettify(repo_name):
        words = re.split(r'[ \-_]', repo_name)
        words = [word.capitalize() for word in words]
        return ' '.join(words)

    def update_or_create(Model, vals, **search_kwargs):
        objects = getattr(Model, 'objects')
        record, created = objects.get_or_create(**search_kwargs, defaults=vals)
        if not created:
            for attr, value in vals.items():
                setattr(record, attr, value)
            record.save()
        return record


    for token_obj in queryset:
        ghub = github.Github(token_obj.token)
        for repo in ghub.get_user().get_repos():
            if not repo.private:
                try:
                    readme = repo.get_readme()
                except:
                    continue

                vals = {
                    'name': repo.name,
                    'display_name': prettify(repo.name),
                    'readme_html': markdown.markdown(
                        requests.get(readme.download_url).text),
                }
                repo_record = update_or_create(Repo, vals, name=repo.name)

                topics = repo.get_topics()

                for topic_name in topics:
                    vals = Topic.default_get(topic_name)
                    topic_record = update_or_create(Topic, vals, url=topic_name)
                    topic_record.repos.add(repo_record)
                    topic_record.save()


fetch_repos.short_description = "Fetch Repositories"



class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sequence')

admin.site.register(Game, GameAdmin)



class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'time', 'score')

admin.site.register(Score, ScoreAdmin)


class JavaScriptFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'path', 'game', 'sequence')


admin.site.register(JavaScriptFile, JavaScriptFileAdmin)



class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sequence')


admin.site.register(Topic, TopicAdmin)


class GithubTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sequence')
    actions = [fetch_repos]


admin.site.register(GithubToken, GithubTokenAdmin)


class RepoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sequence', 'update_date')


admin.site.register(Repo, RepoAdmin)


