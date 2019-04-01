init:

    #define player "e-name" and will input from user
    define player = Character("[e_name]", color="#f44242")
    define Mother = Character("Mother", color="#f4ee42")
    define water_point = 0



screen test:
    frame:
        xpadding 40
        ypadding 40
        vbox:
            text "Type your name"
            input
        align(.5, .5)




label start:

    centered "{color=#024eff}Input your name before the story start{/color}"

    call screen test 
    $ e_name = _return
   

    centered "{color=#e50b0b}That rattle on your mother’s breath has been worrying you for some time now.{/color}"
    centered "{color=#e50b0b}You first noticed it weeks ago as a small and barely audible wheeze.{/color}"
    centered "{color=#e50b0b}however when you ask her about it she tells you not to worry.{/color}"
    centered "{color=#e50b0b}that she has simply feeling under the weather and that she will get better soon.{/color}"
    centered "{color=#e50b0b}Somehow you don’t think this is true.{/color}"
    
    player "Mother, are you well?"
    Mother "I yet live dearest child"
    centered "{color=#e50b0b}Your mother’s voice pulls you from your reverie,\n demanding your attention.{/color}"
    Mother "Attend me closely"
    Mother "You know as well as I that I am not much longer for this world"
    Mother "I have a task that I need you to perform before I depart."
    Mother "You must visit your uncle and bring him to me"
    Mother "Your father’s brother has always been a fine and capable man,\n and visited often before your father passed away,"
    Mother "On the other side of the forest dear, now please go and make haste."
    Mother "Mark that you do not forget the ritual, else the darkness inhabiting that forest will find you"
    
    centered "{color=#024eff}What's your decision?{/color}"
    
    menu:
        "1. You decide to stay with your mother":
            jump stay
        "2. You decide to leave":  
            jump leave

    label stay:
        player "I can’t leave you mother"
        player "I love you, mother"
        return

    label leave:
        centered "{color=#e50b0b}Your mother’s voice pulls you from your reverie{/color}"
        centered "{color=#e50b0b}demanding your attention.{/color}"

    Mother "I know of your dislike, but do not forget the dove!"

    #shrine
    centered "{color=#e50b0b}Walking around the back{/color}"
    centered "{color=#e50b0b}You spy the accursed shrine nestled against the houses outer wall.{/color}"
    centered "{color=#e50b0b}You decide you have procrastinated enough,\nit is time now to begin the ritual.{/color}"
    player "Lo to the Watcher, with power to see"

    menu:
        "1. You offer water":
            $ water_point = 1
            
        "2. You chose not to offer water":  
            $ water_point = 0

    label result:
        if water_point == 1:
            centered "{color=#e50b0b}You reach down and unfasten your flask of water,\nsprinkling a small amount over the shrine. {/color}"
            
        elif water_point == 0:
            centered "{color=#e50b0b}You are not certain how long you will need to travel to reach your uncles home\n
            And may need all the water you can carry.\n
            You chose not to spill any of your precious water\n
            as you are sure that the words themselves are more than enough.{/color}"

    
        


return    
