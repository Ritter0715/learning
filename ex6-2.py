import easygui
names = easygui.enterbox("Hi what's u name ?")
romeNumber = easygui.enterbox("And what's u room number ?")
street = easygui.enterbox("And which street ?")
city = easygui.enterbox("which city ?")
postNumber = easygui.enterbox("Last question the postnumber is ?")

easygui.msgbox("This is u massage: \n" + names + romeNumber + 
street + city + postNumber)  


#easygui.msgbox(""" %s\n ,%s\n ,%s\n ,%s\n ,%s\n """) % (names ,
#romeNumber ,street ,city ,postNumber)







"""
end = easygui.enterbox(" \n")
address = names + end + romeNumber + end  +  street + end   +, 
city + end  + postNumber 

easygui.msgbox(address)
"""
"""
12345

1
2
3
4
5"""