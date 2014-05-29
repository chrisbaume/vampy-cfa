from yaafelib import *
import numpy

class PyCFA: 
	
	def __init__(self,inputSampleRate): 
		self.m_inputSampleRate = inputSampleRate 
		self.m_stepSize = 0
		self.m_blockSize = 0
		self.m_channels = 0
		self.previousSample = 0.0
		self.threshold = 0.005
		self.counter = 0
		
	def initialise(self,channels,stepSize,blockSize):
		self.m_channels = channels
		self.m_stepSize = stepSize		
		self.m_blockSize = blockSize
		return True
	
	def getMaker(self):
		return 'BBC'
	
	def getName(self):
		return 'Continuous Frequency Activation'
		
	def getIdentifier(self):
		return 'vampy-cfa'
	
	def getMaxChannelCount(self):
		return 1
		
	def getInputDomain(self):
		return 'TimeDomain'
			
	def getOutputDescriptors(self):
		
		#descriptors can be returned as python dictionaries
		output0={
		'identifier':'cfa',
		'name':'Continuous Frequency Activation',
		'description':'Continuously (over several seconds) activated '\
                'frequency bands are detected and their spectral peak values '\
                'summed up to the CFA-value',
		'unit':' ',
		'hasFixedBinCount':True,
		'binCount':1,
		#'binNames':['1 Hz',1.5,'2 Hz',3,'4 Hz'],
		'hasKnownExtents':False,
		#'minValue':0.0,
		#'maxValue':0.0,
		'isQuantized':False,
		#'quantizeStep':1.0,
		'sampleType':'FixedSampleRate'
		#'sampleRate':48000.0
		}

		return [output0]


	def getParameterDescriptors(self):
		paramlist1={
		'identifier':'threshold',
		'name':'Noise threshold',
		'description':'',
		'unit':'v',
		'minValue':0.0,
		'maxValue':0.5,
		'defaultValue':0.005,
		'isQuantized':False
		}
		return [paramlist1]


	def setParameter(self,paramid,newval):
		if paramid == 'threshold' :
			self.threshold = newval
                self.fp = FeaturePlan(sample_rate=self.m_inputSampleRate)
                self.fp.addFeature('cfa: ContinuousFrequencyActivation '\
                'BinThreshold=0.1  FFTLength=0 FFTWindow=Hanning  NbPeaks=5 '\
                'NbRunAvgFrames=21 NbSumFrames=100  NormWindow=Hanning '\
                'StepNbSumFrames=50 blockSize=1024  stepSize=1024')
                self.engine = Engine()
                self.engine.load(self.fp.getDataFlow())
                self.engine.reset()
		return

		
	def getParameter(self,paramid):
		if paramid == 'threshold' :
			return self.threshold
		else:
			return 0.0


	# legacy process type: the input is a python list of samples
	def process(self,inbuf,timestamp):
            self.engine.writeInput('audio', numpy.array(inbuf))
            self.engine.process()
            #feats = self.engine.readAllOutputs()

            #output0=[]
            #results = feats['cfa'].tolist()

            #for result in results:
                #feature0={
		#'hasTimestamp':False,		
		#'values':[result],
		#'label':str(result)				
		#}
		#output0.append(feature0)

            return []

	def getRemainingFeatures(self):
            self.engine.flush()
            feats = self.engine.readAllOutputs()

            output0=[]
            results = feats['cfa'].tolist()
            for i in range(len(results)):
                feature0={
                'hasTimestamp':False,
                'values':[results[i]],
                'label':str(results[i])				
                }
                output0.append(feature0)
            return [output0]
