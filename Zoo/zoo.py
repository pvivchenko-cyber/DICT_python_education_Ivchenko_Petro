print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")
camel = r"""
The camel habitat...
@
':;
!; !'',,,',',,,,'!
;
;:
:;
!!
!!;
;
:;
;;
!!
!!
;;
!!
!!
;;
!!
!!
!,!
!,!
!,!
/_I
L_I
L_I
/_I
Look at that!"""

print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print(camel)
print("The lion looks healthy.")
camel = r"""
The camel habitat...
@
':;
!; !'',,,',',,,,'!
;
;:
:;
!!
!!;
;
:;
;;
!!
!!
;;
!!
!!
;;
!!
!!
!,!
!,!
!,!
/_I
L_I
L_I
/_I
Look at that!"""

lion = r"""
The lion habitat...
                                      ,w.
                                , YWMMW  ,M   ,
                           _.-"    "---'  'MMMMMW, wMWMW,
                     _.-""                  YP"WMMMmmmmmmb,
                 _.-'          _.---._        MMMMWWMMMM;
        _.-'          _.-.-'";        `'--""   :MMM[==MWMW^;
 ,mM^"        _.-'   /     ;       ;        /   MMMMb wMWMW"  @\
,MM:.       _.-'   _.'     '       \      ;     MMMMMMMW  "=-./_,
WMMm___.-'.-'    /       _.- \      F'''--+,,   ;_,_ .dMMMMMMMM[,  /  =_}
"^MP___.-'     _.'  _..--""    ;        \   ; ;MMMMMMMMMMW^^;   ___|
             /    .'          ;;      )   )`{  \  "^W^   \   :
            /   .'           /  (       ' /   Ww.       _.- '"
          /   Y,            '    -,_=_{   ;   MMMP""-,  _.-._,-'
       (--, )              _.- / `) \/""^)  ^II       `-, -;"\:
The lion is roaring!"""

deer = r"""
The deer habitat...
               _
            _.'"` `'-.
         .-'        .'
       .'        .-'
      /       _.'
     /      .'
    |     .'
   /    .'
  |   .'
  |  /
  / /
 / /
| |
| |
| |
| |
|_|
It looks fine!"""

goose = r"""
The goose habitat...
(.
(-.
<
<-
(<<
<<
(_<_<
Beautiful!"""

bat = r"""
The bat habitat...
    _.._
  .'    '.
 /   _   \
|  (   )  |
 \  `-'  /
  `------`
It's doing fine."""

rabbit = r"""
The rabbit habitat...
         /\
        /  \
       /    \
      /  /\  \
     /  /  \  \
    /  /    \  \
   /  /      \  \
  /  /        \  \
 /  /          \  \
/__/            \__\
It looks fine!"""

animals = [camel, lion, deer, goose, bat, rabbit]

print("Please enter the number of the habitat you would like to view: ")
habitat_num = int(input("> "))
print(animals[habitat_num])
print("You've reached the end of the program.")
camel = r"""
The camel habitat...
@
':;
!; !'',,,',',,,,'!
;
;:
:;
!!
!!;
;
:;
;;
!!
!!
;;
!!
!!
;;
!!
!!
!,!
!,!
!,!
/_I
L_I
L_I
/_I
Look at that!"""

lion = r"""
The lion habitat...
                                      ,w.
                                , YWMMW  ,M   ,
                           _.-"    "---'  'MMMMMW, wMWMW,
                     _.-""                  YP"WMMMmmmmmmb,
                 _.-'          _.---._        MMMMWWMMMM;
        _.-'          _.-.-'";        `'--""   :MMM[==MWMW^;
 ,mM^"        _.-'   /     ;       ;        /   MMMMb wMWMW"  @\
,MM:.       _.-'   _.'     '       \      ;     MMMMMMMW  "=-./_,
WMMm___.-'.-'    /       _.- \      F'''--+,,   ;_,_ .dMMMMMMMM[,  /  =_}
"^MP___.-'     _.'  _..--""    ;        \   ; ;MMMMMMMMMMW^^;   ___|
             /    .'          ;;      )   )`{  \  "^W^   \   :
            /   .'           /  (       ' /   Ww.       _.- '"
          /   Y,            '    -,_=_{   ;   MMMP""-,  _.-._,-'
       (--, )              _.- / `) \/""^)  ^II       `-, -;"\:
The lion is roaring!"""

deer = r"""
The deer habitat...
               _
            _.'"` `'-.
         .-'        .'
       .'        .-'
      /       _.'
     /      .'
    |     .'
   /    .'
  |   .'
  |  /
  / /
 / /
| |
| |
| |
| |
|_|
It looks fine!"""

goose = r"""
The goose habitat...
(.
(-.
<
<-
(<<
<<
(_<_<
Beautiful!"""

bat = r"""
The bat habitat...
    _.._
  .'    '.
 /   _   \
|  (   )  |
 \  `-'  /
  `------`
It's doing fine."""

rabbit = r"""
The rabbit habitat...
         /\
        /  \
       /    \
      /  /\  \
     /  /  \  \
    /  /    \  \
   /  /      \  \
  /  /        \  \
 /  /          \  \
/__/            \__\
It looks fine!"""

animals = [camel, lion, deer, goose, bat, rabbit]

while True:
    user_input = input("Please enter the number of the habitat you would like to view: > ")
    if user_input == "exit":
        print("See you later!")
        break

    habitat_num = int(user_input)
    print(animals[habitat_num])