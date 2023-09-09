from modules import (
    wikipedia_search,
    open_youtube,
    open_github,
    goodbye,
    search_wikipedia,
    open_website,
    check_internet_speed,
    play_music,
    open_camera,
    open_task_manager,
    remember_message,
    recall_message,
    write_note,
    show_note,
    set_alarm,
    send_email,
    play_songs_on_youtube,
    remove_youtube_ads,
    check_battery_percentage,
    scroll_down_screen,
    minimize_window,
    full_screen,
    send_whatsapp_message,
    open_instagram_profile,
    read_pdf_file,
    search_google,
    get_weather,
    get_wolfram_alpha_results,
    generate_text_with_gpt3,
    taklWithBot,
    checkBattery
)



commands = {
    "wikipedia": {
        "phrases": ["search on Wikipedia", "search in Wikipedia", "Wikipedia", "Wikipedia search"],
        "function": wikipedia_search,
        "requires_query": True
    },
    "open youtube": {
        "phrases": ["open YouTube", "go to YouTube"],
        "function": open_youtube,
        "requires_query": False
    },
    "open github": {
        "phrases": ["open GitHub", "go to GitHub"],
        "function": open_github,
        "requires_query": False
    },
    # Add more commands with variations
    "goodbye": {
        "phrases": ["goodbye", "bye", "exit"],
        "function": goodbye,
        "requires_query": False
    },

    "battery":{
        "phrases": ["battery percentage", "battery status", "battery level","what is the battery percentage "],
        "function": checkBattery,
        "requires_query": False
    },

    "internet speed":{
        "phrases": ["check internet speed","speed of internet", "what is the speed of internet",],
        "function": check_internet_speed,
        "requires_query": False
    },

    "open camera":{
        "phrases": ["open web cam","open camera",],
        "function": open_camera,
        "requires_query": False
    },

    "open task manager":{
        "phrases": ["open task manager","task manager",],
        "function": open_task_manager,
        "requires_query": False
    },

    "remember message":{
        "phrases": ["remember a message","remember for me"],
        "function": remember_message,
        "requires_query": False
    },

    "recall message":{
        "phrases": ["recall a message","recall for me" ,"recall message which i tell you to remaber"],
        "function": recall_message,
        "requires_query": False
    },

    # "lets talk":{
    #      "phrases": ["talk", "let talk", "lets talk"],
    #     "function": taklWithBot,
    #     "requires_query": True
    # }
}


def getCommand():
    return commands
