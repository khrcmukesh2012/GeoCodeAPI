from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from .models import Address
from tablib import Dataset
from django.contrib import messages
import requests
import pandas as pd
import os
# Create your views here.
GOOGLE_API_KEY = 'API key '


def extract_lat_long_via_address(address_or_zipcode):
	lat, lng = None, None
	api_key = GOOGLE_API_KEY
	base_url = "https://maps.googleapis.com/maps/api/geocode/json"
	endpoint = f"{base_url}?address={address_or_zipcode}&key={api_key}"

	r = requests.get(endpoint)
	if r.status_code not in range(200, 299):
	    return None, None
	try:
	    results = r.json()['results'][0]
	    lat = results['geometry']['location']['lat']
	    lng = results['geometry']['location']['lng']
	except:
	    pass
	return lat, lng

class AddressListView(View):
	template_name = "address_list.html"

	def get(self,request):
		data = Address.objects.all()
		return render(request,self.template_name,{'data':data})

class UploadExcelView(View):
	template_name = "upload.html"

	def get(self,request):
		return render(request,self.template_name)

	def post(self,request):
		dataset = Dataset()
		excel_file = request.FILES["excel_file"]
		if not excel_file.name.endswith('xlsx'):
			messages.warning(request, 'Opps Worng File Formate!!') 
			return render(request,self.template_name)
		excel_data = dataset.load(excel_file.read(),format='xlsx')

		for data in excel_data:
			add = '{} {} {} {}'.format(data[0],data[1],data[2],data[3])
			print(add)
			gt_lat_log =extract_lat_long_via_address(add)
			obj = Address()
			obj.address = data[0]
			obj.state = data[1] 
			obj.country = data[2]
			obj.pin_code = data[3]
			obj.lat = gt_lat_log[0]
			obj.log = gt_lat_log[1]
			obj.save()

		return redirect('/')


def download(request):
	df = pd.DataFrame(list(Address.objects.all().values()))
	filename = 'address_download.xlsx'
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename=address_download.xlsx'
	df.drop(['id'], axis=1, inplace=True)
	if os.path.isfile(filename):
	    os.remove(filename)
	df.to_excel(response, index=False)

	return response

