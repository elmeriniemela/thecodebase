
from django.db import models
from django.shortcuts import render

# Create your models here.



class Repo(models.Model):
    name = models.CharField(max_length=150)
    display_name = models.CharField(max_length=150)
    readme_html = models.TextField()
    sequence = models.IntegerField(default=100)
    update_date = models.DateTimeField(auto_now=True)
    no_update = models.BooleanField(default=False)



    class Meta:
        ordering = ('sequence', 'name',)
        constraints = [
            models.UniqueConstraint(fields=['name'], name="name-unique")
        ]



class Topic(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    image_url = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    repos = models.ManyToManyField(Repo)
    sequence = models.IntegerField(default=100)

    class Meta:
        ordering = ('sequence', 'title',)
        constraints = [
            models.UniqueConstraint(fields=['url'], name="topic-url-unique")
        ]

    @staticmethod
    def default_get(topic_name):
        pre_defined = {
            'python': {
                'sequence': 10,
                'description': "Python is currently my goto language. "
                    "It's the main language I've used professionally and in my personal projects. "
                    "Keywords with python include Odoo-ORM, Django-framework, Flask, API Integrations and Data Analysis.",
            },

            'java': {
                'sequence': 20,
                'description': "During my studies Java was the teaching language at University of Helsinki. "
                    "Using Java I learned the basic and advanced consepts of data strucutes and algorithms. "
                    "I believe strongly that the theoretical understanding provides important tools when analysing practical problems.",
            },

            'ansible': {
                'sequence': 30,
                'description': "Automating processes and making life easier has always been my passion. "
                    "Since both Ansible and Odoo ERP are open source and based on python, "
                    "I integrated them at SprintIT and created an interface to handle automated customer deployments.",
            },

            'c-c-plus': {
                'title': 'C/C++',
                'sequence': 40,
                'description': "I've studied the basics of C/C++. "
                    "There's alot I'd like to do with C++ for example rewrite some of the games I've made with pygame. "
                    "What facinates me about C in particular is it's closeness to what the actual hardware supports.",
            },

            'javascript': {
                'title': 'JavaScript',
                'sequence': 50,
                'description': "I aspire to master JavaScript, since it's a popular multipurpose languge and most importantly the language of the web. "
                    "JavaScript is a must for me since increasing number of services are browser based including Odoo ERP which I'm currently working on at SprintIT.",
            },

            'web-development': {
                'title': 'Web Devopment',
                'sequence': 60,
                'description': "This website is one of the examples of my skills with web based technologies. "
                    "Currently I'm interested to learn new web technologies such as Angular or React for frontend and Node.js and MongoDB for backend. "
                    "Automating and deploying Cloud based systems is a big part of my job at SprintIT",

            },
        }

        vals = {
            'title': topic_name.capitalize(),
            'url': topic_name,
            'image_url': 'projects/images/{}.png'.format(topic_name),
            'description': topic_name,
        }

        if topic_name in pre_defined:
            vals.update(pre_defined[topic_name])

        return vals