from django.contrib import admin
from django.urls import path
import evalapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', evalapp.views.home, name='home'),
    path('home_new', evalapp.views.home_new, name='home_new'),
    path('new', evalapp.views.new, name='new'),
    path('popular', evalapp.views.popular, name='popular'),
    path('major/', evalapp.views.major, name='major'),
    path('liberal/', evalapp.views.liberal, name='liberal'),
    path('elective/', evalapp.views.elective, name='elective'),

    #detail
    path('new_detail/<int:new_id>', evalapp.views.new_detail, name='new_detail'),
    path('popular_detail/<int:popular_id>', evalapp.views.popular_detail, name='popular_detail'),
    path('popular_detail_full/<int:pop_full_id>', evalapp.views.popular_detail_full, name='popular_detail_full'),
    path('major/<int:major_id>', evalapp.views.major_detail, name='major_detail'),
    path('liberal/<int:liberal_id>', evalapp.views.liberal_detail, name='liberal_detail'),
    path('elective/<int:elective_id>', evalapp.views.elective_detail, name='elective_detail'),

    #new
    path('major_new', evalapp.views.major_new, name='major_new'),
    path('liberal_new', evalapp.views.liberal_new, name='liberal_new'),
    path('elective_new', evalapp.views.elective_new, name='elective_new'),

    #edit
    path('elective/edit/<int:e_edit_id>', evalapp.views.elective_edit, name='elective_edit'),
    path('liberal/edit/<int:l_edit_id>', evalapp.views.liberal_edit, name='liberal_edit'),
    path('major/edit/<int:m_edit_id>', evalapp.views.major_edit, name='major_edit'),

    #delete
    path('elective/delete/<int:elective_id>', evalapp.views.elective_delete, name='elective_delete'),
    path('liberal/delete/<int:liberal_id>', evalapp.views.liberal_delete, name='liberal_delete'),
    path('major/delete/<int:major_id>', evalapp.views.major_delete, name='major_delete'),

    #comment
    path('elective/<int:elective_id>/comment/create', evalapp.views.e_comment_create, name="e_comment_create"),
    path('liberal/<int:liberal_id>/comment/create', evalapp.views.l_comment_create, name="l_comment_create"),
    path('major/<int:major_id>/comment/create', evalapp.views.m_comment_create, name="m_comment_create"),
    path('new/<int:new_id>/comment/create', evalapp.views.new_create, name="new_create"),

    path('elective/<int:elective_id>/comment/<int:comment_id>/delete', evalapp.views.e_comment_delete, name="e_comment_delete"),
    path('liberal/<int:liberal_id>/comment/<int:comment_id>/delete', evalapp.views.l_comment_delete, name="l_comment_delete"),
    path('major/<int:major_id>/comment/<int:comment_id>/delete', evalapp.views.m_comment_delete, name="m_comment_delete"),

    path('elective/<int:elective_id>/comment/<int:comment_id>/edit', evalapp.views.e_comment_edit, name="e_comment_edit"),
    path('liberal/<int:liberal_id>/comment/<int:comment_id>/edit', evalapp.views.l_comment_edit, name="l_comment_edit"),
    path('major/<int:major_id>/comment/<int:comment_id>/edit', evalapp.views.m_comment_edit, name="m_comment_edit"),

    #month
    path('February', evalapp.views.February, name='February'),  
    path('February/<int:february_id>', evalapp.views.February_detail, name='February_detail'), 

    #empty
    path('empty', evalapp.views.empty, name='empty'),   

    path('search',evalapp.views.search,name='search'),
    path('detail/<int:blog_id>', evalapp.views.detail, name='detail'),
]
