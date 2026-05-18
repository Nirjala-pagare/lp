def medical_expert_system():

    print("================================================")
    print("         HOSPITAL EXPERT SYSTEM")
    print("================================================")

    name = input("Enter patient name: ")
    age = int(input("Enter age: "))

    print("\nAnswer symptoms with yes/no\n")

    fever = input("Do you have fever? : ").lower()
    cough = input("Do you have cough? : ").lower()
    headache = input("Do you have headache? : ").lower()
    body_pain = input("Do you have body pain? : ").lower()
    breathing = input("Do you have breathing difficulty? : ").lower()
    cold = input("Do you have cold/runny nose? : ").lower()
    stomach_pain = input("Do you have stomach pain? : ").lower()
    vomiting = input("Do you have vomiting? : ").lower()
    diarrhea = input("Do you have diarrhea? : ").lower()
    chest_pain = input("Do you have chest pain? : ").lower()
    fatigue = input("Do you feel weakness/fatigue? : ").lower()
    sore_throat = input("Do you have sore throat? : ").lower()

    print("\n================================================")
    print("              DIAGNOSIS REPORT")
    print("================================================")

    print("Patient Name :", name)
    print("Age          :", age)

    
    if fever == "yes" and cough == "yes" and breathing == "yes":
        print("\nPossible Disease : COVID-19")
        print("Advice :")
        print("- Isolate yourself")
        print("- Wear mask")
        print("- Consult doctor immediately")
        print("- Get RTPCR test")

    
    elif fever == "yes" and headache == "yes" and body_pain == "yes":
        print("\nPossible Disease : Malaria")
        print("Advice :")
        print("- Take blood test")
        print("- Drink fluids")
        print("- Consult physician")

    
    elif fever == "yes" and cold == "yes" and sore_throat == "yes":
        print("\nPossible Disease : Flu / Viral Infection")
        print("Advice :")
        print("- Take rest")
        print("- Drink warm water")
        print("- Avoid cold food")

   
    elif stomach_pain == "yes" and vomiting == "yes" and diarrhea == "yes":
        print("\nPossible Disease : Food Poisoning")
        print("Advice :")
        print("- Drink ORS")
        print("- Avoid outside food")
        print("- Consult doctor if condition worsens")

  
    elif chest_pain == "yes" and breathing == "yes":
        print("\nPossible Disease : Heart or Lung Problem")
        print("Advice :")
        print("- Seek emergency medical help")
        print("- Avoid physical activity")

    
    elif headache == "yes" and fatigue == "yes":
        print("\nPossible Disease : Stress / Migraine")
        print("Advice :")
        print("- Take proper sleep")
        print("- Reduce screen time")
        print("- Stay hydrated")

   
    elif cough == "yes" and fever == "yes":
        print("\nPossible Disease : Common Cold")
        print("Advice :")
        print("- Take rest")
        print("- Drink warm fluids")
        print("- Use steam inhalation")

 
    elif fever == "yes":
        print("\nPossible Disease : Mild Fever")
        print("Advice :")
        print("- Take rest")
        print("- Drink water")
        print("- Monitor temperature")

   
    elif body_pain == "yes":
        print("\nPossible Disease : Muscle Fatigue")
        print("Advice :")
        print("- Take proper rest")
        print("- Avoid heavy work")

    
    elif sore_throat == "yes":
        print("\nPossible Disease : Throat Infection")
        print("Advice :")
        print("- Gargle with warm salt water")
        print("- Avoid cold drinks")

    
    else:
        print("\nNo major illness detected.")
        print("Advice : Maintain healthy lifestyle and regular exercise.")

    print("\n================================================")
    print(" Thank You For Using Hospital Expert System ")
    print("================================================")


medical_expert_system()