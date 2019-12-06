#Welcome Greeting

Welcome=str(print("We will be asking you a series of questions in order to best advise you on the severity of your eye problems"))
Rules=str(print("When answering yes or no questions, only capital Y or N is acceptable"))

#inputs
sName=str(input("What is your name?"))
sEye=str(input("In what eye(s) are you having a problem?"))
sFlashes=str(input("Are you having any flashes or floaters?"))





if  sFlashes=="Y":
    sPva=str(input("Is part or all of your vision missing in?"))
elif sFlashes=="N":
    sVision=str(input("Is your eye problem causing blurred vision?"))
if sFlashes=="Y" and sPva=="Y":
    print(sName,"You may have a retinal detachment and should seek medical attention immediately")
elif sFlashes=="Y" and sPva=="N":
    print(sname,"You may have a Posterior Vitreous detachment. This is a normal age related problem and you should see an ophthalmologist within a week")
elif sVision=="Y" and sFlashes=="N":
    sPain=str(input("Is your eye in pain?"))
elif sVision=="N" or sVision=="Y":
    sPain=str(input("Is your eye in pain?"))
    if sPain=="Y" or sPain=="N":
        sDischarge=str(input("Is your eye discharging any substance?"))
        sTearing=str(input("Is your eye tearing?"))
        if sDischarge=="Y" or sTearing=="Y":
            print(sName,"These are common symptoms of dry eye. try using artificial tears that you can get over the counter for a few days before considering making an appointment.")
        elif sPain=="N" or sDischarge=="N":
            sRedness=str(input("Is your eye red?"))
            if sRedness=="Y":
                sCough=str(input("Have you been coughing recently?"))
                sHit=str(input("Did you have anything hit your face recently?"))
                if sCough=="Y" or sHit=="Y":
                    print(sName,"You may have a subconjunctival hemhorrage and there is nothing to worry about. You popped some blood vessels. Even though it may look bad your body will absorb the blood and it will just reabsorb the blood into the eye.")
                else:
                    print(sName,"We dont seem to be able to find anything  that we can diganose. Please call an ophthalmologist to follow up with your problem")
            elif sRedness=="N":
                print(sName,"We dont seem to be able to find anything  that we can diganose. Please call an ophthalmologist to follow up with your problem")

Thankyou=str(print(sName,"Thank you for using our automated triage caller"))



    



    

    
    
    


 



  


    
    







    



