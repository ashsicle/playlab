Cost-Neccessity-Trade-Off

#low income
if 0 < Cost < 3.0:
    if Necc > 5.0:
        high go
    else:
        go
elif 3.0 < Cost < 7.0:
    if (Necc - Cost) <0:
        no go 
    elif (Necc - Cost) > 2.0:
        go
    else:
        low go
elif Cost > 7.0: 
    no go
if Necc > 9.0:
    go
    
    
#high income
if Cost < 3.0:
    if Necc > 5.0:
        high go
    else:
        go
elif 3.0 < Cost < 7.0:
    if (Necc - Cost) < 0: #if Necc larger than Cost
        low go
    elif (Necc - Cost) > 2.0:
        high go
    else:
        go
elif Cost > 7.0:
    if (Necc - Cost) < 0:
        no go 
    elif (Necc - Cost) > 2.0:   
        
        high go
    else:
        low go
if Necc > 9.0:
    go


#visitor
if 0 < Necc < 3.0:
    high go
elif 3.0 < Necc < 7.0:
    if (necc < 5) and (cost < 5):
        high go
    elif (necc > 5) and (cost >5):
        low  go
    else:
        go
elif Necc > 7.0:
    low go
    
    
#global
if 0 < Cost < 3.0:
    low_income = high
    high_income = same
    visitor = same
    
elif 3.0 < Cost < 7.0:
    low_income = low
    high_income = high
    visitor = same
    
elif Cost > 7.0:
    low_income = no
    high_income = same
    visitor = same
    
if 0 < Necc < 3.0:
    low_income = low
    high_income = same
    visitor = high
    
elif 3.0 < Necc < 7.0:
    low_income = same
    high_income = same
    visitor = same
    
elif Necc > 7.0:            
    low_income = same
    high_income = same
    visitor = low
    
    
    
    
    
    
    
    
    
    
