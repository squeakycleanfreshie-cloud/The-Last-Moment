# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Grandpa")
define y = Character("You")
define t = Character("Thought")
define n = Character("Narrator")
define m = Character("Mum")



default time_left = 300  
default game_over = False

init python:
    def format_time(seconds):
        return "%d:%02d" % (seconds // 60, seconds % 60)

    def tick_timer():
        if store.time_left > 0:
            store.time_left -= 1
        if store.time_left <= 0 and not store.game_over:
            store.game_over = True
            renpy.jump("ending")

    config.overlay_screens.append("countdown_timer")

screen countdown_timer():
    zorder 100
    timer 1.0 action Function(tick_timer) repeat True

    frame:
        xalign 0.5
        ypos 10
        background "#000000cc"
        padding (20, 10)
        text "Time left: [format_time(time_left)]":
            size 28
            color "#ffffff"

screen room_items():
    default hover_label = ""

    # photo
    button:
        xpos 200 ypos 300 xysize (150, 150)
        background None
        hover_background "#ffffff22"
        hovered SetLocalVariable("hover_label", "An old photo")
        unhovered SetLocalVariable("hover_label", "")
        action [SetVariable("items_found", items_found + ["photo"]), Jump("photo_item")]

    # letter
    button:
        xpos 600 ypos 450 xysize (100, 80)
        background None
        hover_background "#ffffff22"
        hovered SetLocalVariable("hover_label", "A folded letter")
        unhovered SetLocalVariable("hover_label", "")
        action [SetVariable("items_found", items_found + ["letter"]), Jump("letter_item")]

    # watch
    button:
        xpos 850 ypos 500 xysize (60, 60)
        background None
        hover_background "#ffffff22"
        hovered SetLocalVariable("hover_label", "His old watch")
        unhovered SetLocalVariable("hover_label", "")
        action [SetVariable("items_found", items_found + ["watch"]), Jump("watch_item")]

    if hover_label:
        text hover_label:
            xpos 200 ypos 620
            size 24
            color "#ffffff"

label start:

    scene bg room
    n "You arrive at his house."
    n "You knock at the door."
    n "A familiar face opens it."
    n "You have one thought in mind. One single mission."
    y "Can I see him"
    m "He's asleep. Don't wake him. Go on in, look around if you want."
    n "You walk inside. The smell of old people hits you first."
    n "As a kid you never liked this place."
    n "Everything was so old. And Bigger."
    n "You walk through the kitchen, into your granpa's room."
    n "He lays sleeping."
    n "You know theese are going to be his final moments."
    n "You walk over to him and kneel next to his bed."
    y "Hey grandpa,"
    y "I love you so much."
    n "You kiss him on the forehead."
    n "Then you go and find a chair in the corner."
    n "Its old."

    show screen countdown_timer
    show screen room_items
    call screen room_items

label photo_item:
    hide screen room_items
    scene bg_photo_closeup


    scene black with fade


    scene bg_room with fade
    show screen room_items
    return

label letter_item:
    hide screen room_items
    scene bg_letter_closeup


    scene black with fade


    scene bg_room with fade
    show screen room_items
    return

label watch_item:
    hide screen room_items
    scene bg_watch_closeup


    scene black with fade


    scene bg_room with fade
    show screen room_items
    return

label ending:
    hide screen room_items
    hide screen countdown_timer
    scene black
    if len(items_found) >= 3:

    elif len(items_found) >= 1:

    else:
        n "life is short."
        n "don't waste the time you have."
        n "...."
        n "and enjoy it."
    return

