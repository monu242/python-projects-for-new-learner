#system:-- 
#system wil ask you what's your name
#computer will your age
#age - 1 - 10 = computer will take you tony start videos
#age  10 - 15 = computer will take you to touch some grass buddy 
# age 15 - 20 get some skills dude these are some channels improve your skill..


print("welcome to this awesome place get some form of information here and improve in life if not then enjoy !")
print("-----------------------------x--------------------------------")
user_name = input("What is your name buddy  :  ")
print(f"OH! what a nice name your name is {user_name} .. and it sounds really amazing")

import webbrowser

# user_input what is your age


input_age = input("what is your age buddy :  ")
while True:
    if input_age.isdigit():
        input_age = int(input_age)
    if 1 <= input_age <= 5:
        print("enjoy friend you are small it enjoying time")
        url_1 = "https://youtube.com/@targetsiblingsgamerz?si=p692cmxcRTXsdUvv"
        webbrowser.open(url_1)
    elif 10 <= input_age <= 15:
        print("it's time to touch  some grass")
        url_2 = "https://media.istockphoto.com/id/1349781282/photo/human-palm-touching-lawn-grass-low-angle-view.jpg?s=612x612&w=0&k=20&c=SPV9QmWhfdk1D1QXNPzZaYbHnaO5CEZpUmRDoEJjTpw="
        webbrowser.open(url_2)