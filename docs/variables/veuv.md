# Adult students and continuing education (`veuv`)


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

### `KURSIST_VFRA`

Start date of the course.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Kursistregistret/KURSIST-VFRA)

### `KURSIST_VTIL`

End date of the course.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Kursistregistret/KURSIST-VTIL)

### `UDD`

Code for an education understood as the educational program or activity. All educational programs have a UDD code (eg: Nurse = 5166, Engineer = 5189)

[Official Documentation link](https://www.dst.dk/da/statistik/dokumentation/times/uddannelseregister/udd)

### `AFSLUTN`

Course end. Specifies the way the course is completed for each student, ie. whether the student has, for example, completed or interrupted the course.

- '0' = Continues beyond the period
- '1' = The course is completed and the test passed
- '2' = The course is completed and the test has not passed
- '3' = The course is completed and the student does not attend the exam
- '4' = The course is complete and there is no test attached to the course
- '5' = The student has interrupted the course or has not attended the exam
- '6' = Self-students
- '7' = Uninformed termination
- '8' = No sample associated with the course

[Official Documentation link]https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Kursistregistret/AFSLUTN)

### `AKOMFANG`

The proportion of a full academic year to which the course corresponds. A full-time course is indicated by the value `10000`, while a half-time course is indicated by the value `05000`. `0` must not be deleted.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Kursistregistret/AKOMFANG)
