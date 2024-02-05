# Dependencies: wmi, screeninfo
import requests
import random
from screeninfo import get_monitors
import wmi

class SystemInfo:

  def __init__(self, sd):
    self.sd = sd

  def monitorSize(self):
    for m in get_monitors():
      output = "Your monitor size is "+ str(m.width)+'x'+str(m.height) + " pixels or "+str(m.width_mm)+'x'+ str(m.height_mm) + "mm using a "+ str(m.name) + " connector."
      return output

  def systemSpecs(self):
    computer = wmi.WMI()
    os_info = computer.Win32_OperatingSystem()[0]
    os_version = ' '.join([os_info.Version, os_info.BuildNumber])
    os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    gpu_info = computer.Win32_VideoController()[0]
    proc_info = computer.Win32_Processor()[0]
    system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB
    output = "----------------------------------------" + "\n             System Specs:\n" + 'OS Name: {0}'.format(os_name) + 'v' + os_version
    output = output + "\nCPU: {0}".format(proc_info.Name) + '\nGraphics Card: {0}'.format(gpu_info.Name) + "\nRAM: {0} GB".format(round(system_ram,3)) + '\n"----------------------------------------"'
    return output


class InSpace:

  def __init__(self, sd):
    self.sd = sd

  def list(self):
    data = requests.get("http://api.open-notify.org/astros.json")
    data = data.json()
    self.sd.print("Here is a list of people in space right now: ")
    for people in range(len(data["people"])):
      self.sd.print(data["people"][people]["name"], "is on the", data["people"][people]["craft"])

class Games():

  def __init__(self, sd):
    self.sd = sd

  def coinflip(self):
    outcome = random.randint(0,1)
    if outcome == 0:
      outcome = 'Heads'
    else:
      outcome = 'Tails'
    return outcome

  def diceroll(self):
    outcome = random.randint(1,6)
    return outcome

def titlescreen():
  print(' ______  __  __  ______  ______ ______  ______  ______  ')
  print('/\  ___\/\ \_\ \/\  __ \/\__  _/\  == \/\  __ \/\__  _\ ')
  print('\ \ \___\ \  __ \ \  __ \/_/\ \\\\ \  __<\ \ \/\ \/_/\ \/ ')
  print(' \ \_____\ \_\ \_\ \_\ \_\ \ \_\\\\ \_____\ \_____\ \ \_\ ')
  print('  \/_____/\/_/\/_/\/_/\/_/  \/_/ \/_____/\/_____/  \/_/ ')
