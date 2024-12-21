# Recurring Event Automator

**Recurring Event Automator is a tool that automatically creates recurring events in **Google Calendar** using the Google Calendar API and OAuth2 authentication. With this tool, you can create recurring events with flexible frequency settings, such as daily, weekly, monthly, or yearly.

## Key Features
- **OAuth2 Authentication** for Google Calendar access.
- Ability to create recurring events with flexible frequency options.
- Easy-to-use interactive input for users.
- Event creation logs stored in the `event_automator.log` file.
- Uses Google Calendar API to create events in the user's calendar.

## Prerequisites
1. **Python 2.7**
2. Required **Libraries**:
   - `oauth2client`
   - `google-api-python-client`

## Installation

### 1. Set Up Google Calendar API
Before running the script, you need to enable the Google Calendar API and create credentials:

1. Go to the **Google Cloud Console** at [cloud.google.com/console](https://cloud.google.com/console).
2. Enable the **Google Calendar API** for your project.
3. Create **OAuth2 credentials** (for user-based authentication):
   - Select **Create Credentials** > **OAuth client ID**.
   - Download the credential file (usually named `credentials.json`).
4. Place the `credentials.json` file in the same directory as the Python script.

### 2. Install Dependencies

Install the required dependencies:

```bash
pip install oauth2client google-api-python-client
```

### 3. Prepare `credentials.json`
Ensure you have the `credentials.json` file from **Google Cloud Console** in the same directory as the Python script. These credentials are used for OAuth2 authentication.

## Usage

1. **Run the Script**

   Run the Python script in your terminal or command prompt:

   ```bash
   python recurring_event _automator.py
   ```

2. **Enter Event Details**
   
   The script will prompt you to enter the following event details:
   - **Event Title**
   - **Event Description**
   - **Event Location**
   - **Event Start Time** (Format: YYYY-MM-DDTHH:MM:SS)

3. **Choose Recurrence Settings**
   
   You will then be asked to choose the recurrence type for the event:
   - 1 for **Daily**
   - 2 for **Weekly**
   - 3 for **Monthly**
   - 4 for **Yearly**

4. **Enter the Number of Recurrences**
   
   Next, you will be asked to specify how many times the event should repeat.

5. **OAuth2 Authentication**
   
   If this is your first time running the script, it will prompt you to authenticate and grant access to your Google account. This process only needs to be done once. Afterward, the authentication token will be stored in the `token.json` file.

6. **Recurring Event Created**
   
   Once authenticated, the script will create the recurring event in your Google Calendar according to the selected settings. The created event's link will be displayed in the terminal and logged in the `event_automator.log` file.


## Activity Logs
All event creation activities will be logged in the **`event_automator.log`** file. You can check this file for details about the events that have been created.

## Troubleshooting
- If you encounter authentication issues, ensure that the **`credentials.json`** file is valid and has the necessary access to the calendar.
- If there is an error creating the event, make sure the time format entered is correct (e.g., `2024-12-31T09:00:00`).

