# Construit le site (index.html, icônes, service worker) à la racine du dépôt.
import os,shutil
from PIL import Image
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(H); SA=os.path.join(H,'standalone')
s=open(os.path.join(H,'src.html')).read()
for k,f in [('LOGO','logo'),('BEAR','bear'),('BUNNY','bunny'),('CHICK','chick')]:
    s=s.replace('{{%s}}'%k,'data:image/webp;base64,'+open(os.path.join(H,'img',f+'.txt')).read())
head=open(os.path.join(SA,'head.html')).read(); login=open(os.path.join(SA,'login.html')).read()
open(os.path.join(ROOT,'index.html'),'w').write('<!doctype html><html lang="fr"><head>'+head+'</head><body>'+login+s+'</body></html>')
icon=Image.open(os.path.join(H,'img','icone-koji-tea.png'))
for n,sz in [('icon-512.png',512),('icon-192.png',192),('apple-touch-icon.png',180)]:
    icon.resize((sz,sz),Image.LANCZOS).save(os.path.join(ROOT,n))
for f in ['manifest.webmanifest','sw.js']: shutil.copy(os.path.join(SA,f),ROOT)
if not os.path.exists(os.path.join(ROOT,'firebase-config.js')): shutil.copy(os.path.join(SA,'firebase-config.example.js'),os.path.join(ROOT,'firebase-config.js'))
