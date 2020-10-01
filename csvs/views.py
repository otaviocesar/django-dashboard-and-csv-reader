from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from locUnits.models import LocUnit, Event
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from dateutil.parser import parse
# Create your views here.

@login_required
def upload_file_view(request):
    error_message = None
    success_message = None
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        try:
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)

                for row in reader:
                    row = "".join(row)
                    row = row.replace(";", " ")
                    row = row.split()
                    #data_e_hora_em_texto = row[1] + ' ' + row[2]
                    #data_e_hora = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M')
                    #loc = int(row[0])
                    #data = datetime.strptime(row[1] + ' ' + row[2], '%d/%m/%Y %H:%M')
                    #loc = get_object_or_404(LocUnit,name=row[0])
                    #loc = LocUnit.objects.get_or_create(name=row[0])
                    if row[1] != 'DATA/HORA':
                        hoje = date.today()
                        #input_ocorrencia = row[1]
                        #data_ocorrencia = datetime.strptime(input_ocorrencia, '%d/%m/%y')
                        #diferenca = hoje - data_ocorrencia.date()
                        #print(diferenca.days) # diferença em dias
                        #datetime_format = "%d/%m/%Y  %H:%M:%S"
                        #dataAntiga = "2018-05-09T05:05:34Z"
                        #event_date = row[1]
                        #event_date = row[1] + ' ' + row[2]
                        date_string = row[1]
                    
                        date_object = date(*map(int, reversed(date_string.split("/"))))
                        date_object == datetime.strptime(date_string, "%d/%m/%Y").date()
                        diferenca = hoje - date_object
                        #event_date_convert = datetime.strptime(event_date, datetime_format)
                        loc, _ = LocUnit.objects.get_or_create(name=row[3], number=row[3])
                        Event.objects.create(
                            locUnit=loc,
                            date = date_object
                            )

                        #locUpdate = LocUnit.objects.get(name=row[3])
                        loc.days = diferenca.days
                        loc.date = date_object
                        loc.save()

            obj.activated=True
            obj.save()
            success_message= "Dados Inseridos com Sucesso!"
        except:
            error_message = "Erro ao processar o arquivo"

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'csvs/upload.html', context)