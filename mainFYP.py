class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user 

def get_event_date(event):
  return event.date

def current_users(events):
  sorted_event = sorted(events ,key = get_event_date)
  machine_users = {}
  for event in events:
    if event.machine not in machine_users:
      machine_users[event.machine] = set()
    if event.type == "login":
      machine_users[event.machine].add(event.user)
    elif event.type==" logout":
      machine_users.users[event.machine].remove(event.user)
  return machine_users

def print_list(machines):
  for machine, users in machines.items():
    if len(users):
      detail =  "," .join(users)
      print(f"{machine} -> {detail}")
events = [
  Event('2020-01-21 12:45:56', 'login','myworkstation', 'Fatima'),
  Event('2020-01-21 11:45:56', 'logout','myworkstation', 'Fareeha'),
  Event('2020-01-21 10:45:56', 'login','webserver.local', 'Jordan'),
  Event('2020-01-21 09:12:56', 'logout','mailserver.lcoal', 'Hamza'),
]
machines = current_users(events)
print_list(machines)