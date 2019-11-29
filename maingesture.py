from __future__ import print_function
from pygarl.base import CallbackManager
from pygarl.classifiers import SVMClassifier
from pygarl.mocks import VerboseMiddleware
from pygarl.data_readers import SerialDataReader
from pygarl.predictors import ClassifierPredictor
from pygarl.sample_managers import DiscreteSampleManager
import winsound
MODEL_PATH="C://modell.svm"
PORT="COM3"

 
    #Resets the output file
output_file = open("out.txt","w")
output_file.write("Start-Typing >>>")
output_file.close()
def receive_character(number):
    
    writedata(number)

def writedata(number):#we have to define to write the data
    
    
    
    
     #Add the char to the sentence
    

    #Prints the last char and the sentence
    print (number)
    #Saves the output to a file
    output_file = open("out.txt","a")
    if(number=="32"):
        number = " "
    output_file.write(number)
    winsound.PlaySound("space.wav", winsound.SND_ASYNC)
    output_file.close()

    if(number=="+"):
        output_file = open("out.txt","w")
        output_file.write("Start-Typing >>>")
        output_file.close()

    if(number=="E"):
        output_file = open("out.txt","w")
        winsound.PlaySound("email.wav", winsound.SND_ASYNC)
        output_file.write("Email address is:>> sahildhruv1@gmail.com")
        output_file.close()
    if (number == "M"): #Delete the last character
	output_file = open("out.txt","w")
	output_file.write(number)
	output_file.close()
        
    if (number=="d"):
        winsound.PlaySound("d.wav", winsound.SND_ASYNC)
    if (number=="h"):
        winsound.PlaySound("h.wav", winsound.SND_ASYNC)
    if (number=="r"):
        winsound.PlaySound("r.wav", winsound.SND_ASYNC)
    if (number=="u"):
        winsound.PlaySound("u.wav", winsound.SND_ASYNC)
    if (number=="v"):
        winsound.PlaySound("v.wav", winsound.SND_ASYNC)
    if (number=="1"):
        winsound.PlaySound("one.wav", winsound.SND_ASYNC)    
    if (number=="3"):
        winsound.PlaySound("three.wav", winsound.SND_ASYNC)
    if (number=="+"):
        winsound.PlaySound("ty.wav", winsound.SND_ASYNC)
   
       
  
        
      





# Create the SerialDataReader
sdr = SerialDataReader(PORT, expected_axis=6, verbose=False)

# Create the SampleManager
manager = DiscreteSampleManager()

# Attach the manager
sdr.attach_manager(manager)

# Create a classifier
classifier = SVMClassifier(model_path=MODEL_PATH)

# Load the model
classifier.load()

# Print classifier info
classifier.print_info()

# Create a ClassifierPredictor
predictor = ClassifierPredictor(classifier)

# Attach the classifier predictor
manager.attach_receiver(predictor)

# Create a CallbackManager
callback_mg = CallbackManager(verbose=True)

# Attach the callback manager
predictor.attach_callback_manager(callback_mg)

# Bind all the numbers
for c in ["d","32", "h", "r","u","v","1","3","+","S","M","E"]:
    callback_mg.attach_callback(c, receive_character)

# Open the serial connection
sdr.open()
print("Opened!")

# Start the main loop
sdr.mainloop()
