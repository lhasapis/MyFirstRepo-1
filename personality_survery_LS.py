print ("What's your name?")
name = input().title()
if name == ("Lily"):
    print ("That's my name too!")
else:
    print ("Nice to meet you " + name + "!")

print ("What's your favorite sport?")
sport = input().title()
if sport == "Lacrosse":
    print ("That's my favorite sport, too!")
elif sport == "Dance":
    print ("I love to dance. What's your favorite style?")
    style = input().title()
    if style == ("Jazz"):
        print ("I love jazz too! I also like ballet and Modern.")
    elif style == ("Modern"):
        print ("I love modern too! Jazz and ballet are also my favorites.")
    elif style == ("Ballet"):
        print ("I like doing ballet too! modern and jazz are my two other favorites.")
    else:
        print (style +" looks fun! I do jazz, modern, and ballet.")
else:
    print (sport + " sounds fun! I play lacrosse and I dance.")
