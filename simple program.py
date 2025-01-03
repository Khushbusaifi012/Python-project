    
print("\n**************** Numericals to words ***********************\n\n")
n = int(input("Enter a number you want to convert into words = Minimum =0 Maximum =9900009999999 \n\nThis program can help you within this limit only: "))

# Defining scales and word lists
highers = ["Lakh crores", "Lakh crore", "Hundred crores", "Hundred Crore", "crores", "crore", "Lakhs", "Lakh", "Thousands", "Thousand", "Hundred"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

# Splitting the number into parts
lakhcrores = (n // 100000000000) % 100
hundredcrores = (n // 1000000000) % 100
crore = (n // 10000000) % 100
lakh = (n // 100000) % 100
thousand = (n // 1000) % 100
hundred = (n // 100) % 10
rest = n % 100

finalword = ""  # To store the result word

# Logic to convert each part
if (lakhcrores > 0):
    if (lakhcrores < 20):
        finalword += " " + units[lakhcrores] + " " + highers[0]
    else:
        finalword += " " + tens[lakhcrores // 10] + " " + units[lakhcrores % 10] + " " + highers[0]

if (hundredcrores > 0):
    if (hundredcrores < 20):
        finalword += " " + units[hundredcrores] + " " + highers[2]
    else:
        finalword += " " + tens[hundredcrores // 10] + " " + units[hundredcrores % 10] + " " + highers[2]

if (crore > 0):
    if (crore < 20):
        finalword += " " + units[crore] + " " + highers[4]
    else:
        finalword += " " + tens[crore // 10] + " " + units[crore % 10] + " " + highers[4]

if (lakh > 0):
    if (lakh < 20):
        finalword += " " + units[lakh] + " " + highers[6]
    else:
        finalword += " " + tens[lakh // 10] + " " + units[lakh % 10] + " " + highers[6]

if (thousand > 0):
    if (thousand < 20):
        finalword += " " + units[thousand] + " " + highers[8]
    else:
        finalword += " " + tens[thousand // 10] + " " + units[thousand % 10] + " " + highers[8]

if (hundred > 0):
    finalword += " " + units[hundred] + " " + highers[10]

if (rest > 0):
    if (rest < 20):
        finalword += " " + units[rest]
    else:
        finalword += " " + tens[rest // 10] + " " + units[rest % 10]

if n == 0:
    finalword = "Zero"

# Output the result
print("\n\nHere is the word conversion of the number you entered:", finalword.strip(), "\n")
print("\n**************************\n")






