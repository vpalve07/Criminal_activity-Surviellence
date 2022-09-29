from django.contrib import admin
from home.models import User
from home.models import Officers
from home.models import Other
from home.models import Add_Criminal
from home.models import PASP
from home.models import PDCP
from home.models import PIGP
from home.models import PIP
from home.models import PSIP
from home.models import Reports
from home.models import Search_Name
from home.models import ID



admin.site.register(User)
admin.site.register(Officers)
admin.site.register(Other)
admin.site.register(Add_Criminal)
admin.site.register(PASP)
admin.site.register(PDCP)
admin.site.register(PIGP)
admin.site.register(PIP)
admin.site.register(PSIP)
admin.site.register(Reports)
admin.site.register(Search_Name)
admin.site.register(ID)
