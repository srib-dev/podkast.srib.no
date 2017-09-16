% Sette opp Python 

Om Python er nytt for deg kan du herved få litt hjelp til å sette opp de mest grunleggende
ingrediensene på din pc for å bake god pythonkake.  Kort fortalt handler det om å installere tre ting:
	1. Python
	2. Pip
	3. virtualenvwrapper

#1. Python trengs installeres: 
	Vi liker å ha python når vi jobber med python.
	
	1. gå til [Download Python](https://www.python.org/downloads/) og velg siste versjon (3.x).
	2. Får du spørsmål om å inkludere Pip / Python i PATH under instalasjon: VELG JA!

#2. Pip trengs installeres:
	- Mange python moduler er gull verdt å ha. Spesielt de beste som er skrevet av andre dyktige pythonutviklere. 
	  Disse modulene brukes for å få funksjonalitet som ikke følger med standard python.  PiP er en pakkebrønn for pythonpakker. For å installere requests (en populær http modul), gjør man det enkelt fra terminalen: `pip install requests`.

	1. Åpne terminalen og kjør: `pip --version`. Får du ikke feilmelding har du pip installert allerede. Ferdig. Go on.
	2. Om ikke, google "how to install pip + win|mac|linux". 

	Som regel pleier man installere pip med "getpip.py", et script man laster ned og kjører i terminalen slik: `python getpip.py`

#3. Virtuelle Miljøer trengs:
 
## Windows
Bruk [virtualenvwrapper-win](https://pypi.python.org/pypi/virtualenvwrapper-win) pakken. 
 1. `pip install virtualenvwrapper-win`
 2. Lukk terminalvinduet og åpne ny terminal. (CMD) 

## linux/mac:
  
 1. `pip install virtualenvwrapper`
 2. legg disse to linjene i bunnen av .bashrc eller .profile (den av de to som allerede finns i hjemmemappen din)
 

```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```
 3. restart terminalen. 
