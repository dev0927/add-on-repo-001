import re,io,json


class PlaylistReader(object):
	list = []
	M3U_REGEX =    re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S)
	PARAMS_REGEX = re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S)
	def __init__(self, fileName):
		self.fileName = fileName
	
	def _read(self, fileName):
		try:
			f = open(fileName,'r')
			content = f.read().replace("\n\n", "\n")
			f.close()
		except:
			content = ""
	
		return content
	
	def readList(self):	

		self.list = self.m3u2list(self.fileName)
		return self.list
		
	def write_playlist(self, destination):
		self.save_list(destination, self.readList())	
	
	def save_list(self, filename, _list):
		try:
			with io.open(filename, 'w', encoding='utf-8') as handle:
				handle.write(unicode(json.dumps(_list, indent=4, ensure_ascii=False)))
			success = True
		except Exception as ex:
			print ex
			success = False
			
		return success
	
	def m3u2list(self, fileName):
		content = self._read(self.fileName)
		matches=self.M3U_REGEX.findall(content)

		li = []
		for params, display_name, url in matches:
			item_data = {"params": params, 
						"name": display_name.encode('base64', 'strict').replace('\n', ''), 
						"url": url.encode('base64', 'strict').replace('\n', '')}
			_params=self.PARAMS_REGEX.findall(params)
			for field, value in _params:
				item_data[field.strip().lower().replace('-', '_')] = value.strip()
			li.append(item_data)
		return li
				
def write_playlist(source, destination):	
	r = PlaylistReader(source)
	r.write_playlist(destination)


write_playlist('streams.m3u', '../plugin.video.addon001/resources/playlist')
write_playlist('movies.m3u', '../plugin.video.addon005/resources/playlist')
