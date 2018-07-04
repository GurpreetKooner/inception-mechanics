try:
    p=35376788
    b=234
    p=b/0
    f= open("ab.txt")
    for line in f:
        print(line)
except Exception as e:
    print("Anything at all",e)
# except (FileNotFoundError,ZeroDivisionError):
#     print("Error!!!!!!!!!!!!!!!!!!!")
#  except ZeroDivisionError:
#      print("divisio by zero not allowed")
