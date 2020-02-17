from . import iceflow, jack

def volumeToDB(vol):
    if vol<0.001:
        return -100
    #Calculated usiung curve fitting, assuming that 0 is 0db,
    #0.5 is 10db below, etc.
    return -38.33333 + 77.80645*vol- 39.56989*vol**2

def volumeToRawGain(vol):
    vGain = 10**(volumeToDB(vol)/20)

class AudioFilePlayer(iceflow.GStreamerPipeline):
    def __init__(self, file, volume=1, output="@auto",onBeat=None, _prevPlayerObject=None):

        if output==None:
            output="@auto"
        self.filename = file


        self.lastFileSize = os.stat(file).st_size

        if self.lastFileSize==0:
            for i in range(10):
                self.lastFileSize = os.stat(file).st_size
                if self.lastFileSize>0:
                    break
                time.sleep(1)

        if self.lastFileSize==0:
            raise RuntimeError("File was still zero bytes after 10 seconds")
        
        self.lastPosition = 0
       
        self.lastFileSizeChange = 0

        gstwrapper.Pipeline.__init__(self,str(uuid.uuid4()),systemTime=True,realtime=70)
        self.aw =None
        self.ended = False

        self.lastBeat = 0
        self.peakDetect = 0
        self.detectedBeatInterval = 1/60
        self.beat = onBeat
        
        self._prevPlayerObject = _prevPlayerObject


        self.src = self.addElement('filesrc',location=file)
        self.queue = self.addElement("queue")

        decodeBin = self.addElement('decodebin',low_percent=15)
        #self.addElement('audiotestsrc')
        isVideo=False

        for i in (".mkv",".flv",".wmv",".mp4",".avi"):
            if file.endswith(i):
                isVideo=True
        if isVideo:
            decodeBin.set_property("low-percent",80)
            q=self.addElement('queue', connectToOutput=decodeBin, connectWhenAvailable="audio")
        
            self.addElement('audiorate')
            self.addElement('audioconvert')

        else:
            self.addElement('audioconvert',connectToOutput=decodeBin,connectWhenAvailable="audio")
    
        self.addElement('audioresample')


        
        if onBeat:
            self.addLevelDetector()

        self.fader = self.addElement('volume', volume=volume)

        if output=="@auto":
            self.sink = self.addElement('autoaudiosink')

        elif output.startswith("@alsa:"):
            self.addElement('alsasink',device= output[6:])

        elif output.startswith("@pulse"):
            self.addElement('alsasink',device= output[6:])

        #No jack clients at all means it probably isn't running
        elif not jack.getPorts():
            self.addElement('alsasink',device= output)
        
        #Default to just using jack
        else:
            cname="player"+str(time.monotonic())+"_out"

            self.sink = self.addElement('jackaudiosink', buffer_time=8000 if not isVideo else 80000, 
            latency_time=4000 if not isVideo else 40000,slave_method=2,port_pattern="jhjkhhhfdrhtecytey",
            connect=0,client_name=cname)

            self.aw = jackmanager.Airwire(cname, output)
            self.aw.connect()
        #Get ready!
        self.pause()


    def loopCallback(self):
        size= os.stat(self.filename).st_size
        if not size==self.lastFileSize:
            self.lastFileSizeChange = time.monotonic()
            self.lastFileSize=size

        self.lastPosition = self.getPosition()

    def onEOS(self):
        #If the file has changed size recently, this might not be a real EOS,
        #Just a buffer underrun. Lets just try again 
        if self.lastFileSizeChange> (time.monotonic()-3):
            self.pause()
            self.seek(self.lastPosition-0.1)
            time.sleep(3)
            self.play()
        else:
            gstwrapper.Pipeline.onEOS(self)


    def setFader(self,level):
        "Low level function that sets the raw volume element"
        with self.lock:
            try:
                if self.fader:
                    self.fader.set_property('volume', level)
            except ReferenceError:
                pass


    def setVolume(self,v):
            #We are going to do a perceptual gain algorithm here
            self._volume=v
            #Now convert to a raw gain
            vGain = volumeToRawGain(v)

            self.setFader(vGain if not vGain<-0.01 else 0)

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self.setFader(volume)
    
    def stop(self):

        #Prevent any ugly noise that GSTreamer might make when stopped at
        #The wrong time
        try:
            if self.aw:
                self.aw.disconnect()
        except:
            logging.exception("Err disconnecting airwire")

        gstwrapper.Pipeline.stop(self)

        if self._prevPlayerObject:
            p = self._prevPlayerObject()
            if p:
                p.stop()

    def resume(self):
        self.start()
  
    def onStreamFinished(self):
        self.ended=True

    def isPlaying(self):
        return self.running


    def addLevelDetector(self):
        self.addElement("level", post_messages=True, peak_ttl=300*1000*1000,peak_falloff=60)

    def on_message(self, bus, message,userdata):
        s = message.get_structure()
        if not s:
            return True
        if  s.get_name() == 'level':
            if self.board:
                rms = sum([i for i in s['rms']])/len(s['rms'])
                self.peakDetect = max(self.peakDetect, rms)
                timeSinceBeat = time.monotonic()-self.lastBeat

                threshold =self.peakDetect-(1+ (3*max(1,timeSinceBeat/self.detectedBeatInterval)))
                if timeSinceBeat> self.detectedBeatInterval/8:
                    if rms>threshold:
                        self.beat()
                        self.detectedBeatInterval = (self.detectedBeatInterval*3 + timeSinceBeat)/4
                        self.peakDetect*=0.996
        return True
