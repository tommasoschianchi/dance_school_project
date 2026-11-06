from django.urls import path
from school.views import (
    ApiSchoolDetail, ApiSchoolList, DayOfTheWeekCreateView, DayOfTheWeekListView, DayOfTheWeekDetailView, DayOfTheWeekUpdateView, DayOfTheWeekDeleteView, api_example,
    classroomListView, classroomDetailView, classroomCreateView, classroomUpdateView, classroomDeleteView,
    courseListView, courseDetailView, courseCreateView, courseUpdateView, courseDeleteView,
)


urlpatterns = [path("giorni/", DayOfTheWeekListView.as_view(), name="dayoftheweek_list"), 
               path("giorni/<int:pk>/", DayOfTheWeekDetailView.as_view(), name="dayoftheweek_detail"),
               path("classroom/", classroomListView.as_view(), name="classroom_list"),
               path("classroom/<int:pk>/", classroomDetailView.as_view(), name="classroom_detail"),
               path("classroom/nuovo/", classroomCreateView.as_view(), name="classroom_create"),
               path("classroom/<int:pk>/modifica/", classroomUpdateView.as_view(), name="classroom_update"),
               path("classroom/<int:pk>/elimina/", classroomDeleteView.as_view(), name="classroom_delete"),
               path("course/", courseListView.as_view(), name="course_list"),
               path("course/<int:pk>/", courseDetailView.as_view(), name="course_detail"),
               path("course/nuovo/", courseCreateView.as_view(), name="course_create"),
               path("course/<int:pk>/modifica/", courseUpdateView.as_view(), name="course_update"),
               path("course/<int:pk>/elimina/", courseDeleteView.as_view(), name="course_delete"),
               path("giorni/nuovo/", DayOfTheWeekCreateView.as_view(), name="dayoftheweek_create"),
               path("giorni/<int:pk>/modifica/", DayOfTheWeekUpdateView.as_view(), name="dayoftheweek_update"),
               path("giorni/<int:pk>/elimina/", DayOfTheWeekDeleteView.as_view(), name="dayoftheweek_delete"),
               path("api/example/", api_example, name="api_example"),
               path("api/school/<int:pk>/", ApiSchoolDetail.as_view(), name="api_school"),
               path("api/school/", ApiSchoolList.as_view(), name="api_school_list")
               
]