
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):

    title = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    image_url = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    sequence = models.IntegerField(default=100)

    class Meta:
        ordering = ('sequence', 'title',)
        constraints = [
            models.UniqueConstraint(fields=['url'], name="game-url-unique")
        ]

class JavaScriptFile(models.Model):
    path = models.CharField(max_length=200)
    sequence = models.IntegerField(default=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.path

    class Meta:
        ordering = ('sequence',)


class GithubToken(models.Model):
    name = models.CharField(max_length=200)
    token = models.CharField(max_length=100)
    sequence = models.IntegerField(default=100)


    class Meta:
        ordering = ('sequence',)


class Score(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()

    class Meta:
        ordering = ('-score', '-time',)


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
            'academic': {
                'title': 'Academia and fundamentals',
                'sequence': 10,
                'description': "Strong theoretical background "
                    "and understanding of the fundamentals of computing  "
                    "allows for more indepth analysis and better facillitates learning the technologies built on top of the theory.",
            },
            'web-development': {
                'title': 'Web Development',
                'sequence': 20,
                'description': "The modern user inferface is in the browser. "
                    "The huge advange on building web based applications is that they are instantly cross-platform. "
                    "Developing and desinging the architecture of web-based systems is a big part of my job at SprintIT",
            },
            'cloud-architecture': {
                'title': 'Cloud Architecture',
                'image_url': 'main/images/ansible.png',
                'sequence': 30,
                'description': "Automating processes and making life easier have always been my passion. "
                    "Since both Ansible and Odoo ERP are open source and based on Python, "
                    "I integrated them at SprintIT and created an interface to handle automated customer deployments.",
            },

            'machine-learning': {
                'image_url': 'main/images/machine-learning.jpg',
                'title': 'Machine Learning',
                'sequence': 40,
                'description': "It is amazing what the chain rule and simple linear algebra can achieve with modern computing power. "
                    "Machine learning is one of my passions and I strongly beleive it will change the way we solve problems."
            },

            'game-development': {
                'title': 'Game Development',
                'image_url': 'main/images/game-development.jpg',
                'sequence': 50,
                'description':
                    "Developing games is what got me into programming and finally computer science more generally. "
                    "Simulating the laws of physics is closely related to game engines, which further motivates my interest in game development."
            },
            'python': {
                'sequence': 60,
                'description': "Python is currently my go-to language. "
                    "It's the main language I've used professionally and in my personal projects. "
                    "Keywords with Python include Odoo-ORM, Django-framework, Flask, API Integrations and Data Analysis.",
            },
            'java': {
                'sequence': 70,
                'description': "During my studies at University of Helsinki, Java was the teaching language. "
                    "Using Java I learned the basic and advanced concepts of data structures and algorithms. "
                    "I believe strongly that the theoretical understanding provides important tools when analysing practical problems.",
            },

            'ansible': {
                'sequence': 80,
                'description': "Automating processes and making life easier have always been my passion. "
                    "Since both Ansible and Odoo ERP are open source and based on Python, "
                    "I integrated them at SprintIT and created an interface to handle automated customer deployments.",
            },

            'c-c-plus': {
                'title': 'C++',
                'sequence': 90,
                'description':
                    "C++ is one of the best languages for game development, particularly if you need explicit memory management. "
                    "My experience with C++ comes mainly from Computer Graphics, as I've attended a course where we learned the fundamentals of graphics engines in a C++ framework. "
            },

            'javascript': {
                'title': 'JavaScript',
                'sequence': 100,
                'description': "I aspire to master JavaScript, since it's a popular multipurpose languge and most importantly the language of the web. "
                    "JavaScript is a must for me since increasing number of services are browser based including Odoo ERP which I'm currently working on at SprintIT.",
            },
        }


        aliases = {
            'ansible': 'cloud-architecture',
            'cloud-architechture': 'cloud-architecture',
            'artificial-intelligence': 'machine-learning',
        }

        if topic_name in aliases:
            topic_name = aliases[topic_name]

        vals = {
            'title': topic_name.capitalize(),
            'url': topic_name,
            'image_url': 'main/images/{}.png'.format(topic_name),
            'description': topic_name,
        }

        if topic_name in pre_defined:
            vals.update(pre_defined[topic_name])

        return vals