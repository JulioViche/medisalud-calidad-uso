IF OBJECT_ID('invoices', 'U') IS NULL
CREATE TABLE invoices (
  invoice_id VARCHAR(60) PRIMARY KEY,
  transaction_id VARCHAR(60) NOT NULL,
  patient_id VARCHAR(60) NOT NULL,
  amount DECIMAL(12,2) NOT NULL,
  site VARCHAR(80) NOT NULL,
  duplicated BIT NOT NULL,
  created_at DATETIMEOFFSET NOT NULL
);

