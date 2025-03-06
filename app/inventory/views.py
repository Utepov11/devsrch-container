from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.views.generic import TemplateView
from django.utils.timezone import now
from django.db.models import F
import xlwt, datetime, os
from django.shortcuts import redirect

from .models import Computer, Printer, Accessory, ReportLog
from .forms import MyComputerForm, MyPrinterForm, MyAccessoryForm


# Базовый шаблон
@login_required
def base(request):
    return render(request, 'inventory/base.html', {'user': request.user})


def custom_404(request, exception):
    return render(request, 'inventory/404.html', status=404)


# Главная страница
class MainPage(LoginRequiredMixin, TemplateView):
    def get(self, request):
        return render(request, 'inventory/index.html')


# Авторизация пользователей
class UserLogin(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'inventory/sign-in.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        return render(request, 'inventory/sign-in.html', {'form': form})


# Выход из аккаунта
def logout_view(request):
    logout(request)
    return redirect('login')


# Добавление устройств
@login_required
def add_device(request):
    computer_form = MyComputerForm(request.POST or None)
    printer_form = MyPrinterForm(request.POST or None)
    accessory_form = MyAccessoryForm(request.POST or None)

    if request.method == "POST":
        if 'computer_type' in request.POST:
            if computer_form.is_valid():
                computer = computer_form.save(commit=False)
                computer.computer_author = request.user
                computer.save()
                messages.success(request, "Устройство успешно добавлено!")
                return redirect('add-device')
        if 'printer_type' in request.POST:
            if printer_form.is_valid():
                printer = printer_form.save(commit=False)
                printer.printer_author = request.user
                printer.save()
                messages.success(request, "Устройство успешно добавлено!")
                return redirect('add-device')
        if 'accessory_type' in request.POST:
            if accessory_form.is_valid():
                accessory = accessory_form.save(commit=False)
                accessory.accessory_author = request.user
                accessory.save()
                messages.success(request, "Устройство успешно добавлено!")
                return redirect('add-device')

    return render(request, 'inventory/add-device.html', {
        'computer_form': computer_form,
        'printer_form': printer_form,
        'accessory_form': accessory_form
    })


# Список ПК/ноутбуков
@login_required
def computers_list(request):
    query = request.GET.get('query', '')
    location = request.GET.get('location', '')

    locations = Computer.objects.values_list('computer_location', flat=True).distinct()

    computers = Computer.objects.all()

    if query:
        computers = computers.filter(computer_inventory__icontains=query)

    if location:
        computers = computers.filter(computer_location=location)

    return render(request, 'inventory/computer-list.html', {
        'computers': computers,
        'query': query,
        'location': location,
        'locations': locations,
    })

# Список принтеров/сканеров
@login_required
def printers_list(request):
    query = request.GET.get('query', '')
    location = request.GET.get('location', '')

    locations = Printer.objects.values_list('printer_location', flat=True).distinct()

    printers = Printer.objects.all()

    if query:
        printers = printers.filter(printer_inventory__icontains=query)

    if location:
        printers = printers.filter(printer_location=location)

    return render(request, 'inventory/printer-list.html', {
        'printers': printers,
        'query': query,
        'location': location,
        'locations': locations,
    })

# Список принтеров/сканеров
@login_required
def accessories_list(request):
    query = request.GET.get('query', '')
    location = request.GET.get('location', '')

    locations = Accessory.objects.values_list('accessory_location', flat=True).distinct()

    accessories = Accessory.objects.all()

    if query:
        accessories = accessories_list.filter(accessory_inventory__icontains=query)

    if location:
        accessories = accessories.filter(accessory_location=accessories)

    return render(request, 'inventory/accessory-list.html', {
        'accessories': accessories,
        'query': query,
        'location': location,
        'locations': locations,
    })


# Обновление данных устройств
@login_required
def computer_update(request, computer_slug):
    computer = get_object_or_404(Computer, slug=computer_slug)

    if request.method == 'POST':
        form = MyComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()
            messages.success(request, "Устройство успешно отредактировано!")
    else:
        form = MyComputerForm(instance=computer)
    return render(request, 'inventory/computer-update.html', {'computer_form': form})

@login_required()
def printer_update(request, printer_slug):
    printer = get_object_or_404(Printer, slug=printer_slug)

    if request.method == 'POST':
        form = MyPrinterForm(request.POST, instance=printer)
        if form.is_valid():
            form.save()
            messages.success(request, "Устройство успешно отредактировано!")
    else:
        form = MyPrinterForm(instance=printer)
    return render(request, 'inventory/printer-update.html', {'printer_form': form})

@login_required()
def accessory_update(request, accessory_slug):
    accessory = get_object_or_404(Accessory, slug=accessory_slug)

    if request.method == 'POST':
        form = MyAccessoryForm(request.POST, instance=accessory)
        if form.is_valid():
            form.save()
            messages.success(request, "Устройство успешно отредактировано!")
    else:
        form = MyAccessoryForm(instance=accessory)
    return render(request, 'inventory/accessory-update.html', {'accessory_form': form})


# Удаление устройств
class ComputerDelete(LoginRequiredMixin, TemplateView):
    def post(self, request, computer_slug):
        computer = get_object_or_404(Computer, slug=computer_slug)
        computer.delete()
        return redirect('computers')

class PrinterDelete(LoginRequiredMixin, TemplateView):
    def post(self, request, printer_slug):
        printer = get_object_or_404(Printer, slug=printer_slug)
        printer.delete()
        return redirect('printers')
class AccessoryDelete(LoginRequiredMixin, TemplateView):
    def post(self, request, accessory_slug):
        accessory = get_object_or_404(Accessory, slug=accessory_slug)
        accessory.delete()
        return redirect('accessories')


# Сохраненные отчёты
@login_required
def saved_reports(request):
    reports = ReportLog.objects.all().order_by('-generated_at')[:10]
    return render(request, 'inventory/saved-reports.html', {'reports': reports})


# Формирование и сохранение отчётов
@login_required
def export_computers_xls(request):
    timestamp = now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"computers-list_{timestamp}.xls"
    
    # Путь к папке reports
    upload_dir = os.path.join('media/reports')
    os.makedirs(upload_dir, exist_ok=True)  # Создаёт папку, если её нет
    
    file_path = os.path.join(upload_dir, filename)
    
    # Создание Excel-файла
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Computers')
    
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.height = 240
    
    columns = ['Наименование устройства', 'Инвентарный номер', 'Серийный номер',
               'Расположение', 'Дата добавления', 'Добавил']
    
    for col_num in range(len(columns)):
        ws.col(col_num).width = 7000
        ws.write(row_num, col_num, columns[col_num], font_style)
    
    rows = (
        Computer.objects.all()
        .annotate(
            author_name = F('computer_author__username')
        )
        .values_list(
            'computer_type', 'computer_inventory', 'computer_snumber',
            'computer_location', 'computer_date', 'author_name'
        )
    )

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            value = row[col_num]
            if isinstance(value, (datetime.date, datetime.datetime)):
                value = value.strftime('%d.%m.%Y')  # Преобразование в строку
            ws.write(row_num, col_num, value, font_style)
    
    # Сохранение файла в папке
    wb.save(file_path)
    
    # Сохраняем информацию о созданном отчёте
    ReportLog.objects.create(
        report_name=filename,
        file_path=f"reports/{filename}",  # Сохраняем полный относительный путь
    )

    # Подготовка файла для скачивания
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    wb.save(response)  # Сохранение в HTTP-ответ
    
    return response

@login_required
def export_printers_xls(request):
    timestamp = now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"printer-list_{timestamp}.xls"
    
    upload_dir = os.path.join('media/reports')
    os.makedirs(upload_dir, exist_ok=True)
    
    file_path = os.path.join(upload_dir, filename)
    
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Printers')
    
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.height = 240
    
    columns = ['Наименование устройства', 'Инвентарный номер', 'Серийный номер',
               'Расположение', 'Дата добавления', 'Добавил']
    
    for col_num in range(len(columns)):
        ws.col(col_num).width = 7000
        ws.write(row_num, col_num, columns[col_num], font_style)
    
    rows = (Printer.objects.all()
        .annotate(
            author_name = F('printer_author__username')
        )
        .values_list(
            'printer_type', 'printer_inventory', 'printer_snumber',
            'printer_location', 'printer_date', 'author_name'
        )
    )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            value = row[col_num]
            if isinstance(value, (datetime.date, datetime.datetime)):
                value = value.strftime('%d.%m.%Y')
            ws.write(row_num, col_num, value, font_style)
    
    wb.save(file_path)
    
    ReportLog.objects.create(
        report_name=filename,
        file_path=f"reports/{filename}",
    )

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    wb.save(response)
    
    return response

@login_required
def export_accessories_xls(request):
    timestamp = now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"accessory-list_{timestamp}.xls"
    
    upload_dir = os.path.join('media/reports')
    os.makedirs(upload_dir, exist_ok=True)
    
    file_path = os.path.join(upload_dir, filename)
    
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Accessories')
    
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.height = 240
    
    columns = ['Наименование устройства', 'Инвентарный номер', 'Серийный номер',
               'Расположение', 'Дата добавления', 'Добавил']
    
    for col_num in range(len(columns)):
        ws.col(col_num).width = 7000
        ws.write(row_num, col_num, columns[col_num], font_style)
    
    rows = (Accessory.objects.all()
        .annotate(
            author_name = F('accessory_author__username')
        )
        .values_list(
            'accessory_type', 'accessory_inventory', 'accessory_snumber',
            'accessory_location', 'accessory_date', 'accessory_name'
        )
    )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            value = row[col_num]
            if isinstance(value, (datetime.date, datetime.datetime)):
                value = value.strftime('%d.%m.%Y')
            ws.write(row_num, col_num, value, font_style)
    
    wb.save(file_path)
    
    ReportLog.objects.create(
        report_name=filename,
        file_path=f"reports/{filename}",
    )

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    wb.save(response)
    
    return response