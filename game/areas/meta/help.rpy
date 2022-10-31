# Settings
define hint_text = {
    "hint_1": """
The King may have a serious drinking problem, but he also knows how to find the Orange Narwhal.\n
If you haven't done so already, go talk to him. He's probably in the restroom behind the bar in The Tap.
    """,
    "hint_2": """
The Pirates, the Ninjas, the Clowns, the Mermaids, and the Police are all duking it out at the moment.\n
They're each looking for help completing tasks and will offer you rewards in return for your assistance.\n
Choose carefully. Your actions will have meaningful consequences throughout the rest of the game.
    """,
    "hint_3": """
The Pirates are looking for someone to help them recover their beer from the sea floor.\n
Go to the dock and talk to the Captain upstairs.\n
But beware creatures from the depths whose beauty may tempt you to betray the Captain.
    """,
    "hint_4": """
The Clowns are planning a daring heist, but have not met up with their fifth member.\n
You can seize this opportunity to take his place and claim a portion of the spoils.\n
Though, you may need to look for clues to work out what the plan is.\n
Also, be careful not to run into the Police afterwards.
    """,
    "hint_5": """
The Noodle House in Chinatown is the only place to get noodles, but you can't buy them.\n
You'll have to join the Leauge of Ninjas by demonstrating your dexterity and reflexes.\n
The arcade next door is a good place to start.
    """,
}

# Screens
screen help_button():
    zorder 100
    hbox:
        align (1.0, 0.0)
        imagebutton:
            idle "help_page"
            action [
                ShowMenu("help")
            ]

screen read_hint(text_content):
    add "meta/hint_paper.png":
        align (0.5, 0.5)
    button action [
        Hide()
    ]
    text text_content:
        align (0.5, 0.5)
        text_align 0.5
        xmaximum 0.4
        color "#000"