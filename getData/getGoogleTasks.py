import datetime
import pickle
import os
import json
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print(e)
        print(f'Failed to create service instance for {API_SERVICE_NAME}')
        os.remove(pickle_file)
        return None


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0, 000).isoformat() + 'Z'
    return dt





#task list that is returned is only the one that I have entered the ID for (So will only get mine)
#task list will return a list of json/ dic items. Each item has a title, id and notes section
# if the notes = "none" then there was no note
# if the id = "subTask" then it means that the previous task (that's ID was not "subTask") is the parent
def getTaskList():
    #get info and create the service
    CLIENT_SECRET_FILE = "client_secret_file.json"
    API_NAME = "tasks"
    API_VERSION = "v1"
    SCOPES = ["https://www.googleapis.com/auth/tasks"]
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


    #get the task list
    resp = service.tasks().list(
        tasklist= "MTQ0OTMwMjgxOTY3MzA0NzYwODM6MDow",
        showCompleted = False
    ).execute()
    lstItems = resp.get("items")
    nextToken = resp.get("nextPageToken")


    taskList = []
    subTasksList = []
    mainTask = False
    #refine the retrived task list, and get all of the main tasks
    for task in lstItems:

        #get the task's title
        title = task["title"]
        id = "mainTask"


        #check if task is a sub task and store it for later if it is,
        try:
            if(len(str(task["parent"])) > 0):
                subTasksList.append({"title" : title, "id" : "subTask", "notes" : "none"})
                continue
        except Exception:
            mainTask = True
            pass

        #check if task has a description
        try:
            desc = task["notes"]
        except Exception:
            desc = "none"
            pass

        #add the wanted task info into the dictionary
        taskList.append({"title" : title, "id" : id, "notes" : desc})

        #if this is the first main task then all previous sub tasks are this main tasks children. So add them after
        if(mainTask and len(subTasksList) > 0):
            #append all sub tasks into the main list
            for subTask in subTasksList:
                taskList.append(subTask)

            #clear the sub tasks now they have all been added
            subTasksList.clear()


    return (taskList)

print(getTaskList())