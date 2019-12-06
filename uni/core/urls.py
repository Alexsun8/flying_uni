from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from core.views import home_view, index_view, idea_view, course_view, add_news_view, edit_news_view, edit_course_view, \
    add_course_view, add_course_to_wish, delete_course_from_wish, add_course_to_stud, delete_course_from_stud, \
    add_course_to_know, delete_course_from_know, add_location, index_with_domain_view, index_with_types_view

urlpatterns = [
                  url(r'^index$', index_view, name="index"),
                  url(r'^index_with_domain/(?P<num>\d)/$', index_with_domain_view, name="index_with_domain"),
                  url(r'^index_with_types/(?P<pk>\d+)/$', index_with_types_view, name="index_with_types"),
                  url(r'^home$', home_view, name="home"),
                  url(r'^idea$', idea_view, name="idea"),
                  url(r'^add_news$', add_news_view, name="add_news"),
                  url(r'^edit_news/(?P<pk>\d+)/$', edit_news_view, name="edit_news"),
                  url(r'^add_course$', add_course_view, name="add_course"),
                  url(r'^add_location$', add_location, name="add_location"),
                  url(r'^course/id/(?P<pk>\d+)/$', course_view, name="course_page"),
                  url(r'^course/id/(?P<pk>\d+)/to_wish/$', add_course_to_wish, name="add_to_wish"),
                  url(r'^course/id/(?P<pk>\d+)/del_wish/$', delete_course_from_wish, name="delete_from_wish"),
                  url(r'^course/id/(?P<pk>\d+)/add_stud/$', add_course_to_stud, name="add_to_stud"),
                  url(r'^course/id/(?P<pk>\d+)/del_stud/$', delete_course_from_stud, name="delete_from_stud"),
                  url(r'^course/id/(?P<pk>\d+)/add_know/$', add_course_to_know, name="add_to_know"),
                  url(r'^course/id/(?P<pk>\d+)/del_know/$', delete_course_from_know, name="delete_from_know"),
                  url(r'^course/id/(?P<pk>\d+)/edit/$', edit_course_view, name="edit_course"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
