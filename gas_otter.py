import subprocess

print('''
          .----.
         /     o\\
        |c  o   0).-.
        |      .-;(_/     .-.
         \    /  /)).---._|  `\   ,
         '.  '  /((       `'-./ _/|
           \  .'  )        .-.;`  /
            '.             |  `\-'
              '._        -'    /
        jgs      ``""--`------`

        *** WARNING AND DISCLAIMER ***
        THIS PROGRAM IS SHOULD BE USED FOR TRAINING AND EDUCATIONAL PURPOSES
        ONLY.
        Blending gasses is dangerous. Not only can you seriously injure or
        kill yourself while mixing the gasses, but improper blending can lead
        to serious injury or death of the diver breathing the gas.
        Do not rely on this program to generate correct or accurate results.
        Remember to ALWAYS analyze your gas before diving.

        Gas Otter v0.0.1 by Maxwell Wenger (GitHub @maxwenger)

''')

while True:
    print('''
        Please choose a mode:

        0) Quit Gas Otter

        1) Partial Pressure Nitrox Blender

        2) Cascade simulator - Give an existing container and add different
            mixes to it and see the pressure and mix after each addition.

        3) Cascade instructions - Give an existig container to mix in and
            containers you would like to add to the existing container,
            and get instructions to mix your desired blend.
    ''')

    try:
        selection = int(input("Selection (0-2): "))
    except  ValueError:
        print("Make a valid selection please.")
        continue
    
    if selection == 0:
        print("Goodbye!")
        break
    if selection == 1:
        exec(open("partial_pressure_mix_nitrox.py").read())
    elif selection == 2:
        exec(open("cascade_mix_simulator.py").read())
    else:
        print("Please make a valid selection.")
    
