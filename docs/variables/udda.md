# Education data (`udda`)


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

### `UDD`

Code for an education understood as the educational program or activity. All educational programs have a UDD code (eg: Nurse = 5166, Engineer = 5189)

[Official Documentation link](https://www.dst.dk/da/statistik/dokumentation/times/uddannelseregister/udd)

### `ALMAUDD`

Code for highest completed _general_ education.

Check the documentation for the specific categorical encodings:

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ALMAUDD)

### `ALM_VFRA`

Time of highest completed general education.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ALM-VFRA)

### `ERHAUDD`

Highest completed _vocational_ qualifying education.

Check the documentation for the specific categorical encodings:

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ERHAUDD)

### `ERHINSTNR`

Institutional number of the institution where the highest completed vocational qualifying education has been completed.

Check the documentation for the specific categorical encodings:

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ERHINSTNR)

### `ERH_VFRA`

Time of obtaining vocational competency-providing education

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ERH-VFRA)

### `HFAUDD`

Code for a person's highest completed education at any given time.

Check the documentation for the specific categorical encodings:

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/HFAUDD)

### `HFINSTNR`

Code for the name of the institution where the highest completed education is completed.

Check the documentation for the specific categorical encodings:

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/uddannelsesdata/hoejest-fuldfoerte-uddannelse---status/hfinstnr)

### `HF_VFRA`

Time of highest completed education.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/HF-VFRA)

### `IG_VFRA`

Starting time of ongoing education.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/IG-VFRA)

### `VERSION`

Time reference. The first time data is loaded is `VERSION = 01` for a given REFERENCE TIME, the second time `VERSION = 02`, etc.

[Official Documentation link](https://www.dst.dk/da/statistik/dokumentation/times/moduldata-faelles-variable/version)
