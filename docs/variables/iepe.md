# Inmigration - Descendants Dataset (`iepe`)


### `PNR`

Unique identification of person is used as key to `PERSON_ID`.

People's anonimized CPR. All CPR PNRs are converted to a unidentified PERSON_ID.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/pnr)


### `ALDER`

Age.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/alder)


### `MOR_ID`

`PERSON_ID` of the person's mother.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/mor-id)

### `FAR_ID`

`PERSON_ID` of the person's father.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/far-id)


### `KOM`

Municipal code from the National Register Address.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/kom)


### `CIVST`

Person's marital status (marital status). Unmarried is not included in the marital status table.

The marital code thus became from d. Oct 1 1989 expanded from 4 to 7 marital states.

- 'U' =Unmarried (not included in the marital status table)
- 'G' = Gift 'F' = Divorced
- 'E' = Widow stand The new marital status was as a result of the Registered Partnership Act
- 'P' = Registered Partnership
- 'O' = Repealed registered partnership
- 'L' = Longitudinal living of 2 partners.
- 'D' = Dead

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/civst)


### `FOEDREG_KODE`

Place of birth.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/foedreg-kode)


### `FOEDREG_KODE`

Place of birth.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/foedreg-kode)



### `IE_TYPE`

Definitions of immigrants, descendants, and people of Danish origin, which collectively comprise entire populations, are as follows:

- '1' = Danish. People, regardless of birthplace, who have at least one parent who is both a Danish citizen and born in Denmark.
- '2' = Immigrant. People born abroad. None of the parents are both Danish citizens and born in Denmark.
- '3' = Descendant. People born in Denmark. None of the parents are both Danish citizens and born in Denmark.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/udlaendinge/ie-type)

### `GENERATION`

Whether the father and/or mother were born in Denmark or abroad.

- '0' = Danish (`IE_TYPE` = 1)
- '1' = Parents both born abroad
- '2' = Parents both born in Denmark
- '3' = One parent born in Denmark and another abroad.
- '4' = Parental information not available.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/cpr-oplysninger/generation)


### `KOEN`

Gender (CPR based).

- '1' = Male
- '2' = Female
- '9' = Unknown / Company

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/koen)

### `OPR_LAND`

Citizenship / Country of origin of the person.

Encoding: [Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/lande-psd?)

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/opr-land)


### `STATSB`

Citizenship / Country of origin of the person.

Codes available in the documentation (link below).

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/statsb)

### `STATFODF`

Continent of origin of the father.

Codes available in the documentation (link below).

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/statsb)

### `STATFODM`

Continent of origin of the mother.

Codes available in the documentation (link below).

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/statsb)

### `STATFOED`

Continent of origin of the person.

Codes available in the documentation (link below).

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/statsb)
