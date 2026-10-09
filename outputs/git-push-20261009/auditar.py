from pathlib import Path
import json, re, subprocess

root = Path(__file__).resolve().parents[2]
out = Path(__file__).parent
raw = subprocess.check_output(['git','-c','core.quotepath=false','ls-files','--modified','--deleted','--others','--exclude-standard','-z'],cwd=root)
names=sorted(set(raw.decode('utf-8').rstrip('\0').split('\0')))
excluded=[]; selected=[]; alerts=[]; sizes=[]
patterns = {
    'private_key':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'github_token':r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b',
    'aws_key':r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
    'slack_token':r'\bxox[baprs]-[A-Za-z0-9-]{20,}\b',
    'openai_key':r'\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b',
    'assignment':r'''(?i)(?:api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|password)\s*["']?\s*[:=]\s*["'][A-Za-z0-9/+_=.-]{24,}["']'''
}
text_exts={'.py','.js','.css','.html','.json','.md','.mdc','.txt','.toml','.yml','.yaml','.ps1'}
for name in names:
    p=root/name
    if p.suffix.lower() in {'.log','.tmp','.pid','.lock'} or p.name.startswith('.env') or p.suffix.lower() in {'.pem','.key'}:
        excluded.append(name);continue
    selected.append(name)
    if not p.exists():continue
    sizes.append((p.stat().st_size,name))
    if p.suffix.lower() in text_exts:
        content=p.read_text(encoding='utf-8',errors='replace')
        for kind,pattern in patterns.items():
            for hit in re.finditer(pattern,content):
                alerts.append({'path':name,'kind':kind,'line':content.count('\n',0,hit.start())+1})
payload={'selected':selected,'excluded_local':excluded,'alerts':alerts,'total_bytes':sum(size for size,name in sizes),'largest':sorted(sizes,reverse=True)[:8]}
(out/'inventario.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'files':len(selected),'excluded':excluded,'alerts':alerts,'megabytes':round(payload['total_bytes']/1024/1024,2),'largest':payload['largest']},ensure_ascii=False))
if alerts:raise SystemExit(1)
