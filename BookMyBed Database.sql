CREATE DATABASE BOOKMYBED;

USE BOOKMYBED;

CREATE TABLE QUARANTINE_CENTERS(
CENTER_ID varchar(255), Primary Key
CENTER_NAME varchar(255),
ADDRESS varchar(100),
MOBILE_NO int,
PERSON_IN_CHARGE varchar(255),
BEDS int,
STARTING_PRICE int);


INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) VALUES ("MDTggm01", "Medanta The Medicity", "CH Baktawar Singh Rd near Olympus", "01244141413", "Pranay Natarajan", "21", "650");
INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) Values ("FRTggm02", "Fortis Memorial Research Institute", " Sector Opposite HUDA City Centre Gurugram Haryana", " 01247162201", " Surendra Sood", " 14", " 750");
INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) Values ("CKBggm03", "CK Birla Hospital", " Block J_CK Birla Hospital_Nirvana Central Rd_ Mayfield Garden_Gurugram", " 01244882249", " Rajendra Dey", " 35", " 500");
INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) Values ("ARTggm04", "Artemis Hospital ", " Sector 51 Gurugram Haryana 122001", " 01244511112", " Drishti Bhatia", " 27", " 600");
INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) Values ("APHndo1", "Indraprastha Apollo Hospitals", " Delhi Mathura Road Sarita Vihar New Delhi", " 01242625858", "Suraj Kakar", " 12", " 750");
INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) Values ("FRTnd02", "Fortis Escorts", "Okhla road Sukhdev Vihar Metro Station New Delhi ", " 01244735000", "Jagan Deshmukh", " 24", " 600");
INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) Values ("FRTnd03", "Fortis Hospital Delhi", "A Block Shalimar Bag New Delhi ", " 01245302222", "Anusha Bakshi", " 16", " 700");
INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) Values ("MSSnd04", "Max Super Speciality Hospital", "12 Press Enclave Marg Saket Institutional Area Saket New Delhi ", " 01240554055", "Sima Arora", " 23", " 650");
INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) Values ("FRTgnd01", "Fortis Hospital Noida", "B22 Rasoolpur Nawada D Block Sector 62 Greater Noida ", " 01241743837", "Chiranjivi Tiwari", " 28", " 550");
INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) Values ("JYPgnd02", "Jaypee Hospital", "Goberdhanpur Sector 128 Shahpur Govardhanpur Bangar Noida", " 01244122222", "Disha Bassi", " 32", " 500");
INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) Values ("CKBggm03", "CK Birla Hospital", " Block J_CK Birla Hospital_Nirvana Central Rd_ Mayfield Garden_Gurugram", " 01244882249", " Rajendra Dey", " 35", " 500");
INSERT INTO QUARANTINE_CENTERS (CENTER_ID, CENTER_NAME, ADDRESS, MOBILE_NO, PERSON_IN_CHARGE, BEDS, STARTING_PRICE) Values ("ARTggm04", "Artemis Hospital ", " Sector 51 Gurugram Haryana 122001", " 01244511112", " Drishti Bhatia", " 27", " 600");

create Table Patient(
Patient_ID Varchar(5),
Patient_Name Varchar(30),
Patient_Mobile_No bigint(10),
Guardian_Name Varchar(30),
Guardian_Mob_no bigint(10),
Center_ID Varchar(255),
Status Varchar(15),
PRIMARY KEY (Patient_ID),
FOREIGN KEY (Center_ID) references Quarantine_centers(CENTER_ID)
);
