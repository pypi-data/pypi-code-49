from django.urls import path
from .views import RGPluginsUtil

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('util/enableLogs', RGPluginsUtil.enable_logs),
    path('util/disableLogs', RGPluginsUtil.disable_logs),
    path('util/getLogStatus', RGPluginsUtil.get_log_status),
]
