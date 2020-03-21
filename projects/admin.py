
import re
import requests
from github import Github
import markdown

from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django import forms

# Register your models here.
from .models import Topic, Repo



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


class GithubForm(forms.Form):
    username = forms.CharField(
        label=_("Username"),
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class RepoAdmin(admin.ModelAdmin):

    change_list_template = "projects/change_list.html"

    list_display = ('id', 'name', 'sequence', 'update_date')

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('fetch-repos/', self.fetch_repos_from_remote),
        ]
        return my_urls + urls

    def fetch_repos_from_remote(self, request):
        if request.method == 'POST':
            form = GithubForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                self.save_repos(username, password)

            return redirect('main/home')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = GithubForm()
        return render(request, 'projects/github_credentials.html', {'form': form})

    def save_repos(self, username, password):
        ghub = Github(username, password)
        for repo in ghub.get_user().get_repos():
            if not repo.private and repo.owner.login == username:
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


class TopicAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'sequence')

admin.site.register(Topic, TopicAdmin)
admin.site.register(Repo, RepoAdmin)
