# Residence permit for immigrants data (`ophgin`)


### `PNR`

Unique identification of person is used as key to `PERSON_ID`.

People's anonimized CPR. All CPR PNRs are converted to a unidentified PERSON_ID.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/pnr)


### `CPRTJEK`

CPR check. Control value calculated on a social security number from a given date.

- '0' = The social security number is valid
- '1' = The social security number does not consist of 10 digits
- '2' = Not used replacement number
- '3' = Not valid date of birth in a replacement number
- '4' = Not valid date of birth in a social security number with control digit
- '5' = Not valid date of birth in a social security number without a control digit
- '6' = Social security number without control digit, but not in valid series
- '7' = Date of birth is after the date the age is calculated from

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/cprtjek)

### `CPRTYPE`

CPR type.

- '1' = Traditional pnumber
- '2' = Replacement pnumber
- '3' = Pnumber without control digit, series 1
- '4' = Pnumber without control digit, series 2
- '5' = Pnumber without control digit, series 3

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/cprtype)


### `STATSB`

Citizenship / Country of origin of the person.

Codes available in the documentation (link below).

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/statsb)


### `FORKLAR`

Code for residence permit type from the Immigration Service.

Check the documentation for the specific categorical encodings:

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/HFAUDD)

### `GRUNDLAG`

Code of the subdivision of residence permit type from the Immigration Service.

Check the documentation for the specific categorical encodings:

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/grundlag)

### `IMPUTERET`

Code for imputation status of the person's residence permit. After a process, residence permit are `IMPUTED` (e.g 1, 20, 99) for immigrant persons who do not have Danish / Nordic citizenship and who are born abroad.

- '0' From 1997, Immigration Service
- '1' From 1997, Imputed
- '9' From 1997, Nordic citizen, should not be imputed
- '11' Before 1997, Immigration Service 1993-1996
- '12' Before 1997, Survey Response
- '20' Before 1997, Imputed
- '29' Before 1997, a Nordic citizen, should not be imputed
- '99' Imputed in connection with inventory sheet (statusopgørelse)

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/imputeret)


### `VERSION`

Time reference. The first time data is loaded is `VERSION = 01` for a given REFERENCE TIME, the second time `VERSION = 02`, etc.

[Official Documentation link](https://www.dst.dk/da/statistik/dokumentation/times/moduldata-faelles-variable/version)
