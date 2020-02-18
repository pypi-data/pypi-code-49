from pytwig import bw_object

DEFAULT_VELOCITY = 100

class Clip(bw_object.BW_Object): #abstract
	length = 4.0

	def set_duration(self, length):
		self.length = float(length)
		self.set('duration(38)', self.length)
		return self

	def set_loop(self, enable = None, length = None):
		# TODO: allow to set loop start
		if enable != None:
			self.get('owned_content_timeline(648)').get('cue_marker_timeline(2447)').set(2449, enable)
		if length != None:
			self.get('owned_content_timeline(648)').get(2447).get(2450).set(38, float(length))
		return self

class Note_Clip(Clip):
	def __init__(self, length):
		super().__init__(classnum = 'instrument_note_clip_event(71)')
		clip_content_timeline = bw_object.BW_Object('instrument_note_clip_content_timeline(191)')
		clip_content_timeline.set('note_timeline(1180)',bw_object.BW_Object('polyphonic_instrument_note_timeline(1740)'))
		self.set('owned_content_timeline(648)', clip_content_timeline)
		self.set_duration(length)

	def set_duration(self, length):
		super().set_duration(length)
		cue_marker_timeline = self.get('owned_content_timeline(648)').get('cue_marker_timeline(2447)')
		end = cue_marker_timeline.get('start_marker(2444)').get('time(687)') + self.length
		cue_marker_timeline.get('stop_marker(2445)').set('time(687)', end)
		return self

	def create_note(self, key, pos, dur, vel = None):
		if vel == None:
			vel = DEFAULT_VELOCITY
		note = Note().set_pos(pos).set_dur(dur).set_vel(vel)
		timeline_list = self.get('owned_content_timeline(648)').get('note_timeline(1180)').get('timelines(6347)')
		# note data is stored in a key
		for each_key in timeline_list:
			if key == each_key.get('key(238)'):
				each_key.get('events(543)').append(note)
				return
		# if there is no note data for a given key, make it
		key_timeline = bw_object.BW_Object('instrument_note_event_timeline(66)')
		key_timeline.set('key(238)', key)
		key_timeline.get('events(543)').append(note)
		timeline_list.append(key_timeline)

class Note(bw_object.BW_Object):
	def __init__(self):
		super().__init__(classnum = 102)
		content_timeline = bw_object.BW_Object(41)
		self.set('content_timeline(6288)', content_timeline)
		self.set('owned_content_timeline(648)', content_timeline)

	def set_pos(self, pos):
		self.set(687, float(pos))
		return self

	def set_dur(self, dur):
		self.set(38, float(dur))
		return self

#	def set_key(self, key):
#		self.set(238, int(key))
#		return self

	def set_vel(self, vel, rising_falling = 'rf'):
		if isinstance(vel, int):
			if vel > 127:
				vel = 127
			vel = float(vel)/127.0
		if 'r' in rising_falling:
			self.set(239, vel)
		if 'f' in rising_falling:
			self.set(240, vel)
		return self
