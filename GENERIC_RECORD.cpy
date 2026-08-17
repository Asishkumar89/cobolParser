      ******************************************************************
      * COPYBOOK: GENERIC_RECORD
      * DESCRIPTION: Layout for generic_record_500mb.dat
      * ENCODING:    EBCDIC, IBM CCSID 500 (CP500)
      * RECORD FORMAT: F (fixed length, no RDW/BDW headers)
      * RECORD LENGTH: 50 bytes
      * RECORD COUNT:  10,000,000
      * FILE SIZE:     500,000,000 bytes (500 MB)
      ******************************************************************
       01  GENERIC-RECORD.
           05  RECORD-ID           PIC 9(6).
           05  CUSTOMER-NAME       PIC X(20).
           05  AMOUNT              PIC S9(7)V99 COMP-3.
           05  TRANS-DATE          PIC X(8).
           05  STATUS-CODE         PIC X(1).
           05  FILLER              PIC X(10).
