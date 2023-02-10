from unittest import result


def date_return(days_ago):
  from datetime import timedelta, date
  t = date.today()
  result = t - timedelta(days_ago)
  return(result.strftime('%Y/%m/%d'))


  