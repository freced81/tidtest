from openpyxl import load_workbook
from django.contrib.auth import get_user_model
from .models import Tid


def skapa_tidsedel(start, stopp):
    #queryset = Tid.objects.filter(user_id=get_user_model(), vecka__range=(start, stopp))
    wb = load_workbook('/static/tid_rapport/orginal.xlsx')
    dest_filename = 'TidsedelV' + str(start) + '-' + str(stopp) + '.xlsx'
    ws1 = wb.active
    ws1['A8'] = 32
    wb.save(filename=dest_filename)