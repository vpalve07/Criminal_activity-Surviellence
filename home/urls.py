from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.userLogin, name='home'),
    path("index",views.index, name='index'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name='contact'),
    path("services1",views.services1, name='services1'),
    path("services2",views.services2, name='services2'),
    path("report",views.report, name='report'),
    path("userReg",views.userReg, name='userReg'),
    path("userLogin",views.userLogin, name='userLogin'),
    path("offLogin",views.offLogin, name='offLogin'),
    path("otheroffLogin",views.otheroffLogin, name='otheroffLogin'),
    path("officialRegistration",views.officialRegistration, name='officialRegistration'),
    path("otheroffReg",views.otheroffReg, name='otheroffReg'),
    path("offIndex",views.offindex, name='offIndex'),
    path("OtherOffIndex",views.otheroffindex, name='OtherOffIndex'),
    path("addCriminals",views.addCriminals, name='addCriminals'),
    # path("complaint",views.complaint, name='complaint'),
    path("other_search",views.other_search, name='other_search'),
    path("after_nm_search",views.after_nm_search, name='after_nm_search'),
    path("view_all_criminals",views.view_all_criminals, name='view_all_criminals'),
    path("view_complaints",views.view_complaints, name='view_complaints'),
    path("view_searched_criminals",views.view_searched_criminals, name='view_searched_criminals'),
    path("error",views.error, name='error'),
    path("Pasp",views.Rape, name='Pasp'),
    path("Pdcp",views.Murder, name='Pdcp'),
    path("Pigp",views.Terrorist, name='Pigp'),
    path("Pip",views.Kidnapping, name='Pip'),
    path("Psip",views.Robbery_cases, name='Psip'),
    path("Robbers",views.Robbers, name='Robbers'),
    path("Kidnappers",views.Kidnappers, name='Kidnappers'),
    path("Murderers",views.Murderers, name='Murderers'),
    path("Rapists",views.Rapists, name='Rapists'),
    path("Terrorists",views.Terrorists, name='Terrorists'),
    path("map",views.map, name='map'),
    # path("match",views.match, name='match'),


]
