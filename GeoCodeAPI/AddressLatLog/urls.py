from django.conf.urls import include
from django.urls import path
from AddressLatLog.views import *
app_name = "AddressLatLog"
urlpatterns = [
	path('',AddressListView.as_view(),name='address_list' ),
    path('upload-address',UploadExcelView.as_view(),name='upload_address' ),
    path('download',download)
]