# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_epanet2', [dirname(__file__)])
        except ImportError:
            import _epanet2
            return _epanet2
        if fp is not None:
            try:
                _mod = imp.load_module('_epanet2', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _epanet2 = swig_import_helper()
    del swig_import_helper
else:
    import _epanet2
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


EN_ELEVATION = _epanet2.EN_ELEVATION
EN_BASEDEMAND = _epanet2.EN_BASEDEMAND
EN_PATTERN = _epanet2.EN_PATTERN
EN_EMITTER = _epanet2.EN_EMITTER
EN_INITQUAL = _epanet2.EN_INITQUAL
EN_SOURCEQUAL = _epanet2.EN_SOURCEQUAL
EN_SOURCEPAT = _epanet2.EN_SOURCEPAT
EN_SOURCETYPE = _epanet2.EN_SOURCETYPE
EN_TANKLEVEL = _epanet2.EN_TANKLEVEL
EN_DEMAND = _epanet2.EN_DEMAND
EN_HEAD = _epanet2.EN_HEAD
EN_PRESSURE = _epanet2.EN_PRESSURE
EN_QUALITY = _epanet2.EN_QUALITY
EN_SOURCEMASS = _epanet2.EN_SOURCEMASS
EN_INITVOLUME = _epanet2.EN_INITVOLUME
EN_MIXMODEL = _epanet2.EN_MIXMODEL
EN_MIXZONEVOL = _epanet2.EN_MIXZONEVOL
EN_TANKDIAM = _epanet2.EN_TANKDIAM
EN_MINVOLUME = _epanet2.EN_MINVOLUME
EN_VOLCURVE = _epanet2.EN_VOLCURVE
EN_MINLEVEL = _epanet2.EN_MINLEVEL
EN_MAXLEVEL = _epanet2.EN_MAXLEVEL
EN_MIXFRACTION = _epanet2.EN_MIXFRACTION
EN_TANK_KBULK = _epanet2.EN_TANK_KBULK
EN_DIAMETER = _epanet2.EN_DIAMETER
EN_LENGTH = _epanet2.EN_LENGTH
EN_ROUGHNESS = _epanet2.EN_ROUGHNESS
EN_MINORLOSS = _epanet2.EN_MINORLOSS
EN_INITSTATUS = _epanet2.EN_INITSTATUS
EN_INITSETTING = _epanet2.EN_INITSETTING
EN_KBULK = _epanet2.EN_KBULK
EN_KWALL = _epanet2.EN_KWALL
EN_FLOW = _epanet2.EN_FLOW
EN_VELOCITY = _epanet2.EN_VELOCITY
EN_HEADLOSS = _epanet2.EN_HEADLOSS
EN_STATUS = _epanet2.EN_STATUS
EN_SETTING = _epanet2.EN_SETTING
EN_ENERGY = _epanet2.EN_ENERGY
EN_DURATION = _epanet2.EN_DURATION
EN_HYDSTEP = _epanet2.EN_HYDSTEP
EN_QUALSTEP = _epanet2.EN_QUALSTEP
EN_PATTERNSTEP = _epanet2.EN_PATTERNSTEP
EN_PATTERNSTART = _epanet2.EN_PATTERNSTART
EN_REPORTSTEP = _epanet2.EN_REPORTSTEP
EN_REPORTSTART = _epanet2.EN_REPORTSTART
EN_RULESTEP = _epanet2.EN_RULESTEP
EN_STATISTIC = _epanet2.EN_STATISTIC
EN_PERIODS = _epanet2.EN_PERIODS
EN_NODECOUNT = _epanet2.EN_NODECOUNT
EN_TANKCOUNT = _epanet2.EN_TANKCOUNT
EN_LINKCOUNT = _epanet2.EN_LINKCOUNT
EN_PATCOUNT = _epanet2.EN_PATCOUNT
EN_CURVECOUNT = _epanet2.EN_CURVECOUNT
EN_CONTROLCOUNT = _epanet2.EN_CONTROLCOUNT
EN_JUNCTION = _epanet2.EN_JUNCTION
EN_RESERVOIR = _epanet2.EN_RESERVOIR
EN_TANK = _epanet2.EN_TANK
EN_CVPIPE = _epanet2.EN_CVPIPE
EN_PIPE = _epanet2.EN_PIPE
EN_PUMP = _epanet2.EN_PUMP
EN_PRV = _epanet2.EN_PRV
EN_PSV = _epanet2.EN_PSV
EN_PBV = _epanet2.EN_PBV
EN_FCV = _epanet2.EN_FCV
EN_TCV = _epanet2.EN_TCV
EN_GPV = _epanet2.EN_GPV
EN_NONE = _epanet2.EN_NONE
EN_CHEM = _epanet2.EN_CHEM
EN_AGE = _epanet2.EN_AGE
EN_TRACE = _epanet2.EN_TRACE
EN_CONCEN = _epanet2.EN_CONCEN
EN_MASS = _epanet2.EN_MASS
EN_SETPOINT = _epanet2.EN_SETPOINT
EN_FLOWPACED = _epanet2.EN_FLOWPACED
EN_CFS = _epanet2.EN_CFS
EN_GPM = _epanet2.EN_GPM
EN_MGD = _epanet2.EN_MGD
EN_IMGD = _epanet2.EN_IMGD
EN_AFD = _epanet2.EN_AFD
EN_LPS = _epanet2.EN_LPS
EN_LPM = _epanet2.EN_LPM
EN_MLD = _epanet2.EN_MLD
EN_CMH = _epanet2.EN_CMH
EN_CMD = _epanet2.EN_CMD
EN_TRIALS = _epanet2.EN_TRIALS
EN_ACCURACY = _epanet2.EN_ACCURACY
EN_TOLERANCE = _epanet2.EN_TOLERANCE
EN_EMITEXPON = _epanet2.EN_EMITEXPON
EN_DEMANDMULT = _epanet2.EN_DEMANDMULT
EN_LOWLEVEL = _epanet2.EN_LOWLEVEL
EN_HILEVEL = _epanet2.EN_HILEVEL
EN_TIMER = _epanet2.EN_TIMER
EN_TIMEOFDAY = _epanet2.EN_TIMEOFDAY
EN_AVERAGE = _epanet2.EN_AVERAGE
EN_MINIMUM = _epanet2.EN_MINIMUM
EN_MAXIMUM = _epanet2.EN_MAXIMUM
EN_RANGE = _epanet2.EN_RANGE
EN_MIX1 = _epanet2.EN_MIX1
EN_MIX2 = _epanet2.EN_MIX2
EN_FIFO = _epanet2.EN_FIFO
EN_LIFO = _epanet2.EN_LIFO
EN_NOSAVE = _epanet2.EN_NOSAVE
EN_SAVE = _epanet2.EN_SAVE
EN_INITFLOW = _epanet2.EN_INITFLOW

def ENepanet(*args):
  return _epanet2.ENepanet(*args)
ENepanet = _epanet2.ENepanet

def ENopen(*args):
  return _epanet2.ENopen(*args)
ENopen = _epanet2.ENopen

def ENsaveinpfile(*args):
  return _epanet2.ENsaveinpfile(*args)
ENsaveinpfile = _epanet2.ENsaveinpfile

def ENclose():
  return _epanet2.ENclose()
ENclose = _epanet2.ENclose

def ENsolveH():
  return _epanet2.ENsolveH()
ENsolveH = _epanet2.ENsolveH

def ENsaveH():
  return _epanet2.ENsaveH()
ENsaveH = _epanet2.ENsaveH

def ENopenH():
  return _epanet2.ENopenH()
ENopenH = _epanet2.ENopenH

def ENinitH(*args):
  return _epanet2.ENinitH(*args)
ENinitH = _epanet2.ENinitH

def ENrunH():
  return _epanet2.ENrunH()
ENrunH = _epanet2.ENrunH

def ENnextH():
  return _epanet2.ENnextH()
ENnextH = _epanet2.ENnextH

def ENcloseH():
  return _epanet2.ENcloseH()
ENcloseH = _epanet2.ENcloseH

def ENsavehydfile(*args):
  return _epanet2.ENsavehydfile(*args)
ENsavehydfile = _epanet2.ENsavehydfile

def ENusehydfile(*args):
  return _epanet2.ENusehydfile(*args)
ENusehydfile = _epanet2.ENusehydfile

def ENsolveQ():
  return _epanet2.ENsolveQ()
ENsolveQ = _epanet2.ENsolveQ

def ENopenQ():
  return _epanet2.ENopenQ()
ENopenQ = _epanet2.ENopenQ

def ENinitQ(*args):
  return _epanet2.ENinitQ(*args)
ENinitQ = _epanet2.ENinitQ

def ENrunQ():
  return _epanet2.ENrunQ()
ENrunQ = _epanet2.ENrunQ

def ENnextQ():
  return _epanet2.ENnextQ()
ENnextQ = _epanet2.ENnextQ

def ENstepQ():
  return _epanet2.ENstepQ()
ENstepQ = _epanet2.ENstepQ

def ENcloseQ():
  return _epanet2.ENcloseQ()
ENcloseQ = _epanet2.ENcloseQ

def ENwriteline(*args):
  return _epanet2.ENwriteline(*args)
ENwriteline = _epanet2.ENwriteline

def ENreport():
  return _epanet2.ENreport()
ENreport = _epanet2.ENreport

def ENresetreport():
  return _epanet2.ENresetreport()
ENresetreport = _epanet2.ENresetreport

def ENsetreport(*args):
  return _epanet2.ENsetreport(*args)
ENsetreport = _epanet2.ENsetreport

def ENgetcontrol(*args):
  return _epanet2.ENgetcontrol(*args)
ENgetcontrol = _epanet2.ENgetcontrol

def ENgetcount(*args):
  return _epanet2.ENgetcount(*args)
ENgetcount = _epanet2.ENgetcount

def ENgetoption(*args):
  return _epanet2.ENgetoption(*args)
ENgetoption = _epanet2.ENgetoption

def ENgettimeparam(*args):
  return _epanet2.ENgettimeparam(*args)
ENgettimeparam = _epanet2.ENgettimeparam

def ENgetflowunits():
  return _epanet2.ENgetflowunits()
ENgetflowunits = _epanet2.ENgetflowunits

def ENgetpatternindex(*args):
  return _epanet2.ENgetpatternindex(*args)
ENgetpatternindex = _epanet2.ENgetpatternindex

def ENgetpatternid(*args):
  return _epanet2.ENgetpatternid(*args)
ENgetpatternid = _epanet2.ENgetpatternid

def ENgetpatternlen(*args):
  return _epanet2.ENgetpatternlen(*args)
ENgetpatternlen = _epanet2.ENgetpatternlen

def ENgetpatternvalue(*args):
  return _epanet2.ENgetpatternvalue(*args)
ENgetpatternvalue = _epanet2.ENgetpatternvalue

def ENgetqualtype(*args):
  return _epanet2.ENgetqualtype(*args)
ENgetqualtype = _epanet2.ENgetqualtype

def ENgeterror(*args):
  return _epanet2.ENgeterror(*args)
ENgeterror = _epanet2.ENgeterror

def ENgetnodeindex(*args):
  return _epanet2.ENgetnodeindex(*args)
ENgetnodeindex = _epanet2.ENgetnodeindex

def ENgetnodeid(*args):
  return _epanet2.ENgetnodeid(*args)
ENgetnodeid = _epanet2.ENgetnodeid

def ENgetnodetype(*args):
  return _epanet2.ENgetnodetype(*args)
ENgetnodetype = _epanet2.ENgetnodetype

def ENgetnodevalue(*args):
  return _epanet2.ENgetnodevalue(*args)
ENgetnodevalue = _epanet2.ENgetnodevalue

def ENgetlinkindex(*args):
  return _epanet2.ENgetlinkindex(*args)
ENgetlinkindex = _epanet2.ENgetlinkindex

def ENgetlinkid(*args):
  return _epanet2.ENgetlinkid(*args)
ENgetlinkid = _epanet2.ENgetlinkid

def ENgetlinktype(*args):
  return _epanet2.ENgetlinktype(*args)
ENgetlinktype = _epanet2.ENgetlinktype

def ENgetlinknodes(*args):
  return _epanet2.ENgetlinknodes(*args)
ENgetlinknodes = _epanet2.ENgetlinknodes

def ENgetlinkvalue(*args):
  return _epanet2.ENgetlinkvalue(*args)
ENgetlinkvalue = _epanet2.ENgetlinkvalue

def ENgetversion():
  return _epanet2.ENgetversion()
ENgetversion = _epanet2.ENgetversion

def ENsetcontrol(*args):
  return _epanet2.ENsetcontrol(*args)
ENsetcontrol = _epanet2.ENsetcontrol

def ENsetnodevalue(*args):
  return _epanet2.ENsetnodevalue(*args)
ENsetnodevalue = _epanet2.ENsetnodevalue

def ENsetlinkvalue(*args):
  return _epanet2.ENsetlinkvalue(*args)
ENsetlinkvalue = _epanet2.ENsetlinkvalue

def ENaddpattern(*args):
  return _epanet2.ENaddpattern(*args)
ENaddpattern = _epanet2.ENaddpattern

def ENsetpattern(*args):
  return _epanet2.ENsetpattern(*args)
ENsetpattern = _epanet2.ENsetpattern

def ENsetpatternvalue(*args):
  return _epanet2.ENsetpatternvalue(*args)
ENsetpatternvalue = _epanet2.ENsetpatternvalue

def ENsettimeparam(*args):
  return _epanet2.ENsettimeparam(*args)
ENsettimeparam = _epanet2.ENsettimeparam

def ENsetoption(*args):
  return _epanet2.ENsetoption(*args)
ENsetoption = _epanet2.ENsetoption

def ENsetstatusreport(*args):
  return _epanet2.ENsetstatusreport(*args)
ENsetstatusreport = _epanet2.ENsetstatusreport

def ENsetqualtype(*args):
  return _epanet2.ENsetqualtype(*args)
ENsetqualtype = _epanet2.ENsetqualtype
# This file is compatible with both classic and new-style classes.


