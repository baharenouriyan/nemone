
#اعداد یک  تا پنج رو بررسی کن ..اگه هم بر 3 و هم بر 5  بخش پذیر بود =fizzbuzz..اگر فقط بر 3 بخش پذیر بود =fizz... در غیر این صورت فقط عدد چاپ بشه

for i in range(1,51):
  if i %3==0 and i %5==0 :
       print("fizzbuzz")
  elif i %3==0 :
      print("fizz")
  elif i%5==0 :
        print("buzz")
  else :
        print(i)