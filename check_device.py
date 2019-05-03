import speech_recognition as sr

import py
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
