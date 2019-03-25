init:
    define Ara = Character("Ara", color = "#fc0505")
    define Mother = Character("Mother", color = "#fc0505")
    define narrator = Character(None, kind=nvl)

    image bg forest = "images/bg/forest.jpg"
    

    
label start:
   
    
    "Your mother is dying in bed......."
    nvl clear
    "She fears that it might be her last day on earth."
    
    Mother "Visit your uncle on the other side of the woods and let him know I am very sick." 
    Mother "You need to make an offering to the woods for safe passage"
    Mother "Never talk to anyone. "


    Mother "This is how to do"
    
    Mother "Spill earth, ashes from urn"
    Mother "Spill water, fresh drinking water"
    Mother "Spill blood, grab a dove from the outside cage and kill it"

    show Ara at right
    Ara "I will do it mum, I will be back soon"

    centered "Your mother knows you hate the blood offering and you never personally do it."
    centered "She insists that you have to this time because she is too weak to do it for you."
    centered "Your mum warns you that the witch will see you if you don’t perform the ceremony."

    scene bg forest

    show Ara
    Ara "This is the entering the woods,"
    Ara "I am scared"


    

   

    return
