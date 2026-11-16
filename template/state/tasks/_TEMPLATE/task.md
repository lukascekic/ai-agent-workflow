## Za Luku — <datum, vreme>

Stanje:
Od poslednjeg puta:
Pitanja (doslovno):
Odluke:
Posle tvog odgovora:
Sledeća kapija: *(tačna komanda i kome ide, npr. `continue 03 → Claude`)*

*(Piše samo lead. Kad ništa ne treba: `Nema akcije za Luku`.)*

---

# Task: <id>-<naziv>

**Tip:** software | research/decision | other
**Status:** intake | sealed | revealed | building | review | confirm | closed
**Oznaka:** Fast | Deep — *okidači koji su okinuli + razlog (Deep ako bilo koji pass imenuje važeći okidač, osim ako je Luka odbio eskalaciju u `decisions.md`)*
**Lead:** Claude | GPT · **Reviewer:** GPT | Claude
**Sealed:** da | ne — <razlog> *(`ne` samo za child task iz odobrenog grafa — D49)*
**Graf:** *(samo child task: `00-init`)*
**Otvoren:**
**Dira:** *(fajlovi, moduli, oblasti — dva aktivna taska koja diraju isto se serijalizuju)*
**Next step:** *(uvek aktuelno — po njemu drugi model nastavlja ako ovaj udari u limit)*

### Aktivirani elementi

*Iz mape okidač → element i događaj → element. Element koji nije ovde nije aktiviran — u `outcome.md` se beleži kao `n/a — uslov nije aktiviran`.*

| Element | Aktivirao ga | Gotovo |
|---|---|---|
| | | |

*Falsifier, ako je aktiviran: `isti poziv` (sa challenge-om) ili `zaseban poziv` (okidač novac, bezbednost ili nepovratnost).*

---

## Intake

*Strukturisano ili sirovi braindump — oba modela ga dobijaju neizmenjenog. Nepoznato = `unknown`.*

### Braindump

### Cilj

### Acceptance kriterijumi

### Non-goals

### Ograničenja

### Noseći ulazi

| Ulaz | Status |
|---|---|
| | verified locally · verified externally · user assertion · referenced but unavailable · unknown |

---

## Plan

*Samo kad je deliverable softver ili ima više faza; inače se deliverable pravi direktno.*

*Faze: posle svake faze checkpoint. Ako reviewer ne može da pregleda celinu u jednom pozivu, review ide po fazi (`Opseg: faza N`) — ta faza i njeni ugovori sa već prihvaćenim fazama. Završni review (`Opseg: završni`) pokriva ugovore između svih faza i završni acceptance, i samo on zatvara task.*

---

## Checkpoints

*Samo kad je aktiviran (okidač slab oracle, ili plan ima granice rizika).*

```
Granica rizika:
Šta mora da važi:
Oracle / provera:
Uslov za stop ili rollback:
Ishod:
```

---

## Review

Opseg: završni | faza N *(samo završni review zatvara task; krugovi se broje unutar opsega)*
Review krug: 1
Fokus:
Prepravka materijalna: da | ne

*(Od trećeg kruga, ako treba još jedan krug, lead ovde piše izveštaj o konvergenciji i staje za Luku. Lukina odluka se vezuje za krug:)*

Odluka za krug N (opseg): *(nastavi · promeni pristup · stani — prihvata rizik samo za ovaj opseg · stani ceo task — lead doslovno prepisuje Lukin odgovor `krug N: …` iz `luka.md` ili `Relayed human input`, sa izvorom i vremenom)*

---

## Deferred

*(Samo research/decision. Svaka stavka mora imati revisit trigger.)*

```
Nalaz:
Zašto sada ne blokira:
Revisit trigger:
```

---

## Relayed human input

*(Lukini odgovori koje je model preneo doslovno, sa vremenom i kanalom. `luka.md` piše samo Luka.)*
