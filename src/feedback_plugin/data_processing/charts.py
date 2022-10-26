from django.db.models.functions import ExtractYear, ExtractMonth
from django.db.models import Count

from feedback_plugin.models import Upload

def compute_server_count_by_month(start_date, end_date):

  server_counts = Upload.objects.annotate(
      year=ExtractYear('upload_time'),
      month=ExtractMonth('upload_time'),
  ).values(
      'year', 'month'
  ).annotate(
      count=Count('server__id', distinct=True)
  ).order_by('year','month')

  return {
      'x': [f"{value['year']}-{value['month']:0>2}" for value in server_counts],
      'y': [int(f"{value['count']}") for value in server_counts]
  }


