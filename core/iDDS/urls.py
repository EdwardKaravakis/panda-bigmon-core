"""
URL patterns for Operational Intelligence related views
"""

from django.urls import re_path
from core.iDDS import views as idds_views
from core.iDDS import workflowprogress as idds_progress
from core.iDDS import DAGvisualization
from django.conf import settings


urlpatterns = [
    re_path(r'^idds/$', idds_views.main, name='iddsmain'),
    re_path(r'^idds/collections/$', idds_views.collections, name='iddscollections'),
    re_path(r'^idds/transforms/$', idds_views.transforms, name='iddstransforms'),
    re_path(r'^idds/processings/$', idds_views.processings, name='iddprocessings'),
    re_path(r'^idds/contents/$', idds_views.iddscontents, name='iddsсontents'),
    re_path(r'^idds/getiddsfortask/$', idds_views.getiDDSInfoForTaskRequest, name='getiDDSInfoForTask'),
    re_path(r'^idds/wfprogress/$', idds_progress.wfprogress, name='workflowprogressitems'),
    re_path(r'^idds/daggraph/$', DAGvisualization.daggraph, name='daggraph'),
]

if settings.DEPLOYMENT == 'ORACLE_ATLAS':
    from core.iDDS import logsretrieval
    urlpatterns.append(re_path(r'^idds/downloadlog/$', logsretrieval.downloadlog, name='downloadlog'))
    urlpatterns.append(re_path(r'^idds/downloadhpometrics/$', logsretrieval.downloadhpometrics, name='downloadlog'))
