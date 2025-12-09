import datetime

def time():
  now = datetime.datetime.utcnow()
  return f"{now.hour}:{now.minute}:{now.second}"

def time_second():
  now = datetime.datetime.utcnow()
  return now.second

def time_minute():
  now = datetime.datetime.utcnow()
  return now.minute

def time_hour():
  now = datetime.datetime.utcnow()
  return now.hour

def date():
  now = datetime.datetime.utcnow()
  return f"{now.month}  {now.day}  {now.year}"

def date_day():
  now = datetime.datetime.utcnow()
  return now.day

def date_month():
  now = datetime.datetime.utcnow()
  return now.month

def date_year():
  now = datetime.datetime.utcnow()
  return now.year


