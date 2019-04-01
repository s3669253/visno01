init:
    define Min = Character("Min", color="#ff3352")
    define player = Character("[e_name]", color="#ff3352")
    image frog = "frog1.png"
    transform left_to_right:
        xalign 0.0
        linear 2.0 yalign 1.0
        repeat

screen test:
    imagebutton:
        idle "frog1.png"
        hover "frog1.png"

        action Show("frog")

screen frog:
    add "frog1.png" transform left_to_right

label start:
  

    call screen test 



    Min "My name is Min"

    
return
