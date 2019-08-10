
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

    change_list_template = "projects/admin/change_list.html"

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
        return render(request, 'projects/admin/github_credentials.html', {'form': form})

    topic_descriptions = {
        'python': "Python is my strongest language. "
                  "It's the main language I've used professionally.",
        'java': "I learned Java in University of Helsinki. "
                "I've also used it in my work at SprintIT.",
        'web-development': "This website is an example of my skills with Flask and Bootstrap. "
                           "I've also learned alot about deploying servers from my work at SprintIT.",
        'c-c-plus': "I've studied the basics of C/C++. "
                    "There's alot I'd like to do with C++ for example "
                    "rewrite some of the games I've made with pygame.",
        'javascript': "I aspire to master JavaScript, since I've already encountered "
                      "it in my work as an Odoo developer, but also in personal projects.",
        'ansible': "Automating processes and making life easier has always been my passion. "
                   "Ansible is a great open source tool for deployment automation, which is why i've learned to use it extensively.",
    }

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
                    vals = {
                        'title': topic_name.capitalize(),
                        'url': topic_name,
                        'image_url': 'projects/images/{}.png'.format(topic_name),
                        'description': self.topic_descriptions.get(topic_name, topic_name),
                    }

                    topic_record = update_or_create(Topic, vals, url=topic_name)
                    topic_record.repos.add(repo_record)
                    topic_record.save()


class TopicAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'sequence')

admin.site.register(Topic, TopicAdmin)
admin.site.register(Repo, RepoAdmin)
