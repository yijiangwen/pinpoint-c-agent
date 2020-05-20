from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_builtin_func/<arg>/', views.builtin, name='test_builtin_func'),
    path('test_package_func/', views.date, name='test_package_func'),
    path('test_user_func1/', views.test_func1, name='test_user_func1'),
    path('test_user_func2/', views.test_func2, name='test_user_func2'),
    path('test_user_func3/', views.test_func3, name='test_user_func3'),
    path('test_user_func4/', views.test_func4, name='test_user_func4'),
    path('test_inherit_func/', views.test_inherit, name='test_inherit_func'),
    path('test_recursion/', views.test_recursion_func, name='test_recursion'),
    path('test_higher_order/', views.test_higher_order, name='test_higher_order'),
    path('test_generatior/', views.test_generator, name='test_generatior'),
    path('test_return_func/', views.test_return, name='test_return_func'),
    path('test_lambda/', views.test_lambda, name='test_lambda'),
    path('test_decorator/', views.test_decorator, name='test_decorator'),
    path('test_partial/', views.test_partial, name='test_partial'),
    path('test_band/', views.test_band_func, name='test_band'),
    path('test_mixin/', views.test_mixin_func, name='test_mixin'),
    path('test_special/', views.test_special_func, name='test_special'),
    path('test_private/', views.test_private_func, name='test_private'),
    path('test_abstract/', views.test_abstract_func, name='test_abstract'),
    path('test_staticmethod/', views.test_staticmethod, name='test_staticmethod'),
    path('test_classmethod/', views.test_classmethod, name='test_classmethod'),
    path('test_exception/', views.test_exception_func, name='test_exception'),
    path('test_uncaught_exception/', views.test_uncaught_exception, name='test_uncaught_exception'),
    path('test_caught_exception/', views.test_caught_exception, name='test_caught_exception'),
    path('test_exception_in_recursion/', views.test_exception_in_recursion, name='test_exception_in_recursion'),
    path('test_arguments/', views.test_arguments, name='test_arguments'),
    path('test_returns/', views.test_returns_func, name='test_returns'),
    path('test_mysql/', views.test_mysql, name='test_mysql'),
    path('test_redis/', views.test_redis, name='test_redis'),
    path('call_remote/', views.call_remote, name='call_remote'),
]