import os
import datetime
import logging
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from oauth2client.client import flow_from_clientsecrets
from googleapiclient.discovery import build

def print_banner():
    banner = """
    ==============================================
        RECURRING EVENT AUTOMATOR
        Automate Your Repeated Events Effortlessly
    ==============================================
    """
    print(banner)

logging.basicConfig(filename='event_automator.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    client_secret_file = 'credentials.json'
    storage = Storage('token.json')
    credentials = storage.get()

    if not credentials or credentials.invalid:
        flow = flow_from_clientsecrets(client_secret_file, SCOPES)
        credentials = run_flow(flow, storage)

    return build('calendar', 'v3', credentials=credentials)

def generate_recurrence_rule(choice, count):
    """Generate RRULE based on user's choice."""
    if choice == "1":
        return "RRULE:FREQ=DAILY;COUNT=%d" % count
    elif choice == "2":
        return "RRULE:FREQ=WEEKLY;COUNT=%d" % count
    elif choice == "3":
        return "RRULE:FREQ=MONTHLY;COUNT=%d" % count
    elif choice == "4":
        return "RRULE:FREQ=YEARLY;COUNT=%d" % count
    else:
        return None

def create_recurring_event(service, title, description, location, start_time, recurrence_rule):
    event = {
        'summary': title,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': (datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S") + datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'UTC',
        },
        'recurrence': [
            recurrence_rule
        ],
    }
    created_event = service.events().insert(calendarId='primary', body=event).execute()
    logging.info("Event created: %s" % created_event['htmlLink'])
    print("Event created successfully: %s" % created_event['htmlLink'])

def main():
    print_banner()
    service = authenticate_google_calendar()

    title = raw_input("Enter the title of the event: ")
    description = raw_input("Enter the description of the event: ")
    location = raw_input("Enter the location of the event: ")
    start_time = raw_input("Enter the start time (YYYY-MM-DDTHH:MM:SS): ")

    print("\nChoose the type of recurrence:")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. Yearly")
    choice = raw_input("Enter your choice (1-4): ")
    count = int(raw_input("Enter how many times the event should repeat: "))
    
    recurrence_rule = generate_recurrence_rule(choice, count)
    if recurrence_rule is None:
        print("Invalid choice! Exiting...")
        return

    create_recurring_event(service, title, description, location, start_time, recurrence_rule)
    print("Recurring Event Automator finished successfully!")

if __name__ == '__main__':
    main()
