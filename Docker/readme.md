Õppematerjalide ning internetist leitud materjalide põhjal tegin lihtsa Flask rakenduse, mis teisendab kilomeetrid miilidesse.

Kasutamiseks tuleb navigeerida vastavasse kausta, kus on Dockerfile ja simple_app.py failid.

Seejärel tuleb luua image käsuga ```docker build -t <image_name> .```

Järgmiseks tuleb käivitada container käsuga ```docker run -p 8000:8000 <image_name>```

Seejärel on rakendus kättesaadav aadressil http://localhost:8000
