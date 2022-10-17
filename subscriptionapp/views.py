from urllib import request
from django.shortcuts import render,get_object_or_404
from django.views.generic import RedirectView,ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from projectapp.models import Project
from articleapp.models import Article
from subscriptionapp.models import Subscription

# Create your views here.

@method_decorator(login_required,'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs) :

        return reverse('projectapp:detail',kwargs={'pk':self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs) :

        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user = user, project = project)
        
        if subscription.exists():
            subscription.delete()

        else : 
            Subscription(user=user,project=project).save()
        return super(SubscriptionView,self).get(request, *args, **kwargs)

class SubscriptionListView(ListView):
    model = Article
    template_name = 'subscriptionapp/list.html'
    context_object_name = 'article_list'
    paginate_by = 5

    def get_queryset(self) :
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        print(Subscription.objects.all())
        article_list = Article.objects.filter(project__in=projects)
        print(projects)

        return article_list