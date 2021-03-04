#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.dom.minidom

def tell(seq):
    '''Return a motion event.  An event consists of actions made by at least
    one device.  Refer to `device` function to understand the use case.  
    '''
    xml_obj  = '''<SequenceElements xsi:type="Event" Name="Event">'''
    xml_obj += '''<Description />'''
    xml_obj += '''<DeviceSequences>'''
    xml_obj += '''{SEQ}'''.format( SEQ = seq )
    xml_obj += '''</DeviceSequences>'''
    xml_obj += '''</SequenceElements>'''

    return xml_obj




def device(dev, action):
    '''Return at least one action made by a single device.  The supported
       actions are `wait`, `pulse`, `move_by`, and `move_to`.  

       Each action is a Python function.  Refer to the function to understand 
       the use case.  
    '''
    xml_obj  = '''<Device DeviceName="{DEV}">'''.format( DEV = dev )
    xml_obj += '''<DeviceActions>'''      
    xml_obj += '''{ACTION}'''.format( ACTION = action )
    xml_obj += '''</DeviceActions>'''
    xml_obj += '''</Device>'''

    return xml_obj




def wait(sec):
    '''Return a wait action according to the duration supplied by user.  The 
       unit is second.  
    '''
    sec = int(sec * 1000)   # ...Kinesis only recognizes integer for millisecond
    xml_obj  = '''<Action FunctionName="Wait">'''
    xml_obj += '''<Parameters>'''
    xml_obj += '''<NameValuePairOfObject Name="Time">'''
    xml_obj += '''<Value xsi:type="xsd:int">{SEC}</Value>'''.format( SEC = sec )
    xml_obj += '''</NameValuePairOfObject>'''
    xml_obj += '''</Parameters>'''
    xml_obj += '''</Action>'''

    return xml_obj




def pulse(port, on):
    '''Return a pulse action.  A pulse action sends out a trigger signal from
       KST101 motor.  Signal is sent out through one of the two ports built in
       a KST motor.  A trigger signal have two states: "on" and "off".  

       A user should specify which port to send a signal.  On each KST101
       motor, there are two built-in ports, numbered as "trig 1" and "trig 2".
       If `port` is "1", it represents "trig 1".  If `port` is "2", it
       represents "trig 2".  

       A user should also specify which state the signal is.  If `on` is 1, it
       means an "on" signal.  Otherwise, when `on` is 0, it means an "off"
       signal.  
    '''
    xml_obj  = '''<Action FunctionName="DigitalOutput">'''
    xml_obj += '''<Parameters>'''
    xml_obj += '''<NameValuePairOfObject Name="OutputPort">'''
    xml_obj += '''<Value xsi:type="xsd:int">{PORT}</Value>'''.format( PORT = port )
    xml_obj += '''</NameValuePairOfObject>'''
    xml_obj += '''<NameValuePairOfObject Name="OutputPortState">'''
    xml_obj += '''<Value xsi:type="xsd:int">{ON}</Value>'''.format( ON = on )
    xml_obj += '''</NameValuePairOfObject>'''
    xml_obj += '''</Parameters>'''
    xml_obj += '''</Action>'''

    return xml_obj




def move_by(disp):
    ''' Define a relative move in forward (dirct = 1) or backward (dirct = 2)
        direction.  
    '''
    dirct = 1 if disp > 0 else 2
    xml_obj  = '''<Action FunctionName="MoveRelative">'''
    xml_obj += '''<Parameters>'''
    xml_obj += '''<NameValuePairOfObject Name="Step">'''
    xml_obj += '''<Value xsi:type="xsd:decimal">{DISP}</Value>'''.format( DISP = abs(disp) )
    xml_obj += '''</NameValuePairOfObject>'''
    xml_obj += '''<NameValuePairOfObject Name="Direction">'''
    xml_obj += '''<Value xsi:type="xsd:int">{DIRCT}</Value>'''.format( DIRCT = dirct )
    xml_obj += '''</NameValuePairOfObject>'''
    xml_obj += '''</Parameters>'''
    xml_obj += '''</Action>'''

    return xml_obj




def move_by_at(disp, v, a):
    ''' Define a relative move in forward (dirct = 1) or backward (dirct = 2)
        direction.  
    '''
    dirct = 1 if disp > 0 else 2
    xml_obj  = '''<Action FunctionName="MoveRelativeAt">'''
    xml_obj += '''<Parameters>'''
    xml_obj += '''<NameValuePairOfObject Name="MaxVelocity">'''
    xml_obj += '''<Value xsi:type="xsd:decimal">{V}</Value>'''.format( V = v )
    xml_obj += '''</NameValuePairOfObject>'''
    xml_obj += '''<NameValuePairOfObject Name="Acceleration">'''
    xml_obj += '''<Value xsi:type="xsd:decimal">{A}</Value>'''.format( A = a )
    xml_obj += '''</NameValuePairOfObject>'''
    xml_obj += '''<NameValuePairOfObject Name="Step">'''
    xml_obj += '''<Value xsi:type="xsd:decimal">{DISP}</Value>'''.format( DISP = abs(disp) )
    xml_obj += '''</NameValuePairOfObject>'''
    xml_obj += '''<NameValuePairOfObject Name="Direction">'''
    xml_obj += '''<Value xsi:type="xsd:int">{DIRCT}</Value>'''.format( DIRCT = dirct )
    xml_obj += '''</NameValuePairOfObject>'''
    xml_obj += '''<NameValuePairOfObject Name="RestoreParams">'''
    xml_obj += '''<Value xsi:type="xsd:boolean">true</Value>'''
    xml_obj += '''</NameValuePairOfObject>'''
    xml_obj += '''</Parameters>'''
    xml_obj += '''</Action>'''

    return xml_obj




def move_to(position):
    xml_obj  = '''<Action FunctionName="MoveTo">'''
    xml_obj += '''<Parameters>'''
    xml_obj += '''<NameValuePairOfObject Name="MoveTo">'''
    xml_obj += '''<Value xsi:type="xsd:decimal">{POS}</Value>'''.format( POS = position )
    xml_obj += '''</NameValuePairOfObject>'''
    xml_obj += '''</Parameters>'''
    xml_obj += '''</Action>'''

    return xml_obj




def repeat(name, tag, count):
    xml_obj  = '''<SequenceElements xsi:type="Repeat" Name="{NAME}">'''.format( NAME = name )
    xml_obj += '''<Description />'''
    xml_obj += '''<NameTag>{TAG}</NameTag>'''.format( TAG = tag )
    xml_obj += '''<RepeatCount>{COUNT}</RepeatCount>'''.format( COUNT = count )
    xml_obj += '''</SequenceElements>'''

    return xml_obj




def goto(tag):
    xml_obj  = '''<SequenceElements xsi:type="NameTag" Name="Name Tag">'''
    xml_obj += '''<Description />'''
    xml_obj += '''<NameTag>{TAG}</NameTag>'''.format( TAG = tag )
    xml_obj += '''</SequenceElements>'''

    return xml_obj




def add_device(params):
    alias, device_name, device_prefix, serial_no, actuator = params
    xml_obj  = '''<DeviceDefinition DeviceAlias="{ALIAS}" RestoreParameters="true">'''.format( ALIAS = alias )
    xml_obj += '''<DeviceName>{S}</DeviceName>'''.format( S = device_name )
    xml_obj += '''<DevicePrefix>{S}</DevicePrefix>'''.format( S = device_prefix )
    xml_obj += '''<SerialNo>{SN}</SerialNo>'''.format( SN = serial_no )
    xml_obj += '''<Actuator>{S}</Actuator>'''.format( S = actuator )
    xml_obj += '''</DeviceDefinition>'''

    return xml_obj




def init_device(devs):
    '''Return an initialization statement according to user-supplied device
       designations.  

       The input `devs` is a dictionary with key being the serial number and 
       value being the alias of the device.  

       For example, 
       ```
       ~~ devs = {'26001245': 'Device001', '26001240': 'Device002'} ~~
       devs = [ "Device001", "Benchtop Brushless Motor Controller", "73", "73867454-1", "MLS203 X Axis" ]
       ```

       Serial number is a unique identifier found on any motor made by
       Thorlabs, Inc.  
    '''
    header  = '''<?xml version="1.0"?>'''
    header += '''<Sequence xmlns:xsd="http://www.w3.org/2001/XMLSchema" '''
    header += '''xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" Version="3">'''
    header += '''<Devices>'''

    for dev in devs:
        header += add_device(dev)
    
    header += '''</Devices>'''
    header += '''<SequenceEventCollection>'''

    return header




def end_motion(path):
    end  = '''</SequenceEventCollection>'''
    end += '''<RepeatCount>1</RepeatCount>'''
    end += '''<RepeatContinuously>false</RepeatContinuously>'''
    end += '''<RepeatRun>false</RepeatRun>'''
    end += '''<SequenceLogPath>{PATH}</SequenceLogPath>'''.format( PATH = path )
    end += '''</Sequence>'''

    return end




def pretty(xml_in):
    '''Return a pretty looking xml file.  
       Caveat: the xml input has to be a complete xml string.  
    '''
    xml_obj    = xml.dom.minidom.parseString(xml_in)
    xml_pretty = xml_obj.toprettyxml()

    return xml_pretty
