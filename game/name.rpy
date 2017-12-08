 screen hello_world:
     tag example
     zorder 1
     modal False

    # The phrase in the brackets is the text that the game will display to prompt 
    # the player to enter the name they've chosen.

        $ player_name = renpy.input("What is your name?")

        $ player_name = player_name.strip()
    # The .strip() instruction removes any extra spaces the player may have typed by accident.

    #  If the player can't be bothered to choose a name, then we
    #  choose a suitable one for them:
        if player_name == "":
            $ player_name="John D."
    
    # Now the other characters in the game can greet the player.
    
        #e "Pleased to meet you, %(player_name)s!"
        #Edit: If you are using the new version of ren'py, use the following line instead of the one above, since that changed:
        a "Pleased to meet you, [player_name]!"
