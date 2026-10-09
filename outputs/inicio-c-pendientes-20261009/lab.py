from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit,unquote,parse_qs
import json,mimetypes
ROOT=Path(__file__).resolve().parents[2]
OLD=ROOT/'archive/2026-10-09-inicio-c'
INSTRUMENT=r"""<script>
(() => {
 const result={cls:0,clsTotal:0,lcp:0,fcp:0,shifts:[],ready:false};
 let start=0,last=0,windowValue=0;
 function publish(){document.documentElement.setAttribute('data-qa-metrics',JSON.stringify(result));}
 try {new PerformanceObserver(list=>{for(const e of list.getEntries()){
   if(e.hadRecentInput)continue;
   result.clsTotal+=e.value;
   if(!start||e.startTime-last>1000||e.startTime-start>5000){start=e.startTime;windowValue=0;}
   last=e.startTime;windowValue+=e.value;result.cls=Math.max(result.cls,windowValue);
   result.shifts.push({t:e.startTime,value:e.value,sources:e.sources.map(s=>({tag:s.node?.tagName,cls:s.node?.className,before:s.previousRect.toJSON(),after:s.currentRect.toJSON()}))});publish();
 }}).observe({type:'layout-shift',buffered:true});}catch(e){result.clsError=String(e);}
 try {new PerformanceObserver(list=>{for(const e of list.getEntries()){result.lcp=e.startTime;result.lcpElement={tag:e.element?.tagName,cls:e.element?.className,url:e.url};}publish();}).observe({type:'largest-contentful-paint',buffered:true});}catch(e){result.lcpError=String(e);}
 window.addEventListener('load',()=>{result.load=performance.now();publish();});
 setTimeout(()=>{result.fcp=performance.getEntriesByName('first-contentful-paint')[0]?.startTime||0;result.ready=true;result.resources=performance.getEntriesByType('resource').map(e=>({name:e.name,duration:e.duration,transfer:e.transferSize,encoded:e.encodedBodySize}));publish();},5500);
 publish();
})();
</script>"""
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
 def do_GET(self):
  u=urlsplit(self.path);parts=unquote(u.path).strip('/').split('/')
  if not parts or parts[0] not in ('before','after') or any(x in ('.','..') or x.startswith('.') for x in parts):self.send_error(404);return
  mode=parts.pop(0);rel='/'.join(parts) or 'index.html'
  f=(ROOT/rel).resolve()
  if not f.is_relative_to(ROOT) or not f.is_file():self.send_error(404);return
  if mode=='before' and (OLD/rel).is_file():f=OLD/rel
  data=f.read_bytes();kind=mimetypes.guess_type(f.name)[0] or 'application/octet-stream'
  qa=parse_qs(u.query).get('qa',[''])[0]
  if kind=='text/html' and qa=='metrics':data=data.replace(b'<head>',b'<head>'+INSTRUMENT.encode('utf-8'),1)
  self.send_response(200);self.send_header('Content-Type',kind+'; charset=utf-8' if kind.startswith('text/') else kind)
  self.send_header('Cache-Control','no-store')
  if qa=='nojs':self.send_header('Content-Security-Policy',"script-src 'none'")
  self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
if __name__=='__main__':
 print('Local lab 127.0.0.1:8871',flush=True)
 ThreadingHTTPServer(('127.0.0.1',8871),Handler).serve_forever()
