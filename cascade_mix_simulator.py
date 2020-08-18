import sys
from container_factory import ContainerFactory

print("Please enter the following information to build your destination container")
destinationContainer = ContainerFactory().promptAndGetContainer()

while True: 
    print("Please enter the following information to build your source container that will be added to your destination container.")
    sourceContainer = ContainerFactory().promptAndGetContainer()
   
    if(destinationContainer.getCurrentPressure() > sourceContainer.getCurrentPressure()):
        print("The destination container must be at a lower pressure than the source container. No gas was added.")
    elif(destinationContainer.getCurrentPressure() == sourceContainer.getCurrentPressure()):
        print("Containers are at the same pressure. No gas was added.")
    else:
        destinationContainer.fillUntilEqualPressure(sourceContainer)
        print("Destination container now has " + str(round(destinationContainer.getCurrentPressure())) + " psi of " + str(round(destinationContainer.getFO2() * 100)) + "% nitrox.")

    print()
    if input("Add another container? [Y/n]: ") == 'n':
        print("Goodbye.")
        break
