# Party Calculator

bannerWidth = float(input("Please enter the banner width: "))
bannerLength = float(input("Please enter the banner length: "))
costPerSqIn = float(input("Please enter the cost per square inch: "))

#processing - calculate the total cost
bannerArea = bannerWidth * bannerLength
totalArea = bannerArea * costPerSqIn

#Display the total cost 

print("The total cost of the banner is: ", totalArea) 