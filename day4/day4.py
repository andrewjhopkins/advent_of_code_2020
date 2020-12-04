f = open("input.txt", "r")
input = []

def passportStringToDict(passport): 
    dictionary = {}
    passportSplit = passport.split(" ")

    for entry in passportSplit: 
        entrySplit = entry.split(":")
        dictionary[entrySplit[0]] = entrySplit[1]

    return dictionary


passport = ""
for x in f: 
    if x == "\n": 
        passportEntry = passportStringToDict(passport.strip())
        input.append(passportEntry)
        passport = ""
    else: 
        passport = passport + " " + x.strip()

passportEntry = passportStringToDict(passport.strip())
input.append(passportEntry)

f.close()

def isValidPassport(passport): 
    requiredKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in requiredKeys: 
        if key not in passport: 
            return False
        valid = validateFields(key, passport[key])
        if not valid: 
            return False
    return True

def getValidPassports(input): 
    successCount = 0
    for passport in input: 
        if isValidPassport(passport): 
            successCount += 1
    return successCount

def validateFields(field, value): 
    if field == "byr": 
        valueInt = int(value)
        if valueInt >= 1920 and valueInt <= 2002: 
            return True
        return False

    elif field == "iyr": 
        valueInt = int(value)
        if valueInt >= 2010 and valueInt <= 2020: 
            return True
        return False

    elif field == "eyr": 
        valueInt = int(value)
        if valueInt >= 2020 and valueInt <= 2030: 
            return True
        return False

    elif field == "hgt": 
        measurementType = value[-2:]
        measurementChar = value[:-2]
        if not measurementChar.isdigit(): 
            return False
        measurement = int(measurementChar)
        if measurementType == "in": 
            if measurement >= 59 and measurement <= 76: 
                return True
            return False
        if measurementType == "cm": 
            if measurement >= 150 and measurement <= 193: 
                return True
            return False
        return False
        
    elif field == "hcl": 
        if value[0] == "#": 
            for i in range(1, len(value)): 
                charValue = ord(value[i])
                if (charValue >= 48 and charValue <= 57) or (charValue >= 97 and charValue <= 102): 
                    continue
                else: 
                    return False
            return True
        return False


    elif field == "ecl": 
        validColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        validColorsSet = set(validColors)
        if value in validColorsSet: 
            return True
        return False

    elif field == "pid": 
        if len(value) == 9: 
            return True
        return False

            
print(getValidPassports(input))

