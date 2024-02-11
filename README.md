
# Python Wachtwoordgenerator

## Inleiding:

Weet je hoe belangrijk een goed wachtwoord is?

Nee, nou als een hacker je probeert te hacken door middel van een bruteforce (alle mogelijkheden proberen die er zijn) dan kan dat variëren van direct tot 63 duizend jaar...

|   | 8 karakters | 10 karakters| 12 karakters | 
|---|---|---|---|
| Alleen kleine letters  |  direct | direct   | een paar weken   | 
| + 1 hoofdletter  | half uurtje | 1 maand | 5 jaar| 
| + 1 nummer  | 1 uur  | 6 jaar  | 2 duizend jaar  |
| + 1 symbool | 1 dag | 50 jaar | 63 duizend jaar |

Daarnaast wordt dit getal iedere 2 jaar gehalveerd omdat er telkens betere computers bestaan.

Check hier je eigen wachtwoord: [Password Strength Testing Tool]( https://bitwarden.com/password-strength/)

Het is daarom goed om een sterk wachtwoord te kiezen die je eigenlijk om de 2 jaar moet aanpassen. Maar elke keer weer een goed wachtwoord bedenken kost jou heel veel denkwerk. Maar gelukkig kan jij als developer er een scriptje voor schrijven.


Instructies
---

De applicatie zal je 3 vragen stellen:

   1. Hoeveel letters wil je in je wachtwoord?
   2. Hoeveel symbolen wil je in je wachtwoord?
   3. Hoeveel nummers wil je in je wachtwoord?

Het doel van de applicatie is om de invoer van de gebruiker te ontvangen en vervolgens een willekeurig wachtwoord te genereren.

<details open> 
<summary> <b> Eenvoudige Versie (Stap 1) </b> </summary>


Genereer het wachtwoord in een vooraf bepaalde volgorde. Bijvoorbeeld, als de gebruiker een wachtwoord wil met:

    4 letters
    2 symbolen
    3 nummers

dan zou het wachtwoord er als volgt uit kunnen zien:

`qfIw)+393`

Je ziet dat alle letters bij elkaar staan, alle symbolen bij elkaar, en alle nummers volgen elkaar ook op.


* <details>
  <summary>
     <i>Kom je er niet uit welke module je moet gebruiken?</i>
  </summary>
   
   * 💡Gebruik de `random` module.

* <details>
  <summary>
     <i>Kom je er niet uit hoe je een willekeurig karakter aanspreekt?</i>
  </summary>

   * 💡In `random` zit een methode genaamd `choice`, hiermee kan je een willekeurig karakter aanspreken uit een array.
 
</details>
</details>
</details>




<details> 
<summary> <b>Moeilijke Versie (Stap 2)</b> </summary>
  
Als je de eenvoudige versie hebt voltooid, kun je de moeilijke versie proberen. In deze geavanceerde versie volgt het uiteindelijke wachtwoord geen vast patroon. Dus het bovenstaande voorbeeld zou er als volgt uit kunnen zien:

`3+w3qf)9I`

Dus elke keer dat je een wachtwoord genereert, zijn de posities van de symbolen, cijfers en letters anders.
 
<details>
    <summary><i>Weet je niet wat je nodig hebt?</i></summary>
     je hebt het volgende nodig:

     1 list
     3 for-in-range loops

</details>
 <details>
  <summary>
     <i>Kom je er niet uit hoe je iets aan een lijst toevoegt?</i>
  </summary>

   * 💡Als je de naam van de lijst gebruikt en daar `.append(gegevens die je wilt toevoegen)` bij gebruikt dan wordt het in je lijst toegevoegd. 
</details>

<details>
  
  <summary>
     <i>Kom je er niet uit hoe je een lijst door elkaar husselt?</i>
  </summary>

   * 💡In `random` zit een methode genaamd `shuffle`, hiermee kan je alles binnen de lijst door elkaar husselen.

</details>

<details>
  <summary>
     <i>Kom je er niet uit hoe je een lijst aan elkaar plakt?</i>
  </summary>

   * 💡Als je een print functie gebruikt met als inhoud `"".join` en dan de lijst dan voegt hij het aan elkaar. Kijk nu eens wat er gebeurt als je `"-".join` doet. 

</details>

</details>
</details>

