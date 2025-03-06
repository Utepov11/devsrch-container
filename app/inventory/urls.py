from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='home'), # Начальная страница
    path('accounts/login/', views.UserLogin.as_view(), name='login'), # Авторизация
    path('logout/', views.logout_view, name='logout'), # Для выхода из аккаунта
    path('computers/', views.computers_list, name='computers'), # Список компьютеров
    path('printers/', views.printers_list, name='printers'), # Список принтеров
    path('accessories/', views.accessories_list, name='accessories'), # Список периферии
    path('add-device/', views.add_device, name='add-device'), # Добавление устройств
    path('export_computers_xls/', views.export_computers_xls), # Сформирование отчёта в XLS файл
    path('export_printers_xls/', views.export_printers_xls), # Сформирование отчёта в XLS файл
    path('computer/<slug:computer_slug>/update', views.computer_update, name='computer-update'), # Обновление данных компьютеров
    path('printer/<slug:printer_slug>/update', views.printer_update, name='printer-update'), # Обновление данных принтеров
    path('accessory/<slug:device_slug>/update', views.accessory_update, name='accessory-update'), # Обновление данных принтеров
    path('computer/<slug:computer_slug>/delete', views.ComputerDelete.as_view(), name='computer-delete'), # Удаление компьютера
    path('printer/<slug:printer_slug>/delete', views.PrinterDelete.as_view(), name='printer-delete'), # Удаление принтера
    path('accessory/<slug:device_slug>/delete', views.AccessoryDelete.as_view(), name='accessory-delete'), # Удаление принтера
    path('media/', views.saved_reports, name='saved-reports'), # Список сформированных отчётов
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
