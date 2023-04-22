class information:
    clasroom = "AI&DS"
    section = "I2"

# defining objects,objects inhertage the properties of the class
yash = information()
manoj = information()
# accesing the values
print(yash.clasroom)
print(yash.section)
print()
# changing the values
manoj.clasroom="INF"
manoj.section="BLAH"
print(manoj.clasroom)
print(manoj.section)
print()
# when we change the values of the object class dosent change
print(yash.clasroom)
print(yash.section)


