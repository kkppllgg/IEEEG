# This is our task file :D
# You pick a function to implement
# This is signal processing babyyyy
# The code below is about training a machine learning model to recognize hand movements using ERD/ERS patterns
# GOAL: Filter this database and apply ica, epoch it, compute its psd and  visualize it in skull map, 
# Specifically: An epoch for each hand movement, epochs for idle, a function that computes their psd, train the model
# SECOND GOAL: Repeat the above for alpha waves
# DONT FORGET SCA
#INITIALIZATION (GLOBAL)
from mne.datasets import eegbci
from mne.io import concatenate_raws, read_raw_edf
from mne.channels import make_standard_montage 
import matplotlib.pyplot as plt
from mne import events_from_annotations, find_events
#Those runs concern motor imagery of left and right hand movements
raw_fnames = eegbci.load_data(subject = 1,runs = [4,8,12])
raws = [read_raw_edf(f,preload=True) for f in raw_fnames]
raw = concatenate_raws(raws)


#Dictionary made by CHAT-GPT
channel_mapping = {
    'Fc5.': 'FC5', 'Fc3.': 'FC3', 'Fc1.': 'FC1', 'Fcz.': 'FCz', 'Fc2.': 'FC2', 'Fc4.': 'FC4', 'Fc6.': 'FC6',
    'C5..': 'C5', 'C3..': 'C3', 'C1..': 'C1', 'Cz..': 'Cz', 'C2..': 'C2', 'C4..': 'C4', 'C6..': 'C6',
    'Cp5.': 'CP5', 'Cp3.': 'CP3', 'Cp1.': 'CP1', 'Cpz.': 'CPz', 'Cp2.': 'CP2', 'Cp4.': 'CP4', 'Cp6.': 'CP6',
    'Fp1.': 'Fp1', 'Fpz.': 'Fpz', 'Fp2.': 'Fp2',
    'Af7.': 'AF7', 'Af3.': 'AF3', 'Afz.': 'AFz', 'Af4.': 'AF4', 'Af8.': 'AF8',
    'F7..': 'F7', 'F5..': 'F5', 'F3..': 'F3', 'F1..': 'F1', 'Fz..': 'Fz', 'F2..': 'F2', 'F4..': 'F4', 'F6..': 'F6', 'F8..': 'F8',
    'Ft7.': 'FT7', 'Ft8.': 'FT8', 'T7..': 'T7', 'T8..': 'T8', 'T9..': 'T9', 'T10.': 'T10',
    'Tp7.': 'TP7', 'Tp8.': 'TP8',
    'P7..': 'P7', 'P5..': 'P5', 'P3..': 'P3', 'P1..': 'P1', 'Pz..': 'Pz', 'P2..': 'P2', 'P4..': 'P4', 'P6..': 'P6', 'P8..': 'P8',
    'Po7.': 'PO7', 'Po3.': 'PO3', 'Poz.': 'POz', 'Po4.': 'PO4', 'Po8.': 'PO8',
    'O1..': 'O1', 'Oz..': 'Oz', 'O2..': 'O2', 'Iz..': 'Iz'
}

raw.rename_channels(channel_mapping)
montage = make_standard_montage('standard_1020')
raw.set_montage(montage)

# A WARMUP: GETTING TO KNOW OUR DATA
def info_warmup(raw):
    #Print raw info
    #Print sampling frequency, channel names, channel types
    #Print raw annotations and its duratinons, onsets and types
    
    return 

def visual_warmup(raw):
    #Set raw_eeg to be a raw file with only eeg channels
    #Visualize the electrodes in topomap and in 3d
    #Plot a small time frame of the raw signal of all channels and then just 1 channel
    return

def event_warmup(raw):
    #Create an events array(Hint: From annotations) and return it with its dictionary
    #Plot the events and try to understand what each event represents(right-left movement, idle etc)
    #Hint: look up data documentation (eegbci mne)
    #Plot events and raw data
    return events,event_dict

def preprocessing(raw):
    #Select only channels C3, C4, Cz
    #High-pass channels with cutoff frequency 1Hz , Low pass 40Hz
    #Notch filted data with central frequency 50 or 60 Hz depending on the line noise (see psd to understand which one)
    return raw_filtered

def segment_data(raw_filtered):
    #Segment right/left hand movements into epochs. Choose the correct tmax and tmin in order to capture the movement
    #Visualize image, joint, topomap
    #Segment idle state into epochs
    #Visualize image, joint, topomap
    #Perform psd and visualize for both. What are the differences?
    #IF POSSIBLE visualize topomap of mu rhythm (8-12Hz)
    return epochs
