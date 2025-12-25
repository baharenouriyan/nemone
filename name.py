       #از کاربر اسم بگیر و با حلقه فور هر حرف اسم رو تکی چاپ کن..اگه حرف کوچیک lowercase...اگه بزرگ بود uppercase
name =input("enter your name:")
for ch in name :
    if   ch.isupper() :
          print(ch,"isupper")
    elif ch.islower() :
          print(ch,"islower")